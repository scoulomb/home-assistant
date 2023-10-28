# Apple ecosystem


[See Apple TV in Docking station](https://github.com/scoulomb/docking-station/blob/main/README.md#apple-tv-4k-3gen)


### Atmos

I have 2 Fire TV

https://www.amazon.fr/gp/product/B08C1KN5J2/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1 -> on center or [left screen](#zwiftapple-tv)
https://www.amazon.fr/gp/product/B07PW9VBK5/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1 (FireTV 4K) -> on AVR media player

Both are supposed to support Atmos.
Only latter support 4k.

I have Apple TV 4k 3gen

Example of Atmos movie: Heart of Stone

On firetv AVR front panel is displaying (DD+ + DSur), netflix app shows 5.1 (4k, HDR). 

Whereas on Apple TV 4K 3Gen, AVR front panel is displaying Atmos, netflix app show Atmos (Atmos, Ultra HD 4K). Sound has better quality 
    - Settings video and audio > Format HDR and Atmos selected 
    - Tested via VG32 (not videoprojector)
        - If I plug videoprojector output, the format in settings is auto changed to 1080p SDR and netflix then come to HD
        - Also if Sound mode in AVR is set to 
            -MCHannel Stereo, netlix app whill show Dolby Vision
            - Atmos, netflix app will show atmos
    - Further test will be conducted with initial setup

From Netflix help Atmos support: https://help.netflix.com/en/node/23934
I do not have this Display option: Auto (up to 4K Ultra HD)
I have only automatic

From netflix help

> Sure, let me know on how it goes.
> As we have checked further, there is in fact one supported device for Atmos and it is the Fire TV Stick 4K Max .

> Super interesting, I have fire tv 4k
> not the 4k max but weirdly when checking the spec they claim to support atmos

> You device might support Atmos for other apps, but it is not supported for Netflix

> no, any future plan to support atmos on more device

> As of the moment, there's no new for it. But will take a note of that as a feedback.

Note:
- https://blog.son-video.com/2019/08/votre-ampli-est-il-compatible-avec-le-dolby-digital-plus/: Atmos is delivered via DD+ codec
- https://developer.dolby.com/technology/dolby-atmos/overview/
    > **Dolby Atmos®** is an immersive audio format that can be delivered via multiple audio codecs including **Dolby Digital Plus and Dolby TrueHD** (but NOT Dolby Digital). **Blu-ray Discs deliver Dolby Atmos using Dolby TrueHD (with Dolby Digital Plus as an available alternative), and broadcast and streaming services deliver Dolby Atmos using Dolby Digital Plus.** In order to maintain compatibility with millions of devices in consumer homes, Dolby Atmos in these codecs is implemented as a backwards-compatible extension. Dolby Atmos data is hidden within the bitstream and can be decoded by a Dolby Atmos-compatible A/V Receiver, soundbar or television. Non-Dolby Atmos capable devices will decode a 5.1-ch or 7.1-ch version from the Dolby Digital Plus or Dolby TrueHD bitstreams.wiki
- https://blog.son-video.com/2019/08/votre-ampli-est-il-compatible-avec-le-dolby-digital-plus/: 
    - Dolby true HD bacward compatible Dolby Digital (AC3): Source transmittinmg only dolby digital kernel (section "L’exemple du Dolby True HD")
    - **Dolby Digital Plus (E-AC3)** not fully bacward compatible with Dolby Digital (AC3)
        - > Avec le Dolby Digital Plus, il n’y a pas un système de cœur comme avec le Dolby True HD. Il serait en effet impossible de mettre un cœur qui dispose d’un débit plus important que le flux total.
        - > La rétro-compatibilité est donc pensée au niveau du récepteur. Que ce soit la TV, un lecteur Blu-ray ou un autre lecteur, il contient un décodeur DD+. Ce décodeur Dolby Digital Plus contient aussi un ré-encodeur en Dolby Digital (AC-3). Lorsque le récepteur est branché à un système audio qui ne fait pas de Dolby Digital Plus, il y a possibilité de transcoder en Dolby Digital à 640 kbps, 
        - Confirmed in https://developer.dolby.com/technology/dolby-audio/dolby-digital-plus/
            - > Dolby Digital Plus bitstreams are not directly backwards compatible with Dolby Digital decoders, but Dolby Digital Plus decoders can decode Dolby Digital bitstreams.
- Global view: https://en.wikipedia.org/wiki/Dolby
    > **Dolby Atmos is not a codec**; on the consumer market, pre-recorded Dolby Atmos is **delivered as an extension to a Dolby TrueHD, Dolby Digital Plus (I deduce here E-AC3), or Dolby AC-4 stream**. ==============> Important to understand above
-  Practical Home Theater, 2021. p94 to 109
    - Dolby Pro Logic, Pro logic II (IIx, IIz) -> Stereo/Surround (2) channels matrixing
        - Old school dolby surround (sound on back)
        - Pro logic: front left, front center, front rigth and monaural surround channel
        - Pro Logic II: Breaks mono surround channel to stereo
            - <=> DTS Neo:6
        - Pro logic IIx: Back surround channel (6.1 and 7.1)
            - <=> DTS Neo:6
        - Pro logic IIz: Add 2 heigth channel
            - <=> DTS Neo:X
    - Dolby Digital
        - 5.1
            - No matrixing (real 5.1 channel)
            - + perceptual coding
            - <=> DTS 5.1 (aka DT encore)
        - EX
            - Add back surround channel (6.1 or incorrectly called 7.1)
            - <=> DTS-ES (discrete et matrix: https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/) (aka DTS encore ES)
        - Dolby Digital Plus (DD+)
            - Supports 14 channel
            - Supports data rate from 96kb/s to 6mb/s
            - More efficient than dolby digital 
            - lossy format
            - <=> DTS 96/24 (aka DTS encore 96/24),  DTS HD High-resolution audio 
        - Dolby True HD
            - As DD+ full 5.1, 6.1 or 7.1 channel
            - Supports 14 full range channels (34 in Atmos mode (I guess extended)) 
                - Do not confuse channel with Audio track/Objects
            - lossless encoding
            - <=> DTS-HD Master Audio,
    - Dolby Atmos
        - > One of the advantage of Dolby Atmos, is that it is "one mix to rule them all". Instead of mixing separately for 5.1, 7.1, and Atmos, engineers create just one Atmos mix, which then work on everything 
        - Work on everything is layout 
        - In Home Tehater Atmos supports 128 channel and 64 speakers
        - At home Mini confg is 5.1.2, reco is 5.1.4, max at home is 24.1.10
        - https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/ (Nombre max de canaux théoriques: 34 canaux (particuliers), 64 canaux (professionnels), Nombre d’objets audio max 128)
            - Consistent is 24.1.10 (if remove the sub)
        - Atmos is not a codec it is delivered by DD+ fpr streaming and Dolby True HD for blue-ray
        - <=> DTS:X, DTS:X Pro (transported on DTS HD Master audio) https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/)
        - Those format are 3D audio container
    - If playing non atmos based channel content on Atmos system we use **Dolby Surround UpMixer** (to not confuse with old school dolby surround)
        - <=> DTS Neural X 
        - Equivalent to ProLogic
    - We also have (p108) Dolby Atmos Virtualization to play atmos channel on sterreo, 5.1, sound bar, phone...
        - <=> DTS virtual X (p109)
        - See https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/
