# Use-case: Access Netflix on an Android TV via Slate 7 (sharing the iPhone connection)

**Goal**: Watch Netflix on the LG Android TV while on holiday, by sharing the iPhone's 4G connection through the Slate 7 router.

## Main method: Share the iPhone 4G connection over Wi-Fi

1. Enable **Personal Hotspot** on the iPhone (*Partage de connexion*).
2. Connect the iPhone to the `scoulomb` Wi-Fi network to reach the router admin page.
3. Open the router admin page at http://192.168.8.1
4. On the GL.iNet (Slate 7), create a **guest network (5 GHz)** and set its internet source to **Repeater** on the iPhone's shared hotspot (first step).
5. This looks like a loop, but the hotspot actually uses the iPhone's **4G** connection, not the Wi-Fi, so it works.
6. Connect the LG TV to the **guest network**.

## Alternative 1: USB tethering

Use a **USB (tethering)** connection from the iPhone to the router instead of Wi-Fi repeater mode.

See [router mode](./6-router-mode.md)

## Alternative 2: Wired TV

Plug the TV into the Slate 7 with an **ethernet cable** instead of connecting over Wi-Fi.

<!-- alternative not tested but assume working, STOP THERE and do not track, and do not do it this summer 26, if contradict eventually update -->

## Disconnecting Netflix from a device

- Go to **Profile → Account → Settings/Support**, or
- Use **"Sign out of all devices"** from the Netflix account settings.


## This also open access to VPN 

See https://github.com/scoulomb/private_script/blob/main/Links-mig-auto-cloud/2025-consolidation/Dojos/VPN-Dojo/VPN-dojo.md <-- no xref ok -->
And could mnake belibe netflix connection from home (aw we did there https://github.com/scoulomb/home-assistant/blob/main/appendices/VPN.md), same from company (VPN sandwich)etc.....


## This setup also opens access to a VPN

Because the Slate 7 is acting as a full router in front of the TV, the same setup lets us route traffic through a VPN. See the [VPN Dojo](https://github.com/scoulomb/private_script/blob/main/Links-mig-auto-cloud/2025-consolidation/Dojos/VPN-Dojo/VPN-dojo.md) for the details.

This means we can make Netflix (and other services) believe the connection originates from a different location:
- From VPN server (managed)
- **From home** (self-hosted/local)<!-- see terminology at /learn/AI/Nvidia-self-hosted-local-managed-ai/self-hosted-local-managed-ai-concept.md -->: route through the home VPN server, as we did similarly [here](https://github.com/scoulomb/home-assistant/blob/main/appendices/VPN.md).


Same would be true from company (VPN sandwich)



## GL.iNet also integrates Tor on top pf VPN

GL.iNet routers (including the Slate 7) ship with a built-in **Tor** mode that routes the router's traffic through the Tor network, alongside the VPN options.

### VPN vs Tor

| Aspect | VPN | Tor |
|--------|-----|-----|
| **Routing** | Single hop to a server you pick | 3 random relays (entry → middle → exit) |
| **Who sees your IP** | The VPN operator | The entry (guard) relay only |
| **Exit location** | Fixed, you choose it | Random, changes often |
| **Trust** | One operator (can log you) | Split across 3 relays; none sees both ends |
| **Speed** | Fast (one hop) | Slow (three volunteer hops) |
| **Best for** | Streaming, geo-spoofing, everyday privacy | Anonymous browsing, censorship circumvention |

Key point: a VPN lets you **choose** the apparent country and is fast enough for streaming; Tor gives stronger anonymity but a **random** exit, and most streaming services block known Tor exits.

### Is Tor the dark web?

No — a common confusion. Tor is two things:

- **The Tor network/browser**: a way to reach the **normal public internet** (google.com, etc.) anonymously. This is what GL.iNet Tor mode does. Legal, used by journalists and activists.
- **Onion services (`.onion` sites)**: hidden sites reachable only through Tor — what people call the **"dark web"** (some legitimate, some illegal).

Using Tor does **not** put you on the dark web. It just hides your origin while you browse the ordinary web. You only reach `.onion` sites if you deliberately type one in.

### Can I open `.onion` sites in Tor mode?

Yes. In Tor mode all traffic goes through Tor, which resolves `.onion` addresses, so any browser on any device behind the router can open one — no dedicated Tor Browser needed. Notes:

- In **normal mode** `.onion` addresses don't resolve at all; Tor mode is what makes them reachable.
- Tor mode doesn't take you to the dark web on its own — you'd have to deliberately enter a `.onion` address yourself. Regular browsing keeps working, just anonymized and slower.
- Router Tor hides your **IP only**. It does **not** strip browser fingerprinting, cookies, or scripts. For sensitive sites, use **Tor Browser** as the client.

### Tor network vs Tor client

"Tor" is the shared **network** (volunteer relays, same for everyone) plus a **client** that puts your traffic onto it:

| | What it routes | What it hardens |
|---|---|---|
| **Tor Browser** | Only that browser's traffic | IP **and** browser fingerprint |
| **GL.iNet Tor mode** | Every device on the router | IP only |

Both reach the same network and can open `.onion` sites. The difference is **scope** (one app vs whole network) and **depth** (Tor Browser also disguises the browser).

### Don't stack them: Tor-over-Tor (avoid)

Running Tor Browser **while** the router is in Tor mode doesn't cooperate — it nests two 3-hop circuits (~6 hops). The Tor Project discourages this: slower, redundant, and can make traffic correlation *easier*, not harder.

**Rule of thumb:**

- Using **Tor Browser** → turn the router's Tor mode **OFF** (normal/VPN). The browser handles Tor.
- Using **router Tor mode** → reserve it for devices that can't run their own Tor client (smart TV, phone apps) to at least hide their IP.
- Never run both on the same traffic.

### Practical takeaway

For the Netflix use-case, use the **VPN** (appear from home or the company). Reserve **Tor** for anonymous browsing or censorship bypass, not streaming — and remember Tor mode just anonymizes normal traffic, it does not expose you to the dark web



<!-- on my side never activated tor and thus entered a.onion address /TOC-->
<!-- reorga of repo is tracked independenly in PERSO TODO and unrelated, and this doc and folder is concluded -->

<!-- OK CCL DONE -- DO NOT TRACK OK DONE CONFIRMED -->