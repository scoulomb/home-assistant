# Smart URL


In `NAS` > `myQNAPCloud` > `MyQNAPCloud link`

We can we have a SmartURL 

https://qlink.to/scoulomb


<!-- retest here -->
### Basic test in home network

This smart url is resolved to (from home network):
- if In NAS > myQNAPCloud > Access control > Private: http://192.168.86.96:8080/cgi-bin/
- if In NAS > myQNAPCloud > Access control > Public: https://109.29.148.109/cgi-bin/
- if In NAS > myQNAPCloud > Access control > Custom (publish secure, unpusblish non sec) webadmin: https://109.29.148.109/cgi-bin/
- if In NAS > myQNAPCloud > Access control > Custom (unpublish secure, pusblish non sec): https://109.29.148.109/cgi-bin/, https://scoulomb.myqnapcloud.com/cgi-bin/ (does not seem to impact much)
    - I added NAT rule 8080 -> 8080 at http://192.168.1.1/network/nat on top of NAT rule exposing 9080 no change
    ````
    8080 	TCP 	Port 	8080 	192.168.1.58 	8080
    ````

### More test with Public access and NAT rule in home netowork

- If set access control to public but disable

````
nas-sec2 	TCP 	Port 	443 	192.168.1.58 	8443
````

It will not find 

````
nas-sec 	TCP 	Port 	9443 	192.168.1.58 	8443
````

It is using standart port and it fallback to local address: http://192.168.86.96:8080/cgi-bin/

- If add rule 

````
8080 	TCP 	Port 	8080 	192.168.1.58 	8080
````

And disable 443 still going to local adress: http://192.168.86.96:8080/cgi-bin/

### If I try from device on other nw (4g) 

<!-- wifi it resolved to pub ip adress -->
#### Public acess

With `443` NAT rules activated (and all rules here: [DNS.md intro](DNS.md))
- it resolves to scoulomb.myqnapcloud.com
If I disables all NAT rules
- it resolves to a21a.myqnapcloud.com and it is working !!

#### Private access


Same behavior as public but it will require to login
