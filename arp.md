scoulomb@scoulomb-Precision-3540:~$ sudo arp-scan --interface=wlo1 --localnet
Interface: wlo1, type: EN10MB, MAC: 60:f2:62:e1:1e:46, IPv4: 192.168.86.85
Starting arp-scan 1.9.7 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.86.1	f8:1a:2b:16:e3:d3	(Unknown)
192.168.86.79	ec:b5:fa:8b:56:6c	Philips Lighting BV
192.168.86.120	24:5e:be:3f:2b:f7	QNAP Systems, Inc.
192.168.86.100	c0:95:6d:5d:19:f9	(Unknown)
192.168.86.178	00:22:3f:f1:c2:7c	NETGEAR
192.168.86.160	8c:a9:6f:18:36:f5	D&M Holdings Inc.
192.168.86.161	8c:a9:6f:17:04:5f	D&M Holdings Inc.
192.168.86.114	1c:53:f9:11:38:9d	(Unknown)
192.168.86.198	d2:67:20:21:cf:c1	(Unknown: locally administered)
192.168.86.187	70:70:aa:fe:a6:5b	(Unknown)
192.168.86.255	1c:53:f9:11:38:9d	(Unknown)
192.168.86.183	fc:65:de:0f:b9:14	Amazon Technologies Inc.
192.168.86.157	84:f3:eb:e9:3d:45	Espressif Inc. (DUP: 1)
192.168.86.159	00:06:78:61:27:52	D&M Holdings Inc. (DUP: 1)
192.168.86.168	d8:3a:dd:e0:9b:81	(Unknown) (DUP: 1)

19 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9.7: 256 hosts scanned in 1.970 seconds (129.95 hosts/sec). 15 responded
scoulomb@scoulomb-Precision-3540:~$ nmap -sL 192.168.86.* | grep \(1
Nmap scan report for _gateway (192.168.86.1)
Nmap scan report for philips-hue-v2.lan (192.168.86.79)
Nmap scan report for scoulomb-precision-3540.lan (192.168.86.85)
Nmap scan report for living-room.lan (192.168.86.100)
Nmap scan report for scoulombel-nas.lan (192.168.86.120)
Nmap scan report for esp_e93d45.lan (192.168.86.157)
Nmap scan report for denon-avr-x2700h.lan (192.168.86.159)
Nmap scan report for denon-home-150-3.lan (192.168.86.160)
Nmap scan report for denon-home-150-2.lan (192.168.86.161)
Nmap scan report for pizero.lan (192.168.86.168)
Nmap scan report for amazon-630597f35.lan (192.168.86.187)
Nmap scan report for hs110.lan (192.168.86.190)
Nmap scan report for gateway-2024-5490-0496.lan (192.168.86.194)
Nmap scan report for pizero2.lan (192.168.86.196)
Nmap scan report for ncelrnd1851.lan (192.168.86.199)
Nmap scan report for netatmo.lan (192.168.86.200)
Nmap scan report for desktop-5nn6o2b.lan (192.168.86.201)
scoulomb@scoulomb-Precision-3540:~$ 
'

Daikin does not answer to arp requests!!!
So not visible in google home too

We can ip in application 

And it does not work (error, instead of invalid ip) becuase they disabled local acces 5

























































s