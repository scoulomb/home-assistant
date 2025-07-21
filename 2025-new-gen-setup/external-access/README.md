# Configure external access to Internal Server using GL.iNet based router

Example of Jellyfin and Home Assistant

## GL.iNet is great at simplifying network topo

It will remove double NATing

As explained in [router setup](../Flint3-router-setup.md), we were able to plug directly to ONT to bypass provider box.
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
```

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
client -> WAN IP:443/80  ---BOX NAT --> Raspberry PI 5 IP :443/80 (Port NGINX proxy manager) --> Raspberry PI 5: 8123
````


<!-- alternative to LuCI not done 
Setup tiny proxy on glinet interface 
And the access on Luci: http://192.168.8.1:8080/cgi-bin/luci/admin/services/tinyproxy 
-->

Reminder on HA local port:
- 80: NGINX proxy manager HTTP Port + cert validation (I recommend to have it opened as HTTP-01 challenge only on 80: https://letsencrypt.org/fr/docs/challenge-types/)
- 443: NGINX proxy manager HTTPs Port + cert validation 
- 8123 default HomeAssistant port (`http` in config)


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
homeassistant.coulombel.net 
Scheme*; Forward Hostname / IP*; Forward Port *
http ;192.168.8.101 ; 8123
Ensure `Websockets support` is activated otherwise you could see this error
````


```shell
2025-07-21 13:10:39.798 WARNING (MainThread) [homeassistant.components.http.ban] Login attempt or request with invalid authentication from 163.116.176.129 (163.116.176.129). Requested URL: '/auth/token'. (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15)

```

See https://community.home-assistant.io/t/login-attempt-or-request-with-invalid-authentication-when-trying-to-access-remotely/373848/15



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

Here difference is that this Jellyifn server is not on PI 5/


```shell
% nslookup jellyfin.coulombel.net
[...]

Non-authoritative answer:
jellyfin.coulombel.net  canonical name = gw0a616.glddns.com.
Name:   gw0a616.glddns.com
Address: 78.116.176.161
```

Then do same operation as home assistant and forward to `http://192.168.8.102:8096`.

## Option to not use HA proxy.

As always we can directly NAT to end device (with a double NAT removed here).

<!-- Link to private_script/tree/main/Links-mig-auto-cloud/2025-consolidation/README.md => Details on Inbound via Standard virtual server (with HA proxy or not) -->

<!-- only remaining is tailscale optional CCL OK CLEAR 21 jul OK CCL-->