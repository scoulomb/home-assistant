# pip3 install tuya-connector-python

## ----- IMPORT ------

from tuya_connector import (
	TuyaOpenAPI,
	TuyaOpenPulsar,
	TuyaCloudPulsarTopic,
)

import json
 
import time

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from typing import Any, Dict, Optional, Tuple

## ----- HELPERS ------

def print_json_object(json_object, title=""):
   print(f"{title}\n")	
   json_str = json.dumps(json_object, indent=4, sort_keys=True)
   cap_size = 2000
   json_str_shortened = json_str[:cap_size]
   if len(json_str) > cap_size:
   	json_str_shortened+="Truncated json"
   print(highlight(json_str_shortened, JsonLexer(), TerminalFormatter()))
   print("---------")
	
def open_api_get(path:str) -> Dict[str, Any] :
   res_json_object = openapi.get(path, dict()) # use path here and not api_path, otherwise take caller
   print_json_object(res_json_object, title=path)
   return res_json_object


def open_api_post(path:str, body: Optional[Dict[str, Any]]) -> Dict[str, Any] :
   res_json_object = openapi.post(path, body)
   print_json_object(res_json_object, title=path)
   return res_json_object


ACCESS_ID = ""
ACCESS_KEY = ""
API_ENDPOINT = "https://openapi.tuyaeu.com"
MQ_ENDPOINT = "wss://mqe.tuyacn.com:8285/"

## ----- INIT ------

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call any API from Tuya
api_path = "/v1.0/statistics-datas-survey"
open_api_get(api_path)




## ----- Generic IR API - info ------
api_path = "/v2.0/infrareds/2605606084f3ebe93d45/remotes"
open_api_get(api_path)

api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/keys"
open_api_get(api_path)


## ------ Generic IR API - action ------

''''
api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/command"
body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"key":"T29"}
open_api_post(api_path, body)

api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/command"
body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"key":"F3"}
open_api_post(api_path, body)

api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/command"
body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"key":"M0"}
open_api_post(api_path, body)
'''
# if send bad body error sign invalid, as signed is generated based on body

 
## ------ Specific AC API info ------


api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/ac/status"
open_api_get(api_path)


## ------ Specific AC API info   Several action in one call ------

'''
api_path="/v2.0/infrareds/2605606084f3ebe93d45/air-conditioners/testing/scenes/command"
body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"power":1,"mode":0,"temp": 24,"swing":1,"wind": 0}
print(body)
open_api_post(api_path, body)
'''

### Several actions in 1 call not working. Status is unchanged. It was the case alredy when run this python code in 2022 with SmartHome setup.


## ------ Use AC info + generic IR action to adjust temperature + generic IR Power ON/OFF ------



### Power on

api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/command"
body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"key":"PowerOn"}
open_api_post(api_path, body)


time.sleep(5)

### Adjust temperature

from enum import Enum

class Direction(Enum):
  UP = 1
  DOWN = 2
  

def adjust_temperature(direction: Direction):
   print("==========================================================  adjust temp " + str(direction)) 
   api_path_status ="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/ac/status"
   api_path_cmd ="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/command"
   status = open_api_get(api_path_status)
   
   if (direction == Direction.UP):
   	temp = "T" + str(int(status["result"]["temp"]) + 1)
   else:
   	temp = "T" + str(int(status["result"]["temp"]) - 1)


   body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"key":temp}
   open_api_post(api_path_cmd, body)
      
   open_api_get(api_path_status)
   
   print("==========================================================  adjust temp " + str(direction)) 

adjust_temperature(Direction.DOWN)


time.sleep(5)

### Power off
api_path="/v2.0/infrareds/2605606084f3ebe93d45/remotes/bf41343e7d214c5cc5ovs5/command"
body: Dict[str, Any] =  {"remote_index":10502,"category_id":5,"key":"PowerOff"}

open_api_post(api_path, body)
