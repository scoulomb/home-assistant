## Blue-ray setup BD-D8500

- https://fc.darty.com/notices/DOCUMENTATION/SAMSUNG/3439470/3439470_NOTCOMP.pdf 
- https://github.com/scoulomb/hifi-manual/blob/main/bd-d8500-manual.pdf

### Hard reset

1- Retirez tout disque ou périphérique de stockage USB.
2- Appuyez sur le bouton HOME pour accéder à l'écrand'accueil. 3. Appuyez et maintenez le bouton Arret (■) du panneau avant pendant 5 secondes au minimum.

Tous les réglages sont réinitialisés sur leur valeur d'origine par défaut."

(Solved remote not working with blue ray)


To make it work unplug for a while

### Audio

```text

Audio
Sortie numérique
Vous pouvez définir l'option Sortie numérique de
manière à ce qu'elle corresponde aux capacités du
récepteur AV que vous avez connecté au produit :
•
PCM : Choisissez ce réglage lors de la
connexion d'un récepteur AV prenant en charge
la technologie HDMI.
•
Bitstream (non traités) : Sélectionnez ce réglage
lors de la connexion d'un récepteur AV prenant
en charge la technologie HDMI et le format de
décodage Dolby TrueHD ou DTS-HD Master Audio.
•
Bitstream (DTS Ré-encodé) : Choisissez ce
réglage lors de la connexion d'un récepteur AV
muni d'une entrée optique numérique capable
de décoder le format DTS.
•
Bitstream (Dolby D Ré-encodé) : Sélectionnez
ce réglage lors de la connexion d'un récepteur
AV ne prenant pas en charge la technologie
HDMI mais doté de fonctions de décodage
Dolby Digital.

````

Choose with AVR bitrstream non traite (good surprise as Atmos is transported via True HD, AI got it wrong here)!
AVR is processing everything. See link with [README/apple TV](./README.md#1-why-apple-tv-sends-multichannel-pcm-for-non-atmos-content) as behavior different.

Also use in display sessting 1080i, not auto

Not when channel on DVB (TNT), it is dolby digital but AVR show DSUR (upmixer) but normal as it is dolby digital 2.0 and not DD 5.1
(also when source is D-TRUE-HD 5.1 AVR shows D-TRUE-HD, if source has atmos metadata via True HD AVR shows Atomos,
if source is DD, avr will show DD, same for DD+ (expect it, will not test/document)  (unless it converts DD+ to DD because of optical connection in AVR input) <!-- will not check0--)


**optical (Toslink or SPDIF)** only supports **Dolby Digital (AC-3)** and **DTS** in their **compressed 5.1 formats**, plus uncompressed stereo PCM.

Here’s why:

*   Optical has limited bandwidth (around 3–4 Mbps), so it **cannot carry high-bitrate formats** like **Dolby Digital Plus (DD+)**, **Dolby TrueHD**, or **DTS-HD Master Audio**.
*   DD+ and other advanced codecs require **HDMI** or **eARC** because they need more bandwidth and support for metadata.

If we want **DD+ or Atmos**, you need **HDMI ARC/eARC** or direct HDMI connection to the AVR.

See links with blue-ray wiring connection. <!-- do not dive -->

When 5.1 and atmos speaker if show DD/D-true-HD + DSUR <!-- not fully tested with all cases and will not document but that's the expectations -->
