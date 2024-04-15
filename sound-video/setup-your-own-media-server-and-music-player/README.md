# Setup your own media server and music player 

This doc is 
- referenced in [DNS appendice](../../appendices/DNS.md#add-certificates-alternative-use-a-reverse-proxy)
- referenced in [Sound video README](../README.md#dlna-dmr-dms-dmc-dmp)

And use https://github.com/scoulomb/myhaproxy/README.md (and cross ref ok)

## Acquire music

For this will use Proton VPN 

## Jellyfin setup on a QNAP NAS

The procedure with container setup can be found at: https://jellyfin.org/docs/general/installation/container/

### Step 1: deploy on Linux machine

````
docker pull jellyfin/jellyfin

mkdir jellyfin/config
mkdir jellyfin/cache

sudo docker run -d \
 --name jellyfin \
 # --user uid:gid \
 --net=host \
 --volume /home/scoulomb/jellyfin/config:/config \
 --volume /home/scoulomb/jellyfin/cache:/cache \
 --mount type=bind,source=/home/scoulomb/Music,target=/media \
 --restart=unless-stopped \
 jellyfin/jellyfin
 
````

We can use also compose

Note docker offers 
- Volumes: https://docs.docker.com/storage/volumes/
- Bind Mounts : https://docs.docker.com/storage/bind-mounts/

Quoting bind mount doc

> Bind mounts have been around since the early days of Docker. Bind mounts have limited functionality compared to volumes. When you use a bind mount, a file or directory on the host machine is mounted into a container. The file or directory is referenced by its absolute path on the host machine. By contrast, when you use a volume, a new directory is created within Docker's storage directory on the host machine, and Docker manages that directory's contents.

Note both `--v` (`--volume`), `--mount` can be used to for volumes and bind mount. See
- https://docs.docker.com/storage/volumes/#choose-the--v-or---mount-flag
  - > -v: In the case of named volumes, the first field is the name of the volume, and is unique on a given host machine. For anonymous volumes, the first field is omitted.
- https://docs.docker.com/storage/bind-mounts/#choose-the--v-or---mount-flag
  - > -v: In the case of bind mounts, the first field is the path to the file or directory on the host machine

Note difference of behavior between `--volume` and `--mount` for Bind mounts: https://docs.docker.com/storage/bind-mounts/#differences-between--v-and---mount-behavior

So here we are using bind mounts evrywhere in example above.

EmptyDir, hostPath are volumes in k8s: https://kubernetes.io/docs/concepts/storage/volumes/ ( a volumes is declared separately)

Same here we use bind mount with `--v`: https://github.com/scoulomb/myhaproxy/blob/main/README.md


Note here we deploy Jellyfin directly on NAS, but if deployed in other machine, we can from Jellydin configure SMB/NFS access to remote.
Or we could mount NAS NFS/SMB as a volume: https://docs.docker.com/storage/volumes/#create-a-service-which-creates-an-nfs-volume

See also this note: https://github.com/scoulomb/myhaproxy/blob/main/README.md#run-workload-on-nas-or-raspi

### Step 2 Deploy on QNAP with compose

First create via control panel 2 shared folder: `jellyfin-docker` (which contain `/config`. `/cache`. `/cert`) and `QobuzDownloads`,

Container Station points to shared folder and not `/home/...`

We deploy with compose (+ create application in container section)

```` 
version: '3.5'
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    network_mode: 'host'
    privileged: true
    volumes:
      - type: bind
        source: /share/jellyfin-docker/cache
        target: /cache
        read_only: false
      - type: bind
        source: /share/jellyfin-docker/config
        target: /config
        read_only: false
      - type: bind
        source: /share/jellyfin-docker/cert
        target: /etc/letsencrypt/
        read_only: false
      - type: bind
        source: /share/QobuzDownloads
        target: /media
        read_only: true
    restart: 'unless-stopped'
    # Optional - alternative address used for autodiscovery
    #environment: with
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # Optional - may be necessary for docker healthcheck to pass if running in host network mode
    extra_hosts:
      - 'host.docker.internal:host-gateway'
````

Note `privileged :true` was not in provided doc compose file (but `uid:gi`d, which is also not working with explicit error message on QNAP).
It is necessary to have DLNA working on top of host network mode

The application is available at `http://scoulombel-nas:8096/`

Tested compose and appli with DLNA is working OK (be careful bad tls setup seems to break setup had to restart NAS)


Alternative we create equivalent config manualy (actually can explore/test before writing a compose file)
We need to ensure
- network mode is host
- privileged

Do not hesitate to use duplicate container features

Tested manual: and appli with DLNA is working OK (be careful bad tls setup seems to break setup had to restart NAS)

Note we can also disable DLNA for some speicific user in dashboard.

### Step 3: Perfrom TLS setup

#### Idea 1: Procure certificate without NAS and Server valiadation via Certbot [NOT WORKING]

Our idea was to procure certificate as we did in [DNS.md Objective 2](../../appendices/DNS.md#objective-2)
   
Here with server validation 

- (double) NAT rule to define to certbot server where WAN port is 80 and host port is 80 (port 80 -> intermediate port -> intermediate port (google box) -> 80 (Dell machine where we run certbot server)
- DNS A record music.coulombel.net to create

Then 

````
sudo certbot certonly --standalone
     
     Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/music.coulombel.net/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/music.coulombel.net/privkey.pem
This certificate expires on 2024-06-19.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

````

````
sudo cp /etc/letsencrypt/live/music.coulombel.net/* ~/jellyfincert/
````

Drag and drop file via qfile in Qnap ui or dragN'drop

Mount this volume in the docker  

==> pb private key not copiable easily


#### Idea 2: Procure certificate in the NAS (container) and TEXT valiadation via Certbot [WORKING]
  

Our idea was to procure certificate as we did in [DNS.md](../../appendices/DNS.md#objective-1-ha-in-https)

Try with container station shell but, can not bind on port 80 (used by Apache, could use it but better to use DNS TXT validation then)

So will use DNS TEXT challenge DCV method in container station shell


````
#  certbot certonly --manual --preferred-challenges dns 
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator manual, Installer None
Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
to cancel): music.coulombel.net
Requesting a certificate for music.coulombel.net
Performing the following challenges:
dns-01 challenge for music.coulombel.net

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name
_acme-challenge.music.coulombel.net with the following value:

D2I9diNtM0Ndo28L3HnhjUKTF6vuLhVAPLhY4lNsChE

Before continuing, verify the record is deployed.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue
Waiting for verification...
Cleaning up challenges
Subscribe to the EFF mailing list (email: cloud@coulombel.net).

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/music.coulombel.net/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/music.coulombel.net/privkey.pem
   Your certificate will expire on 2024-06-19. To obtain a new or
   tweaked version of this certificate in the future, simply run
   certbot again. To non-interactively renew *all* of your
   certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

````

Then we have to convert certificate to pkcs 12

````
cd /etc/letsencrypt/live/music.coulombel.net/
openssl pkcs12 -export -in fullchain.pem -inkey privkey.pem -out music.coulombel.net.pfx
chmod 777   music.coulombel.net.pfx # on pfx very important otherwise not working
```` 
 
And we restart container 

To access from outside ensure you natted (or double natter) port `8096`.

Use Jellyfin logs to debug cettificate issues

### Use HA proxy 

Can we do better? we are now facing exact same issue, 

We are falling in the exact same case as [here](../../appendices/DNS.md#add-certificates-alternative-use-a-reverse-proxy), described in  https://github.com/scoulomb/myhaproxy/blob/main/README.md#introduction with [objective 2](../../appendices/DNS.md#objective-2). 

Let's use HA proxy: https://github.com/scoulomb/myhaproxy/blob/main/README.md#introduction

And we can access via https://musik.coulombel.net


In particular see: https://github.com/scoulomb/myhaproxy/blob/main/README.md#ha-proxy-and-f5-re-encryption-comparison


### Ways to acess internal server from external

See
- https://github.com/scoulomb/myhaproxy/blob/main/README.md#we-have-seen-3-ways-to-access-internal-server-from-external
- https://github.com/scoulomb/myhaproxy/blob/main/README.md#ha-proxy-and-f5-re-encryption-comparison
- [DNS md appendice - VPN](../../appendices/DNS.md#secure-connection-via-vpn). 


HA proxy example is B (edge), whereas in section [above](#idea-2-procure-certificate-in-the-nas-container-and-text-valiadation-via-certbot-working), we were in case A with Direct NAT.

Same apply on Navidrome.


<!-- above ccl: we can eventually retry cert on jellyfin-->

## Navidrome setup on QNAP NAS

Alternative to Jellyfin is to use Navidrome.
Navidrome does not support DNLA but it supports Subsonic API server: https://www.navidrome.org/docs/developers/subsonic-api/

We will use the docker installation: https://www.navidrome.org/docs/installation/docker/

[ADD HERE DOCKER DETAUL]

We can not configure TLS directly on it, so we will use https://github.com/scoulomb/myhaproxy/blob/main/README.md
And we can access via https://music.coulombel.net

Reco to configure a Subsonic API client
- Amperfy (iOS)
- Submariner (MacOS)


See https://www.subsonic.org/pages/apps.jsp#android

In player configure transcoding: https://music.coulombel.net/app/#/player.
Working config is MP3 (64, 128). We need the docker ND_ENABLE paramter.

I noticed some latency issue in that case we could directly bypass the proxy and NAT directly Navidrome port. 

##  Music assistant

See https://blog.jlpouffier.fr/chatgpt-powered-music-search-engine-on-a-local-voice-assistant/ with music assitant
<!-- Lien linkedin -->

Advantage is that it enables pure DLNA grouping: https://music-assistant.io/player-support/universal/ (similar to AirPlay 2 multiroom)

Not offered by Jellyfin (we can go though heos group, or Volumio group).

See [mutliroom](../README.md#multiroom) 

REFVIEW SECTION AFTER [here](../../appendices/DNS.md#add-certificates-alternative-use-a-reverse-proxy)




----
In this exact setup: https://github.com/scoulomb/docking-station?tab=readme-ov-file#on-dell-precision-3540, I managed to have something working in the time with Dell Precision (setup B)
- Thunderbolt activated in Bios with user authorization (no boost support)
- setting > privacy > thunderbolt activated (new)

And on top of this setup in settings > display to activate the 3 scrrens (ensure we click on save)

Cool additional setup with 3 screens

However some bugs with mouse, sometimes not recognized 
So moved back to USB-C

Can had RPI by using free hdmi and ub switcher OK



<!-- cross ref sounds perfectly OK -->