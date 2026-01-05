# **Double NAT**, **Bridge Mode**, and **DMZ Mode**

Here’s a clear comparison between **Double NAT**, **Bridge Mode**, and **DMZ Mode** in the context of internet boxes or routers:

---

### 🔁 **Bridge Mode**
- **Function**: Disables the router’s NAT and routing features.
- **Purpose**: Passes the public IP directly to another device (usually a more advanced router).
- **Use Case**: When you want your own router to manage the network.
- **Pros**:
  - Avoids double NAT issues.
  - Simplifies network setup with third-party routers.
- **Cons**:
  - Disables Wi-Fi and firewall features on the internet box.

Nothing to do with bridge in [appendix-TLS-decryption.md](../../../../notes-temp/Links-mig-auto-cloud/2025-consolidation/Dojos/VPN-Dojo/appendix-TLS-decryption.md#parallel-with-customer-inbound-links-customer-to-vip)
<-- also in bottom of [cert chain issue](../../../../notes-temp/Links-mig-auto-cloud/2025-consolidation/deep-dive-F5-bigip/F5-certificate-chain-issue.md)
-->


---

### 🌐 **DMZ Mode (Demilitarised Zone)**
- **Function**: Forwards all incoming traffic to one specific device on the local network.
- **Purpose**: Exposes that device to the internet with minimal firewall protection.
- **Use Case**: Gaming consoles, servers, or devices needing unrestricted access.
- **Pros**:
  - Easier troubleshooting for connectivity issues.
  - Full access for services that struggle behind NAT/firewalls.
- **Cons**:
  - Security risk: the DMZ device is vulnerable to external threats.

---

### 🔄 **Double NAT (Network Address Translation)**
- **Function**: Occurs when two routers are performing NAT (e.g., ISP router + personal router).
- **Purpose**: Unintended setup that can cause connectivity issues.
- **Use Case**: Often accidental when using a router behind another router.
- **Pros**:
  - Basic internet access still works.
- **Cons**:
  - Problems with port forwarding, VPNs, and online gaming.
  - Can cause latency and connection instability.

---

### 🧠 Summary Table

| Feature        | Bridge Mode              | DMZ Mode                        | Double NAT                     |
|----------------|---------------------------|----------------------------------|--------------------------------|
| NAT            | Disabled                  | Enabled                         | Enabled (twice)                |
| IP Address     | Public IP to router       | Local IP with all ports open    | Private IP behind two routers  |
| Use Case       | Use own router            | Expose one device               | Accidental or legacy setup     |
| Security       | Safer (if router is secure)| Risky (device exposed)          | Moderate (but complex)         |
| Common Issues  | None                      | Vulnerable device               | Port forwarding, VPN issues    |

See [section 6/4 on router mode](../6-router-mode.md#part-4-avoiding-double-nat---configuration-combinations)