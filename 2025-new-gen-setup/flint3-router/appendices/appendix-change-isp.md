# Change ISP from SFR to Bouygues BBOX Fiber

See [VPN dojo](../../../../notes-temp/Links-mig-auto-cloud/2025-consolidation/Dojos/VPN-Dojo/VPN-dojo.md) for VPN setup to access home network remotely.

Note on [Double NAT, bridge and DMZ mode](appendix-of-change-isp-appendix-double-nat-bridge-and-dmz.md)
- BBOX does not have separate ONT so not possible to do: https://github.com/scoulomb/home-assistant/blob/main/2025-new-gen-setup/external-access/README.m
  - Actaully we can request a 10G ONT and got it, but flint 3 is 2.5G so could have some loss
- BBOX does not support double NAT (what I used for SFR before move to fiber and ONT) 
- does not support bridge
- only DMZ mode. 

Note SFR with ont + box + ghome was the work as replace by just my own glInet router.

Alternative ipv6 prefix delegation: https://en.wikipedia.org/wiki/Prefix_delegation (equivalent to bridge):https://lafibre.info/installation-ftth/byou-pure-fibre-dmz-ou-mode-bridge-disponible/
