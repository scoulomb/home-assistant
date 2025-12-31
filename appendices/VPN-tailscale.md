# Tailscale VPN

See link to
- https://github.com/scoulomb/myhaproxy/blob/main/README.md#we-have-seen-3-ways-to-access-internal-server-from-external
- [DNS.md](./DNS.md#secure-connection-via-vpn)

Tailscale does not need NAT to VPN. How does it worlk?
[](./media/Tailscale/How%20Tailscale%20works.pdf)
[](./media/Tailscale/How%20NAT%20traversal%20works.pdf)


And here explain how connection outbound without nat:
https://github.com/scoulomb/private_script/blob/main/Links-mig-auto-cloud/Additional-comments.md#socket-establishment-directrion-vs-message-flow-direction


We can even setup tailscale via Home Assistant pluging agent (not agwnt running the NAS) and use certificates in HA (even if VPN): https://tailscale.com/blog/remotely-access-home-assistant  (we will not try) 

Below is a gist import

## Tailscale

### Tailscale is an alternative VPN to access local network, it completes

- https://github.com/scoulomb/home-assistant?tab=readme-ov-file#note-on-vpn
- https://github.com/scoulomb/home-assistant/blob/main/appendices/VPN.md#alternative  -> [VPN.md](./VPN.md)
(link to https://github.com/scoulomb/private_script/blob/main/Links-mig-auto-cloud/Additional-comments.md#socket-establishment-directrion-vs-message-flow-direction)


Here it is described how it is working: https://tailscale.com/blog/how-tailscale-works (2 appraoch: mesh or hub and spoke, tailscale is a mesh with key managed in hub,  qnap vpn approach a kind of hub and spoke) 

It requires an agent running on each host

But we can use relay nodes: https://tailscale.com/kb/1019/subnets

Approach to have agent on QNAP NAS (software center) and phone is great as NAS can then access to LAN (cf heos)

Among VPN feature

- VPN to connect to remote local network
- And have outbound connection from IP adress (SNAT) linked to remote local network

The second one is not offered by default but we can use exit node to have this feature
https://tailscale.com/kb/1103/exit-nodes
> By default, Tailscale acts as an overlay network: it only routes traffic between devices running Tailscale, but doesn’t touch your public internet traffic, such as when you visit Google or Twitter. 

Can be a solution for Netflix: https://github.com/scoulomb/home-assistant/blob/main/appendices/VPN.md#alternative (exit node at home)

See overlay network
https://byteshiva.medium.com/understanding-overlay-networks-and-how-they-compare-with-tailscale-88385e9d727a

Mullvald VPN can actually be used s exit nodes: https://tailscale.com/kb/1258/mullvad-exit-nodes (2 vpn combo here)

When you are in 4g with actived tailscale
IP is IPv6 but actually this the one of SFR 4G SNAT (not tailscale one)

Also some provider do cgnat https://lafibre.info/sfr-la-fibre/ipv4-cgnat/
Tailscale would be useful here

### QNAP VPN still requires to NAT VPN port (and not all ports)

[VPN.md](./VPN.md#connect-to-vpn-via-phone)

(when using ISP box and not bypass as shown in [flint router](../2025-new-gen-setup/flint3-router))

Here they describe How NAT traversal works
https://tailscale.com/blog/how-nat-traversal-works

**Complete concluded discussion Michel (and access links db other topic as said in commit msg 7mar24) : https://github.com/scoulomb/private_script/blob/main/Links-mig-auto-cloud/Additional-comments.md#socket-establishment-directrion-vs-message-flow-direction**

Above we are in [configuration 4 equivalent (4 bis)](../2025-new-gen-setup/flint3-router/5-other-test-on-vpn-with-slate-7.md#reminder-on-nomenclature)

### Example of VPN not related to local access and free

Here we are in [configuration 2 equivalent](../2025-new-gen-setup/flint3-router/5-other-test-on-vpn-with-slate-7.md#reminder-on-nomenclature)

Here usage is for the facade IP

```
protonvpn-cli c
```

Usage avoid ban IP

https://community.roonlabs.com/t/issue-connecting-to-qobuz/212939

when using 

````
qobuz-dl dl qobuzurl3.txt -d /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=homes/admin/QobuzDownloads ;  qobuz-dl dl qobuzurl4.txt -d /run/user/1000/gvfs/smb-share:server=scoulombel-nas.local,share=homes/admin/QobuzDownloads
````

This music in NAS can be accessed via NAT, qnap vpn or tailscale

(music folder in nas in multimedia station to add, it is not music station)

Access it via QMusic or music station UI (there is a direct app), ensure on the fly trancoding: https://www.qnap.com/en-as/how-to/faq/article/how-to-play-lossless-flac-and-alac-files-using-qmusic) in QMusic
To download music

https://github.com/scoulomb/home-assistant/blob/main/appendices/VPN.md#alternative

also if no limit we can have

vod@c....net @@T
redirect mail to myaccount....management@g.com with same pwd
and from here redirect email


Best to replace this is to [have a glinet router to be in configuration 3](../2025-new-gen-setup/flint3-router/5-other-test-on-vpn-with-slate-7.md#reminder-on-nomenclature)

