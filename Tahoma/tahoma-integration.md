# Tahoma integration 


## Volet Hardware setup 

#### Volet chambre 

Use built-in Somfy-IO

#### Volet salon 

Use Izymo IO: https://www.automatismes.net/recepteurs-domotique/5140-somfy-1822660-micro-recepteur-izymo-io-comptabible-volets-roulants.html



##### We had thid initial setup

![initial setup](./media/inital-setup-izymo.PNG)

- Vert 
    - Vert fonce: terre installation 
    - Vert/Jaune qui sort de la gaine: Terre volet rolant
    - Vert/Jaune restant: Terre du store

- Bleu
    - Bleu: terre installation 
    - Bleu qui sort de la gaine: neutre volet rolant
    - Bleu: Terre du store

- Au niveau interrupteur volet de droite a gauche
    - pin1: descente
    - pin3: cable de phase
    - pin4: repiquage de la phase (pour le store)
    - pin6: montee

- Au niveau du trou partant vers l'interrupteur du store on observe ensuite 3 fils qui sont 
    - Marron: descente
    - Noir: montee
    - Noir partant de l'interrupteru phase


##### Standard

Nous sommes donc dans le cas standard, applique 2 fois
- pour le volet
- et pour le store

![](./media/schema-install-standard.PNG)

On observe que c'est 4 cable (car gestion montee et descente, comme si on avait [2 retour lampe](./media/schema-elec-simple-allumage.PNG) : https://www.123elec.com/branchement-interrupteur-va-et-vient)

- L (phase)
    - Phase installation -> (vers) interrupteur
    - Interrupteur -> moteur L1 montee,
    - Interrupteur -> moteur L2 descente (cable en plus car montee descente)
- N (Neutre)  moteur -> neutre installation
- T (terre) moteur -> terre installation


