# Configure external access to Internal Server using GL.iNet based router

Example of Jellyfin and Home Assistant

## GL.iNet is great at simplifying network topo

It will remove double NATing

As explained in [router setup](../flint3-router/1-Flint3-router-setup-SFR), we were able to plug directly to ONT to bypass provider box.
Thus removing the double NAT in our TCP + TLS connection to Home Assistant.

```shell
client -> SFR WAN IP:443 -> Box 8 ---BOX NAT ---> Google Home WAN IP:8443 --> Google router NATing --> LAN IP 
````

Becomes 

````shell
client -> WAN IP:443  ---BOX NAT ---> LAN IP
````


## Usage of HAOS

We are now using HAOS instead of running HA in Docker on NAS.
Additionally, it supports add-ons.


## DynDNS 


GL.iNet has dynDNS integration.

Pre-req to below is to activate it here: http://192.168.8.1/#/dynamicdns

## Use static IP for convenience

Go to http://192.168.8.1/#/lanip

And for example apply following

```shell
192.168.8.101	homeassistant	
192.168.8.102	scoulombel-nas	
192.168.8.103	Slzb mr3
----
192.168.8.111	atollstreamer-ms120 # webcard page in HA to http://192.168.8.111/webclient (not in https webcard page will not work as http, though we could use proxy in front of ms120 with restricted source in nginx proxy, do not do)
```
We need a new DHCP request therefore restart router or end device.
For DHCP details see [here](../../sound-video/dns-sd.md#zeroconf-ip-auto-assignment)

## Method 1:Use a VPN


- When using QVPN we had to NAT (and double NAT here) to VPN port on the NAS.
    - See: [appendices/VPN-tailscale.md](./../../appendices/VPN.md)

- With integration there are 0 NAT to do in the LAN.

- Start wireguard server: http://192.168.8.1/#/wgserver
- Go to `profile tab > add > give name > scan QR code from Android client or copy generated conf`
- Note you can not use mDNS via VPN (option would be a public DNS to private IP)


## Method 2: use tailscale (not tested)

We had to setup Tailscale on each client (Tailscale on NAS), here we can setup at router level.
See: [appendices/VPN-tailscale.md](./../../appendices/VPN-tailscale.md)

When using Add-ons in HA we could also setup tailscale HAOS add-ons.


## Method 3: use HA proxy 

### Topology

We can now use NGINX proxy manager add-ons instead of https://github.com/scoulomb/myhaproxy/blob/main/README.md#ha-proxy-routing

Therefore LAN setup becomes

````text
HA proxy Raspberry -> Home Assistant port in NAS
````
to 

```text
Raspberry PI 5 IP :443 (Port NGINX proxy manager) --> Raspberry PI 5: 8123
```

Here Raspberry PI 5 HA is runnng HA and Proxy manager add-ons.

With double NATing removed we have full picture


````shell
client -> WAN IP:443/80  ---BOX NAT --> Raspberry PI 5 IP :443/80 (Port NGINX proxy manager - HomeAssistant add-ons) --> Raspberry PI 5: 8123 (HomeAssistant)
````


<!-- alternative to LuCI not done 
Setup tiny proxy on glinet interface 
And the access on Luci: http://192.168.8.1:8080/cgi-bin/luci/admin/services/tinyproxy 
-->

### Reminder on HA port

Reminder on HA (`192.168.8.101`) local port:
- 80: NGINX proxy manager HTTP Port + cert validation (I recommend to have it always opened as `HTTP-01` challenge only on 80: https://letsencrypt.org/fr/docs/challenge-types/, even if the HTTP challenge can be done in 443 via `TLS-ALPN-01` (but it does not seem fully supported: https://github.com/NginxProxyManager/nginx-proxy-manager/issues/158 - will not do full test<!-- renew work osef -->). We could also use `DNS-01` validation as an alternative)
- 443: NGINX proxy manager HTTPs Port + cert validation via `TLS-ALPN-01` when supported.
- 81: NGINX admin interface
- 8123 default HomeAssistant port (`http` in config)

All those port accessible locally (proxy routing 80/443 based on header will fail <!--not try more-->)

Thus
- Natting to HA:80/443 (proxy) 
- and proxy to backend
  - HA:8123 (same for HA and proxy)
  - [Jellyfin:8096](#access-to-jellyfin-) below
  - and not exposing backend directly  + TLS

See [cert details](./cert-terminology/README.md)

We do not encrypt inside LAN (HA proxy to back-end <!-- unlike F5 to app, see parallel when cascading F5 and nginx here: private_script/ /Links-mig-auto-cloud/2025-consolidation 
and link with [](./cert-terminology/README.md#self-signed-and-signed) OK -->)

Note port can be configured here: http://homeassistant.local:8123/hassio/addon/a0d7b954_nginxproxymanager/config

### Tuto


- Define Dynamic DNS: http://192.168.8.1/#/dynamicdns
- And DNS CNAME to Dynamic DNS (wait a bit) on squarespace : https://www.squarespace.com

- Verify DNS setup

```shell
% nslookup homeassistant.coulombel.net
[...]
Non-authoritative answer:
homeassistant.coulombel.net	canonical name = gw0a616.glddns.com.
Name:	gw0a616.glddns.com
Address: 78.116.176.161 
```

- Allow port forwarding to HomeAssistant
http://192.168.8.1/#/firewallview

````shell
1	
TCP/UDP
WAN
80
LAN
192.168.8.101:80
---------
2	
TCP/UDP
WAN
443
LAN
192.168.8.101:443
````

- Create reverse proxy cong in HA and restart
See https://www.home-assistant.io/integrations/http/#reverse-proxies

In configuration.yaml at http://homeassistant.local:8123/a0d7b954_vscode/ingress (allowed all private range)

````shell
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16
  ip_ban_enabled: true
````

And restart HA: http://homeassistant.local:8123/developer-tools/yaml

In our case it was not, NOT working due to ip_ban but this missing config.
See also doc here: https://forum.hacf.fr/t/acces-de-l-exterieur-en-https-avec-nginx-proxy-manager/1761


-  Request a cert there: http://homeassistant.local:81/NGINX/certificates

- Create a proxy host using this certificate 

````shell
Details
-------
# Domain names
homeassistant.coulombel.net 
#Scheme*; Forward Hostname / IP*; Forward Port *
http ;192.168.8.101 ; 8123
# `Websockets support` 
is activated otherwise you could see error below
#Access list
publicly accessible

SSL 
-------
# SSL certificate
Select homeassistant.coulombel.net created previously
# Force SSL
Set to true to redirect 80 to 443
````

When `Websockets` support not activated. You will have this error when performing a login attempt.

```shell
2025-07-21 13:10:39.798 WARNING (MainThread) [homeassistant.components.http.ban] Login attempt or request with invalid authentication from 163.116.176.129 (163.116.176.129). Requested URL: '/auth/token'. (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15)
```
Note that to avoid to disable port 80 mapping on router, used for certificate DCV (see steps above), we ensure Force SSL is set to true.
- When set to false: http://homeassistant.coulombel.net:80 => unsecure
- When set to true: http://homeassistant.coulombel.net:80 => redirection to https://homeassistant.coulombel.net/ (tested OK)
- This is equivalent to 
  - Apache: https://stackoverflow.com/questions/16200501/how-can-i-automatically-redirect-http-to-https-on-apache-servers
  - F5: https://my.f5.com/manage/s/article/K10090418: use iRule, if standard port can use system iRule `modify /ltm virtual <virtual server name> rule { _sys_https_redirect }`
    - F5 AS3: `"class": "Service_HTTPS"` when using standard port: https://clouddocs.f5.com/training/community/automation/html/class03/module1/lab02.html
    - Can also use policy (not for case above with iRule we also have a dedicated vs, for as3 would need to check internals): https://github.com/scoulomb/private_script/blob/f10f59118f9bbb4e8e9d8b732461d9308274cbed/Links-mig-auto-cloud/2025-consolidation/Inbound/README.md#ip-move (BB)
<!-- link with /private_script/ /Links-mig-auto-cloud/2025-consolidation/README.md - Linking sufficient here -->

The scheme HTTP is between proxy and target server <!-- similar f5-gw in private-script -->

See related post: https://community.home-assistant.io/t/login-attempt-or-request-with-invalid-authentication-when-trying-to-access-remotely/373848/15

See [how we can do equivalent with IPv6](../flint3-router/3-deep-dive-on-ipv6.md).

## DuckDNS add-ons to replace dynDNS glinet


- We can generate a dynamic DNS with Duck DNS in home assistant add-ons 
- Then we can use NGINX Proxy manager  add-ons to 
    - generate duckdns certificate with Dynamic DNS provider 
    - Expose from the proxy home assistant via https://scoulomb.duckdns.org:443
- Not we can not in ALT name have another domain like coulombel.net as DCV is not possible from Duck DNS perspective
- The alias in Duck DNS UI seems useless (they even do not define a CNAME) — 

Better to use coulombel.net (DO NOT TEST)
- Via NGINX proxy manager generate with let’s encrypt coulombel.net cert 
- And then use home.assistant. homeassisant.COULOMBEL.NET CNAME scoulomb.duckdns.org what we did above with [webserver validation](#Tuto)

<!--
See contact Jerome M AND DCV VALIDATION discussion OK -- optional conv 
-->

See links with: https://github.com/scoulomb/dev-resume-2025/ for certificates.

See certificate is on domain requested by client: https://stackoverflow.com/questions/9935229/cname-ssl-certificates
> Whether your DNS entry uses a CNAME or an A record doesn't matter. What matters is the host name the client is trying to connect to. 
<!-- consistent duck dns section here ok -->


## Access to Jellyfin 

Here difference is that this Jellyifn server is not on PI 5.



```shell
% nslookup jellyfin.coulombel.net
[...]

