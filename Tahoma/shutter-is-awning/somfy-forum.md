# Volet roulant vu comme un Store dans la Tahoma

## Question

https://forum.somfy.fr/questions/3220933-volet-roulant-store-tahoma


Bonjour atous !

Je voulais discuter d'un probleme intéressant à propos de mon volet roulant équipé d'un moteur Somfy IO qui a été installé par Monsieur Store (lien vers le produit : [Volet roulant Monsieur Store](https://monsieurstore.com/produits/volets-roulants/volets-roulants-alu-thermophonic-2)).

Malheureusement, je n'ai pas les détails exacts du modèle (il semblerait que "Intellium" soit une référence interne chez ce revendeur).

Voici le probleme : ce moteur est reconnu comme un "store" dans l'appli Tahoma.
 Ça peut sembler être un petit détail esthétique, mais ça cause quelques problèmes importants :

- Les commandes d'ouverture/fermeture sont inversées (un volet ouvert correspond a un store ferme)). Par exemple, envoyer une commande `setClose` via l'API locale de Tahoma avec un moteur configuré en "store" sur un volet roulant résulte en fait en un `setClose` de (100-X)% pour un vrai volet roulant. Cela perturbe également la commande vocale avec Alexa.
- Le volet roulant est catégorisé sous le groupe "store" (ce qui brouille les actions groupées).

Même après avoir tenté la méthode "supprimer et ré-ajouter" dans Tahoma, le problème persiste.

Alors voilà les détails : J'ai creusé dans l'API Tahoma et j'ai découvert que mon moteur de volet roulant est en fait un moteur de "store" ou considéré tel quel au niveau hardware.

```shell
curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/devices-integrated-motor.json
```

Dans la section **HARDWARE**, il est étiqueté comme un `io:HorizontalAwningIOComponent`, visible ici : [lien vers la source](https://github.com/scoulomb/home-assistant/blob/main/Tahoma/shutter-is-awning/out/devices.json#L963).

J'ai donc questions auxquelles j'espère que vous pourrez répondre :

1. Si je partage le code PIN de ma box Tahoma, pourriez-vous m'aider à identifier le modèle du moteur installé par Monsieur Store ? Et pourriez-vous confirmer s'il s'agit bien d'un moteur "store" utilisé pour un volet roulant ?
 (ou en utilisant le FirmwareRevision qui a pour value ["5104761X04"](https://github.com/scoulomb/home-assistant/blob/main/Tahoma/shutter-is-awning/out/devices.json#L959))


2. Si c'est le cas, est-ce normal qu'un installateur professionnel procède a ce genre d'installation ? Est-il raisonnable de s'attendre à ce que l'installateur propose une solution ? Ça semble être une erreur d'intégration. 
J'ai découvert des moteurs câblés compatibles à la fois avec les stores et les volets roulants, comme celui-ci : [lien vers le produit](https://voleda.fr/moteur-somfy-lt-50/moteur-somfy-lt-50-vectran-50-newtons-5012-472.html). Mais je ne trouve pas de moteur Somfy IO compatible à la fois avec les volets roulants et les stores. Si tel était le cas ne devrait-il pas y avoir un moyen de basculer entre les modes "volet roulant" et "store" dans le firmware du moteur ?

3. D'ailleurs existe-t-il un moyen de configurer Tahoma ou le Moteur pour traiter ce moteur comme un véritable volet roulant plutôt qu'un "store" ? (si ce cas n'est pas prevu (présentement ou a long terme, peut on procéder a un firmware flashing?)

4. Enfin, en termes de garantie de 5 ans, est-ce que cette situation pourrait potentiellement poser des problèmes pour la couverture de la garantie ?

Un grand merci pour votre aide inestimable ! J'ai partagé une analyse détaillée, accompagnée des sorties de l'API locale, ici : [lien vers l'analyse complète](https://github.com/scoulomb/home-assistant/blob/main/Tahoma/shutter-is-awning/README.md).

Merci pour vos idées et suggestions !

Bien à vous,

Sylvain

Problème similaire vu sur le forum: https://forum.somfy.fr/questions/2324963-volet-reconnu-tant-store

## Response

> Un tel roman pour ca....?
Votre moteur est tout simplement un moteur de store, c'est donc tout logiquement que ce moteur soit reconnu comme tel dans Tahoma.
Il arrive que les fabricants posent des moteurs de store dans des VR et inversement.
Il n'y a rien à faire sauf à changer le moteur pour un de VR.
Bonne journée

And on this question https://forum.somfy.fr/questions/3220107-volet-roulant-io-inverse-google-home



>Bonjour,
L'icône de la cuisine est celle d'un store.
Le moteur utilisé par le volet est en fait celui d'un store.
Ce qui explique le problème d'inversion des commande
Un volet ouvert corespond a un store ferme.
J'ai le même probleme:https://forum.somfy.fr/questions/3220933-volet-roulant-store-tahoma#answer_8348356
Bonne journée
Sylvain


> Bonjour Stéphane et Sylvain,
En effet vous avez chacun un moteur installé qui est un moteur de store et non de volet roulant ce qui explique cette inversion.
Bonne journée,


> Mon probleme va ce régler , je vais recevoir un nouveau moteur de volet ce coup ci et le moteur "store" sera retourner car non conforme a ma commande.
Mais c'est quand meme etrange de ne pas pouvoir leur changer d'usage.
Merci pour votre aide
