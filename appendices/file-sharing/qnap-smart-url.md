# Smart URL

## Test context

In `NAS` > `myQNAPCloud` > `MyQNAPCloud link`

We can we have a SmartURL 

https://qlink.to/scoulomb

In https://www.myqnapcloud.com/u#/my_device > Services we can see weh have 5 types of services (when public mode or custom mode with all services published in QNAP)
- QTS desktop 
- File Station 
- Web Server
- Photo Station
- Music Station 


They appear on this section if http://scoulombel-nas:8080/cgi-bin/ > `myQNAPCloud` > `access control` is public, private, custom (if service selected).
In custom mode mode note that we have secure and non secure, it will impact URL advertised when clicking on the service via https://www.myqnapcloud.com/u#/my_device.
Note that the publication checkbox on the NAS admin UI is only unpacted this, it odes not prevent to use service.


When in custom mode and publishing everything when clicking on the service we have all URLs

- QTS desktop
    - https://qlink.to/scoulomb
    - https://192.168.86.96:443/
    - http://192.168.86.96:8080/
    - https://scoulomb.myqnapcloud.com:443/
    - http://scoulomb.myqnapcloud.com:8082/
    - https://109.29.148.109:443/
    - http://109.29.148.109:8082/

- File station (similar for Photo and Music station, and using same port as QTS desktop)
    - https://file.qlink.to/scoulomb
    - https://192.168.86.96:443/filestation/
    - http://192.168.86.96:8080/filestation/
    - https://scoulomb.myqnapcloud.com:443/filestation/
    - http://scoulomb.myqnapcloud.com:8082/filestation/
    - https://109.29.148.109:443/filestation/
    - http://109.29.148.109:8082/filestation/

-Webserver (no smart link here)
    - https://192.168.86.96:8081/
    - http://192.168.86.96:80/
    - https://scoulomb.myqnapcloud.com:8081/
    - http://scoulomb.myqnapcloud.com:80/
    - https://109.29.148.109:8081/
    - http://109.29.148.109:80/

When we are using smart URL based on access control (quoting http://scoulombel-nas:8080/cgi-bin/ > `myQNAPCloud` > `access control` )
- > Private: Your device will not appear in search results. Only you can access your device on myQNAPcloud website. Invited users under Customized will be unable to access the device.
- > Public: Everyone can find your device with the device name and remotely access published services on your device via myQNAPcloud. If you have enabled myQNAPcloud Link, people can access your QTS or other services that you have published. You can switch to custom mode or private mode if you only want to provide access to certain users or just yourself.
- > Custom: Devices can only be searched and accessed by you and users you invite. Search results are invisible to other users. If unauthorized users attempt to connect to your device with a SmartURL, they will not be able to access the device.


But NAT url behavior will not be changed.


For our test purpose we will add on top of NAT rule made in [DNS.md](../DNS.md#intro))

- Port 8080 and 8082 to NAS mgmt in HTTP (why> we use 9080 but we will want to test same port as in NAS behavior, and also we saw above that port 8082 is used in HTTP in QNAP default URL)

````
del-nas 	TCP 	Port 	8080 	192.168.1.58 	8080 	
del-nas-2 	TCP 	Port 	8082 	192.168.1.58 	8080
````

which is tragetting same Ghome port as this rule

````
nas 	TCP 	Port 	9080 	192.168.1.58 	8080
````

we will also add a NAT rule to target webserver in TLS and non TLS

````
del-webserver 	TCP 	Port 	80 	192.168.1.58 	7080 	
del-webserver-s	TCP 	Port 	8081 	192.168.1.58 	7081
````

And then in gHome we will reforward this TCP port 

- 7080 -> 80 NAS
- 7081 -> 8081 NAS 

For this we deleted (disable not sufficient, and did not chnage gHome setup)

````
cert-valid 	TCP 	Port 	80 	192.168.1.58 	8180
````

**Test condition**
- We will test QTS desktop QNAP Smart URL resolution based on NAT port we have (Qfile, QPhoto are smilar)
- We will test also webserver which does not have Smart URL resolution
- We presume algo is order given in myQNAP cloud. We will use custom access where we disabled services publication to see if it does not impact resolution. (we will see it depends on devices)
- We will test in custom acces control with admin user (sco.....l@gmail.com), and NAS service unpublished to prove it does not impact Smart URL resolution (only what is shown in UI)
    - Below behavior was tested
        - When public no login is required to access URL
        - When private only admin can access URL (qnap account s.....l@gmail.com)
        - When custom only admin or allowed user can access URL
        - NAS login always required
- We disable all service publication to show it does not impact    


### QTS desktop

### Local Network 

To start all QTS desktop URL above are working manually

https://qlink.to/scoulomb
    - it resolved to http://109.29.148.109:8082/cgi-bin/
    - Disable:  	del-nas-2 	TCP 	Port 	8082 	192.168.1.58 	8080
    - it resolved to https://109.29.148.109/cgi-bin/
    - Disable  nas-sec2 	TCP 	Port 	443 	192.168.1.58 	8443
    - it resolved to https://192.168.86.96/cgi-bin/

This is the order in laptop, made same test wifi in Iphone we had (where we 
Renable all NAT rule)


https://qlink.to/scoulomb 
    - it resolved to https://scoulomb.myqnapcloud.com (443 implicit)
    - Disable:  	 	nas-sec2 	TCP 	Port 	443 	192.168.1.58 	8443
    - it resolved to  it resolved to http://109.29.148.109:8082/cgi-bin/
    - Disable:  	del-nas-2 	TCP 	Port 	8082 	192.168.1.58 	8080
    - it resolved to https://192.168.86.96/cgi-bin/

### External  (4g, wifi stop)


where we Renable all NAT rule  http://192.168.1.1/network/nat and disable Wifi


https://qlink.to/scoulomb 
    - it resolved to https://scoulomb.myqnapcloud.com (443 implicit)
    - Disable:  	 	nas-sec2 	TCP 	Port 	443 	192.168.1.58 	8443
    - it resolved to  it resolved to http://scoulomb.myqnapcloud.com:8092
    - Disable:  	del-nas-2 	TCP 	Port 	8082 	192.168.1.58 	8080
    - it resolved to https://a31.myqmapcloud.com
        - Same if I disable all NAT rule so NAT is not mandatory


==> Order of resolution depends on device and service publication has no impact expect what is visbile in https://www.myqnapcloud.com/u#/my_device?tab=my_device (Services)
When access control is public or private pas de `service diffuses` in myqnapcloud (even private), only when custom (bug?) <!-- check ok-->

## Webserver

Explore
>

````
scoulomb@scoulomb-Precision-3540:/run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=web$ echo "Hello World !!!" > index.html
````

Re-enable all NAT rule and test local network laptop only.
All mnaual link working.
**Note here we do not have Smart Link**


<!-- QNAP SMART URL CCL OK -->

We re-enable all NAT rules.
