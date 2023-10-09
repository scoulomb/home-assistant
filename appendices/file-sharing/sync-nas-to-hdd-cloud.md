# Sync file between NAS and external source (if pcloud sync worked ccl)

## To hard drive

I am using HBS3 to sync `scoulomb-data` folder to LaCie Harddrive (orange)

## To myQNAP cloud storge beta

See https://www.qnap.com/solution/myqnapcloud-storage/en/
 
For Hybrid Back-up Sync 3 (HBS3) to support qnapcloud storage we have to
- update firmware (optionsl)
- and HBS in app cemter
See https://www.qnap.com/en/how-to/faq/article/how-can-i-start-using-myqnapcloud-storage

If we have pemrssion issue. We can give give rigths in control panel shared folder

We can have filtering rules

Issue: free version limited to 16GB, we have 125GB of data

## To pCloud

See this note on Ubuntu network drives [here](./archive/ubuntu-network-drive.md)

- we can use pCloud drive software in Ubuntu. It may require to mount network drive as described in archive [ubuntu--netowrk-drive](./archive/ubuntu-network-drive.md)
- HBS3: 
    - It is not natively supported by HBS3
    - We can use Webdav synchronization but it is failing most of the time
- We can use Pcloud API but it is complex to use (in Github we have a good python wrapper)
    - https://docs.pcloud.com/methods/intro/authentication.html
    - https://eapi.pcloud.com/userinfo?getauth=1&logout=1&username=coulombel.sylvain@gmail.com&password=MYPASSWORD
    - https://eapi.pcloud.com/listfolder?auth=PGohOVZUvu7ZbLKqknAkG0j9GuB7l3TWqmd63pFV&path=/nas-sync
- We can use rclone
- We can use multicloud platform

**I will focus on latter  option via rClone and multicloud platform**


### How to setup RClone 

#### Ubuntu

We can setup rClone on Ubuntu via snap

````
sudo snap install rclone
````
From there we map NAS folder in NFS (see gist) or use default mount (in explorer, 3 dots, open terminal and pwd to see path) to synchronize

#### QTS

Setup is more complex


We can do it via install script

````
curl -k https://rclone.org/install.sh > rclone.sh
sed -i 's/curl/curl -k/g' rclone.sh # Fix insecure add -k in script
chmod u+x rclone.sh
./rclone.sh
````

It will setup rClone in 

````
/usr/bin/rclone.new config (find path in install script)
````


<!--

if this issue on NAS

[~] # ./rclone.sh
curl: (23) Failed writing body (217 != 4744)
[~] # curl -k -OfsS "$download_link"
curl: Remote file name has no length!
curl: try 'curl --help' or 'curl --manual' for more information
curl: (23) Failed writing received data to disk/application
[~] # curl -k -OfsS "$download_link"

==> space issue (same as fan)
mount -o remount,size=512m,noatime /tmp
https://forum.qnap.com/viewtopic.php?t=147781
-->

It is painful as erased everytime we re-start the NAS

