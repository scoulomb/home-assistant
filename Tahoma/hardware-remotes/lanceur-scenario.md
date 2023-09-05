# Scene Launcher 

## Scene launcher setup

Unlike regular button setup is done via Tahoma app by pressing prog button.
Note this button can be seen in Tahoma unlike regular button (plugged to device directly, see [README](README.md)).
It is not seen as a device but can configure it in scenen laucher section (`...` > `MySceneLauncher`).
It will be even more visible in API call below.

(Box button can be parametrized in box section)
<!-- optionally can check if appear on API -->

## Alternative to Scene launcher Tahoma button 


````
NFC Tag -> HA automation -> Tahoma Box     -> Shutter (IO protocol)
                         -> Hue Hub        -> Ligths
                         -> Denon
                         -> IR controller  -> AC 
````

NFC tag can be replaced by 
- Hue button 
- Companion App localization 

We can achieve similar action with Google Home (location leaving)

## Use Tahoma Scene launcher 


````
Scene launcher -> Tahoma Box   -> Shutter
               -> Tahoma Box   -> Hue Hub -> Ligths
````

Very convenient as no mobile phone, or NAS up dependency.

I would like to complete Tahoma action via HA action for
- Denon
- IR controller AC 


Unfortunately I can not do this directly

````
Scene launcher -> Tahoma Box                                                    -> Shutter
               -> Tahoma Box  -> Hue Hub                                        -> Ligths
               -> Tahoma Box  -> Event on Button HomeAssistant                  -> Denon
               -> Tahoma Box  -> Event on Button HomeAssistant -> IR controller -> AC
````              

### Option 1 use scene event 

- https://community.home-assistant.io/t/trigger-automation-when-scene-is-triggered/7932    
- https://community.home-assistant.io/t/can-i-trigger-an-automation-by-scene-being-activated/222468

It is not working as event not going through HA so not notified

### Option 2 use another device as a bridge

````
Scene launcher -> Tahoma Box  -> Hue Hub -> On Button ->  Hue Event on Button HomeAssistant -> Denon                                                                                        
````     


Not convenient as if device already on or off, and state is unchanged no action is triggered



### Option 3 Use notification on Mobile phone with IFFT and HA hook

````
Scene launcher -> Tahoma Box  -> Android notif -> IFFT notif call webhook -> HA webhook HomeAssistant -> Denon                                                                                        
````     
HA webhook means we use a webhook trigger in an HA automation

Issue is that hard to parse and make distinction leave or arrive

### Option 4 - The chosen one a script to detect event in Tahoma and trigger webhook  


````
Scene launcher -> Tahoma Box  <- Watcher script detects event -> Script call HA webhook -> Denon                                                                                        
````     

Thus final setup would be 


````
Scene launcher -> Tahoma Box                                                           -> Shutter
               -> Tahoma Box  -> Hue Hub                                               -> Ligths
               -> Tahoma Box  <- Watcher script detects event -> call HA webhook       -> Denon
               -> Tahoma Box  <- Watcher script detects event -> call HA webhook -> IR -> AC                                  

````

Script writing tip
- Use Open API: https://somfy-developer.github.io/Somfy-TaHoma-Developer-Mode/, https://github.com/Somfy-Developer/Somfy-TaHoma-Developer-Mode/blob/main/docs/openapi.yaml
- In some setup (corp) mDNS may not work 
- Target HA public IP (some network may have issue with private IP and mDNS when targets HA)
- Use insecure mode if cert shaddow (corp)
- Make a function to register a watcher, get event, process event
- Use chat gpt to witre a code ( as I already wrote the code but lost it in migration)