# UPNP

See
- https://support.google.com/googlenest/answer/6274337?hl=fr
- https://en.wikipedia.org/wiki/Universal_Plug_and_Play


## Here are the protocol step of UPNP.

From https://en.wikipedia.org/wiki/Universal_Plug_and_Play

> UPnP uses common Internet technologies. It assumes the network must run Internet Protocol (IP) and then uses HTTP, SOAP and XML on top of IP, in order to provide device/service description, actions, data transfer and eventing. Device search requests and advertisements are supported by running HTTP on top of UDP using multicast (known as HTTPMU). Responses to search requests are also sent over UDP, but are instead sent using unicast (known as HTTPU). UPnP uses UDP due to its lower overhead in not requiring confirmation of received data and retransmission of corrupt packets. HTTPU and HTTPMU were initially submitted as an Internet Draft but it expired in 2001;[8] these specifications have since been integrated into the actual UPnP specifications.

> UPnP uses UDP port 1900 and all used TCP ports are derived from the SSDP alive and response messages.[9]


### Addressing

> The foundation for UPnP networking is IP addressing. Each device must implement a DHCP client and search for a DHCP server when the device is first connected to the network. If no DHCP server is available, the device must assign itself an address. The process by which a UPnP device assigns itself an address is known within the UPnP Device Architecture as AutoIP. In UPnP Device Architecture Version 1.0,[2] AutoIP is defined within the specification itself; in UPnP Device Architecture Version 1.1,[3] AutoIP references IETF RFC 3927. If during the DHCP transaction, the device obtains a domain name, for example, through a DNS server or via DNS forwarding, the device should use that name in subsequent network operations; otherwise, the device should use its IP address.

### Discovery

> Once a device has established an IP address, the next step in UPnP networking is discovery. The UPnP discovery protocol is known as the Simple Service Discovery Protocol (**SSDP**). When a device is added to the network, SSDP allows that device to advertise its services to control points on the network. This is achieved by sending SSDP alive messages. When a control point is added to the network, SSDP allows that control point to actively search for devices of interest on the network or listen passively to the SSDP alive messages of devices. The fundamental exchange is a discovery message containing a few essential specifics about the device or one of its services, for example, its type, identifier, and a pointer (network location) to more detailed information.



### Description

> After a control point has discovered a device, the control point still knows very little about the device. For the control point to learn more about the device and its capabilities, or to interact with the device, the control point must retrieve the device's description from the location (URL) provided by the device in the discovery message. The UPnP Device Description is expressed in XML and includes vendor-specific manufacturer information like the model name and number, serial number, manufacturer name, (presentation) URLs to vendor-specific web sites, etc. The description also includes a list of any embedded services. For each service, the Device Description document lists the URLs for control, eventing and service description. Each service description includes a list of the commands, or actions, to which the service responds, and parameters, or arguments, for each action; the description for a service also includes a list of variables; these variables model the state of the service at run time, and are described in terms of their data type, range, and event characteristics.

### Control

> Having retrieved a description of the device, the control point can send actions to a device's service. To do this, a control point sends a suitable control message to the control URL for the service (provided in the device description). Control messages are also expressed in XML using the Simple Object Access Protocol (SOAP). Much like function calls, the service returns any action-specific values in response to the control message. The effects of the action, if any, are modeled by changes in the variables that describe the run-time state of the service.

### Event notification

Another capability of UPnP networking is event notification, or eventing. The event notification protocol defined in the UPnP Device Architecture is known as General Event Notification Architecture (GENA). A UPnP description for a service includes a list of actions the service responds to and a list of variables that model the state of the service at run time. The service publishes updates when these variables change, and a control point may subscribe to receive this information. The service publishes updates by sending event messages. Event messages contain the names of one or more state variables and the current value of those variables. These messages are also expressed in XML. A special initial event message is sent when a control point first subscribes; this event message contains the names and values for all evented variables and allows the subscriber to initialize its model of the state of the service. To support scenarios with multiple control points, eventing is designed to keep all control points equally informed about the effects of any action. Therefore, all subscribers are sent all event messages, subscribers receive event messages for all "evented" variables that have changed, and event messages are sent no matter why the state variable changed (either in response to a requested action or because the state the service is modeling changed).

### Presentation