- https://www.aftvnews.com/dolby-atmos-surround-sound-audio-is-supported-in-netflix-on-the-fire-tv-stick-4k-max/:
    - > One of the shortcomings of the original Fire TV Stick 4K is that, even though the device supports Dolby Atmos surround sound audio, it is not supported within the Netflix app. This is because, for some absurd reason, **Netflix has decided that only devices running Fire OS 7 will support Dolby Atmos in Netflix**, even though there are plenty of apps supporting Dolby Atmos on Fire OS 6 devices. Since the original Fire TV Stick 4K runs Fire OS 6, it does not support Dolby Atmos in Netflix. Thankfully, the new Fire TV Stick 4K Max addresses that shortcoming by running Fire OS 7 and it does support Dolby Atmos playback in Netflix.
    - Bacon comment is wrong, no hardware
- https://www.aftvnews.com/fire-tv-stick-4k-is-not-getting-fire-os-7-with-the-new-interface-update/
    - >The biggest exception to that, which I’m aware of, is support for Dolby Atmos audio in Netflix, which is currently only supported on Fire OS 7 devices. It’s assumed that if the Fire TV Stick 4K is updated to Fire OS 7, it will gain Dolby Atmos support in Netflix, which would be a significant perk. 
- If netflix, playing Heart of Stone on FireTV 4k, 5.1 layout we have have (Movie sound mode button)
    - Stereo
    - Doby Audio, DD+
    - Dolby Atmos / DSur, front panel shows DD+ DSur, why ?
        - Even if I have a 5.1 layout, it is an atmos receiver (supports 7.1 or 5.1.2: https://manuals.denon.com/AVRX2700H/EU/FR/DRDZSYiltbhifm.php)
        - So with this mode, it use DD+ 5.1, Use Dolby Surround upmixer to have atmos, and then Atmos to 5.1 layout (even if mini config is 5.1.2)
    - DD+ Neural-X : use DTS UpMixer instead of Dolby Surround UpMixer
    - MultiCh Sterreo
    - Mono Movie
    - Virtual - Kind of ProLogic
- If netflix, playing Heart of Stone on Apple TV, 5.1 layout we have have 
    - Stereo
    - Dolby Atmos
        - Here we receive Atmos and it is translated to 5.1 layout <== best choice
    - MultiCh Sterreo
I do not know if Netflix uses E-AC3 or AC4 codec to send Atmos.

<!-- will not try if prime and atmos is working -->

Also this make it clearer: https://manuals.denon.com/AVRX2700H/NA/fr/DRDZSYyrtgycpw.php

It is consistent with https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/ (saved at [doc](./doc/Dolby%20ou%20DTS%20Quelles%20différences%20Audiophile%20Débutant.html))
<!-- https://www.avforums.com/threads/avrx1300w-downmixing-7-1-atmos.2165059/ -->

<!-- ok now fully ccl --> 

### Remote control

Apple TV has 
- official remote (only 1 per ATV: https://support.apple.com/fr-fr/guide/tv/atvbc9953e63/tvos)
- Other devices 
    - Bluetooth
    - Remote App and devices
        - Macbook pro
        - IPhone
- Learn remote (IR)

We can add a remote game controller via BT: See [Zwift+Apple TV](#zwiftapple-tv).

Xbox 360 I own  does not support BT (both model 1403)
https://www.slashgear.com/1281386/how-to-connect-an-xbox-controller-to-your-apple-tv/

WiiU remote can not be used via Bluetooth, tried to pair but can use pairing code. I ried with Zwift same issue.
<!-- I could try on PC but will not do as suing small ketboard -->

WiiU remote can be used via IR: https://www.reddit.com/r/wiiu/comments/808sj8/tutorial_how_to_use_a_wii_u_gamepad_as_a/?rdt=49701 using learn remote but I can not emable the Option (I do not have a WiiU)

I will use remote of old Android TV.

We can use a replacement remote https://support.apple.com/fr-fr/HT208492

<!-- we can check a dvd dolby digital and blue DTS HD master audio, via player no stop here -->

<!-- we can stop here an ccl -->