On peut donc avoir une installation equivalente (sans le repiquage de phase au niveau de l'interrupteur)

![](./media/installation-equivalente.PNG)

J'ai utilise un interrupteur Somfy Inis: https://www.amazon.fr/Somfy-1870881-Commande-Interrupteur-Descente/dp/B095CVJCJ1/ref=sr_1_4?keywords=interrupteur+volet+roulant&qid=1691931810&refinements=p_4%3ASomfy&s=hi&sr=1-4

On notera le `wago` le plus a gauche, prends la phase de l'installation et renvoit vert l'interrupteur
- Store
- Et volet (cable noir epais)

(Montage en derivation)

##### Nous sommes maintenant donc pret a installer le module `Izymo`.

Utliliser la video et le cablage ici 

https://www.automatismes.net/recepteurs-domotique/5140-somfy-1822660-micro-recepteur-izymo-io-comptabible-volets-roulants.html


![](./media/schema-montage-izymo.PNG)


La notice est aussi dispo: https://www.servistores.com/repository/documents/plans/Notice-recepteur-izymo_volet-roulant_io.pdf ou dans ce [repo](./media/Notice-recepteur-izymo_volet-roulant_io.pdf).


Le motage concret est donc le suivant

![](./media/montage-izymo.PNG)

- wago numero 1 - La terre est inchange 
    - terre: installation
    - terre store
    - terre volet 
- wago numero 2 - Connecte montee moteur volet au Izymo (L1) - fil noir
- wago numero 5 - Connecte descente moteur volet au Izymo (L2) - fil marron
- wago numero 3 - Connecte neutre
    - Neutre installation 
    - Neutre moteur store 
    - Neutre moteur volet
    - Neutre Izymo (N)
- wago numero 4 - connecte phase 
    - Phase installation 
    - Phase interrupteur store
    - **Phase interrupteur volet** (2 fils sur le schema mais un seul phisiquement sur le montage concret)
    - Phase Izymo (L)
- **Enfin (A) et (B) Izymo connecte a montee et descente interrupteur**

On voit donc que ce montage concret est coherent avec le schema de montage.

En gras nous avons mis les connexions non necessaire si utilise pas interrupteur filaire.

On voit donc dans ce cas que le Izymo (voir schema montage Izymo au dessus) prend les meme inputs qu'un cas [standard normal](#standard) (L, montee moteur L1, descente moteur L2) mais a besoin de repiquer le neutre en plus.

Quand interrupteur filaire: montee moteur L1, descente moteur L2 recupere sur Izymo A/B et interupteur connecte sur phase installation (wago). Equivalent donc interrupteur volet [standard](#standard).


Pour gagner espace boitier 
- utiliser wago 2 entree au lieu de 3 entree (wago 2 et 5 sur la photo). Un wago 4 entre n'existe pas.
- Interrupteur 
    - filaire
        - fil phase plus fin
        - interrupteur plus fin : https://www.somfypro.fr/produits/-/e-cat/1811272/COMMANDE_GENERALE_SMOOVE_ORIGIN_IB
    - ou automatique
        - isoler A/B
<!-- ok clear re-cf YES OK STOP - plus espace optional de decrire ici OK-->

Le store de la chambbre etant nativement automatique la phase installation est directemment connecte au moteur (fil L1).
D'ou un wago pour isoler l'ancienne descente (L2).
Et cette phase repart sur le store (qui lui a L1 et L2 car [interrupteur](#standard))

<!-- no need to re-check - could unplug to double check but ok stop -->

## Software setup 


### Pair

Pair with Tahoma box:
- Izymo module, volet
- Eventually Philips hue 

### Network 

See note [on network](../README.md#note-on-network)

<!-- stop checking more -->

### Alexa integration and routines 

Tested OK.
Can use routine. 

### Use apple homekit integration

Working well for "volet natif" but not with Izymo ==> Izymo module is not recognized as HomeKit device.

See https://forum.somfy.fr/questions/2528440-compatibilite-homekit-module-izymo

### Use OverKiz API and HA integration

I had an issue as OverKiz stop working, could believe it was a [network issue](#network),

But from https://github.com/home-assistant/core/issues/93511, this is due to an issue in HA.
Need to use last version (take image from DockerHub not recommend QNAP one).

This is the same problem reported here: https://community.home-assistant.io/t/overkiz-by-somfy-integration-failed-to-connect-how-to-debug/438011.


So I redeploy the docker image with last version as explained here https://www.home-assistant.io/installation/alternative.
See also [README](../README.md#installing-home-assistant-ha-on-qnap-nas).

It worked succesfully.
For store chambre we both have overkiz and HomeKit integration.


In dashbaord we can create (it is cover entity)
- a view with all the cover 
- Edit living room and bedroom view to add respective cover with overkiz (remove homekit one, the one without stop button)

See capture:

![](./media/ha-dashboard.PNG)

Thus we could use OverKiz API directly (via Python client) used by HA: https://github.com/iMicknl/python-overkiz-api/

### Tahoma local API integration

We have to use OverKiz API which is not loca
l.
They are thinking to integrate it in the Python client instead of using OverKiz cloud API: https://github.com/home-assistant/core/issues/69558


We can play with this local API anyway: 
- https://github.com/home-assistant/core/issues/69558#issuecomment-1523101067
- https://community.jeedom.com/t/commande-somfy-tahoma-avec-l-api-locale/106397/2

We have to activate Tahoma in dev mode
- https://github.com/Somfy-Developer/Somfy-TaHoma-Developer-Mode

I use `PowerShell` command given in this link https://community.jeedom.com/t/commande-somfy-tahoma-avec-l-api-locale/106397/2 and convert it to `curl` command using Chatgpt. 

<!-- use ubuntu WSL -->

[HERE]

## No tahoma integration (esphome based)

## Next ideas

- esphomne air sensor
- https://www.la-maison-electrique.com/somfy/62578-lanceur-de-scenario-tahoma-1824035-3660849517052.html
- Izymo on-off mais va etre complique car on la phase et retour lampe sur l'interrupteur (comme L -> L1/L2 moteur) mais neutre pas accessible facilement dans mon installation :(: https://www.somfy.fr/produits/1822649/recepteur-on-off-io-izymo (see montage eventuel)
- retry tuya with new version of HA: https://gist.github.com/scoulomb/8381cac25d5f695a5edf734e7ae47d6e
