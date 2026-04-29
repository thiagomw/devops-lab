# 🚀 Roadmap DevOps — Do Service Desk ao DevOps Engineer
**Perfil:** Formado em Redes (FIAP) · Python iniciante · Service Desk em empresa de IA  
**Dedicação:** 1–2h/dia (dias intensos de 5h são seus dias de laboratório)  
**Infraestrutura:** Oracle Cloud Free Tier · Ubuntu 22.04 LTS · VSCode + Remote SSH

---

## 📌 Visão Geral da Jornada

```
[Você hoje]          [Fase 1 ~3 meses]     [Fase 2 ~4 meses]     [Fase 3 ~5 meses]     [Fase 4 ~6 meses]
Service Desk     →   Linux + Git + Python → Docker + CI/CD     → Monitoramento       → Kubernetes + IaC
Python iniciante     Bash scripting          GitHub Actions        Prometheus + Grafana   Terraform
Redes (teoria)       VM na Oracle Cloud      Containers reais      Logs centralizados     SRE básico
```

> **Como usar este roadmap:**  
> Cada fase tem: material de estudo → checklist de habilidades → cenário prático na VM.  
> Estude o material, pratique os exercícios do checklist, depois execute o cenário.  
> Versione tudo no GitHub desde o primeiro dia — isso vira seu portfólio.

---

## ⚙️ Ambiente — Já Configurado ✅

- [x] VM `devops-lab` criada na Oracle Cloud (Ubuntu 22.04 LTS)
- [x] IP público atribuído (Ephemeral public IP)
- [x] Acesso via SSH funcionando
- [x] VSCode com Remote SSH configurado e conectado

**Conectar na VM quando precisar:**
```bash
ssh ubuntu@163.176.186.92 -i C:\Users\thiag\Downloads\ssh-key-2026-04-23.key
```

Ou pelo VSCode: `Ctrl+Shift+P` → **Remote-SSH: Connect to Host** → **devops-lab**

---

## 🗺️ FASE 1 — Linux, Git e Python na Prática (Meses 1–3)
> *"Aprender as ferramentas que todo DevOps usa todo dia"*

### 📚 Material de Estudo

Siga nesta ordem — estude em paralelo com o cenário prático:

