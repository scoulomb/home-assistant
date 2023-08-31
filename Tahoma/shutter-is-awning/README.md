# Investigation 

## Description 

### Probleme

- Somfy IO integrated shutter est reconnu comme un store (awing) dans l'appli Tahoma. 
- Le comportement est different avec le Izymo IO shutter module

### Experience 


Comparons le comportmeent du
- [Izymo shutter](https://www.somfy.fr/produits/1822660/recepteur-volet-roulant-io-compatible-izymo) : 
- Somfy IO integrated motor (https://monsieurstore.com/produits/volets-roulants/volets-roulants-alu-thermophonic-2/) qui est vu comme store (awning) et non comme un volet routlant (shutter)

**Protocol**: on ajuste dans la  Tahoma app: Izymo shutter and integrated actuator opening pour etre exactement au meme niveau physiquement

Sate experience | Physical state*               | Izymo module* (seen as shutter/volet)| Integrated actuator*(seen as awing/store)|
----------------|-------------------------------|--------------------------------------|------------------------------------------|
1               | Volet Open (opened at 100%)   | 100% (cursor haut)                   | 0% (cursor haut)                         |
2               | Volet Opened at 33% (en bas)  | 33% (cursor en bas)                  | 66% (cursor en bas)                      |
3               | Volet Close (Opened at 0%)    | 0% (cursor bas)                      | 100% (cursor haut)                       |   


*: As indicated in Tahoma app (percentage)
- Izymo (seen as shuuter):   Open at
- Integrated (see as awing): Deployed at

On voit ce probleme d'inversion ouverture/fermeture

- Si on prends les frontiere: state 1 (sate 3 is reversed)
  - Un volet ouvert a 100% (volet en butee haute) physiqument correspond a un
    - Open at 100% dans l'appli Tahoma (curseur en faut) [close at 0%]
    - un setDeploy a 0% (dans l'API execute de Somfy)
    - un setClose a 0% (dans l'API execute de Somfy)
    - un opening a 100% avec les routines Alexa
    - un  `core:ClosureState` a 0% dans l'API status de Somfy

  - Pour avor l'equivalent d'un volet ouvert a 100% avec un moteur de store  montee sur un volet roulant
    - Deploy at 0% dans l'appli Tahoma (curseur en faut) [retracted at 100%]
    - un setDeploy a 0% (dans l'API execute de Somfy)
    - un setClose a 100% (dans l'API execute de Somfy) (un volet ouvert correspond a un store ferme)
    - un opening a 0% avec les routines Alexa (un volet ferme correspond a un store ouvert)
    - un  `core:DeploymentState` a 0% dans l'API status de Somfy

- On peut gneraliser avec le state 2 et 1 (100=x, 0=(100-x))
  - Un volet ouvert a X% (volet en butee X) physiqument correspond a un
    - Open at X% dans l'appli Tahoma (curseur en faut) [close at (100-X)%]
    - un setDeploy a (100-X)% (dans l'API execute de Somfy)  *******
    - un setClose a (100-X)% (dans l'API execute de Somfy) 
    - un opening a X% avec les routines Alexa
    - un  `core:ClosureState` a (100-X)% dans l'API status de Somfy *******

  - Pour avor l'equivalent d'un volet ouvert a X% avec un moteur de store  montee sur un volet roulant
    - Deploy at (100-X)% dans l'appli Tahoma (curseur en haut) [retracted at X%] 
    - un setDeploy at (100-X)% (dans l'API execute de Somfy) *******
    - un setClose a X% (dans l'API execute de Somfy) (un volet ouvert correspond a un store ferme) -----------
    - un opening a (100-X)% avec les routines Alexa (un volet ferme correspond a un store ouvert)
    - un  `core:DeploymentState` a (100-X)% dans l'API status de Somfy *******


On notera les cursor dans Tahoma app au meme niveau mais le pourcentage different
Cela confirme le probleme d'inversion ouverture/feremture.

### Consequence

- les comandes ouverture/fermeture sont inverses
- Aussi si on demande de ouvrir tous les "vrai" stores, cela va fermer le dit volet vu comme un store (non souhaite)

<!-- - je dis vrai store car Izymo IO est concu pour les volets, et assi a noter que Izymo IO est pas reconnu comme du homekit a la difference du  [Somfy IO integrated motor], [cf.](../../tahoma-integration.md#use-apple-homekit-integration) -->

Voir les problemes similaire: 
- https://forum.somfy.fr/questions/2324963-volet-reconnu-tant-store
- https://forum.somfy.fr/questions/3189238-store-reconnu-volet-tahoma

### Note

Supprimer et rajouter le store dans Tahoma ne change rien,


## Investigation

We will try to learn more with API

### Prerequisite

- `vs code + wsl shell`
- Swagger UI: https://somfy-developer.github.io/Somfy-TaHoma-Developer-Mode/#/Setup/get_setup_devices__deviceURL__states


### Get devices 

````
# export BEARER= -- See creds.txt.gpg in Tahoma/local-tahoma 
# as well as $mySecretTahomaPin
export mySecretTahomaPin= See creds.txt.gpg in Tahoma/local-tahoma 

cd Tahoma/shutter-is-awning

curl -k -X 'GET' \
'https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/gateways' \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq

curl -k -X 'GET' \
'https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices' \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/devices.json


# => Integrated motor => "deviceURL": "io://$mySecretTahomaPin/16496531" => use openapi gen => io%3A%2F%2F$mySecretTahomaPin%2F16496531 (vu comme un store)
# => Izymo            =>  "deviceURL": "io://$mySecretTahomaPin/4820485" => use openapi gen => io%3A%2F%2F$mySecretTahomaPin%2F4820485

curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/devices-integrated-motor.json

````


In [devices.json](devices.json), we can see integrated motor **HARDWARE** is an `io:HorizontalAwningIOComponent`
Also visible in Home Assisitant.

## Comparing states



Let's compare state of [expereince](#experience): 1, 2, 3 setting state via Tahoma app.

### State 1

````
curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-physically-open-integrated-actuator.json


curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F4820485//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-physically-open-izymo-actuator.json
````

We can see 

<!-- https://stackoverflow.com/questions/26701538/how-to-filter-an-array-of-objects-based-on-values-in-an-inner-array-with-jq -->

````
diff state-physically-open-integrated-actuator.json  state-physically-open-izymo-actuator.json --side-by-side

cat state-physically-open-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
cat state-physically-open-izymo-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))'
````


output is 

````
$ cat state-physically-open-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "closed"
}
{
  "type": 1,
  "name": "core:DeploymentState",
  "value": 0
}

$ cat state-physically-open-izymo-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))'
{
  "type": 1,
  "name": "core:ClosureState",
  "value": 0
}
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
````

We can see that integrated actuator is considered closed whereas it is opened.
And the postion is the same `core:DeploymentState` <-> `core:ClosureState` (even if did substraction when entered the value in Tahoma app)
Indeed in [pb description section](#description) we have seen that those value `*******` are equivalent.

### State 2

````
curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-physically-intermediate-integrated-actuator.json


curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F4820485//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-physically-intermediate-izymo-actuator.json
````


We can see 



````
cat out/state-physically-intermediate-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
cat out/state-physically-intermediate-izymo-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))'
````


output is 

````
scoulomb@NCEL96011:/mnt/c/Users/scoulombel/dev/home-assistant/Tahoma/shutter-is-awning$ cat out/state-physically-intermediate-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
{
  "type": 1,
  "name": "core:DeploymentState",
  "value": 66
}
scoulomb@NCEL96011:/mnt/c/Users/scoulombel/dev/home-assistant/Tahoma/shutter-is-awning$ cat out/state-physically-intermediate-izymo-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))'
{
  "type": 1,
  "name": "core:ClosureState",
  "value": 67
}
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
````

We can see that both are open (intermediate postion)
And the postion is the same `core:DeploymentState` <-> `core:ClosureState` as in other states.



### State 3


````
curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F4820485//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-physically-close-izymo-actuator.json


curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-physically-close-integrated-actuator.json
`````


We can see 


````
cat out/state-physically-close-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
cat out/state-physically-close-izymo-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))'
````


output is 

````
$ cat out/state-physically-close-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
{
  "type": 1,
  "name": "core:DeploymentState",
  "value": 100
}
$ cat out/state-physically-close-izymo-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))'
{
  "type": 1,
  "name": "core:ClosureState",
  "value": 100
}
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "closed"
}
````

We can see store is considered opened whereas it is closed 
And the postion is the same `core:DeploymentState` <-> `core:ClosureState`

## Use Local API

### Set deployment primitive

Both have set deployment command (see [devices.json](./devices.json)). (to not confuse with awing deployment even if value matching)

Let's try to set deployment at 0%, and edit to 10%

````

curl --insecure https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/exec/apply -H "Authorization: Bearer $BEARER" -H "accept: application/json" -H "Content-Type: application/json" -d @payload/setDeployment-0-integrated-actuator-payload.json

curl --insecure https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/exec/apply -H "Authorization: Bearer $BEARER" -H "accept: application/json" -H "Content-Type: application/json" -d @payload/setDeployment-0-izymo-actuator-payload.json
````

Both have same behavior as we talk about deployment of motor.
Same if we move to 10%. 
Same physical behavior. 


Let's look at state

````
curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F4820485//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-10percent-izymo-actuator.json


curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-10percent-integrated-actuator.json

cat out/state-10percent-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
cat out/state-10percent-izymo-actuator.json  | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 

````


Output is

````
$ cat out/state-10percent-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
{
  "type": 1,
  "name": "core:DeploymentState",
  "value": 10
}
$ cat out/state-10percent-izymo-actuator.json  | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 1,
  "name": "core:ClosureState",
  "value": 10
}
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}

````

And state seems to be the same 
This is aligned `setDeployment` at y <-> `core:DeploymentState` at y <-> `core:ClosureState` at y.
This is in line with what we had seen in [pb description section](#description): those value `*******` are equivalent.


### SetClosure 


If now we use `set closure` command behavior is different 

````
curl --insecure https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/exec/apply -H "Authorization: Bearer $BEARER" -H "accept: application/json" -H "Content-Type: application/json" -d @payload/setClosure-10-integrated-actuator-payload.json

curl --insecure https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/exec/apply -H "Authorization: Bearer $BEARER" -H "accept: application/json" -H "Content-Type: application/json" -d @payload/setClosure-10-izymo-actuator-payload.json
````

Let's look at the state

````
curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F4820485/states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-setClose-10percent-izymo-actuator.json


curl -k -X 'GET' \
"https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices/io%3A%2F%2F$mySecretTahomaPin%2F16496531//states" \
-H 'accept: application/json' \
-H "Authorization: Bearer $BEARER" | jq > out/state-setClose-10percent-integrated-actuator.json


cat out/state-setClose-10percent-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
cat out/state-setClose-10percent-izymo-actuator.json  | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
````
Output is 


````
 cat out/state-setClose-10percent-integrated-actuator.json | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
{
  "type": 1,
  "name": "core:DeploymentState",
  "value": 90
}


$ cat out/state-setClose-10percent-izymo-actuator.json  | jq '.[] | select(.name | contains("core:OpenClosedState", "core:DeploymentState", "core:ClosureState"))' 
{
  "type": 1,
  "name": "core:ClosureState",
  "value": 10
}
{
  "type": 3,
  "name": "core:OpenClosedState",
  "value": "open"
}
````

This is in line with what we had seen in [pb description section](#description).

- Un setClose a X=10% sur le moteur vu comme un store correspond a un setDeploy a 90% (dans l'API execute de Somfy).
- D'ou le 90% at [out/state-setClose-10percent-integrated-actuator.json](out/state-setClose-10percent-integrated-actuator.json)
- Donc volet en bas

- Un setClose a X=10% sur le volet roulant Izymo correspond a un setDeploy a 10% (dans l'API execute de Somfy).
- D'ou le 10% at [out/state-setClose-10percent-izymo-actuator.json]( out/state-setClose-10percent-izymo-actuator.json)
- Donc volet en haut


Note `setPosition` did not lead to physical action

## Conclusion, key take away

- On a monte un moteur de store sur un volet
- Explain different behavior in Alexa see [pb description section](#description)
- If using API use `setDeployment` comand which does not confuse
- `core:DeploymentState`, `core:ClosureState` can be seen as `getDeployment`. See [pb description section](#description) and *******, why they are equivalent

<!-- all concluded do not come back ok, 
todo is to remove perso data DONE -> veut revenir mais etait clair, s'interdire car low added value OK 
and post somfy forum TO BE DONE STOP-->