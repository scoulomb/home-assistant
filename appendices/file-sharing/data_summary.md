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

## So in term of data

*Dernière mise à jour : 30 juin 2026*

### /home/scoulomb-data

- **[★] scoulomb-data** — voir détails dans [sync NAS to HDD/Cloud](./sync-nas-to-hdd-cloud.md). Pourrait être automatisé sur Rasp mais préférable de vérifier manuellement.
  - NAS → pCloud via rClone (`pcloud/scoulomb-data`) — dernière sync complète : 2 avril 2024.
  - NAS → TR-002 via HBS — voir [QNAP TR-002](./QNAP-TR002/hbs.md) — dernière sync complète : 2 avril 2024.
  - Re-sync soon as changes made 30 june 26

### /home/QobuzDownloads

(note shared mount folder mounts /home/QobuzDownloads)

- Sync via HBS vers TR-002 — voir [QNAP TR-002](./QNAP-TR002/hbs.md).
- Réduit la latence dans le setup multiroom (MS120 + HEOS, Moode multiplayer).

### /home/MAO

Not sync

### Photos iPhone

- **iPhone → iCloud** — Sync active et payante. Peut être suspendue si problème de capacité (Réglages > Profil > iCloud).
- **iPhone → `scoulomb-data/iPhone-pic-sync`** — via [QFilePro](./qnap-file-sharing.md) (et non dans `scoulomb-data/Multimedia/Pictures/...`).
  <!-- Les photos peuvent aussi être directement dans le dossier pictures et iPhone pic, ex: scoulomb-data/Multimedia/Pictures/2025-Telethon-Antibes -->
- **iPhone → `pcloud/automatic upload`** — configuré via pCloud > Upload settings. **Ce dossier de backup peut être supprimé si tout est OK, car copie déjà dans `scoulomb-data/iPhone-pic-sync`.**

### Autres données

- Repos Git
- Livres Manning
- OneDrive 1A
- Qobuz achats payants → `scoulomb-data/multimedia/music` (à distinguer de QobuzDownloads qui contient les FLAC téléchargés via [`qobuz-dl`](../../sound-video/qobuz-dl))

Voir [note on book](#note-on-books)

### Divers

- WhatsApp sync vers iCloud ✓
- Authentificator sync vers iCloud ✓

### Optionnel / TODO

- Récupérer les images WhatsApp
- Vérifier que Dropbox est bien vide



## Note on Books

Emplacement : `/Volumes/home/scoulomb-data/DATA/Books`

- **`_Manning-multi-topic`** — Tous les livres Manning.
- **`MAO`** — Livre MAO, aussi disponible sur [MAO repo](https://github.com/scoulomb/MAO/blob/main/PersoMAOAppleNotesExtract/Attachments/A2566FF2-82F6-409C-8EF4-94EE92171F0E.pdf).
- **`network-books-from-private-books-git-main`** — Livres réseau, aussi sur [private-books](https://github.com/scoulomb/private-books).
- **`Notices`** — Notices produits (sauf HIFI). Les notices HIFI sont sur [home-audio-system/Misc-manuals](https://github.com/scoulomb/home-audio-system/blob/main/Misc-manuals). Focusrite aussi sur le [MAO repo](https://github.com/scoulomb/MAO/blob/main/PersoMAOAppleNotesExtract/Attachments/A2566FF2-82F6-409C-8EF4-94EE92171F0E.pdf).
