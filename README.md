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

## Suggestion: define A record pointing to your machine/NAS

Example

````
$ nslookup local.nas.coulombel.net
Name:   local.nas.coulombel.net
Address: 192.168.1.88
````

<!-- https://github.com/open-denon-heos/remote-control#suggestion-define-a-record-pointing-to-your-machinenas -->


Note if using google wifi router, a DNS record is automatically created `scoulombel-nas`.
IP is visible in google home app (unlike SFR wifi), and accessible from device in google home network (to access from SFR add port fw in google home port management)
See [note on network below](#note-on-network)

IP in SFR wifi can be seen via `192.168.1.1`.

## Note on network

### Topo 

I have 2 networks
- SFR Box (Wifi + many eth)
- Google home (wifi + 1 external eth + 1 eth conneced to SFR box eth)

When NAS on SFR box eth, and Denon devices on Google home wifi.

Schematically

````
Internet -> SFR Modem -> SFR router [WAN IP - 109.....109] -> Google router [GW IP in SFR LAN] -> Device in Google network [IP in Google LAN] 
                                                           -> Device in SFR network [IP in SFR LAN]
````

See WAN IP: https://www.belkin.com/fr/support-article/?articleNum=10796

In my case Bridge mode is not availalble: https://support.google.com/googlenest/answer/6277579?sjid=11569360593923687828-EU.
Not that even 
>  `Enable Bridge mode on your Wifi router device` is not possible as WAN IP is public (so not renatting on ISP side, in that case we would have a 3 NAT layer).

I will not consider VPN option: https://networkengineering.stackexchange.com/questions/40773/how-to-make-ipsec-over-double-nat

So I am relying on Double Natting.


### Issue and proposed solution

Denon in Google LAN, NAS with HomeAssistant in SFR LAN.


I did not manage to get it working again. 
In the past I was able to, SSDP discovery worked similar to https://github.com/open-denon-heos/heospy/blob/main/heospy/__init__.py#L105 (without port 1900 forwarding apparently, 2 denon devices had gateway IP).

Then had to dnat  port used by heos in Google wifi => Opened port 1223 (1255?) in google home wifi app (port management)
https://forum.fibaro.com/topic/17590-fibaro-hcl-and-denon-heos/

Decided to plug nas in ethernet plug  of google router to avoid this

**Drawbacks** (we will see [below](#eliminate-drawbacks-of-the-solution), how to eliminate them.

 - Will lose WOW (Wake on Wan) via WOL PROXY CONFIGURED IN THE BOX: https://github.com/scoulomb/misc-notes/blob/master/NAS-setup/Wake-On-LAN.md#setup-2b-wow-with-cloud-server
 - If NAS is doing upnp for port forwarding it will open it in google home wifi and ned to it in SFR wifi 
 - Access to NAS inside Google Wifi network (NAS (home assistant UI, QNAP UI), SSH) from outside (Internet) can be complex 

Then need to have somfy and hue on same wifi netowrk for integration (upnp discovery). Put both in SFR wifi.
Normally home assitant in NAS should see those 2 devices.

However for setup simplification I decided to have everything in same network.
So I plug an ethernet switch on google home wifi external ethernet. In the hub I plugged all ethernet devices

So that we have

````
Internet -> SFR Modem -> SFR router [WAN IP - 109.....109] -> Google router [GW IP in SFR LAN] -> Device in Google network [IP in Google LAN] 
````

### Trying to eLiminate drawbacks of the solution


Use-case: I want to access HomeAssistant in NAS with following topology and where bridge mode is available, without a VPN

````
Internet -> SFR Modem -> SFR router [WAN IP - 109.....109] -> Google router [GW IP in SFR LAN] -> NAS with HA on port 8123 [IP in Google LAN] 
````

#### Solution 1: Double DNAT

I configured a double port forwarding , for instance in SFR

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
- to HA using pub WAN IP  (`109....`) and port 8123 or 9123
- NAS UI using pub WAN IP (`109....`)and port 9080

Note htat when activating UPNP natting rules are not added to SFR box. 

If we disable NAT it stops working


#### Solution 2: Use DMZ 

DMZ will forward all incomng traffic from outside to a chosen device in SFR LAN.
We choose this device to be the gateway.

````
Activation du DMZ 	
Adresse Ip 	: 192.168.1.GOOGLE_GW
````

And in Google Home APP 

`Network settings > Advanced settings > Port mgmt`, do natting 

````
8123 -> NAS:8123
8080 -> NAS:8080
````

After this I can access from outside home (4g), this is working.
- to HA using pub WAN IP  (`109....`) and port 8123 
- NAS UI using pub WAN IP (`109....`)and port 8080

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

Thus either use local IP are connect this machine to SFR wifi when required.
<!-- See [Tuya API](./Tuya-IR-controller/tuya-api.md) -->

#### What do keep?

Use double DNAT rule.
<!-- ok nw ccl - retested double nat OK -->

## Projects

- [Tahoma integration](./Tahoma/tahoma-integration.md)
- [Tuya IR](./Tuya-IR-controller/README.md)
- [Other integration](./Other-integration/README.md)
- [Some automation sample](./Some-automation-sample/README.md)
- [ESPHome](./espHome/README.md)
