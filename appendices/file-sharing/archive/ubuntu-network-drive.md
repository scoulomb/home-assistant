# Ubuntu network drive

This is for archive purpose as new Ubuntu version direcrly gives access to network storage.
- via Windows share/NFS: can see path via 3 dots in explorer: `/run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home/rclone-v1.64.0-linux-amd64$`. So we can SMB (dialct of cifs is used)
- and FTP
- and AFP (did not try)

Note FTP, FTPs, sFTP (equivlanent to SSHFS, do not explore)  detailed also in [sync nas data](../sync-nas-to-hdd-cloud.md#setup-ftp-in-nas))

## Alternative is to use cifs explicitly


````
$ sudo mount -o username=admin -t cifs //192.168.1.88/homes/admin ~/Documents/nas-admin-home
Password for admin@//192.168.1.88/homes/admin: 
````

Note command by default will use root user, but on our side we have admin thus -o
It will promt here admin password (also requires a strong pwd)

It requires `sudo apt install cifs-utils`
Also note the `//`

In NAS Privilege > shared folder we can edit access 

## We can also use nfs

````
$ sudo mount -t nfs -O user=admin 192.168.1.88:/homes/admin ~/Documents/nas-admin-home
mount.nfs: access denied by server while mounting 192.168.1.88:/homes/admin
````

But we can nount public

````
$ sudo mount -t nfs -O user=admin 192.168.1.88:/Public ~/Documents/nas-admin-home
````
We have a right issue with NFS share

````
$ showmount -e 192.168.1.88
Export list for 192.168.1.88:
/Public *
````

In shared folder, edit shared folder permission of homes, select permission type to NFS host access, add access right
See https://stackoverflow.com/questions/34799052/mount-qnap-nfs-share-on-linux-os

````
$ showmount -e 192.168.1.88
Export list for 192.168.1.88:
/homes  *
/Public *
````

We can see public has been added !

````
$ sudo mount -t nfs -O user=admin 192.168.1.88:/homes/admin ~/Documents/nas-admin-home-nfs
````

Note we specify user with big "O"


NFS does not prompt password, protected by source IP

Enable windows ACL support does not impact here

## Actually 

Actually NFS designed for linux:  https://fr.wikipedia.org/wiki/Network_File_System 
And SMB/CIFS for windows: https://en.wikipedia.org/wiki/Server_Message_Block#CIFS 

https://superuser.com/questions/270678/ports-for-nated-windows-share

could try `sshfs` 

````
scoulomb@scoulomb-HP-Pavilion-TS-Sleekbook-14:~/Documents$ sshfs admin@192.168.1.88:/ sshfs
admin@192.168.1.88's password: 
````

## NAS fan failure

Fix FAN failure on QNAP.
QNAP proposed to send back the NAS to change the FAN...

I actually solved issue by increasing tmpfs size.
https://forum.qnap.com/viewtopic.php?f=45&t=147781&p=711289

````
[~] # df -h | grep 100%
tmpfs                    64.0M     64.0M         0 100% /tmp
tmpfs                    64.0M     64.0M         0 100% /share/CACHEDEV1_DATA/.qpkg/MediaSignPlayer/CodexPackExt/tmp
tmpfs                    48.0M     48.0M         0 100% /share/CACHEDEV1_DATA/.samba/lock/msg.lock
[~] # mount -o remount,size=2G,noatime /tmp
[~] # df -h | grep 100%
tmpfs                    48.0M     48.0M         0 100% /share/CACHEDEV1_DATA/.samba/lock/msg.lock
[~] # df -h | grep tmpfs
devtmpfs                  1.8G      8.0K      1.8G   0% /dev
tmpfs                     2.0G     64.0M      1.9G   3% /tmp
tmpfs                     1.8G     13.3M      1.8G   1% /dev/shm
[...]
Filesystem                Size      Used   Available Use% Mounted on <-- Col headers
````
