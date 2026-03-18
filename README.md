# Network Sentinel Cyber Recon 🛡️

O **Network Sentinel** é uma ferramenta modular de OSINT (*Open Source Intelligence*) desenvolvida em Python. Projetada para automatizar a coleta de dados de alvos (domínios, e-mails ou CNPJs), sendo ideal para as fases iniciais de um Pentest ou para estudos de Cybersecurity.

---

## 🚀 Como Usar (Exemplos de Input)

| Opção   | Módulo             | Exemplo de Input (O que digitar)                     |

| **[1]** | **Passive Recon**  | `google.com` ou `alvo.com.br`                        |
| **[2]** | **Deep Harvester** | `seu-alvo@email.com`                                 |
| **[3]** | **SSL/TLS Audit**  | `github.com` ou `site-seguro.com`                    |
| **[4]** | **Business Audit** | `00000000000191` (Apenas números do CNPJ)            |
| **[5]** | **File & History** | `projeto_secreto` ou `empresa_alvo`                  |
| **[6]** | **FULL REPORT**    | `alvo@dominio.com` (Executa Recon + SSL + Harvester) |

---

📥 Instalação por Sistema

🛠️ WINDOWS 11
Instale o Python 3.

No PowerShell/CMD, execute:

```bash
git clone https://www.google.com/search?q=https://github.com/cyb3rl30/Network-Sentinel.git
cd Network-Sentinel
pip install requests
python Network-Sentinel.py
```

🐉 KALI LINUX / DEBIAN
Abra o seu terminal e execute:

```bash
sudo apt update && sudo apt install git python3-pip -y
git clone https://www.google.com/search?q=https://github.com/cyb3rl30/Network-Sentinel.git
cd Network-Sentinel
pip3 install requests
python3 Network-Sentinel.py
```

📲 TERMUX (ANDROID)
No seu celular, abra o Termux e digite:

```bash
pkg update && pkg upgrade
pkg install git python3 -y
git clone https://www.google.com/search?q=https://github.com/cyb3rl30/Network-Sentinel.git
cd Network-Sentinel
pip install requests
python3 Network-Sentinel.py
```

⚠️ Disclaimer
Uso estritamente educacional. O autor não se responsabiliza por uso indevido. Teste apenas em ambientes autorizados.

Desenvolvido por: cyb3rl30 🚀