# Remplacer sa Bbox Fibre par un équipement personnel

Bienvenue : Remplacer sa Bbox Fibre par un équipement personnel

## Avant de commencer : Points clés à considérer

Technologie Fibre (GPON vs XGS-PON) : Bouygues utilise principalement la technologie GPON (Gigabit Passive Optical Network), limitée à 2G/1G partagés. Plus récemment, XGS-PON a été déployé via l'option "debit plus" si disponible dans votre zone, permettant des débits symétriques jusqu'à 8G. Attention : Ces deux technologies sont physiquement incompatibles ! Un ONT ou un module SFP conçu pour GPON ne fonctionnera pas sur une ligne XGS-PON, et vice-versa. Il est crucial de choisir un équipement ONT/SFP strictement compatible avec la technologie activée sur votre prise fibre. Conserver l'ONT Bouygues est le moyen le plus sûr d'éviter cette complexité si vous n'êtes pas certain de votre technologie.
   
Le matériel requis : Vous aurez besoin d'un routeur compatible et potentiellement d'un module ONT ou SFP tiers si vous ne conservez pas l'ONT fourni (voir point ci-dessus et section ONT). Votre routeur doit au minimum gérer les VLAN. La capacité à gérer le tagging CoS 802.1p est fortement recommandée (voir section configuration). Utilisez la recherche pour trouver un tutoriel sur le modèle de routeur que vous souhaiteriez utiliser, car de nombreux membres postent leur configuration à jour.
   
Compétences techniques : Remplacer la Bbox demande une certaine aisance avec la configuration réseau (VLAN, DHCP, QoS, Pare-feu, MAC Cloning, API Bbox, configuration ONT/SFP, etc.). Ce n'est pas une opération "plug and play".
   
Obtention des identifiants : Pour la téléphonie VoIP, Bouygues Telecom ne fournit pas les identifiants SIP nécessaires. Pour le remplacement d'ONT/SFP, l'obtention du Numéro de Série (SN/SLID) peut nécessiter une manipulation spécifique.

# 1. L'ONT (Optical Network Terminal) / Module SFP

L'équipement ONT/SFP convertit le signal optique en signal Ethernet. Plusieurs options existent, choisissez en fonction de votre technologie fibre (GPON ou XGS-PON) !
Conserver l'ONT externe fourni par Bouygues : C'est l'option la plus simple et recommandée, car l'ONT fourni sera forcément compatible avec votre ligne. Vous branchez simplement sa sortie Ethernet sur le port WAN de votre routeur personnel. Note : Obtenir un ONT externe séparé de la Bbox lors d'une nouvelle souscription semble de plus en plus difficile voire impossible auprès de Bouygues.
   
Utiliser un ONT externe tiers compatible : Option plus complexe. Vous devez acheter un modèle compatible avec votre technologie (GPON ou XGS-PON) et impérativement le configurer avec :
       
Le Numéro de Série PON (SN ou SLID) de votre connexion Bbox.
       
Le Mot de passe PLOAM (parfois appelé Registration ID).
       
Exemple GPON 2.5GbE : Le Telekom Glasfaser Modem 2 a été testé avec succès par certains utilisateurs.
   
Utiliser un module SFP ONT tiers : Pour les routeurs équipés d'un port SFP (GPON) ou SFP+ (GPON/XGS-PON). Vous devez acheter un module compatible avec votre technologie fibre (GPON ou XGS-PON) et le configurer avec les mêmes identifiants que pour un ONT externe (SN/SLID et PLOAM/Registration ID).
       
Attention : Le module SFP fourni PAR BOUYGUES (présent dans certaines Bbox comme l'Ultym Wi-Fi 6E) N'EST PAS un ONT SFP standard ! Il s'agit d'un simple convertisseur optique-électrique qui dépend de la Bbox pour fonctionner. Il ne peut PAS être retiré de la Bbox et inséré dans un routeur personnel pour remplacer un ONT. Si votre Bbox a un SFP intégré, vous devez soit utiliser un ONT externe, soit acheter un module SFP ONT tiers configurable.
       
Exemple Module SFP ONT GPON : Le Huawei MA5671A (modifiable via hack-gpon) est un choix populaire. En XGS-PON voir pon.wiki pour des modèles comme le WAS-110).
       
