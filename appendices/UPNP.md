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

## UPNP IGD NAT Traversal

HomeAssistant can be used ton configure Gateway (see IGD in devices and services)

It can also be used by QNAP cloud: https://docs.qnap.com/operating-system/qts/4.5.x/fr-fr/GUID-8E3D6623-6D02-4AB4-B89B-B622631CE707.html
