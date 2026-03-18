from ast import main
import os
import sys
import re
import random
import requests
import ssl
import socket

# --- CONFIGURAÇÃO DE CORES ---
G = "\033[1;32m"
R = "\033[1;31m"
C = "\033[1;36m"
W = "\033[1;37m"
Y = "\033[1;33m"
X = "\033[0m"

# --- USER-AGENTS ---
AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/537.36"
]

def sanitize_input(user_input):
    # Permite alfanumérico, ponto, hífen e o @ para e-mails
    clean = re.sub(r'[^a-zA-Z0-9.\-@]', '', user_input)
    return clean

def header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{R}")
    # Banner comprimido (mantendo seu formato original de caracteres)
    print(r""" @@@  @@@  @@@@@@@@  @@@@@@@  @@@  @@@  @@@  @@@@@@   @@@@@@@   @@@  @@@
 @@@@ @@@  @@@@@@@@  @@@@@@@  @@@  @@@  @@@ @@@@@@@@  @@@@@@@@  @@@  @@@
 @@!@!@@@  @@!         @@!    @@!  @@!  @@! @@!  @@@  @@!  @@@  @@!  !@@
 !@!!@!@!  !@!         !@!    !@!  !@!  !@! !@!  @!@  !@!  @!@  !@!  @!!
 @!@ !!@!  @!!!:!      @!!    @!!  !!@  @!@ @!@  !@!  @!@!!@!   @!@@!@!
 !@!  !!!  !!!!!:      !!!    !@!  !!!  !@! !@!  !!!  !!@!@!    !!@!!!
 !!:  !!!  !!:         !!:    !!:  !!:  !!: !!:  !!!  !!: :!!   !!: :!!
 :!:  !:!  :!:         :!:    :!:  :!:  :!: :!:  !:!  :!:  !:!  :!:  !:!
  ::   ::   :: ::::     ::     :::: :: :::   ::::: ::  ::   :::   ::  :::
  ::    :   : :: :      :       :: :  : :     : :  :    :    : :   :   :::
  @@@@@@   @@@@@@@@  @@@  @@@  @@@@@@@  @@@  @@@  @@@  @@@@@@@@  @@@
 @@@@@@@   @@@@@@@@  @@@@ @@@  @@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@
 !@@       @@!       @@!@!@@@    @@!    @@!  @@!@!@@@  @@!       @@!
 !@!       !@!       !@!!!@!@    !@!    !@!  !@!!@!@!  !@!       !@!
 !!@@!!    @!!!:!    @!@ !!@!    @!!    !!@  @!@ !!@!  @!!!:!    @!!
  !!@!!!   !!!!!:    !@!  !!!    !!!    !!!  !@!  !!!  !!!!!:    !!!
      !:!  !!:       !!:  !!!    !!:    !!:  !!:  !!!  !!:       !!:
     !:!   :!:       :!:  !:!    :!:    :!:  :!:  !:!  :!:       :!:
 :::: ::    :: ::::   ::   ::    ::     ::   ::   ::   :: ::::   :: ::::
 : : :     : :: :    :    :     :      :     :    :    : :: :    : :: :""")
    print(f"{R} [!] USE A VPN OR PROXY TO MASK YOUR IDENTITY [!]{X}")
    print(f"{C} Author  :{X} {W}cyb3rl30{X} | {C}GitHub :{X} {W}github.com/cyb3rl30{X}")
    print(f"{W}" + "-"*75 + f"{X}")

def menu():
    print(f" {G}[1]{X} Passive Recon (WAF & Tech Stack)")
    print(f" {G}[2]{X} Deep Harvester (Emails & Leaks)")
    print(f" {G}[3]{X} SSL/TLS Audit (Secure Ports)")
    print(f" {G}[4]{X} Business Audit (CNPJ & Location)")
    print(f" {G}[5]{X} File & History Audit (Archive/4shared)")
    print(f" {G}[6]{X} GLOBAL SENTINEL REPORT (Full Scan)")
    print(f"{R} [0] Exit System{X}")
    print(f"{W}" + "-"*75 + f"{X}")

def passive_recon(target):
    print(f"\n{Y}[*] Starting Passive Recon: {target}{X}")
    try:
        headers = {'User-Agent': random.choice(AGENTS)}
        r = requests.get(f"https://{target}", headers=headers, timeout=10)
        print(f"{G}[+] Connection successful.{X}")
        for h, v in r.headers.items():
            if h.lower() in ['server', 'x-powered-by', 'x-cdn', 'cf-ray']:
                print(f"{C}[i] Tech Found:{X} {h}: {v}")
    except Exception as e:
        print(f"{R}[!] Recon Error: Dominio offline ou inacessivel.{X}")