| Material | Tipo | Onde acessar | Foco |
|---|---|---|---|
| Linux Journey | Site gratuito | [linuxjourney.com](https://linuxjourney.com) | Módulos: Grasshopper e Journeyman |
| Pro Git Book (PT-BR) | Livro gratuito | [git-scm.com/book/pt-br/v2](https://git-scm.com/book/pt-br/v2) | Capítulos 1, 2 e 3 |
| Python para Zumbis | YouTube gratuito | Buscar "Python para Zumbis" no YouTube | Aulas 1 a 8 |
| Bash Scripting Tutorial | Site gratuito | [ryanstutorials.net/bash-scripting-tutorial](https://ryanstutorials.net/bash-scripting-tutorial) | Do início ao módulo 5 |

### ✅ Checklist de Habilidades

Pratique cada item diretamente na VM via terminal:

**Linux:**
- [✅] Navegar entre diretórios (`cd`, `ls`, `pwd`)
- [✅] Criar, mover, copiar e deletar arquivos (`mkdir`, `mv`, `cp`, `rm`)
- [✅] Editar arquivos com `nano` ou `vim`
- [✅] Entender e alterar permissões (`chmod`, `chown`)
- [✅] Filtrar conteúdo de arquivos (`grep`, `cat`, `tail`, `head`)
- [✅] Instalar pacotes com `apt`
- [✅] Entender processos (`ps`, `top`, `kill`)

**Git:**
- [✅] `git init`, `add`, `commit`, `push`, `pull`
- [✅] Criar e mergear branches
- [✅] Escrever um `README.md` decente
- [✅] Resolver um conflito simples de merge

**Python:**
- [✅] Funções, listas, dicionários, loops, condições
- [✅] Ler e escrever arquivos
- [✅] Usar os módulos `os`, `subprocess`, `socket`
- [ ] Instalar e usar bibliotecas com `pip`

**Bash:**
- [ ] Variáveis, `if`, `for`, `while`
- [ ] Passar argumentos para scripts (`$1`, `$2`)
- [ ] Tornar script executável com `chmod +x`

---

### 🟢 CENÁRIO 1 — Verificador de conectividade rodando na VM

**O que você vai praticar:**
Linux na VM, Python com `socket`, Git para versionar, `cron` para agendar execução automática.

**O que o cenário constrói:**
Um script que verifica se uma lista de hosts está respondendo, salva relatório em arquivo e roda automaticamente de tempos em tempos.

---

**Passo 1 — Conecte na VM e prepare o ambiente**

Abra o terminal no VSCode (`Ctrl+`` `) já conectado na VM e rode:

```bash
# Atualiza o sistema
sudo apt update && sudo apt upgrade -y

# Instala Python e Git
sudo apt install python3 python3-pip git -y

# Confirma as versões
python3 --version
git --version
```

**Passo 2 — Configure o Git com seus dados**
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

**Passo 3 — Clone seu repositório na VM**

Crie um repositório chamado `devops-lab` no GitHub (público), depois:
```bash
git clone https://github.com/SEU_USUARIO/devops-lab.git
cd devops-lab
mkdir cenario-01
cd cenario-01
```

**Passo 4 — Crie o script**
```bash
nano check_hosts.py
```

Cole o conteúdo abaixo:
```python
# check_hosts.py
import socket
import datetime
import os

hosts = [
    {"name": "Google DNS",     "host": "8.8.8.8",    "port": 53},
    {"name": "Cloudflare DNS", "host": "1.1.1.1",    "port": 53},
    {"name": "GitHub",         "host": "github.com", "port": 443},
    {"name": "Oracle Cloud",   "host": "oracle.com", "port": 443},
]

results = []
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for h in hosts:
    try:
        sock = socket.create_connection((h["host"], h["port"]), timeout=3)
        sock.close()
        status = "UP"
        icon = "OK"
    except (socket.timeout, ConnectionRefusedError, OSError):
        status = "DOWN"
        icon = "FALHOU"

    result = f"[{timestamp}] {icon} | {h['name']} ({h['host']}:{h['port']}) — {status}"
    results.append(result)
    print(result)

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_report.txt")
with open(log_file, "a", encoding="utf-8") as f:
    f.write("\n".join(results) + "\n\n")

print(f"\nRelatório salvo em check_report.txt")
```

**Passo 5 — Rode e teste**
```bash
python3 check_hosts.py
cat check_report.txt
```

**Passo 6 — Agende execução automática com cron**
```bash
# Abre o editor de cron
crontab -e

# Adicione esta linha para rodar a cada 5 minutos
*/5 * * * * python3 /home/ubuntu/devops-lab/cenario-01/check_hosts.py
```

Aguarde 5 minutos e verifique:
```bash
cat ~/devops-lab/cenario-01/check_report.txt
```

**Passo 7 — Versione no GitHub**
```bash
cd ~/devops-lab
git add .
git commit -m "feat: cenario-01 - verificador de conectividade com cron"
git push origin main
```

**O que você acabou de fazer na prática:**
- Atualizou um servidor Linux real
- Instalou dependências via `apt`
- Escreveu e rodou Python num servidor remoto
- Agendou execução automática com `cron`
- Versionou tudo no GitHub

---

## 🗺️ FASE 2 — Docker e CI/CD (Meses 3–7)
> *"Containerizar aplicações e automatizar deploy"*

### 📚 Material de Estudo

| Material | Tipo | Onde acessar | Foco |
|---|---|---|---|
| Docker Getting Started | Docs oficiais | [docs.docker.com/get-started](https://docs.docker.com/get-started) | Partes 1 a 6 |
| TechWorld with Nana — Docker | YouTube gratuito | Buscar "Docker Tutorial for Beginners TechWorld Nana" | Playlist completa |
| GitHub Actions Docs | Docs oficiais | [docs.github.com/en/actions](https://docs.github.com/en/actions) | Quickstart + Using workflows |
| Play with Docker | Lab gratuito | [labs.play-with-docker.com](https://labs.play-with-docker.com) | Pratique sem instalar nada |

### ✅ Checklist de Habilidades

- [ ] Instalar Docker numa VM Linux
- [ ] Rodar, parar e remover containers (`docker run`, `stop`, `rm`)
- [ ] Listar containers e imagens (`docker ps`, `docker images`)
- [ ] Escrever um `Dockerfile` básico
- [ ] Fazer build de uma imagem (`docker build`)
- [ ] Usar volumes e variáveis de ambiente
- [ ] Escrever um `docker-compose.yml` com múltiplos serviços
- [ ] Subir e derrubar stack com `docker-compose up/down`
- [ ] Criar um pipeline no GitHub Actions que roda testes automaticamente

---

### 🟡 CENÁRIO 2 — Aplicação containerizada com pipeline CI/CD

**O que você vai praticar:**
Docker, docker-compose, GitHub Actions, testes automatizados com `unittest`.

**O que o cenário constrói:**
Uma aplicação Python dentro de um container Docker, com pipeline no GitHub Actions que roda os testes automaticamente a cada `push`.

---

**Passo 1 — Instale Docker na VM**
```bash
# Instala Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Adiciona seu usuário ao grupo docker
sudo usermod -aG docker ubuntu

# Saia e reconecte pra aplicar o grupo
exit
```

Reconecte na VM e confirme:
```bash
docker --version
docker run hello-world
```

**Passo 2 — Instale docker-compose**
```bash
sudo apt install docker-compose -y
docker-compose --version
```

**Passo 3 — Prepare a estrutura do projeto**
```bash
cd ~/devops-lab
mkdir cenario-02
cd cenario-02
```

**Passo 4 — Crie a aplicação**
```bash
nano monitor.py
```
```python
# monitor.py
import psutil
import datetime

def coletar_metricas():
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memoria_percent": psutil.virtual_memory().percent,
        "disco_percent": psutil.disk_usage('/').percent,
    }

if __name__ == "__main__":
    metricas = coletar_metricas()
    for chave, valor in metricas.items():
        print(f"{chave}: {valor}")
```

**Passo 5 — Crie os testes**
```bash
nano test_monitor.py
```
```python
# test_monitor.py
import unittest
from monitor import coletar_metricas

class TestMonitor(unittest.TestCase):
    def test_retorna_dicionario(self):
        resultado = coletar_metricas()
        self.assertIsInstance(resultado, dict)

    def test_chaves_presentes(self):
        resultado = coletar_metricas()
        self.assertIn("cpu_percent", resultado)
        self.assertIn("memoria_percent", resultado)
        self.assertIn("disco_percent", resultado)

    def test_valores_validos(self):
        resultado = coletar_metricas()
        self.assertTrue(0 <= resultado["cpu_percent"] <= 100)
        self.assertTrue(0 <= resultado["memoria_percent"] <= 100)
        self.assertTrue(0 <= resultado["disco_percent"] <= 100)

if __name__ == "__main__":
    unittest.main()
```

**Passo 6 — Crie o Dockerfile**
```bash
nano Dockerfile
```
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install psutil
CMD ["python", "monitor.py"]
```

**Passo 7 — Build e teste o container**
```bash
docker build -t meu-monitor .
docker run meu-monitor
```

**Passo 8 — Crie o pipeline no GitHub Actions**

No terminal da VM, dentro do repositório:
```bash
cd ~/devops-lab
mkdir -p .github/workflows
nano .github/workflows/ci.yml
```
```yaml
name: CI — Testa o monitor

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v3

      - name: Instala Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Instala dependências
        run: pip install psutil

      - name: Roda os testes
        run: python -m unittest test_monitor.py -v
```

**Passo 9 — Versione e observe o pipeline rodar**
```bash
git add .
git commit -m "feat: cenario-02 - monitor containerizado com CI/CD"
git push origin main
```

Acesse seu repositório no GitHub → aba **Actions** → veja o pipeline rodar em tempo real.

---

## 🗺️ FASE 3 — Observabilidade (Meses 7–12)
> *"Enxergar o que está acontecendo no ambiente antes que vire problema"*

### 📚 Material de Estudo

| Material | Tipo | Onde acessar | Foco |
|---|---|---|---|
| TechWorld with Nana — Prometheus | YouTube gratuito | Buscar "Prometheus Tutorial TechWorld Nana" | Playlist completa |
| Grafana Getting Started | Docs oficiais | [grafana.com/docs/grafana/latest/getting-started](https://grafana.com/docs/grafana/latest/getting-started) | Setup e primeiros dashboards |
| Prometheus Docs | Docs oficiais | [prometheus.io/docs/introduction/overview](https://prometheus.io/docs/introduction/overview) | Conceitos e configuração |
| Loki Getting Started | Docs oficiais | [grafana.com/docs/loki/latest/get-started](https://grafana.com/docs/loki/latest/get-started) | Logs centralizados |

### ✅ Checklist de Habilidades

- [ ] Entender o modelo pull do Prometheus (scraping)
- [ ] Expor métricas no formato Prometheus via Python
- [ ] Configurar targets no `prometheus.yml`
- [ ] Subir Prometheus + Grafana via docker-compose
- [ ] Criar dashboard no Grafana com métricas reais
- [ ] Configurar alertas por threshold no Prometheus
- [ ] Centralizar logs com Loki + Promtail

---

### 🔴 CENÁRIO 3 — Stack completa de monitoramento na VM

**O que você vai praticar:**
`prometheus_client` em Python, docker-compose com múltiplos serviços, Grafana na prática.

**O que o cenário constrói:**
Uma aplicação que expõe métricas reais da VM, coletadas pelo Prometheus e visualizadas no Grafana — acessíveis pelo browser.

---

**Passo 1 — Prepare o ambiente**
```bash
cd ~/devops-lab
mkdir cenario-03
cd cenario-03
pip3 install prometheus_client psutil
```

**Passo 2 — Crie a aplicação que expõe métricas**
```bash
nano app_metricas.py
```
```python
# app_metricas.py
from prometheus_client import start_http_server, Gauge
import psutil
import time

cpu_gauge   = Gauge('vm_cpu_percent',     'Uso de CPU da VM em %')
mem_gauge   = Gauge('vm_memoria_percent', 'Uso de memória da VM em %')
disco_gauge = Gauge('vm_disco_percent',   'Uso de disco da VM em %')

def coletar():
    cpu_gauge.set(psutil.cpu_percent(interval=1))
    mem_gauge.set(psutil.virtual_memory().percent)
    disco_gauge.set(psutil.disk_usage('/').percent)

if __name__ == '__main__':
    start_http_server(8000)
    print("Metricas disponiveis em http://localhost:8000/metrics")
    while True:
        coletar()
        time.sleep(5)
```

**Passo 3 — Crie o Dockerfile**
```bash
nano Dockerfile
```
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app_metricas.py .
RUN pip install prometheus_client psutil
CMD ["python", "app_metricas.py"]
```

**Passo 4 — Crie o docker-compose**
```bash
nano docker-compose.yml
```
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    container_name: app-metricas

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    container_name: prometheus

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin123
    container_name: grafana
```

**Passo 5 — Crie o prometheus.yml**
```bash
nano prometheus.yml
```
```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'app-metricas'
    static_configs:
      - targets: ['app:8000']
```

**Passo 6 — Libere as portas no firewall da Oracle Cloud**

Na Oracle Cloud: **Networking → Virtual Cloud Networks → sua VCN → Security Lists → Ingress Rules**

Adicione regras para:
- Porta `8000` — Protocol TCP — Source `0.0.0.0/0`
- Porta `9090` — Protocol TCP — Source `0.0.0.0/0`
- Porta `3000` — Protocol TCP — Source `0.0.0.0/0`

Depois libere também no firewall da própria VM:
```bash
sudo iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 9090 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
```

**Passo 7 — Suba a stack**
```bash
docker-compose up --build -d
```

**Acesse pelo browser:**
- Métricas brutas: `http://163.176.186.92:8000/metrics`
- Prometheus: `http://163.176.186.92:9090`
- Grafana: `http://163.176.186.92:3000` (admin / admin123)

**Passo 8 — Configure o Grafana**
1. Acesse o Grafana no browser
2. Vá em **Configuration → Data Sources → Add data source**
3. Escolha **Prometheus**, URL: `http://prometheus:9090`
4. Clique em **Save & Test**
5. Vá em **Dashboards → New Dashboard → Add visualization**
6. No campo de query digite: `vm_cpu_percent`
7. Repita para `vm_memoria_percent` e `vm_disco_percent`

**Passo 9 — Versione**
```bash
cd ~/devops-lab
git add .
git commit -m "feat: cenario-03 - stack prometheus + grafana na VM"
git push origin main
```

---

## 🗺️ FASE 4 — Kubernetes e Infraestrutura como Código (Meses 12–18)
> *"Orquestrar serviços e provisionar infra com código"*

### 📚 Material de Estudo

| Material | Tipo | Onde acessar | Foco |
|---|---|---|---|
| TechWorld with Nana — Kubernetes | YouTube gratuito | Buscar "Kubernetes Tutorial for Beginners TechWorld Nana" | Playlist completa |
| Terraform Getting Started | Docs oficiais | [developer.hashicorp.com/terraform/tutorials](https://developer.hashicorp.com/terraform/tutorials) | Tutoriais AWS ou OCI |
| KodeKloud | Plataforma (tem free) | [kodekloud.com](https://kodekloud.com) | Labs de Kubernetes e Terraform |
| Killer.sh | Plataforma | [killer.sh](https://killer.sh) | Simulados de certificação CKA |

### ✅ Checklist de Habilidades

- [ ] Instalar e usar `kubectl`
- [ ] Entender Pods, Deployments, Services, ConfigMaps
- [ ] Subir uma aplicação no Minikube localmente
- [ ] Escrever manifests YAML do Kubernetes
- [ ] Entender o conceito de IaC (Infrastructure as Code)
- [ ] Escrever um `main.tf` básico no Terraform
- [ ] Provisionar uma VM via Terraform

> O cenário desta fase será detalhado conforme você avança nas anteriores. Kubernetes tem uma curva mais acentuada e faz mais sentido construir em cima de uma base sólida de Docker e Linux.

---

## 💼 Como Aproveitar Sua Posição na LTM/ADM

Seu ambiente tem processos consolidados — e isso é bom pra você de outra forma:

1. **Observe como os incidentes de infra são tratados** — você vê o resultado (chamado resolvido), tente entender o que a equipe de N2/N3 fez.
2. **Anote termos técnicos** que aparecem nos chamados e alertas — pesquise depois. Você já está exposto ao vocabulário do ambiente.
3. **Aproxime-se dos times de infra e cloud** — demonstre interesse genuíno no trabalho deles.
4. **Seu GitHub é seu portfólio** — quando aparecer uma oportunidade interna, você tem algo concreto pra mostrar.

---

## 🎯 Checkpoints

**Fim da Fase 1 (mês 3):**
- [ ] VM na Oracle Cloud rodando e acessível via SSH e VSCode ✅
- [ ] Script de verificação rodando automaticamente via cron
- [ ] Repositório GitHub com commits organizados

**Fim da Fase 2 (mês 7):**
- [ ] Aplicação rodando dentro de container Docker na VM
- [ ] Pipeline CI/CD no GitHub Actions funcionando
- [ ] Testes automatizados passando no pipeline

**Fim da Fase 3 (mês 12):**
- [ ] Stack Prometheus + Grafana rodando na VM
- [ ] Dashboard com métricas reais acessível pelo browser
- [ ] Base suficiente pra uma entrevista de DevOps Jr / SRE Jr

---

*Criado em abril de 2026 · Versione este roadmap no seu GitHub e atualize conforme avançar!*
