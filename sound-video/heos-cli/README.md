# HEOS

## Example to play a custom radio url using HEOS

Natural way is to use TuneIN

- Probleme: quelque stations pas referencees dans HEOS/TuneIN, et dependent third-party pour mise a jour des URL quand changements 
- Solution: jouer une custom url

### Via TuneIN

See https://support-eu.denon.com/app/answers/detail/a_id/17180/~/heos---music---adding-a-custom-url-internet-radio-station


- Dans l’appli TuneIn sur iOS
  - Aller dans icône du bas, library puis custom url 
  - Ajouter cette url: http://direct.francebleu.fr/live/fbprovence-midfi.mp3 
  - URL found: http://fluxradios.blogspot.com/2014/07/flux-url-france-bleu-provence.html
  - Puis cocher le cœur pour la mettte en favoris
￼
- Dans appli heos
  - Menu principal, aller dans music services puis tune in et s’identifier 
  - Puis aller sur tune in et favorites pour lancer la lecture


## Via HEOS CLI

Reference of Denon CLI: https://rn.dmglobal.com/usmodel/HEOS_CLI_ProtocolSpecification-Version-1.17.pdf

Alternative is to by-pass tune in et jouer url à partir de la CLI

Avantage pas de pub et independent de Tune IN!

Comprendre que TuneIN n'apporte pas grand chose en realite.


### Step 1: Find IP address of all Denon HEOS devices in the network 

#### Option 1: using SSDP

Use  https://github.com/open-denon-heos/heospy/blob/main/heospy/ssdp.py 

````
% git clone https://github.com/open-denon-heos/heospy
% cd  heospy/heospy 
% python3 
Python 3.11.5 (main, Aug 24 2023, 15:09:45) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ssdp
>>> ssdp.discover("upnp:rootdevice")



