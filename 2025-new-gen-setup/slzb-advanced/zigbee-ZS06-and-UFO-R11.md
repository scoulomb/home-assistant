# Integrating Zigbee ZS06 and UFO-R11 IR Controller with Atoll HD 120 HiFi Receiver

This guide explains how to integrate the Zigbee ZS06 IR controller to control the mute button of the Atoll HD 120 HiFi receiver.

## Useful Links

- [Bitboxer Zigbee IR Integration](https://bitboxer.de/2024/01/20/tuya-zigbee-ir/)
- [Tuya Zigbee IR Remote ZS06 Review](https://smarthomescene.com/reviews/tuya-zigbee-infrared-ir-remote-zs06-review/)
- [Home Assistant Script Integration](https://www.home-assistant.io/integrations/script/)


## 🧰 What You Need

- ZS06 Zigbee IR Blaster (Tuya-based)
- Home Assistant with Zigbee2MQTT integration
- Atoll HD120 remote control
- A stable 5V/1A–2.4A USB power supply (e.g., Belkin USB charger)
- Access to Home Assistant at http://homeassistant.local:8123

## ⚙️ Step 1: Power and Placement

Power the ZS06 using a USB port that supplies 5V, 1A.
In the manual they specify 5V, 1A and believed it was not working but I confirmed it works with a Belkin 5V/2.4A charger.
<!-- I also did a test with Ugreen KVM and usb-c to usb-c wire, see also Tahoma 5v/2a from https://asset.somfy.com/Document/8e23bd99-207a-4d1d-a16f-51837aedc229_TaHoma%20switch_Spec%20Sheet_2024.03.18.pdf?__hstc=149881833.1fff4bc756e3af1090162dfd03c9298e.1752316855278.1752316855278.1752316855278.1&__hssc=149881833.1.1752316855278&__hsfp=2679447906 -->

See more inputs on USB voltage: https://en.wikipedia.org/wiki/USB#Power

Position the ZS06 in front of the Atoll HD120 receiver’s IR sensor. Avoid placing it behind the receiver (though it works in my case and initial issue were not caused by that).

## 📡 Step 2: Learn IR Codes from the Atoll Remote

⚠️ Important: Use the original Atoll remote, not a universal remote like “One For All,” as the learning process may fail otherwise.


Go to:
http://homeassistant.local:8123/45df7312_zigbee2mqtt/ingress

Click “Learn IR Code” (e.g., for the Power ON or Mute button).

Press the corresponding button on the Atoll remote while pointing it at the ZS06.

The learned IR code will appear, e.g.:

BZ8N4wa6AUABAzIFugHgIwHgFy9AH0AD4BMBwB/AB+APAeALH0ATAuwBumABAf//gMdAD0AX4CMBQC9AN+APAUAfQAPgEwHAH8AHwAHgB1fgBx9AAQsyBboBugG6AboBugE=

## 🚀 Step 3: Test the IR Code

Paste the learned code into the IR Send field.
Click outside the text box to trigger the IR signal.
Confirm the Atoll receiver responds (e.g., mutes or powers on).

## 🧪 Step 4: Use the HA Dashboard to Capture Codes as alternative of Zigbee2Mqtt to learn IR code (step 2) and test it (step 4)

On your Home Assistant dashboard:

Click the ⚡ (lightning bolt) icon to send a command.
Press the Mute button twice to generate history.
Click the 👁️ (eye) icon to view the IR code.
Copy the code, e.g.:

BZQN9gasAUABA0cFrAFAAQLmAaxgAUAH4AMDwAHAE0AvwAvAB8ABQA9AH0ADQAtAAUAHQAPAAUALQB9AAUAHQA9AA0AB4AMHQAtAH0ABQAtAA0AB4AMTAf//4AnHwAHAL+AHAcAX4ANHwAFAG0ADQAFAH0ADwA9AAcALQAdAA8AfQAdAAUATwAPAAUAPQB9AB0ABQAdAAwtHBawBrAGsAawBrAE=

in Send (Irealised that sometime a retry did not work here, small bug unlike when using a script as in step 5)

## 🧾 Step 5: Create a Script in Home Assistant
Go to:
http://homeassistant.local:8123/config/script/edit/zs06_duplicate

Create a new script with the learned IR code.

Example YAML:

````yaml
data:
  payload: >-
    {"ir_code_to_send":
    "BZQN9gasAUABA0cFrAFAAQLmAaxgAUAH4AMDwAHAE0AvwAvAB8ABQA9AH0ADQAtAAUAHQAPAAUALQB9AAUAHQA9AA0AB4AMHQAtAH0ABQAtAA0AB4AMTAf//4AnHwAHAL+AHAcAX4ANHwAFAG0ADQAFAH0ADwA9AAcALQAdAA8AfQAdAAUATwAPAAUAPQB9AB0ABQAdAAwtHBawBrAGsAawBrAE="} 
  topic: zigbee2mqtt/0x70c59cfffef600c8/set
action: mqtt.publish
````


## 🧠 Tips & Troubleshooting


If a code doesn’t work (happens when code very long):
Ensure re-learning it with the Atoll remote.
Power cycle the Atoll receiver before retrying.

Tuya IR codes are not consistent across learning attempts.
This is not due to rolling codes, as menitoned here:
https://smarthomescene.com/reviews/tuya-zigbee-infrared-ir-remote-zs06-review/
but Tuya’s own encoding format.
https://www.reddit.com/r/homeassistant/comments/1di1zs7/ir_codes_formatting/

<!-- yaml done via xcode + copilot -->