def ssl_audit(target):
    print(f"\n{Y}[*] Auditing SSL/TLS: {target}{X}")
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((target, 443), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
                subject = dict(x[0] for x in cert['subject'])
                print(f"{G}[+] SSL Verified: {subject.get('commonName', 'Unknown')}{X}")
    except:
        print(f"{R}[!] SSL verification failed on port 443.{X}")

def deep_harvester(target):
    if "@" not in target:
        return
    
    username = target.split("@")[0]
    headers = {'User-Agent': random.choice(AGENTS)}
    
    print(f"\n{Y}[*] RELATORIO DE INTELIGENCIA (OSINT): {target}{X}")
    print(f"{W}" + "="*70 + f"{X}")

    print(f"{C}[i] Monitorando Presenca em Redes Sociais...{X}")
    social = {
        "Instagram": f"https://www.google.com/search?q=site:instagram.com+%22{target}%22",
        "Facebook": f"https://www.google.com/search?q=site:facebook.com+%22{target}%22",
        "LinkedIn": f"https://www.google.com/search?q=site:linkedin.com/in/+%22{username}%22",
        "Twitter/X": f"https://www.google.com/search?q=site:twitter.com+%22{username}%22"
    }
    for rede, link in social.items():
        print(f"{G}[+] {rede}:{W} {link}{X}")

    print(f"\n{C}[i] Buscando Exposicao Tecnica e Codigo Fonte...{X}")
    tech = {
        "GitHub (Leaks)": f"https://www.google.com/search?q=site:github.com+%22{target}%22",
        "Pastebin (Dumps)": f"https://www.google.com/search?q=site:pastebin.com+%22{target}%22",
        "Trello (Boards)": f"https://www.google.com/search?q=site:trello.com+%22{target}%22"
    }
    for site, link in tech.items():
        print(f"{Y}[!] {site}:{W} {link}{X}")

    print(f"\n{C}[i] Consultando base de dados de Leaks...{X}")
    try:
        url = f"https://breachdirectory.org/api/search?term={target}"
        r = requests.get(url, headers=headers, timeout=12)
        if r.status_code == 200:
            res = r.json()
            sources = res.get('sources', [])
            important_leaks = [s for s in sources if s.lower() not in ['deezer', 'spotify', 'wattpad']]
            if important_leaks:
                print(f"{R}[!] ALERTA: {len(important_leaks)} Fontes Criticas Detectadas!{X}")
                for s in important_leaks: print(f"{Y}> Vazamento: {W}{s.upper()}{X}")
            else:
                print(f"{G}[+] Nenhuma credencial exposta em bases conhecidas.{X}")
    except:
        print(f"{Y}[i] Servidor de Leaks offline momentaneamente.{X}")
    print(f"{W}" + "="*70 + f"{X}")

def business_audit(cnpj):
    cnpj_limpo = re.sub(r'[^0-9]', '', cnpj)
    print(f"\n{Y}[*] Searching CNPJ: {cnpj_limpo}...{X}")
    try:
        url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print(f"{G}[+] Razao Social: {data.get('razao_social')}{X}")
            print(f"{C}[i] Situacao: {data.get('descricao_situacao_cadastral')}{X}")
            print(f"{C}[i] Local: {data.get('municipio')}/{data.get('uf')}{X}")
        else:
            print(f"{R}[!] CNPJ nao encontrado.{X}")
    except Exception as e:
        print(f"{R}[!] API Connection Error.{X}")

def search_archives(target):
    query_base = target.strip()
    print(f"\n{Y}[*] VARREDURA POR VAZAMENTOS E ARQUIVOS: {query_base}{X}")
    print(f"{W}" + "-"*75 + f"{X}")
    
    links = {
        "Google Dorks (Pass)": f"https://www.google.com/search?q=%22{query_base}%22+(filetype:txt+OR+filetype:sql+OR+filetype:log)+intext:password",
        "Nuvem (Pastebin)": f"https://www.google.com/search?q=site:pastebin.com+OR+site:4shared.com+%22{query_base}%22",
        "Wayback Machine": f"https://web.archive.org/web/*/{query_base.replace(' ', '')}*",
        "Archive.org (Data)": f"https://archive.org/search.php?query={query_base}&and[]=mediatype%3A%22data%22"
    }

    for desc, link in links.items():
        print(f"{G}[+] {desc}:{W} {link}{X}")
    print(f"{W}" + "-"*75 + f"{X}")

def main():
    while True:
        header()
        menu()
        cmd = input(f"{G}Sentinel@Network:~#{X} ")
        
        if cmd == '0':
            print(f"{R}[!] Desconectando do Sentinel...{X}")
            break
            
        elif cmd in ['1', '2', '3', '4', '5', '6']:
            if cmd == '4': prompt_text = "CNPJ"
            elif cmd == '2': prompt_text = "Target Email"
            else: prompt_text = "Target Domain"
                
            raw_t = input(f"{C}{prompt_text}:{X} ").strip()
            t = sanitize_input(raw_t)
            
            if not t:
                print(f"{R}[!] Erro: O alvo nao pode estar vazio!{X}")
                input(f"{W}Pressione Enter para continuar...{X}")
                continue 
            
            if cmd == '1': passive_recon(t)
            elif cmd == '2': deep_harvester(t)
            elif cmd == '3': ssl_audit(t)
            elif cmd == '4': business_audit(t)
            elif cmd == '5': search_archives(t)
            elif cmd == '6':
                print(f"\n{Y}[*] INICIANDO GLOBAL SENTINEL REPORT...{X}")
                print(f"{W}" + "="*75 + f"{X}")
                is_email = "@" in t
                dom = t.split("@")[-1] if is_email else t
                
                passive_recon(dom)
                ssl_audit(dom)
                if is_email:
                    deep_harvester(t)
                else:
                    print(f"\n{C}[i] Info: Deep Harvester ignorado (Alvo nao e e-mail).{X}")
                search_archives(t)
                
            input(f"\n{W}Busca Finalizada. Pressione Enter para continuar...{X}")
        else:
            if cmd != "":
                print(f"{R}[!] Opcao Invalida!{X}")
                input(f"{W}Pressione Enter...{X}")

if __name__ == "__main__":
    main()