## TORSN00P

#### A comprehensive reconnaissance utility for surface-level analysis of .onion hidden services

designed for ethical research, intelligence gathering, or cybersecurity auditing within the Tor network. Tailored specifically for hidden services, this script performs automated metadata collection, fingerprinting of technologies, content hashing, and structural breakdown of onion-based websites — all via a secure SOCKS5 proxy over Tor.

At its core, this tool leverages the Tor daemon’s SOCKS5 proxy (default: 127.0.0.1:9050) to tunnel HTTP requests directly into the dark web. Using the robust requests library with Tor proxy configuration, it connects to the specified .onion URL and conducts a structured assessment of the service’s public-facing HTML content.

Upon connection, it reports the HTTP status code and measures the response latency, providing insights into service uptime or potential filtering. It captures all HTTP headers, highlighting key indicators such as server type, content type, response size, and any "X-Powered-By" values that might leak underlying tech stacks. The complete page source is saved locally as onion_site.html, enabling offline analysis or archival.

The tool then parses the HTML content using BeautifulSoup, extracting high-value meta information such as the <title> and <meta name="description">, if present. It includes rudimentary CMS detection heuristics, scanning for string patterns suggestive of platforms like WordPress, Drupal, or Joomla. This is accompanied by technology fingerprinting through both HTML content and headers — flagging potential usage of PHP, Python frameworks (Flask, Django), ASP.NET, Cloudflare protection, and popular web servers like Nginx and Apache.

Additionally, the script identifies and lists all linked external resources, including JavaScript files, stylesheets, and images. This serves both as a mapping of third-party dependencies and a method to detect CDN usage or hidden resource loading. It also inspects form elements for common keywords like "login" or "admin", helping flag areas of interest like authentication portals or backend interfaces.

Internal navigation structure is parsed via all anchor tags, automatically resolving and printing discovered links that either reference the same domain or contain .onion identifiers. This lightweight spidering functionality can assist in enumeration of the service without requiring recursive crawling.

To ensure content integrity and allow change tracking, the script generates a SHA-256 hash of the full HTTP response body, acting as a digital fingerprint of the page content at the time of access.

Designed with simplicity and transparency in mind, the tool includes clear print-based output for each step, ideal for terminal-based use in environments where GUI tools are impractical. It does not rely on any external databases or APIs, ensuring fully offline operation (aside from Tor connectivity) and avoiding information leakage.

This utility is perfect for security researchers, OSINT professionals, digital forensics experts, and anyone seeking to safely profile .onion sites without direct interaction or active exploitation. Its passive analysis approach makes it a useful tool for auditing or archiving services on the dark web.

**Requirements:**

- Tor must be running and accessible via localhost:9150

- Python 3.6+

- Dependencies: requests, bs4, Pillow

###### This tool is intended solely for lawful security research, intelligence gathering, and academic study. Use it only on systems you own or are explicitly authorized to test. Unauthorized access to systems you do not own is illegal and unethical. If you wish to report a vulnerability, request a feature, or have concerns about the intended use of this project, please contact the maintainer directly at: prv@anche.no.
