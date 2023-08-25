# (m)DNS


## mDNS

Note when using `scoulombel-nas:8123`. We are using mDNS implemented in Google router.



````
$ curl scoulombel-nas:8123
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html><html><head><title>Home Assistant</title><meta charset="utf-8"><link rel="manifest" href="/manifest.json" crossorigin="use-credentials"><link rel="icon" href="/static/icons/favicon.ico"><link rel="modulepreload" href="/frontend_latest/core--xB4BlSVBjQ.js" crossorigin="use-credentials"><link rel="modulepreload" href="/frontend_latest/app-lVQEYwG9x5Q.js" crossorigin="use-credentials"><link rel="mask-icon" href="/static/icons/mask-icon.svg" 


$ curl scoulombel-nas.local:8123
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html><html><head><title>Home Assistant</title><meta charset="utf-8"><link rel="manifest" href="/manifest.json" crossorigin="use-credentials"><link rel="icon" href="/static/icons/favicon.ico"><link rel="modulepreload" href="/frontend_latest/core--xB4BlSVBjQ.js" crossorigin="use-credentials"><link rel="modulepreload" href="/frontend_latest/app-lVQEYwG9x5Q.js" crossorigin="use-credentials"><link rel="mask-icon" href="/static/icons/mask-icon.svg" 
````

Note `nslookup` will not return mdns
==> https://serverfault.com/questions/579967/why-nslookup-doesnt-use-mdns-while-ping-do

````
$ nslookup coulombel.net
Non-authoritative answer:
Server:  UnKnown
Address:  192.168.86.1

Name:    coulombel.net
Addresses:  185.199.111.153
          185.199.109.153
          185.199.110.153
          185.199.108.153


$ nslookup scoulombel-nas.local
*** UnKnown can't find scoulombel-nas.local: Non-existent domain
Server:  UnKnown
Address:  192.168.86.1

````




It validates we have mDNS ;)

mDNS stands for multicast
- https://en.wikipedia.org/wiki/Multicast_DNS
- https://fr.wikipedia.org/wiki/Routage

It relies on [Apple Bonjour](https://en.wikipedia.org/wiki/Bonjour_(software)).

Similar to [UPNP](./UPNP.md#upnp-service-discovery-example-in-smarthome).


## SFR box local DNS

On SFR box we have a true local DNS (not using mDNS)


Do follwing DNS definition at http://192.168.1.1/network/dns

````
1 	192.168.1.58 	test-dns 	
2 	192.168.1.58 	test-dns.net 	
3 	192.168.1.58 	test-dns.local 	
4 	192.168.1.58 	google.com 	
````

Laptop is connected to in SFR Wifi 

DNS server is the box (see DNS server in nslookup reply)


````
~
$ nslookup test-dns
*** box can't find test-dns: Non-existent domain
Server:  box
Address:  192.168.1.1
````

We need a valid dns extension

````
$ nslookup test-dns.net
Server:  box
Address:  192.168.1.1

Name:    test-dns.net
Address:  192.168.1.58



$ nslookup test-dns.local
Server:  box
Address:  192.168.1.1

Name:    test-dns.local
Address:  192.168.1.58

$ nslookup google.com
Server:  box
Address:  192.168.1.1

Name:    google.com
Addresses:  2a00:1450:4006:80e::200e
          192.168.1.58
````

Removing local Google "overide" ipv4 is back..


````
$ nslookup google.com
Non-authoritative answer:
Server:  box
Address:  192.168.1.1

Name:    google.com
Addresses:  2a00:1450:4006:80e::200e
          142.250.201.14
`````

We can configure ipv6 local dns (http://192.168.1.1/networkv6/dns).
In the example the tagetetted device was google router (`192.168.1.58`), but could use any other device. Google router does not expose an `ipv6 IP.

<!-- note server is box box 192.168.1.1 but in THE PAST,  see links below it was 127.0.1.1#53 -->

## DNS deep dive 

In this page I explained dynamic DNS feature: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-a.md#dynamic-dns-for-public-ip-with-router-configuration

Google DNS by default support DynDNS: https://support.google.com/domains/answer/6147083?authuser=0&hl=en (was using Gandi in the past)

Note usage of SFR local DNS which can be subsituted with [mDNS](#mdns).

Also public DNS can point to private IP (SFR or Google net).
<!-- tested with SFR -->

With time I realized dynamic DNS is not required as box IP is not changing a lot so a simple A record is sufficient.
Like `home.mydomain.net	A	1 hour	109.29.148.109`. 
To access my home assisant at `http://home.mydomain.net:8123` fom outside (and inside) with good NAT rule (even if we go out to go in).


Actually SFR box container a Local Recursive dns, which forward DNS (DNS forwarder to SFR DNS recursive server).

See here what we mean by `Forwarding DNS`:  https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/3-bind-forwarders/dns-forwarding.md). 

This local recusive DNS is obtained via DHCP: https://github.com/scoulomb/myDNS/blob/master/1-basic-bind-lxa/p1-1-dns-cache.md#personal-notes

See DNS query in details: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-a.md#could-we-use-the-dns-as-switch

We can not change the DNS to which we forward the query (meaning we have to use SFR DNS).
Forwarding DNS was visible at  http://192.168.1.1/state/wan  (source: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-a.md#first-we-should-understand-the-resolution-in-details) (not the case in August 2023).

So two option to use an alternative DNS.
- We change the DNS manually on each to target an alternative DNS
- We use another router which allow to change DNS advertised via DHCP (soltuion we do on google nest)
- Configure own DHCP server: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-k.md#use-split-horizon-rather-than-dns-override; https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-c.md#configure-dhcp-server


<!-- mDNS is not visible from SFR network, which is obvious -->

<-- all clear above, ccl  -->

## Use NAS dynDNS and certificate in QNAP cloud

https://docs.qnap.com/operating-system/qts/4.5.x/fr-fr/GUID-8E3D6623-6D02-4AB4-B89B-B622631CE707.html