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
  - Puis uis cocher le cœur pour la mettte en favoris
￼
- Dans appli heos
  - Menu principal, aller dans music services puis tune in et s’identifier 
  - Puis aller sur tune in et favorites pour lancer la lecture


## Via CLI


Alternative is to by-pass tune in et jouer url à partir de la CLI

Avantage pas de pub et independent de Tune IN!

Comprendre que TuneIN n'apporte pas grand chose en realite.


### Via HEOS telnet


See spec: https://rn.dmglobal.com/usmodel/HEOS_CLI_ProtocolSpecification-Version-1.17.pdf (4.4.10)

Command : `heos://browse/play_stream?pid=player_id&url=url_path`

````
telnet 192.168.86.160 1255 
heos://player/get_players
heos://browse/play_stream?pid=735067990&url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3
````
Here is what we are doing
- Line 1: Open telnet session on port 1255, to find AVR IP adress get it in router configuration or via ssdp: https://github.com/open-denon-heos/heospy/blob/main/heospy/ssdp.py 
- Line 2: First command to get player pid
- Line 3: Command to launch music

We can use telnet python library, or android one

### Or do it via heos py

Setup cli at:  https://github.com/open-denon-heos/heospy 

````
heos_player browse/play_stream -p pid=735067990 -p url=http://direct.francebleu.fr/live/fbprovence-midfi.mp3 -c $HOME/.heospy/config.json
````

or my music server API or UI: https://github.com/open-denon-heos/heos-api-server


### What are other possibilities

- Use another streamer (MS120)
- Moode AUDIO with custom URL: https://github.com/moode-player/moode
- TuneIN or URL in Safari + AIR PLAY