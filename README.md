# Home assistant setup

Intro to Home Assistant: https://www.youtube.com/watch?v=TaIwArlov_4

## Some initial setup

- Used https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md
- Recommended complement for this project
  - We can use Dell Precision and https://github.com/scoulomb/docking-station (see setup instruction)
  - I recomment to setup for this project
    - Editor: `apt install vim` + vs code from software application
    - Git: 
      - `Add ssh keys: `ssh-keygen` + https://github.com/settings/keys and clone via ssh
      - https://github.com/scoulomb/dev_vm/blob/master/saltstack/salt/common/git/gitconfig
        - Where we update email
        -for https://github.com/so-fancy/diff-so-fancy/issues/343: add path .bashrc and full path in gitconfig if not working
    - We will also complement natting and DNS configuration in particular for SSH in ["note on network section"](#note-on-network)

## Deploy Home Assistant via Docker Compose

https://www.home-assistant.io/installation/alternative/#docker-compose

### Lab env

- Did not use WSL here: https://github.com/scoulomb/misc-notes/blob/master/lab-env/others.md#use-wsl, or others
- Used https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md

### Quick deploy

````
version: '3'
services:
  homeassistant:
    container_name: homeassistant
    image: "ghcr.io/home-assistant/home-assistant:stable"
    volumes:
      - /PATH_TO_YOUR_CONFIG:/config
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
    privileged: true
    network_mode: host
````

and 

````
docker-compose up -d
````

Once the Home Assistant Container is running Home Assistant should be accessible using http://<host>:8123 (replace with the hostname or IP of the system).



## Installing Home Assistant (HA) on QNAP NAS

### Installing Home Assistant (HA) on QNAP NAS - Pre-req

- Create a shared folder from File station 
- Can delete the shared folder from Control Panel > Shared Folders
- Be careful to select image from Docker hub and not QNAP reco (older one)

### Installing Home Assistant (HA) on QNAP NAS - blog post

From
- https://www.home-assistant.io/installation/alternative/
- https://hackmd.io/@EIIupNI8Qn6uErVkCnaA0A/Skx0J79QG?type=view

Home Assistant https://home-assistant.io/


As QNAP within QTS now supports Docker (with a neat UI), you can simply install Home Assistant using docker without the need for command-line. For details about the package (including compatability-information, if your NAS is supported), see https://www.qnap.com/solution/container_station/en/index.php

The steps would be:

 - Install “Container Station” package on your Qnap NAS 
 - Launch Container Station and move to “Create”-section 
 - Search image  “homeassistant/home-assistant” with
   docker hub and click on “Install”
 - Choose "latest" version and click next
 - Choose a container-name you want (e.g.
   “homeassistant”)
 - Click on “Advanced Settings”
 - Within “Shared Folders” click on "Volume from host" > "Add" and
   choose either an existing folder or add a new folder. The “mount
   point” has to be “/config”, so that Home Assistant will use it for
   the configs and logs.
 - Within “Network” and select Network Mode to “Host”
 - To ensure that Home Assistant displays the correct
   timezone go to the “Environment” tab and click the plus sign then add
   `variable` = `TZ` & `value` = `Europe/London` choosing [your correct timezone](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
 - Click on “Create”
 - Wait for some time until your NAS has created the container
 - Your Home Assistant within Docker should now run and will serve the web interface from port 8123 on your Docker host (this will be your Qnap NAS IP address - for example `http://192.168.1.10:8123`)