Alternative is to downlaid directly software package (this gives me the ida: https://www.stefanwienert.de/blog/2016/09/05/rclone-on-qnap-backup-cloud-storages-to-your-ancient-nas/)

- Download source intel amd 64 bits from: https://rclone.org/downloads/
- Unzip and copy extracted folder to home

then 

````
//share/homes/admin/rclone-v1.64.0-linux-amd64/rclone config

# or
alias rclone="//share/homes/admin/rclone-v1.64.0-linux-amd64/rclone"

rclone config
````

### How to configure RClone with PCloud

#### Ubuntu 

On ubuntu do rclone config, see [Rclone doc for pcloud](to be added)

In all cases be careful to select in advanced config european dc (`**e**api`)


On NAS it is more complex: we will have to get token on a machine which has browser access 
https://rclone.org/remote_setup/

#### QTS

So on QNAP `rclone config` and say no browser access. 

On ubuntu get the token

````
rclone authorize "pcloud"
````

Output will be

````
scoulomb@scoulomb-Precision-3540:~/dev$ rclone authorize "pcloud"
<5>NOTICE: Config file "/home/scoulomb/snap/rclone/477/.config/rclone/rclone.conf" not found - using defaults
<5>NOTICE: If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=AonNpp6Q2nKj4WuVysE4Tg
<5>NOTICE: Log in and authorize rclone for access
<5>NOTICE: Waiting for code...

<5>NOTICE: Got code
Paste the following into your remote machine --->
{"access_token":"Uvu7ZDnONSMYSECRETOTKEN","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}
<---End paste
````

And be careful do copy the full JSON!!!

For instance I made this test on Precsion with following config


````
~/dev$ rclone config file
Configuration file is stored at:
/home/scoulomb/snap/rclone/477/.config/rclone/rclone.conf

$cat /home/scoulomb/snap/rclone/477/.config/rclone/rclone.conf
[pcloud]
type = pcloud
token = Uvu7ZDnONSMYSECRETOTKEN
hostname = eapi.pcloud.com

[pc2]
type = pcloud
hostname = eapi.pcloud.com
token = {"access_token":"Uvu7ZDnASECTOKEN","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}
````

We have an error when syncing with pcloud but not pc2: `Failed to create file system for "pcloud:nas-sync-direct-rclone": failed to configure Pcloud: invalid character 'U' looking for beginning of value`


#### QTS tips Alternative ti setup QNAP is to copy Ubuntu config file to QNAP.

````
vim myconf.txt (open terminal from explorer, be careful this path is not the same in NAS)

[pc]
type = pcloud
hostname = eapi.pcloud.com
token = {"access_token":"Uvu7ZDnASECTOKEN","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}
````

and 

````
# rclone config file
Configuration file doesn't exist, but rclone will use this path:
/root/.config/rclone/rclone.conf
````

````
cat '//share/homes/admin/rclone-v1.64.0-linux-amd64/myconf.txt' >>  /root/.config/rclone/rclone.conf

````

### How to sync with PCloud?

Note copy vs sync: https://forum.rclone.org/t/rclone-copy-or-sync/2089/6

-`-timeout 1000s`:  https://forum.rclone.org/t/rclone-stucks-at-the-end-of-a-big-file-upload/8102
- also use `--track-renames` option 
- use setsid for clsoing shell

````
ssh admin@scoulombel-nas
alias rclone="//share/homes/admin/rclone-v1.64.0-linux-amd64/rclone"

rclone sync //share/homes/admin/scoulomb-data pc:nas-sync-direct-rclone --timeout 1000s --exclude="*.git/"  -P

# setsid does not work with alias (execvp error)
setsid //share/homes/admin/rclone-v1.64.0-linux-amd64/rclone  sync //share/homes/admin/scoulomb-data pc:nas-sync-direct-rclone --timeout 1000s > //share/homes/admin/out.txt
# setsid and `` not working for now (excvp)
tail -f //share/homes/admin/out.txt
````


### ALtnerative ro RClone use multcloud and FTP <!-- OK CCL confirmed-->

https://recoverit.wondershare.com/backup-files/synology-pcloud.html

FTP crash course: https://www.it-connect.fr/les-protocoles-ftp-ftps-et-sftp-pour-les-debutants/

#### Setup FTP in NAS

##### We are doing FTP in passive mode

http://scoulombel-nas:8080/ > `QuFTP` service > `FTP server` > `System` > `General` to activate FTP.

We can use filezilla, to connect `scoulombel-nas` and use port 21 locally => It is working.

Now we want to access from Internet
- We will double NAT port 21 for control
    - http://192.168.1.1/network/nat: `ftp-ctrl 	TCP 	Port 	21 	192.168.1.58 	2221`
    - gHome 2221 -> 21 NAS
- And we need another port for the data usually port 20 in active mode.
- But we are in passive mode so we have to 
    - defne a port range in QuFTP: http://scoulombel-nas:8080/ > `QuFTP` service > `FTP server` > `System` > `Connextion` > Passive FTP definie port range (or could use default). On top to avoid warning we can had response IP as `109.29.148.109` otherwise it would fallback to request IP.
    - http://scoulombel-nas:8080/ > `QuFTP` service > `FTP server` > `User`: I recommend to use dedicated user
    - double NAT this range
        - http://192.168.1.1/network/nat : `tp-data 	TCP 	Plage 	1501-2505 	192.168.1.58 	1501-2505` (we can not define offset ext int port)
        - gHome 2900-3000 -> 2900-3000 (TCP) NAS (same no offset posssible, enter range with `-``) 

##### FTPs

Now we can also activate FTP with certificate (FTPs) in passive mode
http://scoulombel-nas:8080/ > `QuFTP` service > `FTP server` > `System` > `General` to activate FTP with SSL/TLS.

Tested in FileZilla with `scoulombel-nas`, name mismatch war as expected, `home.coulombel.net` wirking like a charm as reusing previous cert made in [DNS and cert appendince](DNS.md)

##### sFTP

https://help.one.com/hc/en-us/articles/115005585709-How-do-I-connect-to-an-SFTP-server-with-FileZilla-


From same location we can enable sFTP (open SSH setting and enable sFTP)
 
````
ssh admin@home.coulombel.net -> password denied
ssh admin@scoulombel-nas -> OK
````

Because SSH NAT port  already opened. Cf. top of document => [DNS.md intro](DNS.md) => see [README](../README.md#solution-1-double-dnat) to precision !!
We need a NAT rule for SSH NAS access.

- http://192.168.1.1/network/nat : `ssh-to-nas 	TCP 	Port 	222 	192.168.1.58 	22222`
- gHome 22222 -> 22 (TCP) NAS 

````
ssh admin@home.coulombel.net -p 222
````

And access in Filezilla 
- `sftp://scoulombel-nas admin pwd default-port=22` OK
- `sftp://home.coulombel.net admin pwd 222` OK
<!-- ssh.scoulombel-nas(.local) did not work -->

#### Multcloud setup 

https://app.multcloud.com/

Configure NAS and PCloud source and sync but does not work well in practise