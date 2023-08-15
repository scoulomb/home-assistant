# Some automation idea

## Home leave

`NFC trigger -> Switch off Denon, Air condititonner IR, Somfy IO`

Example in [leave home](./Leave-home.yaml). 


## Other scenarii

### Tahoma buttons

Could use Tahome scenario button (including the one in the box) to complete unsupported feature in Tahoma

````
Scenario button -> Tahoma     -> Philips gw 
                              -> Somfy IO/RTS
                              -> Sonos
                -> HomeAssis  -> Denon (or telnet command)
                              -> Air condititonner IR
                              
````


### Alarm clock 

Rather than having `NAS cronjob -> calling denon API to Wake UP / Phue API / Tahoma local API`

Do 


`Time trigger Home assistant  -> denon HEOS, Hue, Tahoma Integration` 


### Cinema mode

`Media player Play/Pause button -> hue scene...`
