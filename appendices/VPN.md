# VPN usage 

## Into

Alternative to 
- Setup several TLS certifivate as in [DNS add cert](DNS.md#add-certificates) -> we will have only 1 VPN certficate
- Define several NATs rule as seen in [DNS intro](./DNS.md#intro) -> we will have only 1 VPN NAT rule
    - We can use [UPNP IGD](UPNP.md#upnp-igd-nat-traversal), to avoid defining sveral NAT rules manually 
    - For VPN we have 1 NAT rule (VPN port), but it does not prevent from using UPNP to NAT this port

So we will be like in local and only need to forward 1 port (the VPN port).

See legacy doc: https://github.com/scoulomb/misc-notes/blob/master/NAS-setup/README.md#configure-a-vpn-to-lan-via-nas

Link to 
- private_script/Links-mig-auto-cloud/aks-istio-and-azure-nat.md and 
- https://github.com/scoulomb/myPublicCloud/blob/master/Azure/Networking/basic.md
But those 2 link concluded and clear


Check vpn micode: https://www.youtube.com/watch?v=ckZGQ5cLIfs where it is clear we have: 
- VPN to connect to remote local network
- And have outboubd connection from IP adress (SNAT) linked to remote local network
<!-- consider ok -->

So we will start adding a NAT port on top of what we defined in [DNS intro](./DNS.md) <!--  xref OK-->

http://scoulombel-nas:8080/cgi-bin/ -> QVPN service

## VPN Techno

QNAP URL offers several VPN techno including 
- QBelt
- PPTP
- L2TP/IPSec
- OpenVPN
- WireGuard
We will select OpenVpn 
<!-- do not try qvpn, maybe use smart URL? -->


For the client I will use OpenVPN clientn (but cloud use QVPN)


## Natting

In QVPN we can default port (but can be changed) for OpenVPN is UDP 1194.


````
http://192.168.1.1/network/nat
OpenVPN 	UDP 	Port 	1194 	192.168.1.58 	11194

GHome / Port management
11194 -> 1194 ( to NAS) / UDP (all other rules were in TCP, first UDP rule in this doc)
````

Now rules are defined.

## Connect to VPN via Phone

Do the test from IPhone
- Disable wifi for test
- We will download config file from QVPN in NAS UI and send by email
- We will install OpenVPN client on IPhone
- In iPhone use mail app to open ovpn attanchment  
    - Alternative save mail attachment to file in iCloud 
    - or could have also directly share it in  NAS and get it from QFile)
- In OpenVPN app : Prompt NAS ad usernme and pwd
- Connect
- And then act as if locally:
    - htttps://scoulombel-nas:8123 (use https if we have cert) OK
    - 192.168.1.1 -> router OK
    - However, I observed 
        - qlink.to/scoulo -> resolved to ddns (with 443 NAT rules)
        - and if I disabled all NAT rule execept VPN resolved locallt
        - Same behvaior as locally here. See [qnap-smart-url](./file-sharing/qnap-smart-url.md) <!-- OK -->
        - Note HEOS UPNP does not seem to work
- From phone which is in 4G -> what is my IP gives SFR `109.29....` -> VPN is working

Note actually when VPN connected I can disable the NAT rule, but I will not be able to reconnect --> Wrong see [UPNP.md](./UPNP.md#upnp-igd-nat-traversal)

## Netflix and VPN 

Netflix certified devices based on IP regulalrly (meaning traffic as to come from household).
Thus we could connect device to VPN so that it looks like traffic coming from household.
With this technique I can certify all iphone,ipad, android phone and tablet.
But we have an issue on end device (apple tv, firetv stick, connected tv) whwre VPN client setup is complex.

### VPN on end device

However when we check
- Apple TV does not have OpenVPN client 
- Installing OpenVPN on firetv stcik is a nigthmare:https://help.streamvia.com/VPN/FireTV/OpenVPN
- Or any connected TV

So not a good option

This is a point to site VPN. We would like to achieve site to site VPN.

### Share phone WIFI

My idea is the following
- We connect IPhone to VPN (0pen VPN client on phone)
- We share wifi connection
- We connect firetv/apple tv/laptop (using laptop for test) to IPhone wifi

Issue: VPN connection is used only by Phone but not used by devices using phone wifi hotspot.


Displayed on devices using hotspot is SFR 4G whereas phone connection is using house IP (what is my IP)

This is a known behaviour

- https://www.reddit.com/r/OpenVPN/comments/y26ac5/wifi_hotspot_or_tethering_with_android_phone/
- https://apple.stackexchange.com/questions/273218/ios-hotspot-vpn-behavior
- https://discussions.apple.com/thread/8392148


We could use a device like this between phone and devices using shared connection 
https://www.amazon.fr/GL-iNET-GL-MT300N-V2-Pre-installed-Performance-Compatible/dp/B073TSK26W/ref=asc_df_B073TSK26W/?tag=googshopfr-21&linkCode=df0&hvadid=314673282442&hvpos=&hvnetw=g&hvrand=9321162626209930904&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9054964&hvtargid=pla-491876105460&psc=1&tag=&ref=&adgrpid=61115195445&hvpone=&hvptwo=&hvadid=314673282442&hvpos=&hvnetw=g&hvrand=9321162626209930904&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9054964&hvtargid=pla-491876105460



If I share connection via USB and where VPN client is still on Phone we still have the same issue.

So not a good option 

### laptop hotspot + phone USB with 4G


Idea is the following
- 1. We connect IPhone to Internet direclty (4G). Wifi is disabled. We do not foget to diconect OpenVPN client on Phone
- 2. We share connection via USB port to Dell Precsion (settings, network, usb ethernet)
- 3. We setup VPN on Dell Precision (settings VPN import from file). Fix username to admin in settings if required
    - 3-Check Here we should see Home IP `109.29....` with the VPN: https://whatismyipaddress.com/
- 4. We turn on Wifi, and wifi Hotpsot on Ubuntu (it disables regular wifi) (settings, wifi, 3 dots)
- 5. We connect firetv/apple tv/laptop (using dell laitude 5410 laptop for test) to Precsion wifi (connect using a security key, not pin)
- 6. We expect to see Household (109.29....) IP address


#### Issue on step 3


Come back to LAN to debug (so connect on VPN even if lan)

Seems to be a cert issue 

````
sudo tail -f /var/log/syslog
----
Oct 12 14:28:40 scoulomb-Precision-3540 nm-openvpn[61630]: VERIFY ERROR: depth=0, error=EE certificate key too weak: C=TW, ST=Taiwan, L=Taipei, O=QNAP Systems Inc., OU=NAS, CN=TS Series NAS, name=NAS, emailAddress=admin@qnap.com, serial=1
Oct 12 14:28:40 scoulomb-Precision-3540 nm-openvpn[61630]: OpenSSL: error:0A000086:SSL routines::certificate verify failed
````
See 
- https://superuser.com/questions/1640089/ssl-certificate-ee-certificate-key-too-weakAvaialb
- https://www.openssl.org/docs/man1.1.1/man3/SSL_CTX_set_security_level.html

And https://askubuntu.com/questions/1407774/cant-connect-to-vpn-after-upgrading-to-ubuntu-22-04 (tried in lan)


`````
scoulomb@scoulomb-Precision-3540:~/Downloads$ sudo cat  /etc/NetworkManager/system-connections/scoulombel-nas\(1\).nmconnection | grep -C 2 SECLEVEL
[vpn]
ca=/home/scoulomb/.cert/nm-openvpn/scoulombel-nas(1)-ca.pem
tls-cipher=DEFAULT:@SECLEVEL=0 <==== added this line
cipher=AES-128-CBC
comp-lzo=adaptive

systemctl restart NetworkManager

`````

So we change the level
- With level 1 we have an error 
- Tried level 0
- No error in logs


- Tried from there `3-check` and working, if I disable VPN and refresh I have 77.205.22.216
- Renable VPN on Ubuntu


Then Step 6 worked as expected we have `109.29` IP adress 
-Cut VPN on Ubuntu and refresh `77.205`
- Reenable, wait, refresh we have `109.29`

Stragey is working :) !!!!


#### Also could try with app center ovpn (not done)

````
sudo snap connect simple-openvpn-client:network-control
sudo systemctl stop snap.simple-openvpn-client.vpn-daemon.service
sudo tail -f /var/log/syslog
````

### Not using 4G devices (I can not test as I have a single internet connection @home)

https://frenchmac.com/apple-tv/comment-utiliser-un-vpn-sur-son-apple-tv/. Backup in [media](./media/Comment%20utiliser%20un%20VPN%20sur%20son%20Apple%20TV%20-%20Frenchmac.pdf)

- Le VPN installé sur le routeur

Nest does not support 
A lot does not support 

We can use this https://www.amazon.fr/GL-iNET-GL-MT300N-V2-Pre-installed-Performance-Compatible/dp/B073TSK26W/ref=asc_df_B073TSK26W/?tag=googshopfr-21&linkCode=df0&hvadid=314673282442&hvpos=&hvnetw=g&hvrand=9321162626209930904&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9054964&hvtargid=pla-491876105460&psc=1&tag=&ref=&adgrpid=61115195445&hvpone=&hvptwo=&hvadid=314673282442&hvpos=&hvnetw=g&hvrand=9321162626209930904&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9054964&hvtargid=pla-491876105460

or a router on top which supports VPN natively

- Le VPN sur votre ordinateur portable

Equivalent to [laptop hotspot + phone 4G](#laptop-hotspot--phone-4g) where replace phone USB by Ethernet to router

- Le VPN avec 2 câbles Ethernet

Same technique as bulltet but we use ethernet between laptop and TV (apple TV ethenet from 4K, 3G)

All those technique could help to re-certify a device

I will stop investigation here

So we have a workaround for netflix (no need to chnage the household) <!-- did nit check with netflix but principle validated -->

<!-- section ccl, qvpn client osef-->
<!-- CCL :) -->

<!-- could replace in config generated folder ip by qnap or home.coulombel.net DNS, in particular if IP is changing, but will not try this STOP-->