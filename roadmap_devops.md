# 🚀 Roadmap DevOps — Do Service Desk ao DevOps Engineer
**Perfil:** Formado em Redes (FIAP) · Python iniciante · Service Desk em empresa de IA  
**Dedicação:** 1–2h/dia (dias intensos de 5h são seus dias de laboratório)  
**Infraestrutura:** Oracle Cloud Free Tier + Ubuntu 22.04 LTS

---

## 📌 Visão Geral da Jornada

```
[Você hoje]          [Fase 1 ~3 meses]     [Fase 2 ~4 meses]     [Fase 3 ~5 meses]     [Fase 4 ~6 meses]
Service Desk     →   Linux + Git + Python → Docker + CI/CD     → Monitoramento       → Kubernetes + IaC
Python iniciante     Bash scripting          GitHub Actions        Prometheus + Grafana   Terraform
Redes (teoria)       VM na Oracle Cloud      Containers reais      Logs centralizados     SRE básico
```

> **Como usar este roadmap:**  
> Cada fase tem: material de estudo → checklist de habilidades → cenário prático em VM real.  
> Estude o material, pratique os exercícios do checklist, depois execute o cenário.  
> Versione tudo no GitHub desde o primeiro dia — isso vira seu portfólio.

---

## ⚙️ Preparação — Antes de Começar (Semana 0)

### 1. Crie sua VM gratuita na Oracle Cloud

A Oracle Cloud Free Tier oferece 2 VMs permanentemente gratuitas — sem prazo de expiração.

