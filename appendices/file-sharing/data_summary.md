# Data status

28 Novembre 2020

## Storage backup

- Dropbox
  - syl[....]bel@gmail (via google SSO)
  => import via pcloud autobackup 
  => deleted all content, stop using
  - co[....].[...]bel@gmaildirect login)
  => import via file download to pcloud
  => deleted all content, stop using

==> OK


- Google drive (before copy what to keep in shared with me in own folder)
  - syl[....]bel@gmail.com
  - coulombel.sylvain@gmail.com
  => import both via google takeout (Note import via pcloud missed some files)
  => deleted all content, stop using

==> OK


- Google photos 
  - syl[....]bel@gmail.com copied to: \\scoulombel-nas\homes\admin\scoulomb-data\My Pictures\takeout-google-photos-sylvaincoulombel-20201129-shanghai-mainly
  - co[....].[...]bel@gmailcopied to:  \\scoulombel-nas\homes\admin\scoulomb-data\My Pictures\takeout-google-photos-coulombel-sylvain-2017-2020
  => import via google takeout
  => decide to keep content on Google photos but stop using and syncing
==> OK

- pcloud
  - was used as temporary location for all files now in NAS (compared with winmerge and ok on 5feb20221AM)
  - was used for photos sync from 11jul19 to 16apr22 copied to: \\scoulombel-nas\homes\admin\scoulomb-data\My Pictures\Samsung SM-G950U-Pcloud-sync-11jul19-16Apr22
    - Note pcloud auto upload and google photo "takeout-google-photos-coulombel.sylvain-20201129" (as also synced from phone), we have import doublon from 7/11/2019 (last phone reset) to 28/11/2020 (date we stop google photo sync) .
    - facebook sync:  (this leads to dupe as usually picture coming from above source)
    - NOW Only used for sync from here (NAS) to pcloud via HBS
==> OK

- MyQNAPCloud -> tentative back-up OK via HBS rm

# So in term of data

6oct23

- [**] Current sync : scoulomb-data (see details in [sync NAS to HDD/Cloud](./sync-nas-to-hdd-cloud.md)) (last sync 2 apr complete, could automate on rasp but better manaul to check)
  - NAS to Pcloud via rClone (pcloud/scoulomb-data)
  - NAS to LaCie Orange via HBS

- Iphone photo to iCloud (suspended and deleted from cloud as capa max reached in Settings > Profile > ICloud ) and will not pay extra storage to Apple
- Iphone photo to scoulomb-data/iPhone-pic-sync (and not in scoulomb-data/Multimedia/Pictures/...) via [QFilePro](./qnap-file-sharing.md) --> Then [**] Current-sync
- IPhone photo to pcloud/automatic upload folder (setup via pcloud setting > Upload settings): **this backup folder can be deleted if all fine as we have a copy in scoulomb-data/iPhone-pic-sync**

- QobuzDonwloads -> new 2024 HDD

- We also have 
  - git repo
  - manning book
  - onedrive 1a
  - qobuz paid download (backup, except no zip for london) in scoulomb-data/multimedia/music

- misc
  - Whatsapp sync to iCloud OK
  - Authentificator to iCloud OK

Optional 
 - Get whatapp image
 - Ensure dropbox not empty


Old data summary to ignore OK - do not recheck all here OK