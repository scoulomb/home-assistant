# Sound 


## Home cinema


[See Apple TV in Docking station for setup](https://github.com/scoulomb/docking-station/blob/main/README.md#apple-tv-4k-3gen)



## Concepts

Surround Sound Processing (Dolby Pro Logic: https://en.wikipedia.org/wiki/Dolby_Pro_Logic) and Audio compression (Dolby digital: https://en.wikipedia.org/wiki/Dolby_Digital) 

### Surround Sound Processing


Quoting Dolby Pro Logic: https://en.wikipedia.org/wiki/Dolby_Pro_Logic

> Dolby Pro Logic is a surround sound processing technology developed by Dolby Laboratories, designed to decode soundtracks encoded with Dolby Surround. The terms Dolby Stereo and LtRt are also used to describe soundtracks that are encoded using this technique.

> Dolby Stereo (also known as Dolby MP or Dolby SVA) was developed by Dolby in 1976 for analog cinema sound systems. 
The format was adapted for home use in 1982 as Dolby Surround when HiFi capable consumer VCRs were introduced. It was further improved with the Dolby Pro Logic decoding system after 1987.

> **The Dolby MP Matrix was the professional system that encoded four channels of film sound into two. This track used by the Dolby Stereo theater system on a 35mm optical stereo print and decoded back to the original 4.0 Surround.** 
> **The same four-channel encoded stereo track was largely left unchanged and made available to consumers as "Dolby Surround" on home video.** However, the original Dolby Surround decoders in 1982 were a simple passive matrix three-channel decoder: L/R and Mono Surround. The surround was limited to 7kHz. It also had Dolby Noise Reduction and an adjustable delay for improved channel separation and to prevent dialog leaking and arriving to listeners' ears first. The front center channel was equally split between the left and right channels for phantom center reproduction. This differed from the Cinema Dolby Stereo system which used active steering and other processing to decode a center channel for dialog and center focused on screen action.

> Later on in 1987, the Pro Logic decoding system was released to consumers. It featured virtually the same type of four-channel decoding as the Dolby Stereo theater processor with active steering logic and much better channel separation (up to 30dB) as well as including a dedicated center channel output for the first time. Many standalone Pro Logic decoders also included a phantom center option for compatibility with earlier non-Pro Logic Dolby Surround equipped home theaters to split the center channel signal to the L/R speakers for legacy phantom center reproduction.

> Dolby Surround Pro Logic is the full name that refers to the matrix surround format and decoding system in one. When a Dolby Surround soundtrack is created in post production (Dolby MP Matrix), four channels of sound are matrix-encoded into an ordinary stereo (two-channel) soundtrack. The center channel is encoded by placing it equally in the left and right channels minus 3dB; and the surround channel is encoded using phase shift techniques for out of phase information (L-R). The surround channel was often used for ambient background sounds in the original recording, music scores and effects.

> A Dolby Pro Logic decoder/processor "unfolds" the soundtrack back into its original 4.0 surround—left and right, center, and a single limited frequency-range (7 kHz low-pass filtered[2]) mono rear channel—while systems lacking the decoder play back the audio as standard stereo. 


From Practical Home Theater, 2021. p94 to 109 and https://en.wikipedia.org/wiki/Dolby_Pro_Logic (channels matrixing)
- Old school dolby surround (1984). Quoting wiki
    - > It was capable of decoding Dolby Stereo **four-channel** soundtracks to three output channels (Left, Right, Surround). The Center channel was fed equally to the Left and Right speakers
- Pro logic (1987): front left, front center, front rigth and monaural surround channel
- Pro Logic II (2000): Breaks mono surround channel to stereo
    - <=> DTS Neo:6
- Pro logic IIx (2003): Back surround channel (6.1 and 7.1)
    - <=> DTS Neo:6
- Pro logic IIz (2009): Add 2 heigth channel
    - <=> DTS Neo:X
- Dolby surround (2014). Quoting wiki
    - > Dolby reintroduced the Dolby Surround terminology in 2014. The term now refers to a new upmixer whose purpose is to enable Atmos receivers and speaker configurations to serve non-Atmos signals.
    - > Dolby Surround is a complete replacement for Pro Logic that upmixes stereo and multi-channel inputs to play over Atmos configurations. 


### Digital Audio compression


From Practical Home Theater, 2021. p94 to 109 and https://en.wikipedia.org/wiki/Dolby_Digital

- 5.1
    - No matrixing (real 5.1 channel)
    - + perceptual coding
    - <=> DTS 5.1 (aka DT encore)
- Dolby Digital EX
    - (wiki) > Dolby Digital EX is similar to Dolby's earlier Pro Logic format, which utilized matrix technology to add a center surround channel and single rear surround channel to stereo soundtracks
    - (wiki) > EX adds an extension to the standard 5.1 channel Dolby Digital codec in the form of matrixed rear channels, creating 6.1 or 7.1 channel output. 
    - Similar to Pro-logic
    - <=> DTS-ES matrix: https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/ (aka DTS encore ES) (saved at [doc](./doc/Dolby%20ou%20DTS%20Quelles%20différences%20Audiophile%20Débutant.html)
    - > Formats numériques 5.1 compressés & étendus virtuellement à 6.1 et 7.1 (https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences)
- Dolby Digtal Surround EX
    - Add back surround channel (6.1 or incorrectly called 7.1)
    - (wiki) > It provides an economical and backwards-compatible means for 5.1 soundtracks to carry a sixth, center back surround channel for improved localization of effects. The extra surround channel is matrix encoded onto the discrete left surround and right surround channels of the 5.1 mix, much like the front center channel on Dolby Pro Logic encoded stereo soundtracks.
    - <=> DTS-ES discrete: https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/ (aka DTS encore ES)
    - > Format numérique 6.1 compressé (https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences)
    - I understand here it is matrix encoded and decoded: https://ww2.mathworks.cn/help/audio/ug/surround-sound-matrix-encoding-and-decoding.html, where simple Digital EX no additional encoding, just decosing additional channel
- Dolby Digital Plus (DD+)
    - Supports 14 channel
    - Supports data rate from 96kb/s to 6mb/s
    - More efficient than dolby digital 
    - lossy format
    - <=> DTS 96/24 (aka DTS encore 96/24),  DTS HD High-resolution audio (> Format numérique 5.1haute résolution compressé (https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences)))
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
    - Atmos is not a codec it is delivered by DD+ for streaming and Dolby True HD for blue-ray
    - <=> DTS:X, DTS:X Pro (transported on DTS HD Master audio) https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/)
    - Those format are 3D audio container
    - If playing non atmos based channel content on Atmos system we use [**Dolby Surround UpMixer**](#surround-sound-processing) (to not confuse with old school dolby surround)
        - <=> **DTS Neural X** 
        - Replace Dolby ProLogic
    - We also have (p108) Dolby Atmos Virtualization to play atmos channel on sterreo, 5.1, sound bar, phone...
        - <=> **DTS virtual X** (p109)
    - See https://www.audiophiledebutant.fr/dolby-ou-dts-quelles-differences/

### Virtualisation and Upmix

Here are assumptions...

I assume AVR should do Dolby Atmos Virtualization when playing Atmos content on 5.1 layout silently (also not really virtualiation, remind quote above > Instead of mixing separately for 5.1, 7.1, and Atmos, engineers create just one Atmos mix, which then work on everything ).

So 
- Atmos + Atmos vitualization is implied
- And Atmos + virtual:X / Neural:X does not make sense


Then https://www.reddit.com/r/hometheater/comments/b7ftd5/what_does_dsur_on_my_receiver_actually_mean/?rdt=60452
> I'm watching a movie with Dolby TrueHD. I can choose "Dolby TrueHD" or "DTHD + Dsur" or I'm watching a movie with DTS. I can choose "DTS-HD MA" or i can choose "DTS-HD MA + Dsur."

Here I assume we talk about 5.1 pure source and not Atmos transported by DTHD/DD+(E-AC3) or AC4 as "Engineers create just one Atmos mix, which then work on everything".
Indeed we can not have `Atmos + DSur` but we have `DD+/DD/DTHD + DSur`.
Meaning we play non Atmos channel on Atmos system.

> It adds Dolby Surround processing to the source to upmix or downmix to your current setup. If you have a stereo source and a 5.1 setup it will use DSur to upmix the source. If the source and setup match DSur won't do anything, even if it shows on the display.

So if layout is 5.1, DSur (see [**Dolby Surround UpMixer** above](#digital-audio-compression)) does nothing in that case 

When layout is 7.1 and receive 5.1, I assume DSur up mix (or surround EX)

Here Denon setup https://manuals.denon.com/AVRX2700H/NA/fr/GFNFSYxkcmyvmq.php

For info here is how downmix works for Dolby ProLogic IIx and Dolby Atmos: https://professionalsupport.dolby.com/s/article/How-do-the-5-1-and-Stereo-downmix-settings-work?language=en_US


### Dolby Atmos transported/delivered by Dolby True HD, Dolby Digital Plus (E-AC3), AC-4

- https://en.wikipedia.org/wiki/Dolby
    > **Dolby Atmos is not a codec**; on the consumer market, pre-recorded Dolby Atmos is **delivered as an extension to a Dolby TrueHD, Dolby Digital Plus (I deduce here E-AC3), or Dolby AC-4 stream**. 
- https://blog.son-video.com/2019/08/votre-ampli-est-il-compatible-avec-le-dolby-digital-plus/: Atmos is delivered via DD+ codec
- https://developer.dolby.com/technology/dolby-atmos/overview/
    > **Dolby Atmos®** is an immersive audio format that can be delivered via multiple audio codecs including **Dolby Digital Plus and Dolby TrueHD** (but NOT Dolby Digital). **Blu-ray Discs deliver Dolby Atmos using Dolby TrueHD (with Dolby Digital Plus as an available alternative), and broadcast and streaming services deliver Dolby Atmos using Dolby Digital Plus.** In order to maintain compatibility with millions of devices in consumer homes, Dolby Atmos in these codecs is implemented as a backwards-compatible extension. Dolby Atmos data is hidden within the bitstream and can be decoded by a Dolby Atmos-compatible A/V Receiver, soundbar or television. Non-Dolby Atmos capable devices will decode a 5.1-ch or 7.1-ch version from the Dolby Digital Plus or Dolby TrueHD bitstreams.wiki

**Atmos (which is not a codec) s backward compatible with non atomos AVR.**

### Codec Compatibility (DD+, True HD) avec DD


- https://blog.son-video.com/2019/08/votre-ampli-est-il-compatible-avec-le-dolby-digital-plus/: 
- Dolby true HD bacward compatible Dolby Digital (AC3): Source transmittinmg only dolby digital kernel (section "L’exemple du Dolby True HD")
- **Dolby Digital Plus (E-AC3)** not fully bacward compatible with Dolby Digital (AC3)
    - > Avec le Dolby Digital Plus, il n’y a pas un système de cœur comme avec le Dolby True HD. Il serait en effet impossible de mettre un cœur qui dispose d’un débit plus important que le flux total.
    - > La rétro-compatibilité est donc pensée au niveau du récepteur. Que ce soit la TV, un lecteur Blu-ray ou un autre lecteur, il contient un décodeur DD+. Ce décodeur Dolby Digital Plus contient aussi un ré-encodeur en Dolby Digital (AC-3). Lorsque le récepteur est branché à un système audio qui ne fait pas de Dolby Digital Plus, il y a possibilité de transcoder en Dolby Digital à 640 kbps, 
    - Confirmed in https://developer.dolby.com/technology/dolby-audio/dolby-digital-plus/
        - > Dolby Digital Plus bitstreams are not directly backwards compatible with Dolby Digital decoders, but Dolby Digital Plus decoders can decode Dolby Digital bitstreams.

<!-- I consider eveything above is CCL OK 29 oct 23 -->

### What is PCM?

https://support.denon.com/app/answers/detail/a_id/14872/~/pcm-defined
https://support.denon.com/app/answers/detail/a_id/14872/related/1


> What is PCM and what is it used for?
 
> PCM or Pulse Code Modulation is a digital representation of an analog signal. In most cases, it’s a 2-channel audio signal, but can also be a multi-channel (5.1 or 7.1) audio signal if it’s processed from a source such as a DVD, SACD or Blu-ray player. When your AVR is decoding a PCM based signal, you will see the “PCM” indicator lit on the unit’s front display. When decoding a multi-channel PCM signal from a player, the AVR will show “Multi Ch In” on the front display. 
 
> You can change any 2-channel PCM based signal into a surround field by using the MOVIE, MUSIC or GAME buttons on the VR’s remote. 


### SACD, DVD audio, PCM and DSD

- https://en.wikipedia.org/wiki/Super_Audio_CD#Technology
- Practical Home Theater p127 

## my Atmos setup


### Blue-ray player on PowerDVD with Windows Precision 3540 via HDMI

See https://github.com/scoulomb/docking-station#home-cinema-setup
I removed TB16...because of it does not support HDCP (https://www.reddit.com/r/Dell/comments/8z19u6/hdcp_with_tb16_dock_4k_netflix/)

#### Movie 1: Ad Astra

##### English 1 

- Signal: DTS-HD MSTR (Info button)
- Sound : DTS-HD+NeuX (Info button)

we can also select (non default mode) Sound (Movie sound button on RC (Remote Control))

- Stereo
- DTS-HD MSTR
- DTS-HD + DSur (as said [in virtualisation and upmix section](#virtualisation-and-upmix), in a 5.1 layout it is useless)
- DTS-HD+NeuX (same as DSur)
- DTS-HD+VirtualX (useful if headset is plugged)
- Multi Ch STereo
- Mono Movie
- Virtual

In Power `DVD > Video, Audio, Subtitles > More audio settings > Output mode` is
`Non Decode high-definiton audio to external devices`


If I select: `Non Decoded Dolby digital audio to external devices`

- Signal: DTS
- Sound : DTS+NeuX

we can also select (non default mode) Sound
- Stereo
- DTS Surround
- DTS + DSur
- DTS+NeuX 
- DTS+VirtualX
- Multi Ch STereo
- Mono Movie
- Virtual

We lose the DTS-HD.

I Iselect PCM decoded by power DVD
- Signal: PCM
- Sound : SDur 

we can also select (non default mode) Sound
- Stereo
- Dolby audio dolby suuround
- DTS NeuX
- DTS VirtualX
- Multi Ch STereo
- Rock Arena
- Jazz club
- Matrix
- Virtual

We are using DSur [**Dolby Surround UpMixer** above](#digital-audio-compression)to upmix in 5.1 (or an atmos layout 7.2.4), the downmixed signal by PowerDVD.... 

Set back in non decoded high res

##### english 2 (descriptive audio)

- Signal: DD
- Sound : DD + DSur


we can also select (non default mode) Sound
- Stereo
- Dolby audio - Dolby Digital
- Dolby audio - DD + DSur
- Dolby audio - DD + NeuX
- Multi Ch STereo
- Mono movie
- Virtual

##### english 3 (audio comment)

Same as DD (english 2)

##### French

- Signal: DTS
- Sound : DTS+NeuX

Same as [Movie 1/english 1](#movie-1-ad-astra) with non hih res decoding


#### Movie 2: Boite noire

##### France 1 DTS-HD MA 5.1

- Signal: DTS-HD MSTR
- Sound" DTSHD+NeuX

Then same as [Movie 1/english 1](#movie-1-ad-astra) (including non decoded)

##### France 2 Dolby True HD 7.1

Here PowerDVD indicates it is a 7.1 channel [signal](#digital-audio-compression). <!-- did not check for other -->

- Singal: Dolby atmos - True HD
- Sound: Dolby atmos

And we can select

- Stereo
- Dolby audio - Dolby True hd
- Dolby atmos/dsur
- Dolby audio - TrueHD + NeuX
- Multi Ch STereo
- Mono movie
- Virtual


Fun fact, when dolby atmos/dsur is selected signal is modified from
- Signal `Dolby Audio - True HD` to `Dolby atmos - true HD`

For example

IF we select sound Dolby true HD (via movie sound button of RC)
- Signal Dolby Audio - True HD
- Sound Dolby Audio - Dolby true HD

IF we select Dolby atmos/dsur
- Signal: Dolby Atmos - True HD
- Sound: Dolby Atmos

Dolby Atmos is transported via True HD

If we selected non high res decoded in power dvd

Signal Dolby audio - DD
Sound : Dolby audio - DD + DSur (as said [in virtualisation and upmix section](#virtualisation-and-upmix), in a 5.1 layout it is useless)


Here it is interesring because as in Movie it illustartes [codec compatibility](#codec-compatibility-dd-true-hd-avec-dd)
> Source transmittinmg only dolby digital kernel (section "L’exemple du Dolby True HD")

<!-- was tested actually -->

Front panel shows sound data that we have with `info` button

Expect same for DVD in DD5.1

<!-- star wars surround ex? osef -->

Test were done with Videoprojector.


### TV box

#### Atmos test

I have 2 Fire TV sticks

- https://www.amazon.fr/gp/product/B08C1KN5J2/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1 -> on center or [left screen](https://github.com/scoulomb/docking-station/blob/main/README.md#zwiftapple-tv)
- https://www.amazon.fr/gp/product/B07PW9VBK5/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1 (FireTV 4K) -> on AVR media player

Both are supposed to support Atmos.
Only latter support 4k.

I have Apple TV 4k 3gen (part of apple ecosystem)

Test will be done with VG32 (see https://github.com/scoulomb/docking-station#home-cinema-setup)


#### FireTV 4K

##### Movie 1 - Heart of Stone (which is an Atmos Movie)

It appears as 4k, HDR, 5.1 in app (video project will not show 4k).

- Signal: Dolby Audio - DD+ 
- Sound: Dolby Audio - DD+ + DSur (this is sound mode Dolby Atmos/Dsur)

So we do not have DD but DD+.
And DSur (as said [in virtualisation and upmix section](#virtualisation-and-upmix), in a 5.1 layout it is useless)

We can select sound:
- Stereo
- Dolby audio - Dolby Digital PLus
- Dolby Atmos/Dsur
- Dolby audio - DD + NeuX (same as DSur)
- Multi Ch STereo
- Mono movie
- Virtual

No need to try non atmos movie as here atmos not decoded.

Sound mode in AVR does not impact what netflix app shows (5.1, Vision....)


So Atmos is not supported on FireTV 4k. Oh !!

#### Apple TV 4k


##### Movie 1 - Heart of Stone (which is an Atmos Movie)

It appears as Ultra 4k, Atmos in app (video project will not show 4k).

- Signal: Dolby Atmos
- Sound: Dolby Atmos (same in front panel)

We do not have DSur option as atmos "1 mix for all"
Zone 2 stereo downmix [see info](#virtualisation-and-upmix)

We can select sound:
- Stereo
- Dolby Atmos
- Multi CH Stereo

Sound has better quality than firetv

Note 
- Settings video and audio > Format HDR and Atmos selected 
- Tested via VG32 (not videoprojector)
    - If I plug videoprojector output, the format in settings is auto changed to 1080p SDR and netflix then come to HD
    - Also if Sound mode in AVR is set to (seems randow)
        - MCHannel Stereo, netlix app whill show Dolby Vision
        - Atmos, netflix app will show atmos

If in Aplle TV settings we can change audio format to 
- Dolby Digital 5.1
- Stereo 
Also audio output possible via AirPlay (similar to zoneurn 2).

we have this warning:
Audio will be re-encoded as Dolby Digital 5.1. Turn off change format to improve audio quality and enable Dolby Atmos.
For more inforamtion, see https://support.apple.com/appletv/audio.

I change to 5.1, still display Atmos in netflix app but

- Signal: Dolby Audio - DD
- Sound: Dolby Audio - DD + DSur (same in front panel)

we can also select (non default mode) Sound
- Stereo
- Dolby audio - Dolby Digital
- Dolby audio - DD + DSur
- Dolby audio - DD + NeuX
- Multi Ch STereo
- Mono movie
- Virtual

Same mode as [Blue rayMovie 1 Ad Astra  english 2](#movie-1-ad-astra)

Note here we do not have DD+, Apple TV reencode DD+ signal to DD.
Apple did this for [code compatibility](#codec-compatibility-dd-true-hd-avec-dd).

> Ce décodeur Dolby Digital Plus contient aussi un ré-encodeur en Dolby Digital (AC-3)

If stereo it will downmix to stereo, see -[downmix](#virtualisation-and-upmix).

#### Movie 2 - non Atmos movie - Call my agent e1-s1


I will reveret settings to Auto, Atmos Avaialble (same behavior if set to DD).
Movie is shown as 5.1 in app


- Signal: PCM
- Sound: Multi CH IN


And here surprise Apple TV is not doing a passthrough (unlike Atmos).
It is decoding Netflix DD+ and transmits it as Multi In (so we have 5.1)

- Stereo
- Multi Ch IN 
- Multi In + DSur (and here also useless in 5.1 layout)
- Multi In + NeuX (same as Dsur)
- Multi In + VirtualX
- Multi Ch STereo
- Mono movie
- Virtual

<!-- sutff not tested are not required -->


##### Why Atmos not supported in Netflix with FireTV 4k?

From Netflix help Atmos support: https://help.netflix.com/en/node/23934
I do not have this Display option: Auto (up to 4K Ultra HD) in Netflix app
I have only automatic

From netflix help

> Sure, let me know on how it goes.
> As we have checked further, there is in fact one supported device for Atmos and it is the Fire TV Stick 4K Max .

> Super interesting, I have fire tv 4k
> not the 4k max but weirdly when checking the spec they claim to support atmos

> You device might support Atmos for other apps, but it is not supported for Netflix

> no, any future plan to support atmos on more device

> As of the moment, there's no new for it. But will take a note of that as a feedback.

This is confirmed on this forum

- https://www.aftvnews.com/dolby-atmos-surround-sound-audio-is-supported-in-netflix-on-the-fire-tv-stick-4k-max/:
    - > One of the shortcomings of the original Fire TV Stick 4K is that, even though the device supports Dolby Atmos surround sound audio, it is not supported within the Netflix app. This is because, for some absurd reason, **Netflix has decided that only devices running Fire OS 7 will support Dolby Atmos in Netflix**, even though there are plenty of apps supporting Dolby Atmos on Fire OS 6 devices. Since the original Fire TV Stick 4K runs Fire OS 6, it does not support Dolby Atmos in Netflix. Thankfully, the new Fire TV Stick 4K Max addresses that shortcoming by running Fire OS 7 and it does support Dolby Atmos playback in Netflix.
    - Bacon comment is wrong, no hardware
- https://www.aftvnews.com/fire-tv-stick-4k-is-not-getting-fire-os-7-with-the-new-interface-update/
    - >The biggest exception to that, which I’m aware of, is support for Dolby Atmos audio in Netflix, which is currently only supported on Fire OS 7 devices. It’s assumed that if the Fire TV Stick 4K is updated to Fire OS 7, it will gain Dolby Atmos support in Netflix, which would be a significant perk. 


<!-- will not try if prime and atmos is working -->

Also this make it confusing but our anlysis bring structure: https://manuals.denon.com/AVRX2700H/NA/fr/DRDZSYyrtgycpw.php,
For example DSur should not be in same array as DD.

<!-- we are here all above is well concluded, no delete line but weere rewritten do not come back on diff, virtualization and upmix stop also ccl yes -->



#### Molotov program on AppleTV 4k

- Signal: PCM
- Sound: Multi CH Stereo

We can choosee
- Stereo
- Dolby Audio - Dolby Surround -> Here upmixer makes sense
- DTS NeuralX -> Here upmixer makes sense
- DTS VirtualX
- Multi Ch STereo
- Mono movie
- Virtual
 
This PCM is not multi. <!-- juge understood enoughstop -->
If playing movie stereo from laptop browser (youtube, medaitheque example) -> same as Molotov on Apple TV.
Tested with Youtube. 

<!-- stop here also OK-->

<!-- here -->

## Sound

See as introduction
- https://github.com/scoulomb/docking-station/blob/main/README.md#music
- https://github.com/scoulomb/docking-station/blob/main/README.md#apple-tv-audio
- https://github.com/scoulomb/docking-station/blob/main/README.md#zwiftapple-tv (pre-out)

We can do multi-room music

### Multiroom

We can test with  
- Denon AVR X-2700 H with 5.1 speaker
- 2 denon-home 150
- 1 HIFI player (Atoll MA100 amp +HD120 pre-amp)

Let's do this initial setup:

- We pair the 2 Denon Home as stereo pair in HEOS app
- We set the stereo-pair in same room as AVR in HEOS app
- We have have the AVR zone 2 pre-out + Atoll HD120 as input of Hifi player amp as below

````
Apple TV   -> Zone 2 AVR -> Switch box -> MA100
Laptop USB -> HD120      ->
````

#### 1- Via HEOS (sync avr /denon home stereo pair + stereo pair) + Zone 2 pre-out

- This is working great for source (like vinyle) but weirdly when source is Heos music (for instance deezer via HEOS) we have desynchro (in particular in zone 2!!!!)


#### 2- Via HEOS (stereo pair) +  Zone 2 pre-out + Air Play (embeeded in AVR) + Home 150 AirPlay stereo pair


Note when playing air play, in current implem it ungroup the Home 150 stereo pair from avr (with the main + zone 2), and it is seen as 2 AirPlay spearkers
It does not have functional impact


In the past it was even ungrouping the stereo pair: https://www.denon.com/ro-ro/blog/denon-home-why-you-should-think-about-stereo-pairing-ro
> It is also worth mentioning that, due to technical reasons, as of this moment, Apple Airplay will be disabled in stereo configuration, but support for this streaming option is incoming – so hold tight, Apple fans.


#### 3- Via HEOS (stereo pair) +  Zone 2 pre-out + Air Play (apple TV) + Home 150 AirPlay stereo pair

We can use use AirPlay from Apple TV
It is also working. I noticed less desynchro in this setup.

#### 4- Via HEOS (stereo pair + group AVR/Home 150) +  Zone 2 pre-out + Air Play (apple TV)

Unlike when AirPLay of receiver is used, if we use AirPlay of apple TV, AVR-Home 150 stereo pair is working

#### 5- Same as 3 but we replace Zone 2 pre-out by AirPplay receiver plugeed to HD120 DAC 

It also works with 2 and 4. <!-- not tested the also work work with 2 and 4-->


We can use as AirPlay receiver which supports AirPLay 2 (for multiroom suuport). See 3 versions of AirPlay: https://en.wikipedia.org/wiki/AirPlay
- AirTunes
- Airplay 1
- AirPlay 2

This receiver can be plugged RCA plug, Digital Audio or Coaxial (Digital).
When Digital receiver DAC can be used.

See [music streamer with AirPLay 2](./music-streamer.md)

Alternative is to use laptop with 
- shairport sync: https://github.com/mikebrady/shairport-sync/blob/master/BUILD.md
- where we have switch box active HD120 pre-amp.

##### shairport seyp

I used 

````
shairport-sync -v --statistics
````

 we can  use `&` mode

 ````
 shairport-sync &
 ````

 Note that when used `systemctl`, speakers were not visible as AirPlay speaker from deezer app: https://github.com/mikebrady/shairport-sync/blob/master/BUILD.md#5-enable-and-start-service

 Also noticed that when launching process it has to be startrd when in sound setting output is set to Atoll Digital Output oterwise can stay in built-in.
 In HD120 it using usb-red.

 Stop 

````
$ ps -aux |  grep  shairport
scoulomb   60427  6.4  0.0 839056 27192 pts/1    Sl   12:02   0:22 shairport-sync
scoulomb   62867  0.0  0.0   9216  2560 pts/1    S+   12:08   0:00 grep --color=auto shairport
$ kill -9 60427
````
  
##### AirPLay 1

If we use Kodi as AirPlay receiver. No multiroom is supported.
It will disable other speakers.

Same observed with Triangle AIO-C.
An alternative for multiroom would to use several AIO as aux in Home 150 + AVR.
Similar to **setup 4**.

#### 6- Replace stereo pair by 2  Mono speaker

We can in all setup above ungroup stereo pair and have 2 mono HEOS (1,4) or AirPlay speaker(2,3).

<!-- not all tested setup 6 -->


### Other alternative 

- Receiverlike  AIO-C can embeed
    - Spotify connect 
    - Music provider directly.
    - DLNA
    - AirPLay

See [music streamer with AirPLay 2](./music-streamer.md)

[here-------------------------]
When using Deezer audio output we have 

- IPhone => Builtin speaker, or wire
- AirPlay and Bluetooth -> AirPLay see above and Bluetooth Headset but also HD120 (blue ligth on HD120)
- Google Cast => Google next or any receiver supporting chromecast
- Deezer connect => Phone tablet can be receiver to HD120 (via win app or browser, tested) and some latency

Bluetooth on HD120
- I was impressed by sound quality here: Actually receiver support Apt-x HD AUDIO + AAC 
- When used with iPhone it uses AAC code (to no confuse with AAC compression format). It is not loseless but gives good quality with iPhone
- Not tried: AVR could stream bluetooth signal to HD120

Spotify is the most complete




### Sound quality

- When playing via [Kodi](#kodi) AirPlay, deezer content in Hifi quality it shows this information

`2.0 44.1 khz 1411 kbs 16 bit`

- If I change audio quality to`standard`, it shows the same value. As those are the quality of Airplay tunnel.

#### Understand sampling and bit rate

https://www.headphonesty.com/2019/07/sample-rate-bit-depth-bit-rate/

#### Music quality

- Qutoting deezer app:
> Standard streams at 128kbps, High Quality at 320 kbps, and High Fidelity at 1411 kbps (FLAC), which requires a high-speed resolution.

See here codec details from music provider: https://www.audiophiledebutant.fr/comprendre-laudio/explication-sur-les-formats-numeriques-audio/
<!-- https://manual.yamaha.com/av/18/rxv485/fr-FR/341956619.html -->

- What is CD quality?
44.1 khz sampling frquency with a 16 bit depth is CD quality (Flac). Hi-res audio aims at Higher sampling rate rate.
Quoting https://electronics.sony.com/hi-res-audio-mp3-cd-sound-quality-comparison
> High-Resolution Audio files have a sampling frequency of 96 kHz/24 bit, which is significantly higher than the 44.1 KHz/16 bit sampling frequency of CDs.
I saw even 192 kHz.

- It we talk on bit rate (https://electronics.sony.com/hi-res-audio-mp3-cd-sound-quality-comparison)
    - > When comparing bitrate, or the amount of data transferred per second, High-Resolution Audio’s bitrate (9,216 kbps) is nearly seven times higher than that of CDs (1,411 kbps) and almost 29 times higher than that of MP3s (320 kbps). And the higher the bitrate, the more accurately the signal is measured.
    - > Popular streaming websites like Spotify and Pandora typically use a bitrate of 160 kbps, which is less than that of MP3s. If you spring for Spotify Premium, you’ll still only have access to 320 kbps tracks, which is equivalent to MP3s.

- Note mp3 encoding use psychoacoutic (as Dolby Digital+, Dolby True HD is loseless and I asusme it does not use psychoacoustic)

- How to go from 44.1 Hz/16 bit to bit rate computation
    - CD quality: 44.1 (sample per second)*16 bit*2channel= 1411.2 kbs
    - Hi res:     192 (sample per second)*24 bit*2channel= 9216 kbs



#### LAN Streaming tunnel

- Bluetooth use code (to not confuse with sound format): DBC is the worst, AAC and Apt-x ok with apple device but not lossless and use psychoacoustic.
AAC is relying on AAC lossy codec (https://en.wikipedia.org/wiki/Advanced_Audio_Coding)  to not confuse wiht AAC sound format.
- AirPlay over Wifi : it is limited to CD quality.
See: https://discussions.apple.com/thread/254583373
Which makes us understand the Kodi output in intro.

- A lossless way is to use DLNA. See [DLNA streaming](#dlna-streaming)
    - Not supported by Deezer
    - But Spotify supports it (seems Android only did not find on iPhone)


#### Smart speaker

Smart Speaker in the sense here that the reciver is directly receving the audio from Internet (NOT USING [Lan streaming tunnel](#lan-streaming-tunnel)

- **HEOS Deeezer streaming on AVR is limited to 320kbs** whereas application gives access to CD quality
    - Also see issue with [setup 1](#1--via-heos-sync-avr-denon-home-stereo-pair--stereo-pair--zone-2-pre-out)
- Spotify offers more option (on top of bluetooth/airplay) when streaming with spotify connect on AVR, Heos 150 and Alexa devices (including FireTV
    - Spotify thus offer its own multiroom techno in the end if speaker, receiver supports Spotify connect
    - ANd we do similar setup as with AirPLay (but no tunnel)
    - It is a proprietatary techno
    - Spotfy connect is not integrated directly as Deezer in Heos, they have their own techno


[ALL ABOVE OK -- we are here]


last item is visible as we have an heos service with avahi
alexa des not use spotyify connect (as using avahi)

#### DLNA streaming A


Spotify can use DLNA (did not see it in iOS version though). 
**Deezer does not support DLNA: https://en.deezercommunity.com/ideas/dlna-upnp-support-6742**

From NAS (and music station application) we can stream using DLNA (no multiroom except wired zone 2).
When connecting to music station in IPhone using same mecahanism as [FileStation](../appendices/file-sharing/qnap-file-sharing.md#before-we-go-further-lets-check-qfilepro-in-ios)
<!-- note we do not have DDNS in music station and wan IP in both, did the the check OK-->

We can also use [webUI](../appendices/file-sharing/qnap-smart-url.md#smart-url)) 

- File station (similar for Photo and Music station, and using same port as QTS desktop)
    - https://music.qlink.to/scoulomb
    - https://192.168.86.96:443/musicstation/
    - http://192.168.86.96:8080/musicstation/
    - https://scoulomb.myqnapcloud.com:443/musicstation/
    - http://scoulomb.myqnapcloud.com:8082/musicstation/
    - https://109.29.148.109:443/musicstation/
    - http://109.29.148.109:8082/musicstation/

or via QTS deskop and music app.

Note that multiroom from QMUsic app/webUI is not working though it should be multiroom (and called multizine in app)
https://www.son-video.com/rayonin/haute-fidelite/systemes-multiroom/systeme-hi-fi-multiroom (Sonos, DLNA, AirPlay + HEOS)
Workaround is heos group + wired zone 2 (tested OK)


https://github.com/open-denon-heos/heospy/blob/main/heospy/ssdp.py

avahi-browse --all --resolve | grep -C 4 spotify
~$ avahi-browse -d local _spotify-connect._tcp --resolve
avahi-browse -d local _matter._tcp --resolve
avahi-browse -d local _http._tcp --resolve
http://192.168.86.105/settings/
http://denon-home-150-2.local/settings/

avahi-browse -k --all (to not resolve service type)

avahi-browse -d local _airplay._tcp --resolve


avahi-browse -d local _airplay._tcp --resolve (airplay v1 and v2)

avahi-browse -d local _raop._tcp --resolve (old, airtunes)
https://openairplay.github.io/airplay-spec/service_discovery.html


If start shareport locally
shairport-sync -v --statistics

we can see it: avahi-browse -d local _raop._tcp --resolve
avahi-browse -d local _airplay._tcp --resolve


does it work through vpn??


dlna servvice kodi not visible spotify
avahi??



#### Music assistant

See https://blog.jlpouffier.fr/chatgpt-powered-music-search-engine-on-a-local-voice-assistant/ with music assitant
    - Lien linkedin



## Remote control B

Additional IR remote control on AMzon 


Apple TV has 
- official remote (only 1 per ATV: https://support.apple.com/fr-fr/guide/tv/atvbc9953e63/tvos)
- Other devices 
    - Bluetooth
    - Remote App and devices
        - Macbook pro
        - IPhone
- Learn remote (IR)

We can add a remote game controller via BT: See [Zwift+Apple TV](https://github.com/scoulomb/docking-station/blob/main/README.md#zwiftapple-tv).

Xbox 360 I own  does not support BT (both model 1403)
https://www.slashgear.com/1281386/how-to-connect-an-xbox-controller-to-your-apple-tv/

WiiU remote can not be used via Bluetooth, tried to pair but can use pairing code. I ried with Zwift same issue.
<!-- I could try on PC but will not do as suing small ketboard -->

WiiU remote can be used via IR: https://www.reddit.com/r/wiiu/comments/808sj8/tutorial_how_to_use_a_wii_u_gamepad_as_a/?rdt=49701 using learn remote but I can not emable the Option (I do not have a WiiU)

I will use remote of old Android TV.

We can use a replacement remote https://support.apple.com/fr-fr/HT208492

<!-- we can check a dvd dolby digital and blue DTS HD master audio, via player no stop here -->

<!-- we can stop here an ccl -->

check dlna

OK

C-THAOMA SETUP

dojo: dockig sation + teams + vpn

curl --config: https://everything.curl.dev/cmdline/configfile


airplay truncation: https://help.roonlabs.com/portal/en/kb/articles/airplay-setup#Set-Up

https://www.linkplay.com/
