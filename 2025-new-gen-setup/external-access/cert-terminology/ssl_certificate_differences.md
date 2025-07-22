# 🔐 Differences Between SAN, CN, and SNI in SSL/TLS Certificates

> Prompt: Differences between SAN (Subject Alternative Name), Common Name (CN), and SNI (Server Name Indication) in SSL/TLS certificates.

## 1. Common Name (CN)
- **Definition**: The **Common Name** is a field in an SSL certificate that specifies the **primary domain** the certificate is issued for.
- **Example**: If the CN is `www.example.com`, the certificate is valid for that domain.
- **Limitation**: Only one domain can be specified.
- **Modern Usage**: CN is now largely **deprecated** in favor of SAN. Most modern clients rely on SAN for domain validation.

---

## 2. Subject Alternative Name (SAN)
- **Definition**: SAN is an **extension** to the X.509 certificate standard that allows **multiple domain names** (and IPs, emails, URIs) to be protected by a single certificate.
- **Example**:
  - `example.com`
  - `www.example.com`
  - `mail.example.com`
  - `example.net`
- **Use Case**: Essential for **multi-domain** or **wildcard** certificates.
- **Best Practice**: Always use SANs to list all domains/subdomains the certificate should cover.

---

## 3. Server Name Indication (SNI)
- **Definition**: SNI is a **TLS extension** that allows a client (e.g., browser) to indicate the **hostname** it’s trying to connect to during the TLS handshake.
- **Purpose**: Enables servers to present the correct SSL certificate when hosting **multiple domains** on the same IP address.
- **Without SNI**: The server may not know which certificate to present, leading to errors.
- **Support**: All modern browsers support SNI.

---

## 🧩 Summary Table

| Feature | CN (Common Name) | SAN (Subject Alternative Name) | SNI (Server Name Indication) |
|--------|------------------|-------------------------------|------------------------------|
| **Purpose** | Primary domain in certificate | List of all valid domains | Tells server which domain is requested |
| **Location** | Certificate subject field | Certificate extension | TLS handshake (client-side) |
| **Multiple Domains?** | ❌ No | ✅ Yes | ✅ Yes |
| **Required Today?** | ❌ Deprecated | ✅ Yes | ✅ Yes |
| **Used By** | Certificate itself | Certificate itself | Client (e.g., browser) |