[<SSDPResponse(http://192.168.1.1:49152/rootDesc.xml, upnp:rootdevice, uuid:e0860fe3-5dac-4421-ace3-cef53750f631::upnp:rootdevice)>,
<SSDPResponse(http://192.168.1.99:60006/upnp/desc/aios_device/aios_device.xml, upnp:rootdevice, uuid:fcbac2d7-0721-19a9-0080-00a96f1a879f::upnp:rootdevice)>,
<SSDPResponse(http://192.168.1.84:60006/upnp/desc/aios_device/aios_device.xml, upnp:rootdevice, uuid:dc8c8ab2-7381-1aaf-0080-00a96f18222e::upnp:rootdevice)>,
<SSDPResponse(http://192.168.1.76:60006/upnp/desc/aios_device/aios_device.xml, upnp:rootdevice, uuid:e2121c85-2bee-1d5c-0080-0006786e8eee::upnp:rootdevice)>,
<SSDPResponse(http://192.168.1.42:60006/upnp/desc/aios_device/aios_device.xml, upnp:rootdevice, uuid:1f0569b2-8cdf-153b-0080-00a96f192917::upnp:rootdevice)>]

````

```shell
curl http://192.168.1.84:60006/upnp/desc/aios_device/aios_device.xml  | grep friendlyName | head -n 1
````

Output is 

````shell
<friendlyName>Denon Home 150 Bureau</friendlyName>
````
=> Local IP of `Denon Home 150 Bureau` is `192.168.1.84`


#### Option 2: Find IP address via Mdns

Alternative discovery can be done via mdns (see [dns service discovery](../dns-sd.md)

We can use `dns-sd`: https://www.manpagez.com/man/1/dns-sd/

````shell
dns-sd -B _heos-audio._tcp
````
Where outout is 

````shell
 %  dns-sd -B _heos-audio._tcp
Browsing for _heos-audio._tcp
DATE: ---Thu 26 Dec 2024---
16:28:42.204  ...STARTING...
Timestamp     A/R    Flags  if Domain               Service Type         Instance Name
16:28:42.206  Add        3  14 local.               _heos-audio._tcp.    Denon Home 150 Séjour
16:28:42.206  Add        3  14 local.               _heos-audio._tcp.    Denon Home 150 Chambre
16:28:42.206  Add        3  14 local.               _heos-audio._tcp.    Denon CEOL
16:28:42.206  Add        2  14 local.               _heos-audio._tcp.    Denon Home 150 Bureau
````


In linux we can use `avahi`, on MAC OS I recommend to use `dns-sd`.

Note if we group heos device only one device will appear for `_spotify-connect._tcp` unlike `_heos-audio._tcp`.

````shell
dns-sd -B _spotify-connect._tcp
````

````shell
dns-sd -L "Denon Home 150 Bureau" _heos-audio._tcp
````

Output is 

````shell
DATE: ---Thu 26 Dec 2024---
17:08:52.688  ...STARTING...
17:08:53.082  Denon\032Home\032150\032Bureau._heos-audio._tcp.local. can be reached at Denon-Home-150-Bureau.local.:10101 (interface 14)
 did=3C424E4F8CA96F18222E vers=3.34.620 model=Denon\ Home\ 150 networkid=6c61f46467a8
````

Then 

````shell
dns-sd -q Denon-Home-150-Bureau.local.
````

Output is 

````shell
% dns-sd -q Denon-Home-150-Bureau.local.
DATE: ---Thu 26 Dec 2024---
17:10:24.208  ...STARTING...
Timestamp     A/R  Flags         IF  Name                          Type   Class  Rdata
17:10:24.208  Add  40000002      14  Denon-Home-150-Bureau.local.  Addr   IN     192.168.1.84
````

=> Local IP of `Denon Home 150 Bureau` is `192.168.1.84`

#### Option 3: Other alternative to find IP address

- via HEOS app which is doing SSDP
- BOX admin interface
- Using `arp -a`

```shell
arp -a | grep denon-home-150-bureau
```

Output is 

```shell
 % arp -a | grep denon-home-150-bureau
denon-home-150-bureau (192.168.1.84) at 8c:a9:6f:18:22:2e on en0 ifscope [ethernet]
```

#### Step 2: find Player Id (pid)

Then we can select any of the device to get all player details via `HEOS`, in particular player id (pid).
Note we have to open telnet session on port `1255`.
We cn use `nc` (mac OS, ubuntu) or `telnet` (ubuntu). (we can also use android (termius), telnet python libs, [heospy](#replace-nc-and-telnet-by-heospy))

For example we can query `denon-home-150-bureau` (192.168.1.84) 

````shell
nc 192.168.1.84 1255 
heos://player/get_players
````
<!-- 192.168.1.86 subnet if google home -->


Output is 

````json
{
    "heos": {
        "command": "player/get_players",
        "result": "success",
        "message": ""
    },
    "payload": [
        {
            "name": "Denon Home 150 Bureau",
            "pid": -1950769503,
            "model": "Denon Home 150",
            "version": "3.34.620",
            "ip": "192.168.1.84",
            "network": "wifi",
            "lineout": 0,
            "serial": "BLT27230885013"
        },
        {
            "name": "Denon Home 150 Chambre",
            "pid": -1682999457,
            "model": "Denon Home 150",
            "version": "3.34.620",
            "ip": "192.168.1.99",
            "network": "wifi",
            "lineout": 0,
            "serial": "BLT27240705052"
        },
        {
            "name": "Denon Home 150 Séjour",
            "pid": 1496346665,
            "gid": 1464487734,
            "model": "Denon Home 150",
            "version": "3.34.620",
            "ip": "192.168.1.42",
            "network": "wifi",
            "lineout": 0,
            "serial": "BLT27231094927"
        },
        {
            "name": "Denon CEOL",
            "pid": 1464487734,
            "gid": 1464487734,
            "model": "Denon CEOL",
            "version": "3.34.620",
            "ip": "192.168.1.76",
            "network": "wifi",
            "lineout": 0,
            "serial": "DBDR082111638"
        }
    ]
}
````

CEOL Pid is `1464487734`.

We can partially automated field extraction from `get_players`.
We will be used to study [group feature](#using-group-feature).

````shell
nc -w 2 192.168.1.84 1255 > file.txt 2>&1
heos://player/get_players
````

```shell
cat file.txt | jq .payload | grep pid

cat file.txt | jq .payload | grep gid
```



#### Step 3: Run `France info` command via playurl

See spec: https://rn.dmglobal.com/usmodel/HEOS_CLI_ProtocolSpecification-Version-1.17.pdf (4.4.10)

Command : `heos://browse/play_stream?pid=player_id&url=url_path`

We `nc` to IP of one of the Denon device (here `denon-home-150-bureau` (192.168.1.84) ) in the network
(and not necessarily the one we output music from) and control via the PID.
Here we launch music on Denon CEOL
<!-- this distinction not made in initial doc -->

````shell
nc 192.168.1.84 1255 
heos://browse/play_stream?pid=1464487734&url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3
````

<!-- sometimes we have to run the command twice -->

Note if the pid of the device is included in a group, playback will start (and stop) in the full group (in the get player command you will those are under the same `gid`)

````shell
nc 192.168.1.84 1255 
heos://browse/play_stream?pid=1496346665&url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3
````

### Other basic command

#### Stop / Play

```shell
nc 192.168.1.84 1255 
heos://player/get_player_info?pid=1464487734
heos://player/set_play_state?pid=1464487734&state=stop
```

```shell
nc 192.168.1.84 1255 
heos://player/set_play_state?pid=1464487734&state=play
```

#### Volume

```shell
nc 192.168.1.84 1255 
heos://player/set_volume?pid=1464487734&level=12
```

Note: this will change only level of the player with pid (otherwise use gid) 

### Using group feature

<!-- to explore optionally-->

### Replace nc and telnet by heospy

Instead of using `nc`, `telnet`

- We can setup cli at:  https://github.com/open-denon-heos/heospy 

````
heos_player browse/play_stream -p pid=735067990 -p url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3 -c $HOME/.heospy/config.json
````

- or my music server API or UI: https://github.com/open-denon-heos/heos-api-server
- Python telnet lib
- And termius on Android (use telnet and port `1255`)

<!-- OK --> 

### What are other possibilities

- Use another streamer (MS120) + coaxial
- Moode AUDIO with custom URL: https://github.com/moode-player/moode
- TuneIN or URL in Safari + AIR PLAY
  - Airplay multi room
  
<!-- doc ccl OK 26 dec 24-->

### Notes


- Airplay name mismatch speaker name 
 - Did remove speaker from home app 
 - Rename it on HEOS and AirPlay name resync