Obtenir le SN/SLID : Si vous avez une Bbox avec SFP intégré (et que vous voulez acheter un ONT/SFP tiers), le SN/SLID n'est pas visible dans l'interface web standard. Il faut souvent le récupérer en accédant (depuis votre réseau local) à l'API de la box via l'URL : `https://mabbox.bytel.fr/api/v1/wan/sfp` (authentification admin requise). Voir [ce fil de discussion La Fibre Info](https://lafibre.info/remplacer-bbox/bbox-ultym-pas-de-sn-sfp-dans-linterface/) pour plus de détails. Sur les Bbox avec ONT externe, il peut être dans l'interface d'administration section "Fibre" ou parfois sur l'étiquette de l'ONT.
       
Obtenir le PLOAM Registration ID : Ce n'est pas le mot de passe PLOAM direct. Il est dérivé de l'IMEI de la box (visible sur l'étiquette ou dans l'interface web section "Modèle") auquel on préfixe `00000` (exemple '00000XXXXXXXXXXXXXXX') en GPON et prefix `00000` ET suffixe `1` (exemple '00000XXXXXXXXXXXXXXX1111111111111111111111111111111111111111111111111111') en XGS-PON

# 2. Configuration du routeur : Les paramètres essentiels

C'est le cœur de l'opération. Votre routeur doit impérativement supporter :
Le tagging VLAN sur l'interface WAN.
   
(Fortement recommandé) Le tagging 802.1p (CoS - Class of Service / QoS Priority) sur l'interface WAN. Voir détails plus bas.
Voici les paramètres généralement constatés :

Interface WAN :
Tag VLAN : 100
   
(Recommandé) Cloner l'adresse MAC : Pour accélérer l'obtention d'une adresse IP lors du premier branchement de votre routeur, il est conseillé de configurer l'interface WAN (VLAN 100) de votre routeur avec l'adresse MAC de votre Bbox d'origine. Cela évite d'attendre l'expiration du bail DHCP précédent lié à la Bbox. L'adresse MAC est généralement inscrite sur une étiquette sur la Bbox.
Internet (IPv4) :
Type : Client DHCP
Interface : Port WAN taggué VLAN 100
Option DHCP 60 (Vendor Class ID) : Doit être envoyée avec la valeur `BYGTELIAD` (recommandé pas obligatoire à priori)
   
Tag CoS (802.1p) - Priorité 6 : L'analyse technique du réseau Bouygues montre que la Bbox taggue les requêtes DHCP avec la priorité 6. Il est fortement recommandé de configurer votre routeur pour faire de même. Bien que certains utilisateurs rapportent un fonctionnement sans ce tag, son absence peut entraîner des problèmes d'obtention ou de renouvellement de l'IP, ou une dépriorisation du trafic par le réseau.
Internet (IPv6) :
Type : Client DHCPv6
Interface : Port WAN taggué VLAN 100
Demander la délégation de préfixe (Prefix Delegation - PD). La taille du préfixe délégué est /60.
Tag CoS (802.1p) - Priorité 6 : Idem que pour IPv4, il est fortement recommandé de tagguer les requêtes DHCPv6 avec la priorité 6 pour assurer une bonne communication avec les équipements Bouygues.
Télévision (IPTV) :
Attention edit @mirtouf:De nombreux ONT tiers ne supportent pas le multicast (drop des trames ou crash complet), si certains ont des ONT qui passent le test du multicast pour les flux TV, il serait judicieux d'ajouter cette information en précisant quel était l'ONT/ONU fourni par ByTel..
   
Nécessite un service de proxy/routage multicast : IGMP Proxy (le plus courant) ou potentiellement pimd.
   
Configuration IGMP Proxy :
Interface Upstream (Source) : Port WAN taggué VLAN 100
Interface Downstream (Destination) : Interface(s) LAN où sont connectés les décodeurs TV.
Autoriser les sources multicast Bouygues (peut être nécessaire dans certains cas) : `89.86.96.0/24`, `89.86.97.0/24`, `176.165.8.0/24`, `193.251.97.0/24`. Edit @mirtouf: plus nécessaire pour le replay
   
Le protocole utilisé est généralement IGMPv2.
   
Tag CoS (802.1p) - Priorité 5 : Pour assurer une bonne fluidité des flux TV et une bonne réactivité des changements de chaîne, il est fortement recommandé de tagguer le trafic de contrôle IGMP avec la priorité 5. Les flux multicast entrants arrivent également avec cette priorité et votre routeur devrait idéalement préserver cette priorité vers le LAN. Sans ce tag, des gels d'image ou lenteurs peuvent apparaître.
   
Serveurs DNS pour le décodeur : Il peut être nécessaire de fournir spécifiquement les DNS Bouygues (`194.158.122.10`, `194.158.122.15`) au décodeur TV via une option DHCP sur le LAN.
   
Pare-feu : Assurez-vous que votre pare-feu autorise le trafic IGMP et le trafic multicast UDP depuis les sources Bouygues vers votre LAN.
Téléphonie (VoIP) : Configuration native impossible
La téléphonie fixe chez Bouygues utilise le protocole SIP. Pour la faire fonctionner sur un équipement personnel (routeur, ATA), il faudrait configurer un client SIP avec des identifiants (nom d'utilisateur et mot de passe spécifiques) fournis par l'opérateur.
Le problème majeur et bloquant : Bouygues Telecom ne communique JAMAIS ces identifiants SIP à ses clients grand public. Sans ces identifiants, impossible d'enregistrer un équipement tiers sur leur plateforme VoIP.
   
Conséquence directe : Oubliez l'idée de faire fonctionner la ligne fixe Bouygues directement sur votre routeur ou adaptateur personnel. Ce n'est pas possible faute d'accès aux informations nécessaires.
   
Solution de contournement unique : Conserver la Bbox uniquement pour la téléphonie. Branchez-la derrière votre routeur personnel (sur un port LAN, éventuellement dans un VLAN dédié si vous maîtrisez cette configuration) pour qu'elle puisse accéder à Internet et maintenir le service téléphonique actif. Le téléphone fixe reste alors branché sur la Bbox. C'est la seule méthode viable pour conserver la ligne fixe après avoir remplacé la Bbox comme routeur principal. UPDATE @mirtouf: n'est plus possible ni en ipv4 ni en ipv6 à ce jour.

# 3. Points d'attention et Dépannage

Incompatibilité GPON/XGS-PON : Vérifiez votre technologie fibre avant d'acheter un ONT/SFP de remplacement !
   
Clonage MAC & Option 60 : Assurez-vous que ces deux points sont bien configurés pour obtenir une adresse IP rapidement.
   
Tag CoS 802.1p : Bien que potentiellement pas bloquant pour obtenir une IP dans certains cas, l'absence de ces tags (p6 pour DHCP, p5 pour IGMP/TV) est une cause fréquente de problèmes de stabilité, de performance (débits bridés, TV qui saccade), ou de non-renouvellement des baux DHCP. Il est vivement conseillé de les configurer si votre matériel le permet.
   
Compatibilité et Configuration ONT/SFP : Si vous remplacez l'ONT/SFP, vérifiez sa compatibilité GPON/XGS-PON et assurez-vous d'avoir correctement obtenu et configuré le SN/SLID et le PLOAM/Registration ID. Utilisez l'API si besoin pour le SN.
   
Pare-feu : Un pare-feu mal configuré peut bloquer des flux nécessaires (DHCP, IGMP, Multicast UDP). Commencez avec des règles permissives pour tester, puis affinez.
   
Testez progressivement : Faites fonctionner Internet (IPv4/IPv6) d'abord, puis l'IPTV.
   
Capture de paquets : Des outils comme `tcpdump` ou Wireshark peuvent être très utiles pour analyser ce qui se passe sur l'interface WAN (VLAN 100) et LAN.
Ce post sert de point de départ. N'hésitez pas à consulter les tutoriels spécifiques (tentative par IA de liste des routeur testés https://lafibre.info/remplacer-bbox/recap-2025-a-lire-pour-les-nouveaux-arrivants/msg1116615/#post_config_routeurs).

N'hésitez pas à partager vos propres expériences !