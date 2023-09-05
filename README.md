# Home assistant setup

Intro to Home Assistant: https://www.youtube.com/watch?v=TaIwArlov_4

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

SSH did not work in ny test (to hp pavillon in google wifi) both with
- NAT 
- And DMZ

See potential reasons: https://serverfault.com/questions/404516/ssh-not-working-through-double-nat

Thus either use local IP if in NEST LAN or connect this machine to SFR wifi when access required from Internet.
<!-- See [Tuya API](./Tuya-IR-controller/tuya-api.md) -->

#### What do keep?

Use wired solution with double DNAT rule.
<!-- ok nw ccl - retested double nat OK -->
<!-- Note tuya and hue do not need NAT, probably socket is established from outbound and not inbound, even if msg flow is inbound - OK CCL -->

#### Note on UPNP

See [Appendix on UPNP](./appendices/UPNP.md/)

#### Note on (m)DNS 

Note if using Google NEST wifi router, a DNS record is automatically created `scoulombel-nas`.
Thus can access NAS by doing `scoulombel-nas:8123` in local NEST network. How does it work?
See [Appendix on mDNS](./appendices/DNS.md#mdns).
Private IP is also visible in Google home app ex `http://192.168.86.20:8123`), and accessible from device in google home network (to access from SFR add port fw in google home port management, but DNS name wlll not be visible from SFR network to access NAS in Google network)

We can also access it via `home.mydomain.net:8123`, if A record `home.mydomain.net	A	1 hour	109.29.148.109`. is correctly set. See See [Appendix on (m)DNS](./appendices/DNS.md#dns-deep-dive).
<!-- https://github.com/open-denon-heos/remote-control#suggestion-define-a-record-pointing-to-your-machinenas OK -->
<!-- mdns OK -->
<!-- mdns can be blocked in corp - work in phone / home.mydomain.net:8123 or ip acess will woerk if vpn unlike local ip / access from laptop on site osef-->

## Projects

- [Tahoma integration](./Tahoma/tahoma-integration.md)
- [Tuya IR](./Tuya-IR-controller/README.md)
- [Other integration](./Other-integration/README.md)
- [Some automation sample](./Some-automation-sample/README.md)
- [ESPHome](./espHome/README.md)

## Next to check --

<!-- - Pointer of section OK clear (but come back on point referenced here only), commit 729e389 ok no come back osef-->
<!-- concluded NAT with 
Links-mig-auto-cloud/README.md#migration-and-snatdnat
https://github.com/scoulomb/docker-under-the-hood/blob/main/NAT-deep-dive-appendix/README.md#nat-deep-dive
https://github.com/scoulomb/home-assistant/blob/main/README.md#note-on-network, review not required a link made with @home
See https://github.com/scoulomb/home-assistant/commit/ef7ba4bd7ebdae1af27a0ab66b21bb4e4ff34650 (W1A stuff should not impact but can update even if other commit in HA repo in btw)
-->
- Tahoma open/close (optional vendor follow-up only: https://github.com/scoulomb/home-assistant/commit/7dd77264627883e46a170a73e414870607d48722) 
<!-- volet montage final ccl 
https://github.com/scoulomb/home-assistant/commit/6e413c0fd0175fd6519cbaa95a6e7b762876fcf2 -->

- Volet: [Scenario](./Tahoma/hardware-remotes/lanceur-scenario.md) 
  - https://community.home-assistant.io/t/trigger-automation-when-scene-is-triggered/7932    
   -https://community.home-assistant.io/t/can-i-trigger-an-automation-by-scene-being-activated/222468
- [DNS QNAP cert](./appendices/DNS.md#use-nas-dyndns-and-certificate-in-qnap-cloud) and [UPNP IGD](./appendices/UPNP.md#upnp-igd-nat-traversal)
- [VPN usage](./appendices/VPN.md)
- ESPHome 
- Hue ligths  micro coupure (see [other integ](./Other-integration/README.md)) 
- Izymo on/off
-  Curl command from HA (to use denon, tahoma local API)
-  We can do equivalent of HA using GoogleHome including levave home location (equivalent to what described in [Tahoma Scenario](./Tahoma/hardware-remotes/lanceur-scenario.md))
<!-- tahoma app working when ehtenet hub not AC plugged osef -->

<!-- this repo is ready OK -->
<!-- tips for reduce pic size is to use snipping tool -->