The final step in UPnP networking is presentation. If a device has a URL for presentation, then the control point can retrieve a page from this URL, load the page into a web browser, and depending on the capabilities of the page, allow a user to control the device and/or view device status. The degree to which each of these can be accomplished depends on the specific capabilities of the presentation page and device. 


## NAT traversal

From https://en.wikipedia.org/wiki/Universal_Plug_and_Play

> One solution for NAT traversal, called the Internet Gateway Device Protocol (IGD Protocol), is implemented via UPnP. Many routers and firewalls expose themselves as Internet Gateway Devices, allowing any local UPnP control point to perform a variety of actions, including retrieving the external IP address of the device, enumerating existing port mappings, and adding or removing port mappings. By adding a port mapping, a UPnP controller behind the IGD can enable traversal of the IGD from an external address to an internal client. 

See https://en.wikipedia.org/wiki/Internet_Gateway_Device_Protocol

## UPNP Service discovery example in SmartHome

UPNP is used for [Discovery](#discovery) as Apple Bonjour service.
- by NAS
- HEOS (HomeAssistant and OpenDenonHeos). See [here](../README.md#a-wired-solution).

<-- all clear above, ccl  -->

## UPnP IGD NAT Traversal



It can also be used by QNAP cloud: 

- https://docs.qnap.com/operating-system/qts/4.5.x/fr-fr/GUID-8E3D6623-6D02-4AB4-B89B-B622631CE707.html
- https://docs.qnap.com/operating-system/qts/4.4.x/en-us/GUID-5B1E585C-8A0D-45FD-A255-3E18F54CB582.html

Go to `http://scoulombel-nas:8080/` > `burger left to application` > `myQNAPCloud` > `DDNS` > `To set up UPnP port forwarding, click here`.


We will  test it with [OpenVPN port](./VPN.md#natting).

We had defined 

````
http://192.168.1.1/network/nat
OpenVPN 	UDP 	Port 	1194 	192.168.1.58 	11194

GHome / Port management
11194 -> 1194 ( to NAS) / UDP (all other rules were in TCP, first UDP rule in this doc)
````

Note we do not use `1194 -> 1194` (default)
But `11194` -> `1194`.

- Phone in 4G (cut wifi) > we can connect
- GHome port mamangement -> remove `11194 -> 1194 ( to NAS) / UDP` NAT rules (can put wifi for faster response to do the config)
- Remove wifi, and try to reconnect to VPN (connection IS cut after NAT port removal, but it takes some time) -> unable to connect, connection timeout
- `http://scoulombel-nas:8080/` > `burger left to application` > `myQNAPCloud` > `DDNS` > `To set up UPnP port forwarding, click here`.
    - Enable UPNP port forwarding
    - Add NAS service targetting default port (for ovpn it is 1194) will not work): port in use error (even if UPNP using that service is disabled in UI (some bug to disable ovpn but tried with another one) <!-- I activated all NAT rule on SFR router to check if link with the fact could not disable open vpn UPNP in NAS UI but not related, rules remain disabled, can enable and disable other rule easily in UPNP UI, openvpn UPNP rule causing issue -->
    - So we will also change NAT rule on box to
        - http://192.168.1.1/network/nat
        - OpenVPN 	UDP 	Port 	1194 	192.168.1.58 	1194 (we have to rm nat, diabling not sufficient)
    - We can connect OK
- Now I will turn off UPNP and try to reconnect -> timeout
- Turn on UPNP again ->Working
- I come back to initial setup
    - Disable UPNP
    - initial NAT rules 
    - Tested working OK

- If I disable NAT rule on SFR, it will disconnect (I have re-check, what happened when come back to initial setup OK, if I renable NAT rule it will reconnect auto)



Note this is goung further that upnp: https://www.qnap.com/fr-fr/how-to/faq/article/how-do-i-disable-the-upnp-service

## UPNP/IGD in HA

HomeAssistant (see IGD in devices and services)

https://www.home-assistant.io/integrations/upnp

It is called IGD: https://en.wikipedia.org/wiki/Universal_Plug_and_Play / https://en.wikipedia.org/wiki/Internet_Gateway_Device_Protocol

But it does not help to set up NAT traversal rules to my knowledge

<!-- I have an error and will not explore more -->

<!-- ccl OK -->

