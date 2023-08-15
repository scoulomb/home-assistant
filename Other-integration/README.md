# Here we cover other integration (the easy one)

## Hue

Magic integration 

````
gpg -c Hue-ref.md
gpg  Hue-ref.md.gpg
````

<!-- use wsl from vs code, it requires ubuntu wsl started, or git bash -->

We can also integrate Hue Hub in Tahoma to link ligth with Tahoma ecosystem (without HA).
It makes additional entities in HA.

Note this cool stuff: https://community.hueessentials.com/t/how-to-set-up-power-on-behaviour-for-my-lights/720

## Denon

Magic intergation But some feature missing. Idea to call [API](#api-integration) 


## Netamo integration in HA

https://dev.netatmo.com/apidocumentation/weather#getstationsdata


Use HomeKit.
See code 

````
gpg -c Netatmo-hk-code.md
gpg  Netatmo-hk-code.md.gpg
````

## Android TV integration in HA (FireTV)

https://www.home-assistant.io/integrations/androidtv/

## API integration

Use this https://www.home-assistant.io/integrations/rest_command/ (not tried)

- [Tuya API](../Tuya-IR-controller/tuya-api.md) (may have to deploy API server for credentials management or HA python module)
- [Tahome Local](../Tahoma/tahoma-integration.md#tahoma-local-integration) 
- My denon API server on top of denon telnet: https://github.com/open-denon-heos/remote-control
