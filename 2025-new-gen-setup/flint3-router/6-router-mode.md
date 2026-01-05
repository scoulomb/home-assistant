# GL.iNet Router Configuration - Complete Guide

Based on your GL.iNet router's two configuration pages:
- **Internet settings**: http://192.168.8.1/#/internet
- **Network Mode settings**: http://192.168.8.1/#/bridge

## Part 1: Internet Connection Options (How Router Gets Internet)

Found at: http://192.168.8.1/#/internet

These determine **your internet source**:

### Ethernet 1/2
- Router receives internet through physical ethernet cable
- Cable connects from modem or upstream router to GL.iNet's WAN/ethernet port
- Most common and stable connection method

### Repeater
- Router connects **wirelessly** to another Wi-Fi network as a client
- Uses that wireless connection as its internet source
- Your GL.iNet then creates its own separate network (different SSID by default)
- Useful when ethernet cable isn't available

### Tethering
- Router gets internet from USB-connected smartphone
- Uses your phone's mobile data connection
- Good for temporary internet or travel situations

### vCellular
- Router uses virtual cellular connection
- Requires USB modem or built-in cellular module
- Provides LTE/mobile data connectivity

As described in [section 5](5-other-test-on-vpn-with-slate-7.md#note-on-repeater-and-other-options)

## Part 2: Network Mode Options (How Router Functions)

Found at: http://192.168.8.1/#/bridge

These determine **your router's role** in the network:

### Router Mode (Default)
**What it does**:
- Creates separate network with its own subnet (typically 192.168.8.x)
- Full NAT, firewall, and DHCP server enabled
- Devices behind it are isolated from upstream network

**Network structure**:
```
Internet → ISP Router (192.168.1.x) → GL.iNet (192.168.8.x) → Your devices
          [Network A]                  [Network B - separate]
```

**GL.iNet features available**: ✅ ALL
- VPN (WireGuard, OpenVPN)
- AdGuard Home / DNS filtering
- Firewall rules
- Guest network isolation
- Traffic monitoring
- Port forwarding

**Pros**:
- Full access to all GL.iNet advanced features
- Additional security layer
- Can create isolated guest networks
- Easy VPN setup for all connected devices

**Cons**:
- Double NAT (can cause issues with some apps/games)
- More complex network architecture
- May need port forwarding on both routers

**Best for**: Users who want VPN, AdGuard, or other advanced GL.iNet features

### Access Point Mode
**What it does**:
- Disables routing (no NAT, no firewall, no DHCP)
- Acts as simple Wi-Fi broadcaster
- All devices appear on same network as upstream router
- Requires **wired ethernet connection** to upstream router

**Network structure**:
```
Internet → ISP Router (192.168.1.x) → GL.iNet (AP) → Your devices (192.168.1.x)
          [Single unified network - all devices on same subnet]
```

**GL.iNet features available**: ❌ MOST DISABLED
- ❌ VPN (WireGuard, OpenVPN)
- ❌ AdGuard Home / DNS filtering
- ❌ Firewall rules
- ❌ Guest network isolation
- ❌ Traffic monitoring/QoS
- ✅ Wi-Fi broadcasting
- ✅ Basic admin interface

**Pros**:
- No double NAT issues
- Simple network management (one DHCP server, one firewall)
- Easy device communication across network
- Better for port forwarding (single layer)

**Cons**:
- Lose all advanced GL.iNet features
- No additional security layer
- Cannot isolate devices

**Best for**: Simple Wi-Fi extension when you don't need advanced features

### Extender Mode

**What it does**:
- Connects wirelessly to existing Wi-Fi network (like Repeater for internet source)
- Rebroadcasts with **same SSID** to create seamless extended network
- Optimized for network extension with better roaming/handoff
- Likely disables NAT/routing (acts like Access Point but wireless)

**Comparison**:
- **Extender**: Automatically copies SSID, optimized for seamless extension
- **Repeater (internet) + manual same SSID**: Similar result but less optimized
- **Extender** is purpose-built for extending networks

**Best for**: Extending existing Wi-Fi coverage with seamless roaming

See comment [section 5](./5-other-test-on-vpn-with-slate-7.md#repeater-mode-vs-mesh-vs-same-ssid)

### WDS (Wireless Distribution System)
**What it does**:
- Creates wireless bridge between routers using MAC addresses
- True Layer 2 bridge - all devices on same network
- Both routers must support WDS and be configured together

**Technical details**:
- **MAC-based authentication**: Enter MAC addresses of partner routers
- **Same channel required**: All WDS nodes must use identical wireless channel
- **Compatibility dependent**: Not all routers work together, even with WDS support
- **Security**: Supports WPA2/WPA, but older implementations may be limited
- **Bandwidth cost**: Each wireless hop reduces bandwidth by ~50%

**Configuration steps**:
1. Set both routers to same channel (critical!)
2. Enter MAC addresses of partner routers on each device
3. Use same SSID and encryption settings
4. Disable DHCP on secondary routers (only one DHCP server needed)

**WDS vs others**:
- **vs Extender**: More efficient but requires compatible hardware
- **vs Repeater**: All routers act as equals, one unified network
- **vs Access Point**: Wireless connection instead of wired

**Best for**: 
- Connecting multiple buildings without cables
- Advanced users with compatible hardware
- When you need better performance than simple repeater

**Not recommended for**: Most home users (Extender mode is simpler and more reliable)

## Part 3: Key Concepts Clarified

### Internet Source vs Network Mode
- **Internet options** = Where internet comes from (Ethernet, Repeater, Tethering, vCellular)
- **Network modes** = How router functions (Router, AP, Extender, WDS)
- You can **combine them**: e.g., Ethernet internet + Access Point mode

### Repeater vs Extender
- **Repeater** (internet source): Gets internet wirelessly, creates different SSID
- **Extender** (network mode): Rebroadcasts with same SSID for seamless coverage
- **Manual workaround**: Repeater + manually matching SSID ≈ Extender (but less optimized)

### Access Point vs Bridge
- **Bridge**: General networking concept - connects two network segments
- **Access Point**: Specific type of bridge (wired-to-wireless bridge)
- WDS and Extender are also types of bridges (wireless-to-wireless)

## Part 4: Avoiding Double NAT - Configuration Combinations

When using ISP router + GL.iNet, you need to configure **both devices**. Your ISP router typically has these modes:

**ISP Router Modes**:
- **Bridge Mode**: ISP router becomes "dumb" modem, passes public IP to GL.iNet
  - Not supported by Bouygues
- **DMZ Mode**: ISP router forwards ALL incoming traffic to GL.iNet
- **Router Mode** (default) / Double NAT : Normal operation, creates double NAT when combined with GL.iNet in Router Mode

See [Appendices](./appendices/appendix-of-change-isp-appendix-double-nat-bridge-and-dmz.md)
---

### ⭐ Configuration 1: ISP Bridge Mode + GL.iNet Router Mode  (not supported by Btel)
**ISP Router**: Bridge Mode  
**GL.iNet**: Router Mode (http://192.168.8.1/#/bridge)

**How to set up**:
1. Enable Bridge Mode on ISP router
2. Keep GL.iNet in Router Mode (default)
3. Connect ISP router to GL.iNet's WAN port via ethernet

**Result**:
- GL.iNet gets public IP directly
- Single NAT layer (only GL.iNet does NAT)
- ISP router acts as simple modem

**GL.iNet features**: ✅ ALL (VPN, AdGuard, firewall, etc.)

**Network structure**:
```
Internet → ISP Router (Bridge/Modem) → GL.iNet (Router) → Your devices
          [No routing]                  [Single NAT layer]
```

**Pros**:
- Cleanest setup, single NAT
- Full GL.iNet functionality
- GL.iNet is your true router
- Best performance

**Cons**:
- Lose ISP router's Wi-Fi and routing features
- May lose ISP tech support (some ISPs don't support bridge mode)
- Some ISP routers don't support bridge mode

**Best for**: Power users who want GL.iNet as their main router with full features

---

### ⭐ Configuration 2: ISP DMZ Mode + GL.iNet Router Mode (RECOMMENDED)

**ISP Router**: DMZ pointing to GL.iNet  
**GL.iNet**: Router Mode (http://192.168.8.1/#/bridge)

**How to set up**:
1. Connect GL.iNet to ISP router via ethernet
2. Note GL.iNet's WAN IP (e.g., 192.168.1.100)
3. Configure DMZ on ISP router to point to that IP
4. Optional but recommended: Set static IP/DHCP reservation for GL.iNet on ISP router
5. Keep GL.iNet in Router Mode

**Result**:
- Technical double NAT exists, but DMZ makes it transparent
- All incoming traffic goes to GL.iNet
- Works like single NAT for most purposes

**GL.iNet features**: ✅ ALL (VPN, AdGuard, firewall, etc.)

**Network structure**:
```
Internet → ISP Router (DMZ enabled) → GL.iNet (Router) → Your devices
          [Routes but forwards all to GL.iNet] [Full routing]
```

**Pros**:
- Keep all GL.iNet features
- Keep ISP router's Wi-Fi (can use both)
- No double NAT issues for most applications
- Easiest option that keeps full functionality

**Cons**:
- Still technically double NAT (though mostly transparent)
- GL.iNet is "exposed" to internet (but has its own firewall)

**Best for**: Most users who want GL.iNet's VPN/advanced features without losing ISP router functionality

---

### Configuration 3: ISP Router Mode + GL.iNet Access Point Mode

**ISP Router**: Normal Router Mode  
**GL.iNet**: Access Point Mode (http://192.168.8.1/#/bridge)

**How to set up**:
1. Connect GL.iNet to ISP router via ethernet
2. Set GL.iNet to Access Point Mode
3. Configure Wi-Fi settings on GL.iNet

**Result**:
- Single unified network
- GL.iNet is just a Wi-Fi access point
- ISP router handles all routing

**GL.iNet features**: ❌ DISABLED (no VPN, AdGuard, firewall)

**Network structure**:
```
Internet → ISP Router (full routing) → GL.iNet (AP only) → Your devices
          [Single network - all devices on ISP router's subnet]
```

**Pros**:
- Simple, clean network
- No NAT issues at all
- Easy management (single network)

**Cons**:
- Lose ALL GL.iNet advanced features
- GL.iNet becomes generic access point

**Best for**: Users who only need Wi-Fi coverage extension, don't care about GL.iNet features

---

### Configuration 4: ISP Router Mode + GL.iNet Router Mode (Accept Double NAT)

**ISP Router**: Normal Router Mode  
**GL.iNet**: Router Mode (http://192.168.8.1/#/bridge)

**How to set up**:
1. Connect GL.iNet to ISP router via ethernet
2. Keep both in Router Mode
3. Do nothing special

**Result**:
- True double NAT
- Two separate networks

**GL.iNet features**: ✅ ALL (VPN, AdGuard, firewall, etc.)

**Network structure**:
```
Internet → ISP Router (192.168.1.x) → GL.iNet (192.168.8.x) → Your devices
          [NAT layer 1]                [NAT layer 2]
```

**Pros**:
- Simplest setup - no configuration needed
- Keep all GL.iNet features
- Keep both routers' Wi-Fi networks
- Works fine for most users

**Cons**:
- Double NAT can cause issues with:
  - Some online games
  - P2P applications
  - Hosting servers
  - UPnP functionality
  - VoIP/video calls (sometimes)
- Need port forwarding on both routers if hosting services

**Best for**: Users who don't have double NAT issues and want simplest setup

---

### ⚠️ Configuration 5: ISP Bridge Mode + GL.iNet Access Point Mode
**ISP Router**: Bridge Mode  
**GL.iNet**: Access Point Mode

**Result**: ❌ **This configuration doesn't work!**   (and bridge not supported by Btel)

**Why**: If ISP router is in bridge mode (just a modem), and GL.iNet is in Access Point mode (expects upstream router), there's no router to handle NAT/DHCP. Your network won't function.

**Don't use this combination!**

---

## Part 5: Quick Decision Matrix

| Your Priority | ISP Router Setting | GL.iNet Setting | Features | NAT Issues |
|---------------|-------------------|-----------------|----------|------------|
| **Full GL.iNet features + cleanest setup** | Bridge Mode | Router Mode | ✅ All | None |
| **Full GL.iNet features + keep ISP router** | DMZ Mode | Router Mode | ✅ All | Minimal |
| **Just need Wi-Fi extension** | Router Mode | Access Point | ❌ None | None |
| **Simplest setup, features work** | Router Mode | Router Mode | ✅ All | Yes (minor) |

---

## Part 6: Recommended Configurations by Use Case

### 🎯 You want VPN on all devices + best performance
→ **ISP Bridge Mode + GL.iNet Router Mode**
- ISP router becomes modem only
- GL.iNet is your main router with full features
- Single NAT, cleanest setup

### 🎯 You want VPN + keep ISP router Wi-Fi working
→ **ISP DMZ Mode + GL.iNet Router Mode** ⭐ RECOMMENDED
- Both routers operational
- No double NAT problems
- All GL.iNet features work
- Best balance of features and simplicity

### 🎯 You only need better Wi-Fi coverage
→ **ISP Router Mode + GL.iNet Access Point Mode**
- GL.iNet extends Wi-Fi only
- Single clean network
- Don't need GL.iNet advanced features

### 🎯 You're not sure / want simplest setup
→ **ISP Router Mode + GL.iNet Router Mode (Double NAT)**
- Default configuration
- Try this first
- If you encounter issues, switch to DMZ or Bridge

### 🎯 You need to extend existing Wi-Fi coverage
→ **ISP Router Mode + GL.iNet Extender Mode**
- Seamless Wi-Fi roaming with same SSID
- No ethernet cable needed
- Good for extending coverage wirelessly

---

## Part 7: Step-by-Step Setup Guide (DMZ Method - Recommended)

This is the sweet spot for most users who want full GL.iNet features:

### On ISP Router:
1. Access ISP router admin panel (usually http://192.168.1.1)
2. Find DMZ settings (often under "Advanced", "Firewall", or "Security")
3. Connect GL.iNet via ethernet and let it boot up
4. Find GL.iNet's WAN IP in ISP router's connected devices list (e.g., 192.168.1.100)
5. Enable DMZ and enter GL.iNet's IP address
6. **Optional but recommended**: Create DHCP reservation for GL.iNet so IP doesn't change
7. Save settings and reboot ISP router if required

### On GL.iNet (http://192.168.8.1/#/bridge):
1. Verify it's in Router Mode (default setting)
2. Go to http://192.168.8.1/#/internet and confirm ethernet connection
3. Configure VPN, AdGuard, or other features as desired
4. Connect your devices to GL.iNet's Wi-Fi network

### Verification:
- Test that internet works on devices connected to GL.iNet
- Test VPN connection if configured
- Check if port forwarding works (if needed) by only configuring it on GL.iNet

**Result**: Full GL.iNet functionality without double NAT headaches!

---

## Part 8: Complete Feature Comparison Table

| Feature/Mode | Router Mode | Access Point | Extender | WDS |
|--------------|-------------|--------------|----------|-----|
| **Internet via** | Ethernet/Repeater/Tethering/vCellular | Wired ethernet only | Wireless | Wireless |
| **VPN (WireGuard/OpenVPN)** | ✅ Yes | ❌ No | ❌ No | ⚠️ Limited |
| **AdGuard Home** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Firewall** | ✅ Yes | ❌ No | ❌ No | ⚠️ Limited |
| **Guest Network** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Traffic Monitoring** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Creates Separate Network** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **NAT** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **DHCP Server** | ✅ Yes | ❌ No | ❌ No | Only one needed |
| **Same SSID as Upstream** | Can configure | N/A | ✅ Automatic | ✅ Yes |
| **Wireless Backbone** | ❌ No | ❌ No | ✅ Yes | ✅ Yes |
| **Requires Compatible Hardware** | ❌ No | ❌ No | ❌ No | ✅ Yes |
| **Setup Complexity** | Medium | Low | Low | High |
| **Best for** | Full features | Simple Wi-Fi | Coverage extension | Multi-building |

---

## Part 9: Troubleshooting Common Scenarios

### Scenario 1: "I need VPN but have double NAT issues"
**Solution**: Configure DMZ on ISP router pointing to GL.iNet
- Keeps all GL.iNet features
- Eliminates double NAT problems

### Scenario 2: "I just want better Wi-Fi, don't care about VPN"
**Solution**: Use GL.iNet in Access Point Mode
- Simple setup
- No double NAT
- Clean single network

### Scenario 3: "I want to use both routers' Wi-Fi networks"
**Solution**: Use DMZ or accept double NAT with both in Router Mode
- Both Wi-Fi networks operational
- DMZ eliminates most double NAT issues

### Scenario 4: "Can't run ethernet cable to GL.iNet"
**Solution**: Use Repeater (internet source) + Router Mode
- GL.iNet gets internet wirelessly
- Keeps all features
- Or use Extender Mode for seamless coverage

### Scenario 5: "Gaming/P2P not working properly"
**Solutions in order of preference**:
1. Enable DMZ on ISP router pointing to GL.iNet
2. Put ISP router in Bridge Mode
3. Configure port forwarding on both routers (last resort)

### Scenario 6: "Need to connect two buildings wirelessly"
**Solution**: Use WDS if both routers support it
- Otherwise use Extender Mode (simpler but may be less efficient)

---

## Part 10: Final Recommendations

### For Most Home Users:
**Use ISP DMZ Mode + GL.iNet Router Mode**
- Perfect balance of features and simplicity
- All GL.iNet features work
- Minimal configuration needed
- No double NAT issues

### For Power Users:
**Use ISP Bridge Mode + GL.iNet Router Mode**  (not suppored btel)
- GL.iNet becomes your main router
- Cleanest network architecture
- Maximum performance

### For Simple Wi-Fi Extension:
**Use ISP Router Mode + GL.iNet Access Point Mode**
- Don't need GL.iNet features
- Just want better coverage
- Simplest management

### When In Doubt:
**Start with Double NAT (both in Router Mode)**
- Try it first - it often works fine
- If you encounter issues, upgrade to DMZ
- If still issues, consider Bridge Mode

---

## Summary

The key insight is that you're configuring **two independent settings**:
1. **Where GL.iNet gets internet** (http://192.168.8.1/#/internet)
2. **How GL.iNet functions** (http://192.168.8.1/#/bridge)

And when using an ISP router, you also configure:
3. **How ISP router treats GL.iNet** (Bridge/DMZ/Normal)

**The golden rule**: If you bought GL.iNet for its VPN or advanced features, keep it in **Router Mode** and use **DMZ on your ISP router**. This gives you the best of both worlds with minimal hassle.



## What we did

In section [2](./2-Flint3-router-setup-BYTEL.md);

- Here: No ISP router and Flint3 Ethernet (connection option)/router mode (network mode)
  - 1: Setup Flint 3 connected with XGS-PON directly and thus bypassing the BBOX
  - 2: Same with NETWORK ACCELERATION DISABLED 

- Here nothing todo
  - 4: WIFI BBOX EN DIRECT ET XGS-PON interne
  - 5: TEST WIFI BBOX EN DIRECT ET XGS-PON externr
                                                                                                                                         
- Here: ISP router (DMZ mode or router mode ie. double NAT (actually did not configure it for test)) and Flint3 Ethernet (connection option)/router mode (network mode)   
  - 6:TEST WIFI FLINT3 (wire 2.5g flint 3 original, and 1G port of BBOX) to BBOX to XGS-PON externe (via 10G and ugreen cat8 ethernet wire)
  - 3: FLINT 3 WIFI CONNECTED TO BBOX and bbox internal XGS-PON   
                                                                                                  

- Here SLATE 7 repeater mode (connection) and router (network mode)
  - [section 5](./5-other-test-on-vpn-with-slate-7.md#connect-slate-7-to-wireguard-vpn-server-on-flint-3-with-iphone-hotspot)
