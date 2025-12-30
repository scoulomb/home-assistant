# Other test with VPN and slate 7

Previously in section [setup VPN with flint 3 router](./4-deep-dive-vpn-and-routing.md#setup-vpn-with-flint-3-router), we showed how to configure flint3 to target proton VPN wireguard server.

We are in case  
[`3. Public commercial VPN on home WireGuard router: Laptop → GL.iNet (client, home) WireGuard → Proton VPN server  → Internet`](#reminder-on-nomenclature)


## Wireguard VPN test with slate 7 and flint 3

### Set up a WireGuard server on Flint 3, connected to the ONT at home on Bouygues Telecom Fiber network.

- Connect Mac Mini device to Flint 3's WiFi.
-  Access the Flint 3 WireGuard server configuration page at `http://192.168.8.1/#/wgserver` and generate the server configuration.

### Connect Slate 7 to WireGuard VPN server on flint 3 with iPhone hotspot

- Switch the Mac Mini device's WiFi connection to Slate 7.
- Confirm the iPhone device is not connected to Flint 3's WiFi (connect to Slate 7 to ensure, anyway an iPhone cannot simultaneously consume Wi-Fi and share Wi-Fi (i.e., it cannot take internet from one Wi-Fi network and rebroadcast it to others).
- Check IP address using `https://whatismyipaddress.com/`, from Iphone we have `86.71.230.168` and an IPv6 address `2a02:8440:e505:24ba:dc15:28e2:79a8:c453`.
- This IP is SFR ISP 4G network IP address.
- Repeat on Slate7 iphone 4G hotspot connection:
  - https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/ 
  - Also not here we are not using the wan interface but wwan and wwan6
- Check the public IP address on Mac Mini it shows SFR IPv4, e.g., `86.71.230.168`). IPv6 is not detected since not activated in slate 7.
- Visit `https://whatismyipaddress.com/ip/86.71.230.168` to confirm this is the SFR IPv4 address.
- Activate the VPN client at `http://172.16.0.1/#/wgclient` while still connected to Slate 7's WiFi.
- Check the public IP address again (should now show the home WiFi IP (Bouygues ISP), e.g., [`176.143.200.212`](./4-deep-dive-vpn-and-routing.md#lets-observe-the-routing-table-before-vpn-setup-). IPv6 is not detected.
- So we did a vpn to home :)
- Confirm VPN connection routes traffic through the home network.
- Disconnect the VPN and verify the public IP and it reverts to the SFR IPv4 (`86.71.230.168`).

### Use LuCI instead of glInet wiregaurd interface

Follow exact same procedure: https://protonvpn.com/support/openwrt-wireguard?srsltid=AfmBOoo6_PFiI6OyzvkPA9OfJvmYG7feitiYKw0HEhV21vYSIRLlR_rj

See [Proton VPN](./4-deep-dive-vpn-and-routing-media/protonVPN-wireguard.pdf)

Note In firewall setup when creating zone homevpn with `lan => homevpn`, do not forget to tick masquerading so as to
>Enable network address and port translation IPv4 (NAT4 or NAPT4) for outbound traffic on this zone. This is typically enabled on the wan zone

And ensure zone associated to interface 


Not client from glint gui created the zone wgclinet (with not needed forwarding `wgclient => WAN` and always present `lan =>wgclient` rule)

It work when activating the VPN interface from LuCI

When disabling the interface I go back to SFR IP: `IPv4: ? 86.71.230.168`

We are in case  
[`4. Private site\-to\-site (home) VPN: Laptop → GL.iNet (client, holiday location) WireGuard → GL.iNet (server, home) → Internet`](#reminder-on-nomenclature)

When we use mobile phone to connect to wireguard server (directly) same applies, and it leads to same results as if phone is connected to router which hosts the VPN client (could not test phone via router as phone is used for 4G connection here but easily extrapolated by this test [below](#testing-with-slate-7-as-a-repeater-of-flint-3-wifi-where-flint-3-connected-to-fiber-and-where-slate-7-is-running-a-wireguard-client-to-a-proton-vpn-wireguard-server).
What we did [external access section](./../external-access/README.md#method-1use-a-vpn).






## Comment on IPv6 and repeat mode without VPN 


**IPv6 Native Mode Test (Without VPN)**

1. Enable IPv6 in native mode at `http://172.16.0.1/#/ipv6`.
2. On the router's status page (`http://172.16.0.1/#/internet`), observe:
   - IPv4: `172.20.10.8`
   - IPv6: `2a02:8440:e505:24ba:4af:94ff:fe88:dc96/64`
3. On the laptop, check public IP:
   - IPv4: `86.71.230.168`
   - IPv6: Not detected
4. On the phone (connected directly to the network), check public IP:
   - IPv4: `86.71.230.168`
   - IPv6: `2a02:8440:e505:24ba:dc15:28e2:79a8:c453`
5. This shows IPv6 prefix delegation is active, and IPv4 uses SNAT.

The router applies the same mechanism as seen [in section 3](./3-deep-dive-on-ipv6.md#ipv4ipv6-and-snat)

---
## Testing with Slate 7 as a repeater of Flint 3 WiFi (where flint 3 connected to Fiber), and where slate 7 is running a wireguard client to a proton VPN WireGuard Server

Note in section [Wireguard VPN test with slate 7 and flint 3](#wireguard-vpn-test-with-slate-7-and-flint-3) we did
- Slate 7 as a repeater of **iPhone 4G connection**, and where slate 7 is running a wireguard client to a **home** VPN WireGuard Server running on flint 3

[Here](#testing-with-slate-7-as-a-repeater-of-flint-3-wifi-where-flint-3-connected-to-fiber-and-where-slate-7-is-running-a-wireguard-client-to-a-proton-vpn-wireguard-server) we do
- Slate 7 as **a repeater of Flint 3 WiFi**(where flint 3 connected to Fiber), and where **slate 7 is running a wireguard client to a proton VPN WireGuard Server**

Steps are

1. Duplicate the Flint 3 WiFi setup.
2. Connect to the WireGuard server provided by Proton VPN, following the same steps [as previously described](#use-luci-instead-of-glinet-wiregaurd-interface).
3. Mac Mini connected to Slate 7's WiFi (which is repeating Flint 3's WiFi).
4. Check the public IP address on Mac Mini:
   - IPv4: `212.102.51.97` (Proton VPN server in Tokyo, Japan)
   - IPv6: Not detected
4. IP details:
   - ISP: DataCamp Limited
   - Service: VPN Server
   - Location: Tokyo, Japan


I also connected iphone to slate 7 wifi repeater and checked public IP: We have same results. 

We are still in case  
[`3. Public commercial VPN on home WireGuard router: Laptop → GL.iNet (client, home) WireGuard → Proton VPN server  → Internet`](#reminder-on-nomenclature)


So VPN client also behind a NAT (in case we keep ISP box) would not be an issue.
However VPN server we would have to DNAT/forward or DMZ mode (or bridge) if we plug flint3 behind ISP box (we have the VPN IP in wireguard server conf).
See [appendices](./appendices/appendix-of-change-isp-appendix-double-nat-bridge-and-dmz.md)



## About this post 

![](./5-other-test-on-vpn-with-slate-7-media/glinet-iS-CRUISE.jpg)


Note in section [Wireguard VPN test with slate 7 and flint 3](#wireguard-vpn-test-with-slate-7-and-flint-3) we did
- Slate 7 as a repeater of **iPhone 4G connection**, and where slate 7 is running a wireguard client to a **home** VPN WireGuard Server running on flint 3

This is exactly the same as this cruise case :).

## A crazy case that could work too (but did not manage in practise)


- Slate 7 (repeat iPhone 4G) -> VPN -> home Flint 3 -> Iphone 4g
- home Flint 3 -> VPN -> protonvpn server

I should see proton VPN IP...


Will not dive more this case. (I had kept wgserver in fw)

It would be a [combination of](#reminder-on-nomenclature)
> - 3. Public commercial VPN on home WireGuard router: Laptop → GL.iNet (client, home) WireGuard → Proton VPN server  → Internet
> - 4. Private site\-to\-site (home) VPN: Laptop → GL.iNet (client, holiday location) WireGuard → GL.iNet (server, home) → Internet  

## Proton VPN software 

Instead, we can install the ProtonVPN software directly on the machine (tested and confirmed to work).
However, configuring it on a GL.iNet router offers additional benefits:

*   Multiple devices can connect through a single VPN endpoint, removing the limitation of per-device setup in free version.
*   You can easily choose the VPN server location not allowed via free version

**Note:** In general, using WireGuard on a GL.iNet router also allows you to maintain a VPN connection on laptops where you don’t have full administrative (corp) and can not install the client.


[It would be case 2. Public commercial VPN on laptop: Laptop → ProtonVPN client → Proton VPN server  → Internet  ](#reminder-on-nomenclature)

It could also help to have a VPN on TV stick in particular locked apple TV (fireTV easier but need a client on the stick, [case 2 in nomenclature](#reminder-on-nomenclature)) 


We also have proton CLI (still case 2) but note

Note the:
- GUI (Free plan) → Auto-connects to the fastest free server, no manual server choice.
- CLI and OpenWRT even with free plan → Lets you pick country and even specific server using commands like

But CLI has still this limitation of connection number

See also [this notes](../../appendices/VPN.md) and protonVPN CLI with qobuz DL: https://github.com/scoulomb/home-assistant/tree/074f96f93a05b7defd4129098ecd1c98639a54bb/sound-video/setup-your-own-media-server-and-music-player


## Comment on Proton Double hop

Proton’s **Double Hop VPN** is a feature offered by Proton VPN that routes your internet traffic through 
**two VPN servers in different countries** instead of just one.


### ✅ **How it works**

*   Normally, a VPN sends your traffic through a single encrypted tunnel to one server.
*   With **Double Hop**, your traffic goes through **two encrypted tunnels**:
    1.  **First server**: Entry point (e.g., in France)
    2.  **Second server**: Exit point (e.g., in Switzerland)
*   The second server is the one that connects to the internet, so websites only see the IP of the second server.

### 🔒 **Benefits**

*   **Extra privacy**: Even if one server were compromised, the second hop adds another layer of protection.
*   **Harder to trace**: Your real IP is hidden behind two layers.
*   **Useful for high-risk activities** (journalists, activists, etc.).

### ⚠️ **Trade-offs**

*   **Slower speeds**: Two hops mean more latency.
*   **Not always needed** for everyday browsing or streaming.

Proton calls this feature **Secure Core** when the first hop is in a privacy-friendly country (like Switzerland or Iceland) 
and the second hop is elsewhere.



## Reminder on nomenclature

[Reminder on nomenclature here](../../../notes-temp/Links-mig-auto-cloud/2025-consolidation/Dojos/VPN-Dojo/VPN-dojo.md)

> - 1. Corporate VPN on laptop : Laptop → Corporate VPN client → Corporate VPN server → Internet  
> - 2. Public commercial VPN on laptop: Laptop → ProtonVPN client → Proton VPN server  → Internet  
> - 3. Public commercial VPN on home WireGuard router: Laptop → GL.iNet (client, home) WireGuard → Proton VPN server  → Internet
> - 4. Private site\-to\-site (home) VPN: Laptop → GL.iNet (client, holiday location) WireGuard → GL.iNet (server, home) → Internet  
> - 5. Double VPN: Corporate VPN inside private home WireGuard path (or ordering variant).  


If we use on top of case 3,4 a VPN on laptop 1 (corporate),2 (not tested) we enter in case 5.
And even triple VPN if we consider [case 5](#a-crazy-case-that-could-work-too-but-did-not-manage-in-practise) <!-- not details more triple -->

## Comment on VPN IP

Note VPN could help to have a fix static IPv4 if we pay for this option, if ISP offer only a dynamic IPv4.

[See more details](../../../notes-temp/Links-mig-auto-cloud/2025-consolidation/Dojos/VPN-Dojo/VPN-dojo.md).
<!-- VPN snat fix ip -->  emy -->is actually vpn provider one -->, 

IPv6 is most likely always static though.

## When sharing phone connection aboard avoid charges by using following tip

On an iPhone, you can avoid **cellular data roaming** and control **network selection** easily through Settings. Here’s how:

***

### ✅ **Disable Cellular Data Roaming**

1.  Open **Settings** → **Cellular** (or **Mobile Data**).
2.  Tap **Cellular Data Options**.
3.  Tap **Data Roaming** and **turn it OFF**.
    *   This prevents your phone from using data when you’re on a foreign network.

***

### ✅ **Disable Voice Roaming (Optional)**

*   In the same menu, you can also turn off **Voice Roaming** if available, to avoid calls on other networks.

***

### ✅ **Manual Network Selection**

1.  Go to **Settings** → **Cellular** → **Network Selection**.
2.  Turn **Automatic** OFF.
3.  Choose your home carrier manually.
    *   This prevents the phone from switching to a roaming partner network.

***

### ✅ **Extra Tips**

*   If you want **zero roaming**, you can also **disable Cellular Data completely**:
    **Settings** → **Cellular** → toggle **Cellular Data OFF**.
*   For trips abroad, consider enabling **Airplane Mode** and using **Wi-Fi only**.

(why 4g may not work in Monaco)

## Note on LAN settings

When we replicate Flint 3 wifi [here](#testing-with-slate-7-as-a-repeater-of-flint-3-wifi-where-flint-3-connected-to-fiber-and-where-slate-7-is-running-a-wireguard-client-to-a-proton-vpn-wireguard-server).


**We encountered a LAN conflict because both routers were using the same IP settings:**

*   **IP Address:** `192.168.8.1`
*   **Subnet Mask:** `255.255.255.0`
*   **Default DHCP Range:** `192.168.8.100 – 192.168.8.249`

To resolve this, I changed the **Slate 7** router configuration to:

*   **IP Address:** `172.16.0.1`
*   **Subnet Mask:** `255.255.255.0`
*   **Default DHCP Range:** `172.16.0.100 – 172.16.0.249`

If I increase the subnet mask, the DHCP range remains the same by default.  
However, with a **255.255.255.0** mask, the maximum usable IP in this subnet is `172.16.0.254` (not `172.16.255.254`, which would require a /16 so (`255.255.0.0`)mask).

See http://172.16.0.1/#/lanip

## Note on first time setup

On flint3 I used the first time the password printed on the router via https://docs.gl-inet.com/router/en/4/user_guide/gl-be9300/
<!-- and mac kept it --> and then setup a new wifi. On slate 7 we have the screen. <!-- stop here -->

<-- all above ccl and this doc is concluded OK DONE CCL -->
<!-- all flint3 router and external access ccl DONE, reccl post xmas OK DONE CONFIRMED-->

<!-- qobuzDL details to document is independent and not mandatory, and link made,
branchement router independent and will be done as planned-->