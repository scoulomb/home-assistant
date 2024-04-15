# DNS SD and mulicast DNS

## Standard unicast DNS vs multicast DNS

### Global Intro

Standard Unicast DNS was studied in this repo:  https://github.com/scoulomb/myDNS/blob/master/1-basic-bind-lxa/p2-1-zz-note-on-recursive-and-authoritative-dns.md#recursive-dns-and-authoritative-dns 


In this doc we have studied DNS in scope of HA with certificate perspective [HA and DNS, mDNS: appendices/readme.md](../appendices/DNS.md). Note we had seen
-  [1. Local DNS](../appendices/DNS.md#local-dns)
   - [1.1 m(ulticast) DNS](../appendices/DNS.md#local-dns)
   - [1.2 SFR Box local Standard Unicast DNS](../appendices/DNS.md#sfr-box-local-dns)
- [2. Public Standard unicast DNS](../appendices/DNS.md#public-dns)

Service discovery showcased in [sound/video README](./README.md#how-does-service-discovery-work-behind-the-scene) leverage mDNS.

### Standard Unicast DNS

**[Case 1.2 and 2](#global-intro)**


In general client targets directly 
   - recursive DNS like `8.8.8.8` (dns query sent to outside as 8.8.8.8 not in LAN via UDP port 53)
   - or target recursive DNS setup in default gw (forwarding DNS) 
      - SFR box -> SFR recursive DNS (https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/1-real-own-dns-resolution-example.md)
         - Inside a LAN, router can also be a DNS for machine located inside the LAN (internal IPs, we we can do with SFR router) 
            - **[This is case 1.2](#global-intro)**
            - Note the DNS adress of router is provided by DHCP server, when also given the IP adress to machine  
            - consistent with https://youtu.be/CPOpPTpMSiE?t=80
      - Nest router -> 8.8.8.8 (or customizable)



Consistent with: See https://youtu.be/CPOpPTpMSiE?t=164.

Note after DNS resolution IP address to MAC machine IP adress is done by ARP protocol: https://fr.wikipedia.org/wiki/Address_Resolution_Protocol


### Multicast DNS

**[Case 2](#global-intro)**

#### Intro

https://en.wikipedia.org/wiki/Multicast_DNS

> In computer networking, the multicast DNS (mDNS) protocol resolves hostnames to IP addresses within small networks that do not include a local name server. It is a zero-configuration service, using essentially the same programming interfaces, packet formats and operating semantics as unicast Domain Name System (DNS). 
> It was designed to work as either a stand-alone protocol or compatibly with standard DNS servers.[1] It uses IP multicast User Datagram Protocol (UDP) packets and is implemented by the Apple Bonjour and open-source Avahi software packages, included in most Linux distributions. Although the Windows 10 implementation was limited to discovering networked printers, subsequent releases resolved hostnames as well.[2] mDNS can work in conjunction with DNS Service Discovery (DNS-SD), a companion zero-configuration networking technique specified separately in RFC 6763.[3]
History


#### Protocol overview

https://en.wikipedia.org/wiki/Multicast_DNS

> When an mDNS client needs to resolve a hostname, it sends an IP multicast query message that asks the host having that name to identify itself. That target machine then multicasts a message that includes its IP address. All machines in that subnet can then use that information to update their mDNS caches. Any host can relinquish its claim to a name by sending a response packet with a time to live (TTL) equal to zero.

It's not necessary a A, AAAA record.
For service disscovery we have a PTR, SRV, TXT record.
See [DNS-SD key take away](#rfc-key-take-away) section.

> By default, mDNS exclusively resolves hostnames ending with the .local top-level domain. This can cause problems if .local includes hosts that do not implement mDNS but that can be found via a conventional unicast DNS server. Resolving such conflicts requires network-configuration changes that mDNS was designed to avoid.

Compliant with https://youtu.be/CPOpPTpMSiE?t=240

#### Packet structure

> An mDNS message is a multicast UDP packet sent using the following addressing:

`````
IPv4 address 224.0.0.251 or IPv6 address ff02::fb
UDP port 5353
When using Ethernet frames, the standard IP multicast MAC address 01:00:5E:00:00:FB (for IPv4) or 33:33:00:00:00:FB (for IPv6)
`````

The payload structure is based on the unicast DNS packet format, consisting of two parts—the header and the data.[5]

The header is identical to that found in unicast DNS, as are the sub-sections in the data part: queries, answers, authoritative-nameservers, and additional records. The number of records in each sub-section matches the value of the corresponding *COUNT field in the header. 

See also: https://www.youtube.com/watch?v=v8poeqoeRgE

## DNS-SD 

### RFC quote

Quoting RFC=-6793" https://datatracker.ietf.org/doc/html/rfc6763#section-7.1

`````

1.  Introduction

   This document specifies how DNS resource records are named and
   structured to facilitate service discovery.  Given a type of service
   that a client is looking for, and a domain in which the client is
   looking for that service, this mechanism allows clients to discover a
   list of named instances of that desired service, using standard DNS
   queries.  This mechanism is referred to as DNS-based Service
   Discovery, or DNS-SD.

   This document proposes no change to the structure of DNS messages,
   and no new operation codes, response codes, resource record types, or
   any other new DNS protocol values.

   **
   This document specifies that a particular service instance can be                  
   described using a DNS SRV [RFC2782] and DNS TXT [RFC1035] record.
   The SRV record has a name of the form "<Instance>.<Service>.<Domain>"
   and gives the target host and port where the service instance can be
   reached.  The DNS TXT record of the same name gives additional
   information about this instance, in a structured form using key/value
   pairs, described in Section 6.  A client discovers the list of
   available instances of a given service type using a query for a DNS
   PTR [RFC1035] record with a name of the form "<Service>.<Domain>",
   which returns a set of zero or more names, which are the names of the
   aforementioned DNS SRV/TXT record pairs.
   **

   **
   This specification is compatible with both Multicast DNS [RFC6762]
   and with today's existing Unicast DNS server and client software.
   
   When used with Multicast DNS, DNS-SD can provide zero-configuration
   operation -- just connect a DNS-SD/mDNS device, and its services are
   advertised on the local link with no further user interaction [ZC].
   **

   When used with conventional Unicast DNS, some configuration will
   usually be required -- such as configuring the device with the DNS
   domain(s) in which it should advertise its services, and configuring
   it with the DNS Update [RFC2136] [RFC3007] keys to give it permission
   to do so.  In rare cases, such as a secure corporate network behind a



Cheshire & Krochmal          Standards Track                    [Page 3]


RFC 6763               DNS-Based Service Discovery         February 2013


   firewall where no DNS Update keys are required, zero-configuration
   operation may be achieved by simply having the device register its
   services in a default registration domain learned from the network
   (see Section 11, "Discovery of Browsing and Registration Domains"),
   but this is the exception and usually security credentials will be
   required to perform DNS updates.

   Note that when using DNS-SD with Unicast DNS, the Unicast DNS-SD
   service does NOT have to be provided by the same DNS server hardware
   that is currently providing an organization's conventional host name
   lookup service.  While many people think of "DNS" exclusively in the
   context of mapping host names to IP addresses, in fact, "the DNS is a
   general (if somewhat limited) hierarchical database, and can store
   almost any kind of data, for almost any purpose" [RFC2181].  By
   delegating the "_tcp" and "_udp" subdomains, all the workload related
   to DNS-SD can be offloaded to a different machine.  This flexibility,
   to handle DNS-SD on the main DNS server or not, at the network
   administrator's discretion, is one of the benefits of using DNS.

   Even when the DNS-SD functions are delegated to a different machine,
   the benefits of using DNS remain: it is mature technology, well
   understood, with multiple independent implementations from different
   vendors, a wide selection of books published on the subject, and an
   established workforce experienced in its operation.  In contrast,
   adopting some other service discovery technology would require every
   site in the world to install, learn, configure, operate, and maintain
   some entirely new and unfamiliar server software.  Faced with these
   obstacles, it seems unlikely that any other service discovery
   technology could hope to compete with the ubiquitous deployment that
   DNS already enjoys.  For further discussion, see Appendix A,
   "Rationale for Using DNS as a Basis for Service Discovery".

   This document is written for two audiences: for developers creating
   application software that offers or accesses services on the network,
   and for developers creating DNS-SD libraries to implement the
   advertising and discovery mechanisms.  For both audiences,
   understanding the entire document is helpful.  For developers
   creating application software, this document provides guidance on
   choosing instance names, service names, and other aspects that play a
   role in creating a good overall user experience.  However, also
   understanding the underlying DNS mechanisms used to provide the
   service discovery facilities helps application developers understand
   the capabilities and limitations of those underlying mechanisms
   (e.g., name length limits).  For library developers writing software
   to construct the DNS records (to advertise a service) and generate
   the DNS queries (to discover and use a service), understanding the
   ultimate user-experience goals helps them provide APIs that can meet
   those goals.

`````



And 

`````

12.1.  PTR Records

   When including a DNS-SD Service Instance Enumeration or Selective
   Instance Enumeration (subtype) PTR record in a response packet, the
   server/responder SHOULD include the following additional records:

   o  The SRV record(s) named in the PTR rdata.
   o  The TXT record(s) named in the PTR rdata.
   o  All address records (type "A" and "AAAA") named in the SRV rdata.

12.2.  SRV Records

   When including an SRV record in a response packet, the
   server/responder SHOULD include the following additional records:

   o  All address records (type "A" and "AAAA") named in the SRV rdata.



Cheshire & Krochmal          Standards Track                   [Page 30]

RFC 6763               DNS-Based Service Discovery         February 2013


12.3.  TXT Records

   When including a TXT record in a response packet, no additional
   records are required.

`````




And

`````

7.1.  Selective Instance Enumeration (Subtypes)

   This document does not attempt to define a sophisticated (e.g.,
   Turing complete, or even regular expression) query language for
   service discovery, nor do we believe one is necessary.

   However, there are some limited circumstances where narrowing the set
   of results may be useful.  For example, many network printers offer a
   web-based user interface, for management and administration, using
   HTML/HTTP.  A web browser wanting to discover all advertised web
   pages issues a query for "_http._tcp.<Domain>".  On the other hand,
   there are cases where users wish to manage printers specifically, not
   to discover web pages in general, and it is good accommodate this.
   In this case, we define the "_printer" subtype of "_http._tcp", and
   to discover only the subset of pages advertised as having that
   subtype property, the web browser issues a query for
   "_printer._sub._http._tcp.<Domain>".

   The Safari web browser on Mac OS X 10.5 "Leopard" and later uses
   subtypes in this way.  If an "_http._tcp" service is discovered both
   via "_printer._sub._http._tcp" browsing and via "_http._tcp" browsing
   then it is displayed in the "Printers" section of Safari's UI.  If a
   service is discovered only via "_http._tcp" browsing then it is
   displayed in the "Webpages" section of Safari's UI.  This can be seen
   by using the commands below on Mac OS X to advertise two "fake"
   services.  The service instance "A web page" is displayed in the
   "Webpages" section of Safari's Bonjour list, while the instance
   "A printer's web page" is displayed in the "Printers" section.

      dns-sd -R "A web page"           _http._tcp          local 100
      dns-sd -R "A printer's web page" _http._tcp,_printer local 101

   Note that the advertised web page's Service Instance Name is
   unchanged by the use of subtypes -- it is still something of the form



Cheshire & Krochmal          Standards Track                   [Page 21]

RFC 6763               DNS-Based Service Discovery         February 2013


   "The Server._http._tcp.example.com.", and the advertised web page is
   still discoverable using a standard browsing query for services of
   type "_http._tcp".  The subdomain in which HTTP server SRV records
   are registered defines the namespace within which HTTP server names
   are unique.  Additional subtypes (e.g., "_printer") of the basic
   service type (e.g., "_http._tcp") serve to allow clients to query for
   a narrower set of results, not to create more namespace.

   Using DNS zone file syntax, the service instance "A web page" is
   advertised using one PTR record, while the instance "A printer's web
   page" is advertised using two: the primary service type and the
   additional subtype.  Even though the "A printer's web page" service
   is advertised two different ways, both PTR records refer to the name
   of the same SRV+TXT record pair:

   ; One PTR record advertises "A web page"
   _http._tcp.local. PTR A\032web\032page._http._tcp.local.

   ; Two different PTR records advertise "A printer's web page"
   _http._tcp.local. PTR A\032printer's\032web\032page._http._tcp.local.
   _printer._sub._http._tcp.local.
                     PTR A\032printer's\032web\032page._http._tcp.local.

   Subtypes are appropriate when it is desirable for different kinds of
   client to be able to browse for services at two levels of
   granularity.  In the example above, we describe two classes of HTTP
   clients: general web browsing clients that are interested in all web
   pages, and specific printer management tools that would like to
   discover only web UI pages advertised by printers.  The set of HTTP
   servers on the network is the same in both cases; the difference is
   that some clients want to discover all of them, whereas other clients
   only want to find the subset of HTTP servers whose purpose is printer
   administration.
`````

### RFC key take-away

So we have

- The PTR [RFC1035] record with a name of the form "<Service>.<Domain>", which returns a set of zero or more names, which are the names of the a forementioned DNS SRV/TXT record pairs.
- The SRV record(s) named in the PTR rdata: Instance>.<Service>.<Domain>
- The TXT record(s) named in the PTR rdata: Instance>.<Service>.<Domain>
- All address records (type "A" and "AAAA") named in the SRV rdata.



We can also have PTR subtype <subservice>._sub.<Service>.<Domain>

- Like  `_http._tcp.<domain>` and `_printer._sub._http._tcp.<Domain>` to have granualarity of all webpages or printer configuration webpages only.

DNS-SD work with conventional standard unicast DNS and mDNS.

I asume we have a PTR record on each machine hosting the service.

### DNS-SD query using conventional unicast DNS

Int this section I will myself do the convenitional unicast DNS DNS-SD query performed in the RFC-6793.
 

> 13.1.  What web pages are being advertised from dns-sd.org?``


````
scoulomb@scoulomb-Precision-3540:~/dev$  nslookup -q=ptr _http._tcp.dns-sd.org.
;; Truncated, retrying in TCP mode.
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
_http._tcp.dns-sd.org   name = Source\032de\032T\195\169l\195\169vision,\032D\195\169partement\032de\032Langues._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032eBay,\032online\032auctions._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Wired,\032Technology,\032Culture,\032Business,\032Politics._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Apple,\032makers\032of\032the\032iPod._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032BBC,\032World\032news._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Zeroconf._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032SlashDot,\032News\032for\032Nerds,\032Stuff\032that\032Matters._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \207\128._http._tcp.\226\128\162bullets\226\128\162.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Yahoo,\032maps,\032weather,\032and\032stock\032quotes._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Amazon\.com,\032on-line\032shopping._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032CNN,\032World\032news._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = Stuart\226\128\153s\032Printer._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Multicast\032DNS._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032Google,\032searching\032the\032Web._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = About\032Bonjour\032in\032Web\032Browsers._http._tcp.dns-sd.org.
_http._tcp.dns-sd.org   name = \032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org.

Authoritative answers can be found from:
````

> Answer: There are four, called "Zeroconf", "Multicast DNS", "Service Discovery", and "Stuart's Printer".

Note we have more in my outout, here above it is the answer in the RFC

> 13.2.  What printer-configuration web pages are there?


````
$ nslookup -q=ptr _printer._sub._http._tcp.dns-sd.org.
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
_printer._sub._http._tcp.dns-sd.org     name = Stuart\226\128\153s\032Printer._http._tcp.dns-sd.org.

Authoritative answers can be found from:
````

> Answer: "Stuart's Printer" is the web configuration UI of a network printer.

This is an example of sub type. 
Note this relates to same SRV, and TXT record referenced in `_http._tcp.dns-sd.org.` PTR record.

> 13.3.  How do I access the web page called "Service Discovery"?

Note I changed `Service\032Discovery._http._tcp.dns-sd.org."` to `\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org.`
So as to be consistent with PTR output (but first record is working)



`````
scoulomb@scoulomb-Precision-3540:~/dev$ nslookup -q=any "\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org."
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org      service = 0 0 80 dns-sd.org.
\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org      text = "txtvers=1" "path=/"

Authoritative answers can be found from:

`````

> Answer: You need to connect to dns-sd.org port 80, path "/".
> The address for dns-sd.org is also given (64.142.82.154).


We can split SRV from TXT record


`````
scoulomb@scoulomb-Precision-3540:~/dev$ nslookup -q=SRV "\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org."
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org      service = 0 0 80 dns-sd.org.

Authoritative answers can be found from:

scoulomb@scoulomb-Precision-3540:~/dev$ nslookup -q=TXT "\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org."
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
\032*\032DNS\032Service\032Discovery._http._tcp.dns-sd.org      text = "txtvers=1" "path=/"

Authoritative answers can be found from:
`````

In SRV record we have `dns-sd.org.`, so we can resolve it 


`````
scoulomb@scoulomb-Precision-3540:~/dev$ nslookup -q=A dns-sd.org.
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   dns-sd.org
Address: 96.76.212.165
`````
and then `curl 96.76.212.165:80/`

We can find printer conf in a similar way

`````
scoulomb@scoulomb-Precision-3540:~/dev$ 
nslookup -q=any  "Stuart\226\128\153s\032Printer._http._tcp.dns-sd.org."
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Stuart\226\128\153s\032Printer._http._tcp.dns-sd.org    service = 0 0 80 exampleprinter.dns-sd.org.
Stuart\226\128\153s\032Printer._http._tcp.dns-sd.org    text = "txtvers=1" "path=/"
`````



### DNS-SD query using conventional unicast DNS but doing the same with **Avahi**


````
$ avahi-browse -d dns-sd.org. _http._tcp  --resolve --terminate 
+    n/a  n/a  * eBay, online auctions                      Web Site             dns-sd.org
+    n/a  n/a  * DNS Service Discovery                      Web Site             dns-sd.org
+    n/a  n/a Stuart___s Printer                            Web Site             dns-sd.org
+    n/a  n/a  * CNN, World news                            Web Site             dns-sd.org
+    n/a  n/a  * BBC, World news                            Web Site             dns-sd.org
+    n/a  n/a  * Multicast DNS                              Web Site             dns-sd.org
+    n/a  n/a  * Zeroconf                                   Web Site             dns-sd.org
+    n/a  n/a __                                            Web Site             \226\128\162bullets\226\128\162.dns-sd.org
+    n/a  n/a  * Wired, Technology, Culture, Business, Politics Web Site             dns-sd.org
+    n/a  n/a Source de T__l__vision, D__partement de Langues Web Site             dns-sd.org
+    n/a  n/a  * SlashDot, News for Nerds, Stuff that Matters Web Site             dns-sd.org
=    n/a  n/a  * eBay, online auctions                      Web Site             dns-sd.org
   hostname = [www.ebay.com]
   address = [23.51.49.78]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a  * DNS Service Discovery                      Web Site             dns-sd.org
   hostname = [dns-sd.org]
   address = [96.76.212.165]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a  * CNN, World news                            Web Site             dns-sd.org
   hostname = [www.cnn.com]
   address = [151.101.195.5]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a  * BBC, World news                            Web Site             dns-sd.org
   hostname = [news.bbc.co.uk]
   address = [212.58.249.144]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a  * Multicast DNS                              Web Site             dns-sd.org
   hostname = [multicastdns.org]
   address = [96.76.212.165]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a  * Zeroconf                                   Web Site             dns-sd.org
   hostname = [zeroconf.org]
   address = [96.76.212.165]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a  * Wired, Technology, Culture, Business, Politics Web Site             dns-sd.org
   hostname = [wired.com]
   address = [151.101.194.194]
   port = [80]
   txt = ["path=/" "txtvers=1"]
=    n/a  n/a Source de T__l__vision, D__partement de Langues Web Site             dns-sd.org
   hostname = [tools.ietf.org]
   address = [2606:4700::6810:2d63]
   port = [80]
   txt = ["path=/html/rfc6763" "txtvers=1"]
=    n/a  n/a  * SlashDot, News for Nerds, Stuff that Matters Web Site             dns-sd.org
   hostname = [slashdot.org]
   address = [104.18.36.64]
   port = [80]
   txt = ["path=/" "txtvers=1"]
Failed to resolve service 'π' of type '_http._tcp' in domain '\226\128\162bullets\226\128\162.dns-sd.org': DNS failure: NXDOMAIN
Failed to resolve service 'Stuart’s Printer' of type '_http._tcp' in domain 'dns-sd.org': DNS failure: NXDOMAIN
````

We can find data from above 

`````
+    n/a  n/a  * DNS Service Discovery                      Web Site             dns-sd.org
+    n/a  n/a Stuart___s Printer                            Web Site             dns-sd.org
[...]
=    n/a  n/a  * DNS Service Discovery                      Web Site             dns-sd.org
   hostname = [dns-sd.org]
   address = [96.76.212.165]
   port = [80]
   txt = ["path=/" "txtvers=1"]
[...]
Failed to resolve service 'Stuart’s Printer' of type '_http._tcp' in domain 'dns-sd.org': DNS failure: NXDOMAIN
`````

Note the printer resolution failed for unknown reason in Avahi (bug?)...


We can also find the printer subtype

`````
scoulomb@scoulomb-Precision-3540:~/dev$  avahi-browse -d dns-sd.org _printer._sub._http._tcp  --resolve --terminate 
+    n/a  n/a Stuart___s Printer                            Web Site             dns-sd.org
`````

<!-- sometimes some answer disappear, here it is a copy/aste from command line -->



What is interesting is to the usage of SRV (service) and TXT (text) records.

### DNS-SD using mDNS

mDNS will implement the exact same DNS-SD. It shows DNS-SD is not exclusive to mDNS (though frequently combined).

However mDNS SD doe snot seem to work with `dig` or `nslookup`. Those tool does not enable to resolve mDNS record.



`````
scoulomb@scoulomb-Precision-3540:~/dev$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 22.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy

scoulomb@scoulomb-Precision-3540:~/dev$ dig -p 5353 @224.0.0.251  _heos-audio._tcp.local
;; communications error to 224.0.0.251#5353: timed out
;; communications error to 224.0.0.251#5353: timed out
;; communications error to 224.0.0.251#5353: timed out

; <<>> DiG 9.18.12-0ubuntu0.22.04.3-Ubuntu <<>> -p 5353 @224.0.0.251 _heos-audio._tcp.local
; (1 server found)
;; global options: +cmd
;; no servers could be reached

scoulomb@scoulomb-Precision-3540:~/dev$  nslookup -q=ptr 224.0.0.251 -port=5353  _heos-audio._tcp.local
nslookup: couldn't get address for '_heos-audio._tcp.local': failure
`````

So we can not apply this : https://stackoverflow.com/questions/4309740/how-do-i-obtain-model-name-for-a-networked-device-potentially-using-bonjour


We can make it work with some magic trick: https://askubuntu.com/questions/1068131/ubuntu-18-04-local-domain-dns-lookup-not-working 

While for some it is not working as design: https://gitlab.isc.org/isc-projects/bind9/-/issues/3428 😮

It is resolvable via Avahi, here with `_heos-audio._tcp`

`````
scoulomb@scoulomb-Precision-3540:~/dev$ avahi-browse -d local _heos-audio._tcp  --resolve --terminate 
+   wlo1 IPv6 Denon Home 150 2                              _heos-audio._tcp     local
+   wlo1 IPv4 Denon Home 150 3                              _heos-audio._tcp     local
+   wlo1 IPv4 Denon Home 150                                _heos-audio._tcp     local
+   wlo1 IPv4 Denon Home 150 2                              _heos-audio._tcp     local
+   wlo1 IPv4 Denon AVR-X2700H                              _heos-audio._tcp     local
=   wlo1 IPv6 Denon Home 150 2                              _heos-audio._tcp     local
   hostname = [Denon-Home-150-2.local]
   address = [192.168.86.105]
   port = [10101]
   txt = ["networkid=f81a2b16e3d3" "model=Denon Home 150" "vers=3.1.232" "did=3C424E4F8CA96F17045F"]
=   wlo1 IPv4 Denon Home 150 3                              _heos-audio._tcp     local
   hostname = [Denon-Home-150-3.local]
   address = [192.168.86.121]
   port = [10101]
   txt = ["networkid=f81a2b16e3d3" "model=Denon Home 150" "vers=3.1.232" "did=3C424E4F8CA96F1836F5"]
=   wlo1 IPv4 Denon Home 150                                _heos-audio._tcp     local
   hostname = [Denon-Home-150.local]
   address = [192.168.86.116]
   port = [10101]
   txt = ["networkid=f81a2b16e3d3" "model=Denon Home 150" "vers=3.1.232" "did=3C424E4F8CA96F10B875"]
=   wlo1 IPv4 Denon Home 150 2                              _heos-audio._tcp     local
   hostname = [Denon-Home-150-2.local]
   address = [192.168.86.105]
   port = [10101]
   txt = ["networkid=f81a2b16e3d3" "model=Denon Home 150" "vers=3.1.232" "did=3C424E4F8CA96F17045F"]
=   wlo1 IPv4 Denon AVR-X2700H                              _heos-audio._tcp     local
   hostname = [Denon-AVR-X2700H.local]
   address = [192.168.86.42]
   port = [10101]
   txt = ["networkid=f81a2b16e3d3" "model=Denon AVR-X2700H" "vers=3.1.232" "did=3C424E4F000678612752"]
scoulomb@scoulomb-Precision-3540:~/dev$ 
`````
If required launch several time command to have full conf (using cache).


Same with `_http._tcp`

`````
scoulomb@scoulomb-Precision-3540:~/dev$ avahi-browse -d local _http._tcp  --resolve --terminate 
+   wlo1 IPv6 Denon AVR-X2700H                              Web Site             local
+   wlo1 IPv4 scoulombel-nas                                Web Site             local
+   wlo1 IPv4 Denon AVR-X2700H                              Web Site             local
=   wlo1 IPv6 Denon AVR-X2700H                              Web Site             local
   hostname = [Denon-AVR-X2700H.local]
   address = [192.168.86.42]
   port = [80]
   txt = ["path=/settings/"]
=   wlo1 IPv4 scoulombel-nas                                Web Site             local
   hostname = [scoulombel-nas.local]
   address = [192.168.86.96]
   port = [8080]
   txt = ["path=/"]
=   wlo1 IPv4 Denon AVR-X2700H                              Web Site             local
   hostname = [Denon-AVR-X2700H.local]
   address = [192.168.86.42]
   port = [80]
   txt = ["path=/settings/"]
`````

In both all `_heos-audio._tcp` and `_http._tcp` we have a SRV record for `Denon-AVR-X2700H.local` (if we deduce compared to unicast DNS output).
Therefore a A record (as per DNS-SD spec exists).

For instance 

````
hostname = [Denon-AVR-X2700H.local]
address = [192.168.86.42]
````

Though this record is not resovalble by `nslookup`, `dig` a `avahi`, `ping`, `curl` will work
And from DNS records we know a webpage is available at `Denon-AVR-X2700H.local/settings:80`


``````
scoulomb@scoulomb-Precision-3540:~/dev$ avahi-resolve --name Denon-AVR-X2700H.local
Denon-AVR-X2700H.local  192.168.86.42
``````

`````
scoulomb@scoulomb-Precision-3540:~/dev$ ping Denon-AVR-X2700H.local
PING Denon-AVR-X2700H.local (192.168.86.42) 56(84) bytes of data.
64 bytes from denon-avr-x2700h.lan (192.168.86.42): icmp_seq=1 ttl=64 time=6.29 ms
64 bytes from denon-avr-x2700h.lan (192.168.86.42): icmp_seq=2 ttl=64 time=8.58 ms
64 bytes from denon-avr-x2700h.lan (192.168.86.42): icmp_seq=3 ttl=64 time=6.64 ms
^C
--- Denon-AVR-X2700H.local ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 6.288/7.167/8.577/1.006 ms
scoulomb@scoulomb-Precision-3540:~/dev$ 
`````


`````
$ curl Denon-AVR-X2700H.local/settings:80
Error 403: Forbidden
Access Forbidden
`````

Note what is weird is that txt records points to `/settings` whereas top level seems accurate.

`````
coulomb@scoulomb-Precision-3540:~/dev$  curl -k Denon-AVR-X2700H.local -v
*   Trying 192.168.86.42:80...
* Connected to Denon-AVR-X2700H.local (192.168.86.42) port 80 (#0)
> GET / HTTP/1.1
> Host: Denon-AVR-X2700H.local
> User-Agent: curl/8.1.2
> Accept: */*
> 
< HTTP/1.1 301 Moved Permanently
< Location: https://192.168.86.42:10443
* Connection #0 to host Denon-AVR-X2700H.local left intact

scoulomb@scoulomb-Precision-3540:~/dev$  curl -L -k Denon-AVR-X2700H.local
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" dir="ltr">

    <head>
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <title>Home</title>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0" />
        <link rel="stylesheet" type="text/css" href="common.css" />
        <script type="text/javascript" src="jquery.js"></script>
`````

We also have a A record created for Denon Home speaker

````
hostname = [Denon-Home-150-2.local]
address = [192.168.86.105]
````

Which is working, and this time on path `/settings` but no advertised as `_http._tcp`

- http://192.168.86.105/settings/
- http://denon-home-150-2.local/settings/

<!-- when retried did not see it osef -->

``````
scoulomb@scoulomb-Precision-3540:~/dev$ curl http://denon-home-150-2.local/settings/ | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" dir="ltr"> 
    <head>
        <title>Network Settings</title>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0"/>
        <!-- Load the 'handheld' style sheet by default -->
        <!-- Please update version query which is attached to css file names when you update/modify the css file for cache busting. -->
        <link type="text/css" rel="stylesheet" href="handheld.css?ver=20210419" id="stylesheetused"/>
100 15964  100 15964    0     0   122k      0 --:--:-- --:--:-- --:--:--  123k
curl: (23) Failed writing body
``````


It also show mDNS can contain SRV, TXT and A record.

And sometimes we can discover the service but there is no A record necessarily created behind, so it is not resolvable via a avahi-resolve, ping, curl. 
<!-- juge ok, case with jm? osef OK -->

Also A record can be shared by several service: HEOS, Spotify, AirPlay.


**We have seen application of this in [music provider and mDNS](README.md#how-does-service-discovery-work-behind-the-scene)**


### See record resolution in wireshark


`sudo wireshark` and capture wl01.

````
sudo avahi-daemon --kill 
avahi-browse -d local _heos-audio._tcp  --resolve --terminate 
`````


Exporting wireshark JSON we can see mDNS reply of a given speaker


`````json
        "mdns": {
          "dns.id": "0x0000",
          "dns.flags": "0x8400",
          "dns.flags_tree": {
            "dns.flags.response": "1",
            "dns.flags.opcode": "0",
            "dns.flags.authoritative": "1",
            "dns.flags.truncated": "0",
            "dns.flags.recdesired": "0",
            "dns.flags.recavail": "0",
            "dns.flags.z": "0",
            "dns.flags.authenticated": "0",
            "dns.flags.checkdisable": "0",
            "dns.flags.rcode": "0"
          },
          "dns.count.queries": "0",
          "dns.count.answers": "1",
          "dns.count.auth_rr": "0",
          "dns.count.add_rr": "8",
          "Answers": {
            "_heos-audio._tcp.local: type PTR, class IN, Denon Home 150._heos-audio._tcp.local": {
              "dns.resp.name": "_heos-audio._tcp.local",
              "dns.resp.type": "12",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "0",
              "dns.resp.ttl": "4500",
              "dns.resp.len": "17",
              "dns.ptr.domain_name": "Denon Home 150._heos-audio._tcp.local"
            }
          },
          "Additional records": {
            "Denon Home 150._heos-audio._tcp.local: type TXT, class IN, cache flush": {
              "dns.resp.name": "Denon Home 150._heos-audio._tcp.local",
              "dns.resp.type": "16",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "4500",
              "dns.resp.len": "82",
              "dns.txt.length": "24",
              "dns.txt": "did=3C424E4F8CA96F10B875",
              "dns.txt.length": "12",
              "dns.txt": "vers=3.1.232",
              "dns.txt.length": "20",
              "dns.txt": "model=Denon Home 150",
              "dns.txt.length": "22",
              "dns.txt": "networkid=f81a2b16e3d3"
            },
            "Denon Home 150._heos-audio._tcp.local: type SRV, class IN, cache flush, priority 0, weight 0, port 10101, target Denon-Home-150.local": {
              "dns.srv.service": "Denon Home 150",
              "dns.srv.proto": "_heos-audio",
              "dns.srv.name": "_tcp.local",
              "dns.resp.type": "33",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "120",
              "dns.resp.len": "23",
              "dns.srv.priority": "0",
              "dns.srv.weight": "0",
              "dns.srv.port": "10101",
              "dns.srv.target": "Denon-Home-150.local"
            },
            "Denon-Home-150.local: type A, class IN, cache flush, addr 192.168.86.116": {
              "dns.resp.name": "Denon-Home-150.local",
              "dns.resp.type": "1",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "120",
              "dns.resp.len": "4",
              "dns.a": "192.168.86.116"
            },
            "Denon-Home-150.local: type AAAA, class IN, cache flush, addr fd84:cb3f:8f2f:4593:ff84:3d06:745f:1eb6": {
              "dns.resp.name": "Denon-Home-150.local",
              "dns.resp.type": "28",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "120",
              "dns.resp.len": "16",
              "dns.aaaa": "fd84:cb3f:8f2f:4593:ff84:3d06:745f:1eb6"
            },
            "Denon-Home-150.local: type AAAA, class IN, cache flush, addr fe80::2578:b1e8:21a3:eae9": {
              "dns.resp.name": "Denon-Home-150.local",
              "dns.resp.type": "28",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "120",
              "dns.resp.len": "16",
              "dns.aaaa": "fe80::2578:b1e8:21a3:eae9"
            },
            "Denon-Home-150.local: type AAAA, class IN, cache flush, addr fd4f:dede:16f0:24c6:65b:544b:bd56:e098": {
              "dns.resp.name": "Denon-Home-150.local",
              "dns.resp.type": "28",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "120",
              "dns.resp.len": "16",
              "dns.aaaa": "fd4f:dede:16f0:24c6:65b:544b:bd56:e098"
            },
            "Denon Home 150._heos-audio._tcp.local: type NSEC, class IN, cache flush, next domain name Denon Home 150._heos-audio._tcp.local": {
              "dns.resp.name": "Denon Home 150._heos-audio._tcp.local",
              "dns.resp.type": "47",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "4500",
              "dns.resp.len": "9",
              "dns.nsec.next_domain_name": "Denon Home 150._heos-audio._tcp.local",
              "dns.resp.type": "16",
              "dns.resp.type": "33"
            },
            "Denon-Home-150.local: type NSEC, class IN, cache flush, next domain name Denon-Home-150.local": {
              "dns.resp.name": "Denon-Home-150.local",
              "dns.resp.type": "47",
              "dns.resp.class": "0x0001",
              "dns.resp.cache_flush": "1",
              "dns.resp.ttl": "120",
              "dns.resp.len": "8",
              "dns.nsec.next_domain_name": "Denon-Home-150.local",
              "dns.resp.type": "1",
              "dns.resp.type": "28"
            }
          },
          "dns.unsolicited": "1"
        }
      }
    }
  },
`````

### What is Avahi 

https://avahi.org/

> Avahi is a system which facilitates service discovery on a local network via the mDNS/DNS-SD protocol suite. This enables you to plug your laptop or computer into a network and instantly be able to view other people who you can chat with, find printers to print to or find files being shared. Compatible technology is found in Apple MacOS X (branded "Bonjour" and sometimes "Zeroconf").

### What is ZeroConf?

From https://en.wikipedia.org/wiki/Zero-configuration_networking


> Zero-configuration networking (zeroconf) is a set of technologies that automatically creates a usable computer network based on the Internet Protocol Suite (TCP/IP) when computers or network peripherals are interconnected. It does not require manual operator intervention or special configuration servers. Without zeroconf, a network administrator must set up network services, such as Dynamic Host Configuration Protocol (DHCP) and Domain Name System (DNS), or configure each computer's network settings manually.

> Zeroconf is built on three core technologies: 
- automatic assignment of numeric network addresses for networked devices,
- automatic distribution and resolution of computer hostnames,
- and automatic location of network services, such as printing devices.

#### ZeroConf IP Auto assignment

Usually done via DHCP (which provides local IP and also local DNS IP to the host: cf. [SFR above](#global-intro)).

We had seen DHCP in details in this page: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-c.md#configure-dhcp-server.

See also this wikipedia page: 
https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol (DHCPREQUEST should be unicast as IP in DHCPOFFER ) consider OK



With zeroconf they use Link Local Adress: https://en.wikipedia.org/wiki/Link-local_address

Note it implies mDNS for resolution as there is no central authority (as explain in ZeroConf wikipoedia page)

#### ZeroConf Name service dsicovery 


mDNS is used

From https://en.wikipedia.org/wiki/Zero-configuration_networking

> In 2000, Bill Manning and Bill Woodcock described the Multicast Domain Name Service[7] which spawned the implementations by Apple and Microsoft. Both implementations are very similar. Apple's Multicast DNS (mDNS) is published as a standards track proposal RFC 6762, while Microsoft's Link-local Multicast Name Resolution (LLMNR) is published as informational RFC 4795. LLMNR is included in every Windows version from Windows Vista onwards[8] and acts as a side-by-side alternative for Microsoft's NetBIOS Name Service over IPv4 and as a replacement over IPv6, since NetBIOS is not available over IPv6. Apple's implementation is available as the Bonjour service since 2002 in Mac OS X v10.2. The Bonjour implementation (mDNSResponder) is available under the Apache 2 Open Source License[9] and is included in Android Jelly Bean and later[10] under the same license.


#### ZeroConf Service discovery

From https://en.wikipedia.org/wiki/Zero-configuration_networking

> Name services such as mDNS, LLMNR and others do not provide information about the type of device or its status. A user looking for a nearby printer, for instance, might be hindered if the printer was given the name "Bob". Service discovery provides additional information about devices. Service discovery is sometimes combined with a name service, as in Apple's Name Binding Protocol and Microsoft's NetBIOS.

We have 

- NetBIOS Service Discovery
- WS-Discovery
- DNS-based service discovery with multicast as studied [above](#dns-sd-and-mulicast-dns)
- UPnP: UPnP has some protocol components with the purpose of service discovery.
 - [SSDPdiscovery](../appendices/UPNP.md#discovery)
   - Example of SSDP as an alternative [Avahi mDNS discovery](README.md#how-does-service-discovery-work-behind-the-scene): https://github.com/open-denon-heos/heospy/blob/main/heospy/ssdp.py
 - DLNA service discovery is layered on top of UPnP SSDP. See https://en.wikipedia.org/wiki/DLNA.
 - Note UPnP relies on DHCP (which is not ZeroConf, see [Zero Conf IP auto assignment](#zeroconf-ip-auto-assignment)). See [UPNP appendices](../appendices/UPNP.md#addressing)

#### Major implementations

From https://en.wikipedia.org/wiki/Zero-configuration_networking

##### Apple Bonjour

Bonjour from Apple, uses mDNS and DNS Service Discovery. Apple changed its preferred zeroconf technology from SLP to mDNS and DNS-SD between Mac OS X 10.1 and 10.2, though SLP continues to be supported by Mac OS X.

Apple's mDNSResponder has interfaces for C and Java[33] and is available on BSD, Apple Mac OS X, Linux, other POSIX based operating systems and MS Windows. The Windows downloads are available from Apple's website.[34]

#### Avahi

Avahi is a Zeroconf implementation for Linux and BSDs. It implements IPv4LL, mDNS and DNS-SD. It is part of most Linux distributions, and is installed by default on some. If run in conjunction with nss-mdns, it also offers host name resolution.[35]

Avahi also implements binary compatibility libraries that emulate Bonjour and the historical mDNS implementation Howl, so software made to use those implementations can also utilize Avahi through the emulation interfaces.


#### Spotify ZeroConf


https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/zeroconf

[Spotify ZeroConf test made in this repo](./README.md#how-does-service-discovery-work-behind-the-scene)

Thus they are using DNS-SD with m(ulticast)DNS for [service discovery](#service-discovery). 
On top of this they an API server on top of it. 

#### Interesting doc on the topic

http://igm.univ-mlv.fr/~dr/XPOSE2007/jbleuzenZeroConf_implementation_Bonjour/info_others.html


#### Side comments

We say in this doc standard unicast DNS because we can do unicast query and response via multicast DNS.


##### Unicast response

See https://datatracker.ietf.org/doc/html/rfc6762#section-5.5

https://en.wikipedia.org/wiki/Multicast_DNS
In query (query is boradcast but it requests a unicast response)
> The UNICAST-RESPONSE field is used to minimize unnecessary broadcasts on the network: if the bit is set, responders SHOULD send a directed-unicast response directly to the inquiring node rather than broadcasting the response to the entire network. 

 
##### Unicast query

See https://datatracker.ietf.org/doc/html/rfc6762#section-5.5

https://book.hacktricks.xyz/network-services-pentesting/5353-udp-multicast-dns-mdns

> Another important flag is the QU bit, which denotes whether or not the query is a unicast query. If the QU bit isn’t set, the packet is a multicast query (QM).

I assume in that case we target direclty machine which we assume contain the record.


See also http://wapiti.enic.fr/Commun/ens/peda/options/ST/RIO/pub/exposes/exposesrio2009/CUSINPANIT-DUTHILLEUL/glossaire.html


##### Kind of queries

http://wapiti.enic.fr/Commun/ens/peda/options/ST/RIO/pub/exposes/exposesrio2009/CUSINPANIT-DUTHILLEUL/protocole_part2.html


https://datatracker.ietf.org/doc/html/rfc6762#section-5

Avahi consider "One-shot queries, accumulating multiple responses" when terminate is used, and continous when not used.

For Spotify I do not know

See also that protocol can batch several queries (no check further with wireshark)
https://datatracker.ietf.org/doc/html/rfc6762#section-5.3

<!-- side comments ok ccl topic closed -->


##### Type of routing in Internet (not in a LAN)

See TAN p413.

- Unicast
- Broadcast
- Multicast (MOSPF)
- Anycast

We have parallel with 
- [Standard unicast DNS](#standard-unicast-dns): it actually uses Anycast routing !!
- [Multicast DNS](#multicast-dns): Local multicast routing


##### ARP

See TAN p497

Domain -- DNS --> IP @ -- ARP --> ETHernet @

mDNS process similar to ARP.

(Gratuitous) ARP gratuit est similaire  "Gratuitous Multicast DNS Response" (machine asks its own DNS for other to update their cache)/

See http://wapiti.enic.fr/Commun/ens/peda/options/ST/RIO/pub/exposes/exposesrio2009/CUSINPANIT-DUTHILLEUL/protocole_types.html



##### Muticast range

Tan p 480

Today we use CIDR routing (not per class, see p 477/478 including longest prefix rule). <!-- assume on top of BGP and out of scope here -->
However we stull use D class for multicast 
> On utilise toujues les addresses de classe D dans l'internet pur le mutlicast (voir figure 5.53 p 478)

More exactly 

- 224.0.0.1  ->  224.0.0.255 adresses multicast locales
- 224.0.1.1  ->  239.255.255.254 adresses multicast publiques (routables sur Internet)

See http://wapiti.enic.fr/Commun/ens/peda/options/ST/RIO/pub/exposes/exposesrio2009/CUSINPANIT-DUTHILLEUL/generalites.html

<!-- enic sit stop here -->

<!-- 31jan23 OK CCL only BGP could be linked larer in the last section, and link to DLNA -->