# mDNS, DNS and certificates


We can access to HomeAssitant using local Private IP which is visible in Google home app for instance `http://192.168.86.20:8123`), and accessible from deviced in google home network (to access from SFR network add port fw in google home port management anf use Google Home WAN private IP (but note [mDNS](#mdns) name will not be visible from SFR network to access NAS in Google network).

We can also use SFR WAN Public IP such as `109.29.148....:8123` (or `9123`, do not consider it in rest of doc) where **WARNING**: Port depends on NAT setup (see [README](../README.md#solution-1-double-dnat))


In http for now.

Similar for QNAP mgmt UI on port where **WARNING**: Port depends on NAT setup (see [README](../README.md#solution-1-double-dnat))

- `9080` (http)
- `9443` and `443` (https)

<!-- __[1] make this comment clear: https://github.com/scoulomb/home-assistant/commit/ef7ba4bd7ebdae1af27a0ab66b21bb4e4ff34650#commitcomment-125603663 and not ref here: https://gist.github.com/scoulomb/d71c757c346a0b4032bc49a6934ebe15, and rewrite no need more check OK
-->

Note when we will setup certificate if using IP, it is like a domain nmismatch if we do not include the IP in SAN. Certbot will not allow it (even if not CN and just SAN). QNAP mentions it in myQNAPcloud UI

````
Certbot output: The Let's Encrypt certificate authority will not issue certificates for a bare IP address.
````

QNAP mentions it in myQNAPcloud UI

> Warning The certificate only secures connections to the myQNAPcloud domain name. It does not secure the IP address. Learn more.

## NAT port note

**Note** <!-- clear and ok, no come back -->
Link made in port with this doc next section and [README](../README.md#solution-1-double-dnat)) are clear.
Other NAT port (http://192.168.1.1/network/nat) ot mentionned in this introduction are
- ssh 22 -> 2222 for Precision (seen at [README](../README.md#solution-1-double-dnat))
- cert valid 80 -> 8180 (see at next [section](#objective-1-ha-in-https))
- inactive denon [README](../README.md#double-nat-with-devices-on-2-networks))
- [file-sharing](file-sharing/sync-nas-to-hdd-cloud.md#setup-ftp-in-nas) 
  - NAT for FTP in passive mode range 
  - sFTP using ssh to NAS (222)
- [VPN](VPN.md) -> OK CLEAR

And reforward in ghome OK 
<!-- Stop do not recheck osef - yes was ccl forbidden OK - loss of time as quickly checked already toc - recheck and indeed ok no more required.


Mix tls non tls port, in the end termination counts so could send 443 to 80?
For instance 
nas-sec2 	TCP 	Port 	443 	192.168.1.58 	8443
and 
ghome 8443 -> 8080 (not 80, which us forbideen in nas locally)instead of 8443 -> 443 of nas


coulomb@scoulomb-Precision-3540:~$ curl -I  http://home.coulombel.net:443 | head -n 2
HTTP/1.1 200 OK
Date: Wed, 04 Oct 2023 18:46:53 GMT

scoulomb@scoulomb-Precision-3540:~$ curl -I home.coulombel.net:443 | head -n 2
HTTP/1.1 200 OK
Date: Wed, 04 Oct 2023 18:46:59 GMT

Note that curl see that 443 default port protocol (https) not working and use http
Same in mozilla can see connection not encrypted in sec info of cert so use http

If force

scoulomb@scoulomb-Precision-3540:~$ curl -I https://home.coulombel.net:443 | head -n 2
curl: (35) OpenSSL/1.1.1f: error:1408F10B:SSL routines:ssl3_get_record:wrong version number

In firefox Error code: SSL_ERROR_RX_RECORD_TOO_LONG

Revert to initial setup in ghome 

-->

## Local DNS

### mDNS


Note if using Google NEST wifi router, a DNS record is automatically created `scoulombel-nas`.
Thus can access NAS by doing `scoulombel-nas:8123` in local NEST network. How does it work? 
We are using mDNS implemented in Google router.

<!-- mdns OK -->
<!-- mdns can be blocked in corp win - work in phone, corp mac/ home.mydomain.net:8123 or ip acess will woerk if vpn unlike local ip / access from laptop on site osef-->



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


### SFR box local DNS

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
````

We can configure ipv6 local dns (http://192.168.1.1/networkv6/dns).
In the example the tagetetted device was google router (`192.168.1.58`), but could use any other device. Google router does not expose an `ipv6 IP.

<!-- note server is box box 192.168.1.1 but in THE PAST,  see links below it was 127.0.1.1#53 -->

Note usage of SFR local DNS which can be subsituted with [mDNS](#mdns).

## Public DNS

**WARNING**: Port depends on NAT setup (see [README](../README.md#solution-1-double-dnat))

### Google DNS to HA

We can also access HA via `home.coulombel.net:8123`, if A record `home.coulombel.net	A	1 hour	109.29.148.109`. is correctly set
<!-- https://github.com/open-denon-heos/remote-control#suggestion-define-a-record-pointing-to-your-machinenas OK -->


What we had done here: https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md#add-a-nat-rule-to-access-from-internet with simple NAT <!-- __[2] OK -->

In [DNS deep dive](#dns-deep-dive) we explain that a dynDNS is not required as SFR IP is static but we could have a DynDNS configuration.

**https xor http will depend on certificate setup [below](#certificate-setup))**

If not setup is done so HTTP we have 
- http://home.coulombel.net:8123/ : OK but warn that connection is not secure
- https://home.coulombel.net:8123/ : `Error code: SSL_ERROR_RX_RECORD_TOO_LONG`

### QNAP dynDNS to HA

QNAP also offers a (Dyn)DNS via myQNAPCloud, so we can access HA via as side effect via `home.coulombel.net:8123` (ha rule) 

**https xor http will depend on certificate setup [below](#certificate-setup))**


If not setup is done so HTTP we have 
- http://scoulomb.myqnapcloud.com:8123/ : OK but warn that connection is not secure
- https://scoulomb.myqnapcloud.com:8123/ : `Error code: SSL_ERROR_RX_RECORD_TOO_LONG` (do F5 to refresh)

## In comparsion local mDNS has same behavior to HA

- http://scoulombel-nas:8123/ : OK but warn that connection is not secure
- https://scoulombel-nas:8123/ : `Error code: SSL_ERROR_RX_RECORD_TOO_LONG`

**Before next section I disabled any cert setup in NAS (inital status)  > `myQNAPCloud` > `My DDNS`**

### QNAP dynDNS to QNAP mgmt UI


- `http://scoulomb.myqnapcloud.com:9080` (`nas` NAT rule): OK but warn that connection is not secure
- `https://scoulomb.myqnapcloud.com:9080` (`nas` NAT rule):  `Error code: SSL_ERROR_RX_RECORD_TOO_LONG`


- `http://scoulomb.myqnapcloud.com:9443` (`nas-sec` NAT rule): BAD Request: You're speaking plain HTTP to an SSL-enabled server port.
- `https://scoulomb.myqnapcloud.com:9443` (`nas-sec` NAT rule):  `Warning: Potential Security Risk Ahead` but can access / Advanced* `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT`

Disable sec exception to see the error

- `http://scoulomb.myqnapcloud.com:443` (`nas-sec2` NAT rule): BAD Request: You're speaking plain HTTP to an SSL-enabled server port.
- `https://scoulomb.myqnapcloud.com:443` or `https://scoulomb.myqnapcloud.com/` (default port( (`nas-sec2` NAT rule):  `Warning: Potential Security Risk Ahead` / Advanced `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT` but can access


Can remove non secure HTTP rule NAT rule over Internet.

**So here it is working well with HTTP and HTTPS.**

### Google DNS to NAS mgmt UI ?


- `http://home.coulombel.net:9080` (`nas` NAT rule): OK but warn that connection is not secure
- `https://home.coulombel.net:9080` (`nas` NAT rule):  `Error code: SSL_ERROR_RX_RECORD_TOO_LONG`


- `http://home.coulombel.net:9443` (`nas-sec` NAT rule): BAD Request: You're speaking plain HTTP to an SSL-enabled server port.
- `https://home.coulombel.net:9443` (`nas-sec` NAT rule):  `Warning: Potential Security Risk Ahead` / Advanced `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT` but can access


- `http://home.coulombel.net:443` (`nas-sec2` NAT rule): BAD Request: You're speaking plain HTTP to an SSL-enabled server port.
- `https://home.coulombel.net:443` or `https://home.coulombel.net/` (default port( (`nas-sec2` NAT rule):  `Warning: Potential Security Risk Ahead` / Advanced `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT` but can access

So exactly same behavior as [QNAP dynDNS to QNAP mgmt UI](#qnap-dyndns-to-qnap-mgmt-ui)

Note
`but can access` == Set a security exception 

## In comparsion local mDNS has similar behvaior to mgmt UI


QNAP offer local access in http (`8080`) and https (`443`)

- http://scoulombel-nas:8080/ : OK but warn that connection is not secure
- https://scoulombel-nas:8080/ : `Error code: SSL_ERROR_RX_RECORD_TOO_LONG`


- http://scoulombel-nas:443/ : BAD Request: You're speaking plain HTTP to an SSL-enabled server port.
- https://scoulombel-nas:443/  or `https://scoulombel-nas:` `Warning: Potential Security Risk Ahead` / Advanced `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT` but can access



We will see in certificate section how to setup those.


## SSH

And thus example with [SSH](../README.md#about-ssh) and domain usage https://github.com/scoulomb/docking-station#misc-notes

<!-- __[3] https://github.com/scoulomb/docking-station/commit/7a09cd14c2616066e4082c57424128fc2939b38c#commitcomment-128854058 OK and CCL -->

## DNS deep dive 

In this page I explained dynamic DNS feature:
- https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-a.md#dynamic-dns-for-public-ip-with-router-configuration
- https://github.com/scoulomb/misc-notes/blob/master/lab-env/README.md#dyndns

Google DNS by default support DynDNS: https://support.google.com/domains/answer/6147083?authuser=0&hl=en (was using Gandi in the past)


Also public DNS can point to private IP (SFR or Google net).
<!-- tested with SFR -->

With time I realized dynamic DNS is not mandatory as box IP is not changing a lot so a simple A record is sufficient.
Like `home.coulombel.net	A	1 hour	109.29.148.109`. 
To access my home assisant at `http://home.coulombel.net:8123` fom outside (and inside) with good NAT rule (even if we go out to go in).


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

<!-- all clear above, ccl  -->


## Add certificates 

We will setup certificate for HomeAssisant.

### Objective 1: HA in HTTPS

We want those URL
- [Google DNS to HA](#google-dns-to-ha)
- [QNAP (dyn)DNS to HA](#qnap-dyndns-to-ha)
- [In comparsion local mDNS has same behavior to HA](#in-comparsion-local-mdns-has-same-behavior-to-ha) (As we setup HA in HTTPS, we could want `scoulombel-nas` to work without security exception locally, but it is not possible). See certbot error:  "scoulombel-nas": Domain name needs at least one dot and Cannot issue for "scoulombel-nas.local": Domain name does not end with a valid public suffix (TLD)


To work in HTTP**S** and disable HTTP.

We can not listen on `HTTP` and `HTTPS` at same time with HA: https://community.home-assistant.io/t/listen-on-both-http-and-https-configuration/484395

We will use cert bot to generate a cert with
- CN: home.coulombel.net
- ALT name
  - scoulomb.myqnapcloud.com

We will generate a certificate with same metho as described here: https://github.com/scoulomb/myDNS/blob/18150f476eb6f6141d5c2f349b0f6ffccf9cb254/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-h.md#how-to-generate-a-certificate-signed-by-a-ca-server-validation

````
sudo snap install core; sudo snap refresh core
sudo apt-get remove certbot,
sudo snap install --classic certbot
sudo certbot certonly --standalone
````

For cert validation only we will need NAT rule to route Dell machine where certificate challenge is running

- `http://192.168.1.1/network/nat` => `cert-valid 	TCP 	Port 	80 	192.168.1.58 	8180`
- `gHome` > `Port mgmt` > `8180 -> 80`  of Dell Precision 

Request cert for  home.coulombel.net scoulomb.myqnapcloud.com

Output is 

````
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/home.coulombel.net/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/home.coulombel.net/privkey.pem
This certificate expires on 2024-01-02.
````

We can not extend date: https://community.letsencrypt.org/t/how-to-extend-the-expiry-date-of-domain-certificate-to-one-year/67744


Note automatic renwal can work: `systemctl list-timers`



````
$ systemctl list-timers | grep certbot
Wed 2023-10-04 08:55:00 CEST 5h 40min left n/a                          n/a           snap.certbot.renew.timer       snap.certbot.renew.service

````

And 

````
systemctl list-units | grep certbot
cat /etc/systemd/system/snap.certbot.renew.timer   
cat /etc/systemd/system/snap.certbot.renew.service
````

Then we will copy certificates to HA folder in NAS

We are manipulate symlink 

````
scoulomb@scoulomb-Precision-3540:/etc/letsencrypt/live/home.coulombel.net$ ls -l
total 4
lrwxrwxrwx 1 root root  42 oct.   4 03:12 cert.pem -> ../../archive/home.coulombel.net/cert2.pem
lrwxrwxrwx 1 root root  43 oct.   4 03:12 chain.pem -> ../../archive/home.coulombel.net/chain2.pem
lrwxrwxrwx 1 root root  47 oct.   4 03:12 fullchain.pem -> ../../archive/home.coulombel.net/fullchain2.pem
lrwxrwxrwx 1 root root  45 oct.   4 03:12 privkey.pem -> ../../archive/home.coulombel.net/privkey2.pem
-rwxrwxr-x 1 root root 692 oct.   3 20:31 README
````

````
# /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home-assistant-docker cn be fond via explorer, 3 dots open term
mkdir /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home-assistant-docker/tls
cp /etc/letsencrypt/live/home.coulombel.net/* /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home-assistant-docker/tls # No sudo here
````



Edit  `vim /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home-assistant-docker/configuration.yaml` 

````
http:
  ssl_certificate: ./tls/cert.pem
  ssl_key: ./tls/privkey.pem # not ssl here
````


Then in http://scoulombel-nas:8123/developer-tools/yaml -> restart

And we can test it is working

- http://home.coulombel.net:8123/ : `The connection was reset`
- https://home.coulombel.net:8123/ : OK WORKING


- http://scoulomb.myqnapcloud.com:8123/ : `The connection was reset`
- https://scoulomb.myqnapcloud.com:8123/ : OK WORKING

- http://scoulombel-nas:8123/ : `The connection was reset`
- https://scoulombel-nas:8123/ : OK Warning but  `Warning: Potential Security Risk Ahead` as we could not put a local name in cert/ `Error code: SSL_ERROR_BAD_CERT_DOMAIN`
  - In advanced section 

  ````
  Websites prove their identity via certificates. Firefox does not trust this site because it uses a certificate that is not valid for scoulombel-nas:8123. The certificate is only valid for the following names: home.coulombel.net, scoulomb.myqnapcloud.com
 
  Error code: SSL_ERROR_BAD_CERT_DOMAIN
  ````


We could use a domain not in cert to show a cert mismatch

https://domains.google.com/registrar/coulombel.net/dns

````
home.coulombel.net	A	1 hour	
109.29.148.109 

house.coulombel.net	A	1 minute	
109.29.148.109 
````

- https://house.coulombel.net:8123 : `Warning: Potential Security Risk Ahead` / `Error code: SSL_ERROR_BAD_CERT_DOMAIN`


### Objective 2 = 

- Objective 1 (HA in HTTPS only) working as above in [objective 1](#objective-1-ha-in-https)
- + QNAP certificate setup remove  `Warning: Potential Security Risk Ahead`:`MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT`/  in HTTPS and keep HTTP as is
  - [QNAP dynDNS to QNAP mgmt UI](#qnap-dyndns-to-qnap-mgmt-ui)
  - [Google DNS to NAS mgmt UI ?](#google-dns-to-nas-mgmt-ui)
  - **Except local domain**: [In comparsion local mDNS has similar behvaior to mgmt UI](#in-comparsion-local-mdns-has-similar-behvaior-to-mgmt-ui) but we expect to have for `Warning: Potential Security Risk Ahead`: `Error code: SSL_ERROR_BAD_CERT_DOMAIN` instead of `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT`


We will go to `https://scoulombel-nas` (with sec exception) > `MyQNAOcloud` > `SSL certificate`

Here we have 2 options
- myQNAPCloud (Payment)
  - > The myQNAPcloud SSL Web Service Certificate provides a secure environment for exchanging confidential information online and confirms the identity of your site to employees, business partners, and other users. You can purchase SSL certificates online from the QNAP Software Store. Visit myQNAPcloud Features for more information about SSL certificates.

- Let's encrypt (free)
  - > Let's Encrypt is a free, automated, and open certificate authority that issues domain-validated security certificates. You can install Let's Encrypt certificates with the DDNS service provided by myQNAPcloud. This certificate is renewed automatically unless you choose to remove it.


We will go for let's encrypt certificate

It may require to open NAT/port 443 for certificate validation (NAT `nas-sec-2` rule) (Did not try to remove as altrady there)

When done we can test

- `https://scoulomb.myqnapcloud.com:9443`: Now working OK no WARNING
- `https://scoulomb.myqnapcloud.com:443` or `https://scoulomb.myqnapcloud.com/`: Now working OK no WARNING


- `https://home.coulombel.net:9443`: we have `SSL_ERROR_BAD_CERT_DOMAIN` instead of `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT`
- `https://home.coulombel.net:443` or `https://home.coulombel.net/`:  we have `SSL_ERROR_BAD_CERT_DOMAIN` instead of `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT`

- https://scoulombel-nas:443/  or `https://scoulombel-nas:` we have `SSL_ERROR_BAD_CERT_DOMAIN` instead of `MOZILLA_PKIX_ERROR_SELF_SIGNED_CERT`

For local domain we can do nothing.
But for `home.coulombel.net:443` we can add alternative domain to certificate

It is managed in a different panel in QNAP

- We should go to   `control panel` >> `SSL Certificate & Privtae Key` 
- Then replace certificate, we have 3 options (import cert (for example the one we did for HA), get from let's encrypt or self signed), we choose get from let's encrypt.

Here we see challenge could can use port 80 or 443

We add `scoulomb.myqnapcloud.com` domain as CN and `home.coulombel.net` as alt domain (can add several with `,`)
But it time out

Actually even if NAT rule (`nas-sec2`) listens port 80.
We have this rule we did above

````
- `http://192.168.1.1/network/nat` => `cert-valid 	TCP 	Port 	80 	192.168.1.58 	8180`
- `gHome` > `Port mgmt` > `8180 -> 80` on Dell Precsion. 
````

We change to port 80 of NAS (validation process see we have something on port 80 but not pointing to good machine thus the failure). So 443 port not used here. And note port `80` is NAS is forbidden so only for validation. (do not investigate more0)


Then it worked with all `home.coulombel.net` domain.
<!-- Weirdly when we use `https://scoulomb.myqnapcloud.com:9443` on non standard port (not the the case for `https://home.coulombel.net:9443/`) we no dot have Safe lockin firefox, had ro restrat browser, bug ok
-->


Now we can use this certificate in HA ! (so that we can benefit from renew, even more true if full QNAP cert)

From control panel, download cert and copy them to `./ssl/QNAPCert`

Automating it not easy: https://community.home-assistant.io/t/adding-https-access-on-qnap-nas/382815/7


Edit  `vim /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home-assistant-docker/configuration.yaml` 


````
http:
  ssl_certificate: ./tls/QNAPCert/SSLcertificate.crt
  ssl_key: ./tls/QNAPCert/SSLprivatekey.key
````


Then in https://scoulombel-nas:8123/developer-tools/yaml -> restart (`https` this time)

And check it is still workinhg

- https://home.coulombel.net:8123/ : OK WORKING
- https://scoulomb.myqnapcloud.com:8123/ : OK WORKING

YEAH !

<!--
with cert from qnap we can see 

CN (Common Name):	scoulomb.myqnapcloud.com <-- clear in UI
Subject Alternative Names
DNS:	home.coulombel.net
DNS:	scoulomb.myqnapcloud.com
Critical:	No

And from certbot
Subject Name
CN (Common Name):	home.coulombel.net <- so first domain in command line
Subject Alternative Names
DNS:	home.coulombel.net
DNS:	scoulomb.myqnapcloud.com
Critical:	No

We can also see it in browser
-->

<!-- Note xref __[1], __[2], __[3], also NAT rule can be refound including DENON , all OK
Story for testing juge ok do not check more -->

Note we patch a bit https://github.com/scoulomb/misc-notes/blob/master/lab-env/ but it is still valid <!-- do not read it, no xref ok -->

Note in MyQNAPcloud this custom (with SAN) SSL certificate is recognized as active but it took some time and it mentions auto renew.