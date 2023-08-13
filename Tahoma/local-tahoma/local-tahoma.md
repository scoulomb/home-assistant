# Tahoma Local API usage

## Doc

- https://github.com/Somfy-Developer/Somfy-TaHoma-Developer-Mode
- https://github.com/home-assistant/core/issues/69558#issuecomment-1523101067
- https://community.jeedom.com/t/commande-somfy-tahoma-avec-l-api-locale/106397/2

We have to activate Tahoma in dev mode
- https://github.com/Somfy-Developer/Somfy-TaHoma-Developer-Mode

I use `PowerShell` command given in this link https://community.jeedom.com/t/commande-somfy-tahoma-avec-l-api-locale/106397/and converted it to `curl` command using Chatgpt. 

<!-- use ubuntu WSL -->

## Credentials

Complete and export variable in [cred-template.txt].

We can encrypt/decryppt with your own credentials.

````shell
# in vs code can open a wsl bash
gpg -c Tahoma/local-tahoma/creds.txt
gpg Tahoma/local-tahoma/creds.txt.gpg
````

## Get local token


````
# Login and store session
session=$(curl -k -X POST "https://$cloud/enduser-mobile-web/enduserAPI/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "userId=$userId&userPassword=$userPassword" \
  -c session.cookie.txt \
  -b session.cookie.txt)

# Generate Token
token_response=$(curl -k -X GET "https://$cloud/enduser-mobile-web/enduserAPI/config/$pin/local/tokens/generate" \
  -H "Content-Type: application/json" \
  -b session.cookie.txt)

token=$(echo "$token_response" | jq -r '.token')

# Post Token
curl -k -X POST "https://$cloud/enduser-mobile-web/enduserAPI/config/$pin/local/tokens" \
  -H "Content-Type: application/json" \
  -b session.cookie.txt \
  -d "{\"label\":\"Mon token\",\"token\":\"$token\",\"scope\":\"devmode\"}"


curl -k https://$cloud/enduser-mobile-web/enduserAPI/config/$pin/local/tokens/devmode \
  -H "Content-Type: application/json" \
  -b session.cookie.txt 

echo $token
````

See details in https://github.com/Somfy-Developer/Somfy-TaHoma-Developer-Mode


## Make query to API


### Find Tahoma ip via router and check status


````
curl -k  -X 'GET' 'https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/apiVersion'-H 'accept: application/json'
````

### Make query to get doc

See OpenAPI definnition
- https://github.com/Somfy-Developer/Somfy-TaHoma-Developer-Mode/blob/main/docs/openapi.yaml
- https://somfy-developer.github.io/Somfy-TaHoma-Developer-Mode/

````
# export BEARER= -- See creds.txt.gpg

curl -k -X 'GET' \
  'https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $BEARER" | jq | grep -i -C 14 shutter | tail -20

curl -k -X 'GET' \
  'https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/setup/devices' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $BEARER" | jq | grep -i -C 20 deviceUrl | grep -C 15 io://
````


output is

````
        },
        {
          "name": "core:FirmwareRevision"
        }
      ],
      "uiClass": "RollerShutter",
      "commands": [
        {
          "commandName": "stop",
          "nparams": 0
        },
        {
          "nparams": 1,
          "commandName": "setDeployment",
          "paramsSig": "p1"
        },
        {
          "nparams": 1,
          "commandName": "delayedStopIdentify",
          "paramsSig": "p1"````


````

and 

````
[...]
  "deviceURL": "io://[....]/4820485",
    "available": true,
    "synced": true,
    "type": 1,
    "states": [
      {
        "type": 3,
        "name": "core:StatusState",
        "value": "available"
[....]
````

### Deduce command to run

Replace with your device url in [test-body.json](./test-body.json).

````
cd Tahoma/local-tahoma

curl --insecure https://192.168.86.64:8443/enduser-mobile-web/1/enduserAPI/exec/apply -H "Authorization: Bearer $BEARER" -H "accept: application/json" -H "Content-Type: application/json" -d @test-body.json
````

This will close at the given position (tested and working with Izymo).

### Integrate in home asssitant this curl command

It is explained here https://github.com/home-assistant/core/issues/69558#issuecomment-1523101067 (not done as worked with OverKiz)

<!-- optinal to do -->

### Note on Update

Tahoma update may disable token.
We can disable automatic update.
