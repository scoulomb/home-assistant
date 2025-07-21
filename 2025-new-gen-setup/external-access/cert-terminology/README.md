# Certificate and F5 terminology 

 
## Simplified terminology 

Good terminology here: https://securityboulevard.com/2024/04/what-is-certificate-provisioning/
> Certificate provisioning refers to the process of obtaining, deploying, and managing digital certificates within an organization’s IT infrastructure. 


## Certificate enrollment and full process

From https://www.encryptionconsulting.com/education-center/what-is-certificate-enrollment-and-how-is-it-used/ 

Certificate Enrollment is the process by which an entity, such as an individual or an organization, requests and obtains a digital certificate from a Certificate Authority (CA). 
Digital certificates are used to secure communications and authenticate the identity of a server, client, or user in various secure protocols like SSL/TLS (for securing websites), S/MIME (for email encryption and signing), and more.

The primary purpose of certificate enrollment is to obtain a digital certificate that contains a public key and associated identity information (such as the Common Name, Organization, etc.).
The CA signs the certificate, establishing a trusted relationship between the public key and the entity’s identity. 
This process ensures that the entity’s identity is validated and that the public key can be used securely for encryption, digital signing, or other cryptographic operations.

The Comprehensive Lifecycle of Certificate Enrollment (IMO installation, use and renewal could be considered out of enrollment, procurement can be used as synonym of enrollment )

### Generating Certificate Signing Request (CSR)

To initiate the certificate enrollment process, the entity generates a **Certificate Signing Request (CSR)**. The CSR includes:
- The **public key**
- Information about the entity, such as:
  - Domain name (for SSL/TLS certificates)
  - Email address (for S/MIME certificates)

### Submitting the CSR to the CA

The CSR is submitted to the **Certificate Authority (CA)** during the enrollment process. The CA verifies:
- The identity of the entity
- The information in the CSR

Verification methods may include:
- Email verification
- Domain validation  
- Manual verification of legal documents

=> Perso notes: domain validation includes: Add via DNS-01, HTTP-01, and TLS-ALPN-01: https://letsencrypt.org/fr/docs/challenge-types/
=> Here is DigiCert process: https://www.digicert.com/faq/public-trust-and-certificates/how-do-i-order-a-tls-ssl-certificate

### Certificate Issuance

Once the CA completes verification and confirms the entity’s legitimacy, it issues a **digital certificate** containing:
- The entity’s public key
- Identity information
- Validity period
- The CA’s digital signature

### Certificate Delivery

The issued certificate is delivered back to the entity. Delivery methods may include:
- Email
- Secure portal
- Other secure channels

### Certificate Installation
The entity installs the certificate on the appropriate server or device.  
For example, in SSL/TLS, the certificate is installed on the **web server** to secure website connections.

=> This can be done via Venafi which push certificate to F5 cluster<!--Test/Prod + internet/extranet -->.

### Certificate Use

Once installed, the certificate enables **secure communication protocols**.  
Clients and users can verify the certificate’s authenticity via the CA’s digital signature, ensuring a **secure and trustworthy connection**.

### Certificate Renewal

Certificates have a limited validity period (typically **1–2 years**).  
Before expiration, the entity must **renew the certificate** through a similar enrollment process to avoid service disruption.


<!-- => New+Inbound+Links+creation --> 

![](./cert-lifecycle-mgmt.png)


## SSL offloading means this

https://www.f5.com/fr_fr/glossary/ssl-offloading

> Le déchargement SSL est le processus de suppression du cryptage SSL du trafic entrant pour soulager un serveur Web de la charge de traitement du décryptage et/ou du cryptage du trafic envoyé via SSL. Le traitement est déchargé sur un périphérique distinct conçu spécifiquement pour l'accélération SSL ou la terminaison SSL .
La terminaison SSL est particulièrement utile lorsqu'elle est utilisée avec des clusters de VPN SSL , car elle augmente considérablement le nombre de connexions qu'un cluster peut gérer.

And not to deploy cert on the F5

## We can find same steps referenced in my TLS doc with CA 

- signature of CSR by user + signature of cert by CA
- See https://github.com/scoulomb/misc-notes/blob/master/tls/tls-certificate.md#man-in-the-middle-attach-and-need-of-a-ca

## self-signed and signed

Also in myDNS

<!-- link to Case, 17jul25 and more precise -->
- Generate a self-signed certificate: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-g.md#step-1-how-to-generate-a-self-signed-certificate
- Generate a certificate signed by a public CA: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-h.md#step-1-how-to-generate-a-certificate-signed-by-ca
  - Quoting
    - > - Without shell access (they support different hosting providers, it is equivalent to shell access server validation). Github page falls into that [category](https://community.letsencrypt.org/t/web-hosting-who-support-lets-encrypt/6920).
          It relies on the fact DNS (own or Gandi live DNS) is pointing to server. {add: at least of github so server validation}
    - > With shell access: https://certbot.eff.org/lets-encrypt/ubuntufocal-other where we have
        > - Server validation (standalone or not). 
        > - TXT record validation.   
    - Note here from https://letsencrypt.org/fr/docs/challenge-types/,
      - Server validation: `HTTP-01` (port 80), `TLS-ALPN-01` (port 443), `TLS-SNI-01` (deprecated, port 443)
      - DNS validationn (TXT record): `DNS-01`
    - Here showed how to deploy this cert on Python server(via double nat directly at the [cf external access README](../README.md) or to an Ingress k8s (with double NAT). Ingres is equivalent to our nginx proxy manager.
    - See also https://certbot.eff.org, the webserver validation
    - We can generate a CSR manually: https://phoenixnap.com/kb/generate-openssl-certificate-signing-request (instead of cert bot))
  - Self-signed vs signed?:
    - From: https://medium.com/@talyitzhak/understanding-digital-certificates-and-self-signed-certificates-b1cdca759bbc
    - >   A self-signed certificate is a certificate that is signed by the same entity whose identity it certifies. Unlike certificates issued by a CA, self-signed certificates are not inherently trusted by other systems and require manual configuration to be trusted. They are often used in development and testing environments where setting up a CA is not necessary. “Self-signed” means that the public key embedded in the certificate validates the signature on the certificate.
    - So here is the key https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-part-g-use-certificates/appa.prd.coulombel.it.key used for CSR and CA...

We can also sign a JWT with private key: https://github.com/scoulomb/misc-notes/blob/af5d6dd89ad1f59af2f82883a3fdc5b3719ca41f/tls/oauth-appendix.md?plain=1#L11 
<!-- but not found here as in case https://github.com/scoulomb/myDNS/blob/main/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-h.md#L738 -->

<!-- priv script mtls etc stop -->