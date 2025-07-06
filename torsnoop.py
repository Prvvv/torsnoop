import requests
import hashlib
from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urlparse, urljoin
from PIL import Image
from PIL.ExifTags import TAGS
import os
from time import strftime, gmtime


tor_proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}

onion_url = '' #insert onion url

try:
    print("[*] Connecting to:", onion_url)
    r = requests.get(onion_url, proxies=tor_proxy, timeout=30)
    print("[+] Status Code:", r.status_code)
    print("[+] Response Time:", r.elapsed.total_seconds(), "seconds")
    
    print("\n[+] Headers:")
    for header, value in r.headers.items():
        print(f"    {header}: {value}")
        
    print("\n[+] Highlighted Headers:")
    print("[+] Server:", r.headers.get('Server', 'No Server Header Found'))
    print("[+] Content-Type:", r.headers.get('Content-Type', 'Unknown'))
    print("[+] Content-Length:", r.headers.get('Content-Length', 'Unknown'))
    print("[+] X-Powered-By:", r.headers.get('X-Powered-By', 'Not disclosed'))
    
    content_hash = hashlib.sha256(r.content).hexdigest()
    print("[+] SHA-256 Content Hash:", content_hash)

    with open('onion_site.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
        print("[+] HTML content saved to onion_site.html")

    soup = BeautifulSoup(r.text, 'html.parser')

    title = soup.title.string.strip() if soup.title else 'No title tag'
    print("[+] Page Title:", title)

    description = soup.find('meta', attrs={'name': 'description'})
    if description:
        print("[+] Meta Description:", description.get('content'))

    if 'wp-content' in r.text:
        print("[+] Possible CMS: WordPress")
    elif 'Drupal.settings' in r.text:
        print("[+] Possible CMS: Drupal")
    elif 'Joomla!' in r.text:
        print("[+] Possible CMS: Joomla")

    print("\n[+] Technology/Framework Indicators:")
    tech_indicators = {
        'PHP': ['.php', 'PHPSESSID'],
        'Python (Django/Flask)': ['csrftoken', '_ga', 'sessionid'],
        'ASP.NET': ['.aspx', 'ASP.NET'],
        'Cloudflare': ['cf-ray', '__cfduid'],
        'Nginx': ['nginx'],
        'Apache': ['Apache'],
    }

    for tech, indicators in tech_indicators.items():
        if any(indicator in r.text or indicator in str(r.headers) for indicator in indicators):
            print(f"    [+] Possible Technology/Framework: {tech}")
            
    scripts = soup.find_all('script', src=True)
    if scripts:
        print("\n[+] External Scripts:")
        for script in scripts:
            print("    ", script['src'])

    stylesheets = soup.find_all('link', rel='stylesheet')
    if stylesheets:
        print("\n[+] Stylesheets:")
        for sheet in stylesheets:
            print("    ", sheet['href'])

    images = soup.find_all('img', src=True)
    if images:
        print("\n[+] Images:")
        for img in images:
            print("    ", img['src'])

    forms = soup.find_all('form')
    for form in forms:
        form_text = str(form).lower()
        if 'login' in form_text:
            print("[+] Possible login form detected.")
        if 'admin' in form_text:
            print("[+] Possible admin panel reference found.")

    internal_links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/'):
            internal_links.add(onion_url + href)
        elif '.onion' in href:
            internal_links.add(href)

    if internal_links:
        print("\n[+] Internal Links Found:")
        for link in internal_links:
            print("    ", link)


except requests.exceptions.RequestException as e:
    print("[-] Failed to connect:", e)