Remark: to update your Home Assistant on your Docker within Qnap NAS, you just remove container and image and do steps again(Don't remove "config" folder)

If you want to use a USB Bluetooth adapter or Z-Wave USB Stick with Home Assistant on Qnap Docker, Fallow this step:

**Z-wave:**

 - Connect to your NAS over SSH
 - Load cdc-acm kernel module(when nas restart need to run this command)
    `insmod /usr/local/modules/cdc-acm.ko`
 - Find USB devices attached. Type command:
    `ls /dev/tty*`
    The above command should show you any USB devices plugged into your NAS. If you have more than one, you may get multiple items returned. Like : `ttyUSB0`
    
 - Run Docker command:
    `docker run --name home-assistant --net=host --privileged -itd -v /share/CACHEDEV1_DATA/Public/homeassistant/config:/config -e variable=TZ -e value=Europe/London --device /dev/ttyACM0 homeassistant/home-assistant`
    
    `-v` is your config path
    `-e` is set timezone
    
 - Edit configuration.yaml

```
zwave:
  usb_path: /dev/ttyACM0
```

That will tell Home Assistant where to look for our Z-wave radio.

**Bluetooth:**

 - Connect to your NAS over SSH
 - Run Docker command:
    `docker run --name home-assistant --net=host --privileged -itd -v /share/CACHEDEV1_DATA/Public/homeassistant/config:/config -e variable=TZ -e value=Europe/London --device /dev/ttyUSB0 -v /dev/bus/usb:/dev/bus/usb -v /var/run/dbus:/var/run/dbus homeassistant/home-assistant`
    
    First `-v` is your config path
    `-e` is set timezone
    
 - Edit configuration.yaml

```
device_tracker:
  - platform: bluetooth_tracker
```
## Compose on QNAP NAS, volume issue?

Same issue as for Denon heos API server
- https://github.com/open-denon-heos/heos-api-server/blob/main/README.md#using-docker-in-dev-mode
- https://github.com/open-denon-heos/heos-api-server/blob/main/README.md#with-volume-mapping
  
Alternative could be https://github.com/scoulomb/misc-notes/blob/master/lab-env/others.md#but-discover-container-station-can-deploy-a-k3s-natively
<!-- see also https://github.com/scoulomb/misc-notes/blob/master/replicate-k8s-ingress-locally-with-compose/README.md#k3s, not documented in heos, https://github.com/scoulomb/TODO-perso ref clear -->

  
## Store config in git
  
See also https://community.home-assistant.io/t/sharing-your-configuration-on-github/195144


## Note on network

Before read some NAT foundation on top of this repo at 
- https://github.com/scoulomb/docker-under-the-hood/blob/main/NAT-deep-dive-appendix/README.md#nat-deep-dive <!-- chema compliant between this doc and here, and detaill the @home -->
- Links-mig-auto-cloud/README.md#migration-and-snatdnat <!-- link made ok -->

Also in this repo we gave example of some NATing and DNS usage: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-a.md.
This repo is linked (and consistent) to DNS section [of this file](#note-on-mdns).

We also had NAT configuration here (no NEST router): https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md#add-a-nat-rule-to-access-from-internet

See also NAT and [VPN](./appendices/VPN.md).

### Config 

At home with Google Wifi

- SFR Box (Modem + Router) (Wifi + Many eth)
- Google Nest Home (Router) (Wifi + 1 external eth + 1 eth conneced to SFR box eth)


### Double NAT with devices on 2 networks

If NAS on SFR box network via ethernet (B), denon device on Google Next Wifi (A)

Schematically


````
[Client Source IP, Source Port] --Internet--> [SFR: WAN IP, WAN/DNAT Port] --SFR LAN-->  [Google Nest: WAN IP, WAN/NAT Port] --Google Nest LAN-->  [Laptop/Device IP, Laptop/Device Port] - A
                                                                           --SFR LAN-->  [Laptop/Device IP, Laptop/Device Port] - B
````

We can access NAS from device in google wifi network (SNAT)
But if home assistant is on the NAS, to access smart speaker on Google WIFI network need to configure DNAT (port management in google home app) and use Google router WAN IP.

What is did in Google Home App Port Management
`TCP/UDP 1255 -> 1255 Denon AVR x2700h - only TCP is required, this is for telnet HEOS API (note denon avr integration (non heos requires standard telnet port 23)`
`TCP/UDP 1900 -> 1900 Denon AVR x2700h for UPNP disvovery but unused - only UDP is required`

In BOX UI: http://192.168.1.1/network

````
# 	Adresse MAC 	Nom d'hôte 	Adresse IP 	Port
1 	xx:xx:xx:xx:e3:d2 	test-dns 	      192.168.1.58 	      LAN 1   <- Google NEST IP in SFR LAN
2 	xx:xx:xx:xx:2b:f7 	scoulombel-nas 	192.168.1.88      	LAN 3   <- NAS         IP in SFR LAN
````

Then in Home Assistant delete HEOS integration. 
http://192.168.1.88:8123/config/integrations/integration/heos

And add integration again we have a prompt

````
Please enter the host name or IP address of a Heos device (preferably one connected via wire to the network).
````

Here we enter Google Nest WAN IP: 192.168.1.58

So that it targets speaker, with port 1255 (from heos cli pdf sepc). We  will see the 2 speaker (home 150, avr).
UPNP is not used.
Magic is that Denon Home is also recongized (as part of heos even if NAT only done to AVR)

<!-- I managed to have this work again 24aug23 -->

However we saw some issue with UPNP : Media server on NAS and remote control app: https://github.com/open-denon-heos/heospy/blob/main/heospy/ssdp.py#L38 (also use non heos command for power shut down requires extra port 23).
- http://192.168.1.88:8000/ (HEOS CLI port) -- If we restart HEOS container in container station discovery does not work even if UPNP port 1900 forwarded (this was tested OK) <!-- initial test -->

- Same with home assistant (this was tested OK) <!-- do not retry Ok replugged for retest -->



### Can we avoid this Double NAT??

In my case Bridge mode is not availalble: https://support.google.com/googlenest/answer/6277579?sjid=11569360593923687828-EU.
Not that even 
>  `Enable Bridge mode on your Wifi router device` is not possible as WAN IP is public (so not renatting on ISP side, in that case we would have a 3 NAT layer).

I will not consider VPN option: https://networkengineering.stackexchange.com/questions/40773/how-to-make-ipsec-over-double-nat


### A wired solution 

Have all device in Google Nest Home LAN
- to avoid NAT issue between devices in SFR LAN and Google NEST LAN.,
- Benefit from UPNP,
- Manage all devices in Google Nest ,
- Simplify Somfy hub (in nest wifi) with Philips Hue

We will use Ethernet port of Google Nest HUB. 
- We plug a L2 Switch to Nest external eth port
- Then Nest router connected to SFR box directly via primary ethernet port.
- We connect NAS (but also Philips Hue Hub) to the switch

**Drawbacks** (we will see [below](#eliminate-drawbacks-of-the-solution), how to eliminate them.

 - Will lose WOW (Wake on Wan) via WOL PROXY CONFIGURED IN THE BOX: https://github.com/scoulomb/misc-notes/blob/master/NAS-setup/Wake-On-LAN.md#setup-2b-wow-with-cloud-server
 - To access NAS service from outside (internet), we will need Double NAT (or simple NAT for devices in SFR LAN (but nothing should now be there))


When doing this we get NAS IP from Google home app (or use mdns)
- http://192.168.86.20:8000 -- Restart container -- HEOS SSDP discovery worked
- http://192.168.1.88:8123/config/integrations/dashboard -- Restart container -- SSDP discovery worked

### Trying to eLiminate drawbacks of the solution


Use-case: I want to access HomeAssistant in NAS with below topology and where bridge mode is available, without a VPN from Intenet

````
[Client Source IP, Source Port] --Internet--> [SFR: WAN IP, WAN/DNAT Port] --SFR LAN-->  [Google Nest: WAN IP, WAN/NAT Port] --Google Nest LAN-->  [NAS IP, Port=8123]
````


#### Solution 1: Double DNAT

If NAT config not required for call inside home, we need double NAT for outsode access

I configured a double port forwarding , for instance in SFR BOX IPv4 NAT

````
1 	ha 	TCP 	Port 	8123 	192.168.1.58 	8123 	
2 	nas TCP 	Port 	9080 	192.168.1.58 	8080 	
3 	ha 	TCP 	Port 	9123 	192.168.1.58 	8123
````

And in Google Home APP 

`Network settings > Advanced settings > Port mgmt`, do natting 

````
8123 -> NAS:8123
8080 -> NAS:8080
````

After this I can access from outside home (4g), this is working.
- to HA using pub WAN IP  (SFR WAN IP `109....`) and port 8123 or 9123
- NAS UI using pub WAN IP (SFR WAN IP `109....`)and port 9080

We can also double forward port 443 as NAS will allow access via both HTTP (8080) and HTTPS (443)

````
x 	nas-sec  TCP 	Port 	9443 	192.168.1.58 	8443 	
x 	nas-sec2 TCP 	Port 	443 	192.168.1.58 	8443 	
# `Network settings > Advanced settings > Port mgmt`, do natting 
8443 -> NAS:443
````

#### Solution 2: Use DMZ 

DMZ will forward all incoming traffic from outside to a chosen device in SFR LAN.
We choose this device to be the NEST gateway.

````
Activation du DMZ 	
Adresse Ip 	: 192.168.1.GOOGLE_NEST_WAN_IP
````

And in Google Home APP 

`Network settings > Advanced settings > Port mgmt`, do natting 

````
8123 -> NAS:8123
8080 -> NAS:8080
````

After this I can access from outside home (4g), this is working.
- to HA using pub WAN IP  (SFR WAN IP `109....`) and port 8123 
- NAS UI using pub WAN IP (SFR WAN `109....`)and port 8080

It is a workaround to bridge mode: https://la-communaute.sfr.fr/t5/installation-et-param%C3%A9trage/nb6vac-utilisation-en-mode-bridge/td-p/2327729 

#### Solution 2, does it allow to do WOW!?

See https://github.com/scoulomb/misc-notes/blob/master/NAS-setup/Wake-On-LAN.md#in-practise
And just re-use 
- Setup made in Android APP 
- And box has proxy wake on lan + dmz activated

Unforutanetly not

#### About SSH 

Trying to do equivalent of 
- https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md#add-a-nat-rule-to-access-from-internet with double NAT
- https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md#add-ssh

SSH did not work in ny test to hp pavillon in google wifi both with
- NAT 
- And DMZ

See potential reasons: https://serverfault.com/questions/404516/ssh-not-working-through-double-nat

Thus either use local IP if in NEST LAN or connect this machine to SFR wifi when access required from Internet.

I managed to have this working with Precision: https://github.com/scoulomb/docking-station#misc-notes

````
# box
3	ssh	TCP	Port	22	192.168.1.58	2222 (where .58 is nest router)

# Ghome app - port forwarding
2222 -> 22 (laptop ip, wait if not seen, can have old name attached to mac@)
````
See [Appendices DNS/SSH](./appendices/DNS.md#ssh) (IP and then with domain (see  [Note on (m)DNS and certificates](#note-on-mdns-and-certificates))
<!-- See [Tuya API](./Tuya-IR-controller/tuya-api.md) -->



#### What do keep?

Use wired solution with double DNAT rule.
<!-- ok nw ccl - retested double nat OK -->
<!-- Note tuya and hue do not need NAT, probably socket is established from outbound and not inbound, even if msg flow is inbound - OK CCL -->

_________________________


<!-- In this page concluded NAT with 
Links-mig-auto-cloud/README.md#migration-and-snatdnat
https://github.com/scoulomb/docker-under-the-hood/blob/main/NAT-deep-dive-appendix/README.md#nat-deep-dive
https://github.com/scoulomb/home-assistant/blob/main/README.md#note-on-network, review not required a link made with @home
See https://github.com/scoulomb/home-assistant/commit/ef7ba4bd7ebdae1af27a0ab66b21bb4e4ff34650 (Work1A stuff should not impact but can update even if other commit in HA repo in btw)
-->
<!-- OK - spearator NAT commit OK (many topics no NAT, and NAT update no more check) --> 

## Note on (m)DNS and certificates

 See [Appendix on (m)DNS](./appendices/DNS.md). <!-- ccl -->

 Note SSH on NAS and Precsion at [Appendix on (m)DNS](./appendices/DNS.md#intro).
 Good alternative to multidesk with https://github.com/scoulomb/docking-station


 <!-- EDIT:
 Was well concluded
 https://github.com/scoulomb/home-assistant/blob/191da58ec8d6314ff889a67a286e3595d75a5daf/appendices/DNS.md?plain=1#L29

 https://github.com/scoulomb/home-assistant/blob/191da58ec8d6314ff889a67a286e3595d75a5daf/appendices/DNS.md?plain=1#L35

 And link obj 1 and 2 well made with above 
 https://github.com/scoulomb/home-assistant/blob/191da58ec8d6314ff889a67a286e3595d75a5daf/appendices/DNS.md?plain=1#L350
 https://github.com/scoulomb/home-assistant/blob/191da58ec8d6314ff889a67a286e3595d75a5daf/appendices/DNS.md?plain=1#L481
 Check and OK nore than sufficient
 Then all 4 oct commit shows OK
 STOP

 And note that 

 "See [Appendices DNS/SSH](./appendices/DNS.md#ssh) (IP and then with domain (see  [Note on (m)DNS and certificates](#note-on-mdns-and-certificates))
 compliant with https://github.com/scoulomb/home-assistant/blob/191da58ec8d6314ff889a67a286e3595d75a5daf/appendices/DNS.md?plain=1#L6
 -->

 <!-- https://github.com/scoulomb/docking-station/commit/7a09cd14c2616066e4082c57424128fc2939b38c#commitcomment-128854058 OK CCL 
 + https://github.com/scoulomb/docking-station/commit/7a09cd14c2616066e4082c57424128fc2939b38c#commitcomment-129601917 (borrowed laptop) OK -->

 <!-- EDIT: see comment last line where linking done 
 https://github.com/scoulomb/docking-station/commit/5a65b6d1ce9e36a191e9a90b194ba4e4edba724c (circular ok stop here)
 -->

<!-- so dns is really ccl STOP, and rework backlog do not recheck that ci, and check quick OK stop-->
<!-- Added ref ci: https://github.com/scoulomb/home-assistant/commit/223239b848add5c4ae1b9a2dfdca894120034231 -->


## Note on QNAP Smart URL and file sharing

See [Note on QNAP Smart URL and file sharing](./appendices/file-sharing/README.md)

<!-- note with DNS OK and this was written after -->
<!-- CONCLUDED OK, only optional stuff OK -->

## Note on VPN

[VPN usage and NAS](./appendices/VPN.md)

<!-- See link to https://github.com/scoulomb/home-assistant/commit/e4dc75b2c6ad43c70aea40947ec33e411feeab5e OK -->
<!-- this is ccl -->

## Note on UPnP and UPnP IGD 


See [Appendix on UPNP](./appendices/UPNP.md)


IGD subpart of UPnP.

<!-- concluded OK, well done -->
<!-- ALL NETWORK APPENDICES DONE: https://github.com/scoulomb/home-assistant/commit/30d72433462800fd69baa99c1da8f01dd1627d59#diff-bfb4e89cd42e2d89ad2e4e402b397857ebe2e6dd2cff8af4e0f9ee2c32bc9c95R229, recf 13oct23 1:05 PM OK -->
<!--and commit after reamde update ok-->


## Projects


- [Tahoma integration](./Tahoma/tahoma-integration.md)
  - Tahoma open/close (optional vendor follow-up only: https://github.com/scoulomb/home-assistant/commit/7dd77264627883e46a170a73e414870607d48722 + https://forum.somfy.fr/questions/3220107-volet-roulant-io-inverse-google-home#answer_8397238 (reply OK)) 
  <!-- volet montage final ccl 
  https://github.com/scoulomb/home-assistant/commit/6e413c0fd0175fd6519cbaa95a6e7b762876fcf2 -->
- [Tuya IR](./Tuya-IR-controller/README.md)
- [Other integration](./Other-integration/README.md)
- [Some automation sample](./Some-automation-sample/README.md)
- [ESPHome](./espHome/README.md)

## Apple TV 

[See Apple TV in Docking station](https://github.com/scoulomb/docking-station/blob/main/README.md#apple-tv-4k-3gen)

<!-- ccl OK STOP: https://github.com/scoulomb/docking-station/commit/7a09cd14c2616066e4082c57424128fc2939b38c -->

## Apple smarthome ecosystem as alternative to HA

See [Apple ecosystem](./apple-ecosystem/README.md).


## Next to check -- HERE

<!-- - Pointer of section OK clear (but come back on point referenced here only), commit 729e389 ok no come back osef-->

### Interesting

- Paper notes (letter)
- Optional tagged part in [Note on QNAP Smart URL and file sharing](./appendices/file-sharing/README.md) 
- Volet: [Scenario](./Tahoma/hardware-remotes/lanceur-scenario.md) -> Docker image (HA staging aera == secdata file moved to https://gist.github.com/scoulomb/ac0b63607102e4d94abcc562d33d6f06)
- Also apple HomeKit. Check [Apple ecosystem](#apple-smarthome-ecosystem-as-alternative-to-ha)
  - Resetup (see paper) via HomeKit
    - https://www.philips-hue.com/fr-fr/explore-hue/works-with/apple-homekit/set-up#Je_suis_dj_connect__Apple_Home_mais_je_souhaite_utiliser_Matter__la_place_Comment_changer
    - https://service.somfy.com/downloads/be_v5/faqhomekit_and_tahoma_compatibility.pdf
  - Mac/iphone/apple tv integration + Shortcuts (same ghome)
  - Apple TV in HA
  - Thread (home assistant -> thread -> 3 borders routers) / Matter
  - Integration via Matter or HomeKit or Provider Api (like Alexa) (example of Hue)
    - https://www.numerama.com/tech/1170068-matter-va-revolutionner-la-maison-connectee-tout-savoir-sur-cet-incroyable-alliance.html
- sock listen and receive: lien http socket
  - https://www.qnx.com/developers/docs/qnx_4.25_docs/tcpip50/prog_guide/sock_advanced_tut.html
  - https://stackoverflow.com/questions/6810444/two-way-communication-in-socket-programming-using-c
- note vs code end
- VPN config file to understand optionally (DO NOT DO: do not try to use ddns here, commit ccl upnp STOP ;) Stop)
- Somfy vendor follow-up [optional](#projects)
- link vs code

### Very optional

- ESPHome + lampe Quechua
- Hue ligths  micro coupure (see [other integ](./Other-integration/README.md)) 
- Izymo on/off
- Curl command from HA (to use denon, tahoma local API)
- We can do equivalent of HA using GoogleHome including levave home location (equivalent to what described in [Tahoma Scenario](./Tahoma/hardware-remotes/lanceur-scenario.md))
- Equivalent to Tahoma scenario via hue button (promo darty)
- Ant+ : https://gist.github.com/scoulomb/a5ad314e3c9f1c9a39c58aebaa13d4bf + fan shutter
- gitconfig as in beg of this doc in mac (also this readme and [DNS](./appendices/DNS.md) complements original doc: https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md which is till valid and keep it like this OK STOP)
- QNAP 2FA
<!-- tahoma app working when ehtenet hub -> normal it is on wifi -->
<!-- this repo is ready OK -->
<!-- tips for reduce pic size is to use snipping tool -->

<!-- ignore rick graziani video on nat -->

<!-- ok as part ref in vs code, we have all here under seprarator ok-->
<!-- commit verified in lab env osef ok -->
<!-- firmare update 5410 changes nothing as usb-c for docking -->