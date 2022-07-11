# Home assistant

Intro to Home Assistant: https://www.youtube.com/watch?v=TaIwArlov_4

## Deploy Home Assistant via Docker Compose

https://www.home-assistant.io/installation/alternative/#docker-compose

### Lab env

- Did not use WSL here: https://github.com/scoulomb/misc-notes/blob/master/lab-env/others.md#use-wsl
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

