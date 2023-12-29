# QNAP file sharing 

It will leverage what we have seen in [SMART url](./qnap-smart-url.md)

## Access NAS

### Before we go further let's check QFilePro in iOS

It allows connection vua
- LAN IP `192...`
- myQNAPcloud (set to DDNS)
- myQNAPcloud link
- DDNS
- Update: we also have WAN IP

exactly what we have seen in Smart URL

### Before we go further let's check QManager in iOS

It has 
-LAN IP,
- myQNAPCloud (set to DDNS)
- DDNS
- No QNAPCloud link

The difference between myQNAPCloud with DDNS and QNAPCloudl link is not clear at all

## Sync

### QFile pro sync

We will sync photo using QFile pro: Auto upload settng camera roll

See [data summary](./data_summary.md#so-in-term-of-data)

### Alternative

- QSyncPro pro could achieve same result (and connection same way) but have to enter file path manaully
- QPhoto could also work
- In [sync NAS to HDD/Cloud](./sync-nas-to-hdd-cloud.md) we present other sync method, also used in [data summary](./data_summary.md#so-in-term-of-data)


## Share file with Friend

I renabled all NAT rules as of end of [QNAP smart URL section](./qnap-smart-url.md)

- We can use QNAP
    - https://192.168.86.96/cgi-bin/ > File station 5 > rigth click > share > create share link only > and here in domain we can choose smarshare, local ip, public ip, ddns
    - DDNS we get 2 links
        - https://192.168.86.96/share.cgi?ssid=27cc1c2555bf47e89f96b87f3bfe79af
        - https://scoulomb.myqnapcloud.com/share.cgi?ssid=27cc1c2555bf47e89f96b87f3bfe79af
        - OK tested we access the NAS locally
    - Smartshare we have
        - https://192.168.86.96/share.cgi?ssid=763dbe1cfe244c12bbdc6cfb45cf5629, we access the NAS directly
        - https://www.myqnapcloud.com/smartshare/74899gi44l6p700tv5uvv504_331gfj3jnn812p13rsvv2xby46cg9186, we access QNAP cloud (bnot the NAS directly)
             - if we disable NAT rule, DDNS will not work, LAN IP will work in local
             - But similarly to Smart URL, smartshare will work without NAT!! (tested OK !!)

    - If we do all links we have in https with all NAT disabled
        - Share link (local)
        - Local IP
        - SmartShare
        - MyQNAPCloud (whic is the DDNS)
    - If we do all links without HTTPS with all NAT disabled
        - Share link (loacal in HTTPs)
        - local IP in HTTP
        - Samrt share in HTTPs
        - myQNAP cloud in HTTP (8080)
    - If adding NAT rule it adds the WAN IP `109.`

Note that password is managed by smartshare or NAS locally.


- If [sync NAS to HDD/Cloud](./sync-nas-to-hdd-cloud.md) we can use pCloud file sharing for faster donwload (do not try OK)

<!-- ok CCL -->