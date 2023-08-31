# Hardware remote (point of control)


## Intgrated actuator 

### Pre conf or first remote

- A firt `somfy smoove` was pre-configured initially 

- If not the case there is a special procedure via powercut
    - See https://service.somfy.com/downloads/hu_v5/suneascreen_io.pdf, [save here](./suneascreen_io.pdf) (I took awing given [my shuuter has an awing actuator](./../shutter-is-awning/README.md).
    - >  After a single power cut
        	- > 1) Press the Up and Down buttons simultaneously on the new control point until the awning moves. 
            - > 2) Briefly press the proog button on this control point: awning will make a brief movement; the control point has been programmed.

### Add additional remote on integrated

- We added other Somfy remote (situo 1, situo 5 chanel 1, could be amother smoove) by
 - Pressing Smoove prog button until shutter blink
 - Pressing Prog button of the remote
 - As documented in https://service.somfy.com/downloads/hu_v5/suneascreen_io.pdf, and https://service.somfy.com/downloads/fr_v5/somfynotice_situo_1_et_5_io.pdf saved [here](./somfynotice_situo_1_et_5_io.pdf). Note situo remote manual refer to actuator mannual to setup first remote.

Did this on Situo 1 + Situo 5 (channel 1)

### Tahoma setup

- We added it in Tahoma by doing
    - `Add device`
    - `Winfow covering`
    - `Shutters`
    - select `Somfy smoove existing` control point 
    - Scan QR code, press prog on smmove remote
    - It can prompt if we have centralize remote or a box
    - Say no and continue searching
    - Device will be found (Alexa will even reach before Tahoma app)

- I did not try to add this shutter without a remote


Note in Tahoma app if we add a control, remote control and scan QR code of Smoove or Situo it say QR code not recognized.
I did not test from Situo 1 but expect same behavior.

## Izymo IO

### Tahoma without remote setup

This what I did initially as I did not have a remote
<!-- procedure was re-tested -->    

- We added it in Tahoma by doing
    - `Add device`
    - `Winfow covering`
    - `Shutters`
    - `Micro-receivers`
    - `Somfy`
    - `Other control point` 
    - `Other switch`
    - `Press Prog Button on IzymoIO module for 3 sec`
    - select `Somfy smoove existing` control point 
    - It can prompt if we have centralize remote or a box
    - Say no and continue searching
    - Device will be found (Alexa will even reach before Tahoma app)

### First and additional remote setup

- Or I install remote 
    - By pressing prog button on Izymo module 
    - Pressing Prog button of the remote
    - Izymo module prog button is equivalent to any other prog IO button. So equivalent do ["Add additional remote above"](#add-additional-remote)

Did this on Situo 5 (channel 2) +  Smoove Discret

(If we do Tahoms setup without remote or additional remote it does not unprogram)

### Add additional remote on Izymo alternative

This procedure is also possible.
Same as [add additinal remote on integrated](#add-additional-remote-on-integrated) 
Tested by re-programming Smoove from situo 5 (channel 2) (and vice-versa)
<!-- does not seem to program 2 channel in situo 5 targetting same device-->


### Tahoma setup with rc

Same proc as [Tahoma setup above](#tahoma-setup) where we select shutter and scan QR code (test with Smoove)


We can also (tested with Smoove and Situo OK)
    - `Add device`
    - `Winfow covering`
    - `Shutters`
    - `Micro-receivers`
    - `Somfy`
    - `Somfy Smooove` ( or `SOmfy remote control > IO > Icon 1`)
    - `Press 3 sec` on smoove  (or Situo but srlect good chanel before, reasobn why better to use Snoove)
    - select `Somfy smoove existing` control point 
    - It can prompt if we have centralize remote or a box
    - Say no and continue searching
    - Device will be found (Alexa will even reach before Tahoma app)
No QR code is required.

Adding more remotes will re-use same principle
<!-- this is concluded ok -->

See also [lanceur de scenario](./lanceur-scenario.md)