**Passo a passo:**
1. Acesse [cloud.oracle.com](https://cloud.oracle.com) e crie uma conta gratuita
2. No painel, vá em **Compute → Instances → Create Instance**
3. Configure:
   - **Nome:** `devops-lab`
   - **Image:** Ubuntu 22.04 LTS
   - **Shape:** `VM.Standard.E2.1.Micro` (gratuito)
   - **SSH Keys:** gere um par de chaves ou faça upload da sua chave pública
4. Na seção **Primary VNIC:**
   - Crie uma nova VCN (pode usar o nome gerado ou `devops-lab-vcn`)
   - Em **Public IP type**, selecione **Ephemeral public IP** — sem isso a VM não terá IP público
   - Se esquecer durante a criação: **Instance → Instance access → ephemeral public IP**
5. Clique em **Create** — a VM sobe em ~2 minutos
6. Anote o IP público da VM

> 💡 **Sobre VCN e VNIC:**
> - **VCN (Virtual Cloud Network)** → sua rede privada na nuvem, equivalente a uma LAN virtualizada
> - **Subnet** → subdivisão da VCN, como subnets de redes tradicionais
> - **VNIC (Virtual Network Interface Card)** → a placa de rede virtual da VM, equivalente a uma NIC física
> - **IP Público** → o que você usa pra conectar via SSH da internet
> - **IP Privado** → comunicação interna entre recursos na mesma VCN

**Conectar via SSH:**
```bash
ssh ubuntu@SEU_IP_PUBLICO -i sua_chave_privada.key
```

> No Windows, use o **Windows Terminal** ou **VSCode com extensão Remote SSH**.  
> O Remote SSH abre uma nova janela do VSCode conectada à VM — é o comportamento esperado.  
> O canto inferior esquerdo mostra `SSH: devops-lab` confirmando a conexão.  
> Use `` Ctrl+` `` pra abrir o terminal da VM direto no VSCode.

### 2. Crie sua conta no GitHub
- Acesse [github.com](https://github.com) e crie uma conta
- Crie um repositório chamado `devops-lab` — público
- Configure o `.gitignore` desde o início (veja seção Git abaixo)

### 3. Instale no seu computador local
- [VSCode](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- Python 3.11+ ([python.org](https://python.org))
- Extensões VSCode: **Remote - SSH**, **Markdown Preview Enhanced**, **Markdown All in One**

---

## 🗺️ FASE 1 — Linux, Git e Python na Prática ✅
> *"Aprender as ferramentas que todo DevOps usa todo dia"*

### 📚 Material de Estudo

| Material | Tipo | Onde acessar | Foco |
|---|---|---|---|
| Linux Journey | Site gratuito | [linuxjourney.com](https://linuxjourney.com) | Módulos: Grasshopper e Journeyman |
| Pro Git Book (PT-BR) | Livro gratuito | [git-scm.com/book/pt-br/v2](https://git-scm.com/book/pt-br/v2) | Capítulos 1, 2 e 3 |
| Python para Zumbis | YouTube gratuito | Buscar "Python para Zumbis" no YouTube | Aulas 1 a 8 |
| Bash Scripting Tutorial | Site gratuito | [ryanstutorials.net/bash-scripting-tutorial](https://ryanstutorials.net/bash-scripting-tutorial) | Do início ao módulo 5 |

### ✅ Checklist de Habilidades

**Linux — praticado na VM via SSH:**
- [x] Navegar entre diretórios (`cd`, `ls`, `pwd`)
- [x] Criar, mover, copiar e deletar arquivos (`mkdir`, `mv`, `cp`, `rm`)
- [x] Editar arquivos com `nano`
- [x] Entender e alterar permissões (`chmod`, `chown`)
- [x] Filtrar conteúdo de arquivos (`grep`, `cat`, `tail`, `head`)
- [x] Instalar pacotes com `apt`
- [x] Entender processos (`ps`, `top`, `kill`)
- [x] Rodar processos em background com `&`
- [x] Usar operadores de redirecionamento `>` e `>>`

**Git:**
- [x] `git init`, `add`, `commit`, `push`, `pull`
- [x] Criar e mergear branches
- [x] Escrever um `README.md`
- [x] Resolver um conflito simples de merge
- [x] Configurar `.gitignore` corretamente

**Python:**
- [x] Funções, listas, dicionários, loops, condições
- [x] Ler e escrever arquivos com `open()`
- [x] Usar os módulos `os`, `subprocess`, `socket`
- [x] Instalar e usar bibliotecas com `pip` (`psutil`, `requests`)

---

### 📖 Referência Rápida — Linux

#### Permissões
```
drwxr-xr-x
↑ ↑↑↑ ↑↑↑ ↑↑↑
│  │    │    └── outros
│  │    └─────── grupo
│  └──────────── dono
└─────────────── tipo (d=diretório, -=arquivo, l=link)

r = 4 (leitura)
w = 2 (escrita)
x = 1 (execução)
```

**Tabela chmod numérico:**

| Número | Permissão | Quando usar |
|---|---|---|
| `777` | todos fazem tudo | Evitar — muito permissivo |
| `755` | dono tudo, outros leem/executam | Diretórios, scripts |
| `644` | dono lê/escreve, outros só leem | Arquivos comuns |
| `700` | só o dono acessa | Diretórios com dados sensíveis |
| `600` | só o dono lê/escreve | Chaves SSH, arquivos sensíveis |
| `400` | só o dono lê | Chaves privadas |

```bash
chmod 755 arquivo.txt           # numérico
chmod u+x arquivo.txt           # simbólico — adiciona execução pro dono
chmod g-w arquivo.txt           # simbólico — remove escrita do grupo
chown ubuntu:ubuntu arquivo.txt # muda dono e grupo
```

> ⚠️ A chave privada SSH deve ter permissão `400` ou `600` — o SSH recusa conexão se estiver mais aberto.

#### Grupos
```bash
sudo groupadd desenvolvedores           # cria grupo
sudo usermod -aG desenvolvedores user   # adiciona usuário ao grupo
# -a = append (não remove de outros grupos)
# -G = grupos suplementares
# SEMPRE use -aG juntos — só -G remove o usuário de todos os outros grupos
groups usuario                          # lista grupos do usuário
```

#### Processos
```bash
ps aux              # lista todos os processos
top                 # monitor em tempo real (q pra sair, k pra matar)
kill PID            # encerra processo
kill -9 PID         # força encerramento
sleep 60 &          # roda em background — terminal vai exibir o PID
```

#### tail e head
```bash
head -n 5 arquivo.log   # primeiras 5 linhas
tail -n 5 arquivo.log   # últimas 5 linhas
tail -f arquivo.log     # segue em tempo real — Ctrl+C pra sair
```

> 💡 `tail -f` é o mais usado no dia a dia pra monitorar logs de servidor em tempo real.

#### Redirecionamento
```bash
echo "linha 1" > arquivo.txt   # sobrescreve (cria se não existir)
echo "linha 2" >> arquivo.txt  # adiciona ao final (não apaga)
```

#### apt
```bash
sudo apt update            # atualiza lista (não instala nada)
sudo apt upgrade -y        # instala atualizações
sudo apt install pacote -y # instala
sudo apt remove pacote     # remove
```

> 💡 Sempre rode `apt update` antes de instalar — garante a versão mais recente.  
> O `-y` evita confirmação manual — útil em scripts automatizados.

#### Scripts Bash
```bash
#!/bin/bash           # shebang — define o interpretador (primeira linha do script)
chmod 755 script.sh   # dá permissão de execução
./script.sh           # executa
```

#### Buscar ajuda sobre comandos
```bash
man chmod       # manual completo (setas pra navegar, / pra buscar, q pra sair)
chmod --help    # resumo rápido
whatis chmod    # descrição curta
apropos disk    # busca comandos relacionados a uma palavra
```

---

### 📖 Referência Rápida — Git

```bash
# Configuração inicial (uma vez só)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
# O e-mail precisa ser o mesmo do GitHub para vincular os commits ao perfil

# Fluxo básico
git clone https://github.com/usuario/repo.git
git status                      # estado dos arquivos
git add arquivo.py              # adiciona arquivo específico ao stage
git add .                       # adiciona todos os arquivos modificados
git commit -m "feat: mensagem"
git push origin main
git pull origin main

# Branches
git checkout -b nova-branch     # cria e troca
git checkout main               # volta pra main
git merge nova-branch           # merge na branch atual
git branch -d nova-branch       # deleta branch local
git log --oneline               # histórico resumido
```

> 💡 **Stage:** arquivos modificados → `git add` (stage) → `git commit` (histórico). O stage te dá controle sobre o que entra em cada commit — você pode commitar arquivos separados em commits diferentes.

> ⚠️ O GitHub não aceita senha — use **Personal Access Token**: Settings → Developer Settings → Personal Access Tokens → Tokens Classic → marcar `repo` → usar no lugar da senha no push.

#### .gitignore — Boa Prática Importante
Arquivos gerados pelos scripts (`.txt`, `.log`) **não devem** ir pro repositório — só código fonte.

```bash
# .gitignore
*.txt
*.log
__pycache__/
*.pyc
```

```bash
# Se já commitou arquivos indesejados:
git rm --cached *.txt
git rm --cached *.log
git commit -m "chore: remove arquivos gerados do repositorio"
git push origin main
```

---

### 📖 Referência Rápida — Python

#### Boas práticas aprendidas na prática

```python
# 1. Imports sempre no topo do arquivo
import os, subprocess, socket, datetime, time
import psutil, requests

# 2. Separação de responsabilidades — função com uma responsabilidade só
#    Loop fica FORA da função, não dentro
def checar_host(host, porta, timeout=3):
    try:
        socket.create_connection((host, porta), timeout=timeout)
        return True
    except Exception:
        return False

for host, porta in lista_hosts:       # loop fora
    resultado = checar_host(host, porta)

# 3. if __name__ == "__main__" — só roda quando executado diretamente
#    Se outro script importar este arquivo, esse bloco não executa
if __name__ == "__main__":
    checar_host("8.8.8.8", 53)

# 4. encoding="utf-8" em todo open() — evita quebra de acentos
with open("arquivo.txt", "a", encoding="utf-8") as f:
    f.write("conteúdo\n")
    # f.write() NÃO quebra linha automaticamente — use \n explícito
    # print() JÁ quebra linha automaticamente

# 5. .strip() precisa guardar o resultado
linha = linha.strip()   # correto
linha.strip()           # não faz nada — resultado é descartado

# 6. Aspas dentro de f-string — defina a variável antes
conectividade = "OK" if code == 200 else "INACESSÍVEL"
f"Status: {conectividade}"   # correto
# f"Status: {"OK" if ...}"   # SyntaxError em Python < 3.12

# 7. subprocess — comando como lista, não string
subprocess.run(["ls", "-la"], ...)    # correto
subprocess.run(["ls -la"], ...)       # errado — tenta achar programa "ls -la"
resultado.returncode == 0             # 0 = sucesso, outro valor = erro
resultado.stdout                      # saída do comando

# 8. Valor padrão em parâmetro de função
def funcao(host, porta, timeout=3):   # timeout=3 é usado quando não passado
    pass
funcao("8.8.8.8", 53)       # timeout = 3 (padrão)
funcao("8.8.8.8", 53, 10)   # timeout = 10 (sobrescreve o padrão)
```

#### Módulos essenciais
```python
# os
os.getcwd()                         # diretório atual
os.makedirs("pasta", exist_ok=True) # cria diretório recursivo
os.listdir(".")                     # lista arquivos
os.path.exists("pasta")            # verifica se existe

# subprocess
r = subprocess.run(["df", "-h"], capture_output=True, text=True)
r.stdout.splitlines()               # divide saída em lista de linhas

# psutil
psutil.cpu_percent(interval=1)
psutil.virtual_memory().percent
psutil.virtual_memory().total / (1024**3)  # bytes → GB
psutil.disk_usage('/').percent
processos = psutil.process_iter(['pid', 'name', 'memory_percent'])
top5 = sorted(processos, key=lambda p: p.info['memory_percent'], reverse=True)[:5]

# requests
r = requests.get("https://url.com")
r.status_code                       # 200 = OK
r.json().get("campo")               # acessa campo do JSON
```

---

### 🟢 CENÁRIO 1 — Verificador de conectividade rodando na VM

**O que você vai praticar:** Linux na VM, Python com `socket`, Git, `cron`

**Passo 1 — Conecte na VM e prepare o ambiente**
```bash
ssh ubuntu@SEU_IP_PUBLICO -i sua_chave.key
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
```

**Passo 2 — Clone e prepare o projeto**
```bash
git clone https://github.com/SEU_USUARIO/devops-lab.git
cd devops-lab && mkdir cenario-01 && cd cenario-01
```

**Passo 3 — Crie o script**
```python
# check_hosts.py
import socket, datetime, os

hosts = [
    {"name": "Google DNS",   "host": "8.8.8.8",    "port": 53},
    {"name": "Cloudflare",   "host": "1.1.1.1",    "port": 53},
    {"name": "GitHub",       "host": "github.com", "port": 443},
    {"name": "Oracle Cloud", "host": "oracle.com", "port": 443},
]

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
results = []

for h in hosts:
    try:
        sock = socket.create_connection((h["host"], h["port"]), timeout=3)
        sock.close()
        status, icon = "UP", "✅"
    except (socket.timeout, ConnectionRefusedError, OSError):
        status, icon = "DOWN", "❌"

    result = f"[{timestamp}] {icon} {h['name']} ({h['host']}:{h['port']}) — {status}"
    results.append(result)
    print(result)

with open("check_report.txt", "a", encoding="utf-8") as f:
    f.write("\n".join(results) + "\n\n")
```

**Passo 4 — Agende com cron**
```bash
python3 check_hosts.py
crontab -e
# Adicione: */5 * * * * python3 /home/ubuntu/devops-lab/cenario-01/check_hosts.py
```

**Passo 5 — Versione**
```bash
cd ~/devops-lab
git add . && git commit -m "feat: cenario-01 - verificador de conectividade" && git push origin main
```

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

**Passo 1 — Instale Docker na VM**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
# Saia e reconecte — necessário pra aplicar o grupo docker
exit && ssh ubuntu@SEU_IP -i sua_chave.key
docker run hello-world
sudo apt install docker-compose -y
```

**Passo 2 — Crie o projeto**
```bash
cd ~/devops-lab && mkdir cenario-02 && cd cenario-02
```

Crie `monitor.py`, `test_monitor.py`, `Dockerfile` e `.github/workflows/ci.yml` conforme estrutura do roadmap.

**Passo 3 — Build e teste**
```bash
docker build -t meu-monitor .
docker run meu-monitor
git add . && git commit -m "feat: cenario-02 - monitor containerizado com CI/CD" && git push origin main
# GitHub → aba Actions → veja o pipeline rodar em tempo real
```

---

## 🗺️ FASE 3 — Observabilidade (Meses 7–12)
> *"Enxergar o que está acontecendo no ambiente antes que vire problema"*

### 📚 Material de Estudo

| Material | Tipo | Onde acessar |
|---|---|---|
| TechWorld with Nana — Prometheus | YouTube gratuito | Buscar "Prometheus Tutorial TechWorld Nana" |
| Grafana Getting Started | Docs oficiais | [grafana.com/docs](https://grafana.com/docs) |
| Prometheus Docs | Docs oficiais | [prometheus.io/docs](https://prometheus.io/docs) |

### ✅ Checklist de Habilidades

- [ ] Entender o modelo pull do Prometheus (scraping)
- [ ] Expor métricas no formato Prometheus via Python
- [ ] Subir Prometheus + Grafana via docker-compose
- [ ] Criar dashboard no Grafana com métricas reais
- [ ] Configurar alertas por threshold

---

### 🔴 CENÁRIO 3 — Stack completa de monitoramento na VM

Stack: app Python expondo métricas → Prometheus coletando → Grafana visualizando.

**Portas a liberar no firewall da Oracle Cloud:**
- Networking → VCN → Security Lists → Ingress Rules → TCP `8000`, `9090`, `3000`

```bash
# Também libera no firewall da VM
sudo iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 9090 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 8000 -j ACCEPT

docker-compose up --build -d
```

Acesse: `http://SEU_IP:3000` (Grafana) → Data Sources → Prometheus → `http://prometheus:9090`

---

## 🗺️ FASE 4 — Kubernetes e IaC (Meses 12–18)
> *"Orquestrar serviços e provisionar infra com código"*

### 📚 Material de Estudo

| Material | Tipo | Onde acessar |
|---|---|---|
| TechWorld with Nana — Kubernetes | YouTube gratuito | Buscar "Kubernetes Tutorial TechWorld Nana" |
| Terraform Getting Started | Docs oficiais | [developer.hashicorp.com/terraform/tutorials](https://developer.hashicorp.com/terraform/tutorials) |
| KodeKloud | Plataforma | [kodekloud.com](https://kodekloud.com) |

### ✅ Checklist de Habilidades

- [ ] Instalar e usar `kubectl`
- [ ] Entender Pods, Deployments, Services, ConfigMaps
- [ ] Subir aplicação no Minikube localmente
- [ ] Escrever manifests YAML do Kubernetes
- [ ] Escrever um `main.tf` básico no Terraform
- [ ] Provisionar uma VM via Terraform

> O cenário desta fase será detalhado conforme você avança nas anteriores.

---

## 💼 Como Aproveitar Sua Posição na LTM/ADM

Seu ambiente tem processos consolidados (ServiceNow, alertas estruturados, equipes especializadas). O valor do trabalho atual é observar e absorver contexto:

1. **Observe como os incidentes de infra são tratados** — você vê o resultado, tente entender o que N2/N3 fez
2. **Anote termos técnicos** que aparecem nos chamados — pesquise depois
3. **Aproxime-se dos times de infra e cloud** — demonstre interesse genuíno
4. **Seu GitHub é seu portfólio** — quando aparecer uma oportunidade, você tem algo concreto pra mostrar

---

## 🎯 Checkpoints

**Fim da Fase 1 ✅**
- [x] VM na Oracle Cloud rodando e acessível via SSH
- [x] Exercícios Python (ex01 ao ex04) concluídos e no GitHub
- [x] Conhecimento sólido de Linux, Git e Python aplicado a infra
- [x] Repositório com commits organizados e `.gitignore` configurado

**Fim da Fase 2 (mês 7)**
- [ ] Aplicação rodando em container Docker na VM
- [ ] Pipeline CI/CD no GitHub Actions funcionando
- [ ] Testes automatizados passando no pipeline

**Fim da Fase 3 (mês 12)**
- [ ] Stack Prometheus + Grafana rodando na VM
- [ ] Dashboard com métricas reais acessível pelo browser
- [ ] Base pra entrevista de DevOps Jr / SRE Jr

---

*Criado em abril de 2026 · Atualizado após conclusão da Fase 1*  
*Versione este roadmap no seu GitHub e atualize conforme avançar!*
