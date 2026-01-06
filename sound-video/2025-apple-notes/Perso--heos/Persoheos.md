# Perso::heos  
  
[https://github.com/scoulomb/home-assistant/blob/main/sound-video/heos-cli/README.md](https://github.com/scoulomb/home-assistant/blob/main/sound-video/heos-cli/README.md)  
[https://rn.dmglobal.com/usmodel/HEOS_CLI_ProtocolSpecification-Version-1.17.pdf](https://rn.dmglobal.com/usmodel/HEOS_CLI_ProtocolSpecification-Version-1.17.pdf)  
  
## Controller device   
  
scoulombel@NCELRND1851 ~ % arp -a | grep -e denon -e amp  
heos-amp.lan (192.168.86.24) at 0:5:cd:d7:68:4e on en0 ifscope [ethernet]  
denon-home-bathroom.lan (192.168.86.30) at 8c:a9:6f:17:4:5f on en0 ifscope [ethernet]  
denon-home-bedroom-right.lan (192.168.86.33) at 8c:a9:6f:10:b8:75 on en0 ifscope [ethernet]  
denon-avr-x2700h.lan (192.168.86.159) at 0:6:78:61:27:52 on en0 ifscope [ethernet]  
denon-home-bedroom-left.lan (192.168.86.224) at 8c:a9:6f:18:36:f5 on en0 ifscope [ethernet]  
  
  
We can choose any heos device of the network, here we use heos-amp.lan (192.168.86.24) as a controller  
  
nc 192.168.86.24 1255  
  
  
**Get player and groups **  
  
heos://player/get_players             
{"heos": {"command": "player/get_players", "result": "success", "message": ""}, "payload": [{"name": "Denon Home Bedroom Right", "pid": 672898756, "gid": 735067990, "model": "Denon Home 150", "version": "3.67.270", "ip": "192.168.86.33", "network": "wifi", "lineout": 0, "serial": "BLT27220241004"}, {"name": "Heos Amp", "pid": -727243330, "model": "HEOS Amp", "version": "3.67.270", "ip": "192.168.86.24", "network": "wifi", "lineout": 0, "serial": "ABY27190418467"}, {"name": "Denon Home Bedroom Left", "pid": -1683771164, "gid": 735067990, "model": "Denon Home 150", "version": "3.67.270", "ip": "192.168.86.224", "network": "wifi", "lineout": 0, "serial": "BLT27230884839"}, {"name": "Denon Home Bathroom", "pid": -1682689296, "gid": 735067990, "model": "Denon Home 150", "version": "3.67.270", "ip": "192.168.86.30", "network": "wifi", "lineout": 0, "serial": "BLT27230473409"}, {"name": "Denon AVR-X2700H", "pid": 735067990, "gid": 735067990, "model": "Denon AVR-X2700H", "version": "3.67.270", "ip": "192.168.86.159", "network": "wifi", "lineout": 0, "serial": "DBCD022110605"}]}  
  
  
heos://player/get_groups   
{"heos": {"command": "player/get_groups", "result": "success", "message": ""}, "payload": [{"name": "Denon AVR-X2700H + Denon Home Bedroom Right + Denon Home Bedroo", "gid": 735067990, "players": [{"name": "Denon Home Bedroom Right", "pid": 672898756, "role": "member"}, {"name": "Denon Home Bedroom Left", "pid": -1683771164, "role": "member"}, {"name": "Denon Home Bathroom", "pid": -1682689296, "role": "member"}, {"name": "Denon AVR-X2700H", "pid": 735067990, "role": "leader"}]}]}  
  
  
  
nc 192.168.86.24 1255 << EOF  
heos://player/get_groups  
EOF  
  
  
Note we control stream from one device pid of the group where for volume master use group id not the pid  
Note that gid == pid of leader  
  
  
## PLay url and optical in   
  
heos://player/get_now_playing_media?pid=735067990  
{"heos": {"command": "player/get_now_playing_media", "result": "success", "message": "pid=735067990"}, "payload": {"type": "station", "song": "Optical In", "station": "Optical In", "album": "", "artist": "", "image_url": "", "album_id": "inputs/", "mid": "inputs/optical_in_1", "qid": 1, "sid": 1027, "gid": 735067990}, "options": []}  
  
  
[heos://browse/play_stream?pid=735067990&url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3](heos://browse/play_stream?pid=735067990&url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3)  
  
heos://browse/play_input?pid=735067990&spid=-727243330&input=inputs/optical_in_1  
  
  
nc 192.168.86.24 1255 << EOF  
heos://browse/play_input?pid=735067990&spid=-727243330&input=inputs/optical_in_1  
EOF  
  
Note here said is id of heos amp where ms120 plugged to optical in   
  
## Set group volume  
  
[heos://player/set_volume?gid=735067990&level=12](heos://player/set_volume?gid=735067990&level=12)  
  
  
nc 192.168.86.24 1255 << EOF  
heos://player/set_volume?gid=672898756&level=20  
EOF  
  
  
# Group   
  
672898756,  
-1683771164  
-1682689296  
735067990  
  
Create new group:  
Creates new group. First player id in the list is group leader.  
  
nc 192.168.86.24 1255 << EOF  
[heos://group/set_group?pid=672898756,-1683771164,-1682689296,735067990](heos://group/set_group?pid=672898756,-1683771164,-1682689296,735067990)  
EOF  
  
  
Ungroup all players in the group  
Ungroup players. Player id (pid) should be the group leader id.  
  
nc 192.168.86.24 1255 << EOF  
heos://group/set_group?pid=672898756  
EOF  
  
  
  
  
