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