Non-authoritative answer:
jellyfin.coulombel.net  canonical name = gw0a616.glddns.com.
Name:   gw0a616.glddns.com
Address: 78.116.176.161
```

Then do same operation as home assistant and forward to `http://192.168.8.102:8096`.

````shell
Details
-------
# Domain names
jellyfin.coulombel.net 
#Scheme*; Forward Hostname / IP*; Forward Port *
http ;192.168.8.102 ; 8096
# `Websockets support` 
is activated otherwise you could see error below
#Access list
publicly accessible

SSL 
-------
# SSL certificate
Select jellyfin.coulombel.net created previously
# Force SSL
Set to true to redirect 80 to 443
````

The local Jellyfin port can be defined at: http://192.168.8.102:8096/web/index.html#!/networking.html

## Option to not use HA proxy.

As always we can directly NAT to end device (with a double NAT removed here).
Amd aborted tuto to configure [Jellyfin in TLS](../../sound-video/setup-your-own-media-server-and-music-player/README.md)

<!-- Link to private_script/tree/main/Links-mig-auto-cloud/2025-consolidation/README.md => Details on Inbound via Standard virtual server (with HA proxy or not) -->

<!-- only remaining is tailscale optional CCL OK CLEAR 21 jul OK CCL, jellfin TLS comment above not do-->

## VPN usage

VPN can be used to fix issue, like access to `192.168.8.101:81` (homeassistant add-ons) to fix nginx issue. cf [HA port](#reminder-on-ha-port).

<!-- link with private-script in inital d notes ok as implicit and documented, same with slzb dojo -->
<-- external access above is FULLY concluded OK -->
<!-- mydomain unliked duckdns not considered as new domain from corp -->

## Other backend

We can add Navidrome on port 4533 and other back-end later. <!-- do not prevent from ccl as obvious -->
Why Navidrome? Jellyfin transcoding is blurry. We can set internet bitrate streaming only:
- Globally: > administration > dashboard > server> playback : `/web/index.html#!/streamingsettings.html`
- Per user: > administration > dashboard > server> user > select user 

We can check in Mac OS with `Activity Monitor`, `> Network tab`, when a song start we have around ~30 mb of data received <!-- (not here message flow dir != from socket) , private_script: private_script/ /Links-story-notes/socketEstablishmentDirection.md -->

<!-- fully ccl OK as other BE optional and mentioned in -->
See [](./../README.md) 
<!-- as such this file not in apple notes -->