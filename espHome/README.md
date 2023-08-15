# ESPHome

## Intro

We can build smart home project using ESP32.
See See https://oliverfalvai.com/notes/posts/how-to-make-infrared-devices-smarter-using-esphome/




Rather than using code , homeassistant launched this project: https://esphome.io/guides/getting_started_hassio.html

We have seen that that 
- [Tahoma integration and Somfy IO](../Tahoma/tahoma-integration.md#no-tahoma-integration-esphome-based)
- [Tuya integration and IR remote](../Tuya-IR-controller/README.md)
- [Netatmo Weather and air quality](../Other-integration/README.md#netamo-integration-in-ha)

Those requires to be conneted to the remote provider (and Internet) and not good for privacy.

If devlopping own module  HA will bring on top of integration of various technology, local access. 

Equivalent project:

- Tahome home made: https://forum.arduino.cc/t/commande-de-volets-roulants-somfy-a-base-desp32/664069
- IR remote: https://community.home-assistant.io/t/faking-an-ir-remote-control-using-esphome/369071
- ESPhome air sensor: https://www.pieterbrinkman.com/2021/02/03/build-a-cheap-air-quality-meter-using-esphome-home-assistant-and-a-particulate-matter-sensor/



We can start with simple connected button. 

Note I consider [Tahoma local API](../Tahoma/tahoma-integration.md#tahoma-local-integration), not fully local, we to go to Tahoma cloud to get the local token :(.

## WHcih ESP to buy

This version seems interesting with MicroPython support + Arduino cloud: https://store.arduino.cc/products/nano-esp32-with-headers



We can see in Wifi list that [Tuya integration and IR remote](../Tuya-IR-controller/README.md) I bougth is based on ESP32, we could flash it get ride of Tuya ! 
- https://tasmota.github.io/docs/Tuya-Convert/
- https://lofurol.fr/joomla/electronique/domotique/302-home-assistant-piloter-une-climatisation-daikin-avec-l-infrarouge


<!--here -->