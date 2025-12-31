#!/usr/bin/bash


disconnect_vpn () {
  echo “Terminating VPN connection”
  protonvpn-cli d
  sleep 4
  curl ifconfig.me
}



connect_vpn () {
  echo “Start VPN connection”
  protonvpn-cli connect --fastest --protocol udp
  sleep 4
  curl ifconfig.me
}


while :
do
  echo “Start dl loop”
  connect_vpn # avoid throttling
  timeout 7200 qobuz-dl dl qobuzurl25.txt -d /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=homes/admin/QobuzDownloads;sleep 5;timeout 7200 qobuz-dl dl qobuzurl25.txt -d /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=homes/admin/QobuzDownloads
  disconnect_vpn
  echo “Terminating dl loop”


  # We can press Ctrl + C to exit the script
done


trap "disconnect_vpn" INT

# following folders can be used if via explorer we login as user (admin) with R/W user in QNAP shared folder (control panel > privilge) so as to mount them, this should be done before protonvpn is connected otherwise it will fail
# /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=home/QobuzDownloads
#/run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=homes/admin/QobuzDownloads
# to discover those folders open term
# This one not working even if write access
# /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=qobuzdownloads


 # Use thids extension to build DL file: https://addons.mozilla.org/fr/firefox/addon/export-tabs-urls-and-titles/ (dranf and drop album to adress bar)