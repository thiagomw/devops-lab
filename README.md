# 🚀 devops-lab

Repositório de estudos e projetos práticos da minha jornada do Service Desk ao DevOps Engineer.

![Status](https://img.shields.io/badge/status-em%20andamento-yellow)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-E95420?style=flat&logo=linux&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-C74634?style=flat&logo=oracle&logoColor=white)

---

## 👤 Sobre

Service Desk Engineer na LTM, atendendo cliente ADM em ambiente corporativo Microsoft.
Formado em Redes de Computadores pela FIAP, construindo base técnica em Linux, Python, Docker, CI/CD e Observabilidade com foco em DevOps.

**Infraestrutura de estudo:** Oracle Cloud Free Tier · Ubuntu 22.04 LTS · Python 3.11

---

## 📁 Estrutura do Repositório

```
devops-lab/
├── exercicios_python/
│   ├── ex01_basico.py          # Funções, listas, dicionários, loops, condições
│   ├── ex02_arquivos.py        # Leitura e escrita de arquivos
│   ├── ex03_modulos.py         # Módulos os, subprocess e socket
│   └── ex04_bibliotecas.py     # pip, psutil e requests
├── cenario-01/
│   ├── check_hosts.py          # Monitor de conectividade com geração de log
│   └── check_report.log        # Log gerado automaticamente (ignorado pelo git)
├── cenario-02/                  # Em breve — Docker + CI/CD
├── cenario-03/                  # Em breve — Prometheus + Grafana
└── .gitignore
```

---

## 🗺️ Roadmap

| Fase | Conteúdo | Status |
|------|----------|--------|
| Fase 1 | Linux · Git · Python · VM Oracle Cloud | ✅ Concluída |
| Fase 2 | Docker · docker-compose · GitHub Actions | 🔄 Em andamento |
| Fase 3 | Prometheus · Grafana · Observabilidade | ⏳ Pendente |
| Fase 4 | Kubernetes · Terraform · IaC | ⏳ Pendente |

---

## 🔍 Cenário 01 — Monitor de Conectividade

Script Python rodando em VM Ubuntu na Oracle Cloud que verifica a conectividade de hosts via socket TCP e gera um log com timestamp, status e ícone de resultado.

**Hosts monitorados:** Google DNS (8.8.8.8), Cloudflare (1.1.1.1), GitHub e Oracle Cloud

**Saída gerada:**
```
[2025-05-10 14:32:01] ✅ Google DNS:53 — UP
[2025-05-10 14:32:01] ✅ Cloudflare:53 — UP
[2025-05-10 14:32:01] ✅ GitHub:443 — UP
[2025-05-10 14:32:01] ✅ Oracle Cloud:443 — UP
```

**Conceitos aplicados:**
- `socket.create_connection()` com timeout para verificação TCP
- Geração de log em arquivo com `open()` no modo append
- Timestamp com `datetime`
- Tratamento de erros com `try/except`
- Estrutura de dados com lista de dicionários

**Como rodar:**
```bash
python3 cenario-01/check_hosts.py
```

**Para automatizar com cron (a cada 5 minutos):**
```bash
crontab -e
# adicionar a linha:
*/5 * * * * /usr/bin/python3 /home/ubuntu/devops-lab/cenario-01/check_hosts.py
```

---

## 🛠️ Exercícios Python

Exercícios progressivos com foco em automação de infraestrutura.

### ex01_basico.py
Fundamentos de Python aplicados a inventário de servidores:
- Listas e loops — percorrer e filtrar servidores
- Dicionários — estrutura de dados de servidor (nome, IP, status, CPU, memória)
- Funções com separação de responsabilidades
- Verificação de alertas com thresholds

### ex02_arquivos.py
Leitura e escrita de arquivos — base de qualquer automação de log:
- Criar e escrever arquivos com `open()` nos modos `w`, `a`, `r`
- Gerar logs no formato `[DATA HORA] NIVEL mensagem`
- Filtrar linhas por nível (INFO, WARNING, ERROR)
- Função `gerar_log()` reutilizável

### ex03_modulos.py
Módulos da biblioteca padrão para automação de infra:
- `os` — manipulação de diretórios e arquivos do sistema
- `subprocess` — execução de comandos do sistema operacional
- `socket` — verificação de conectividade em hosts e portas
- Desafio: relatório de conectividade salvo em arquivo

### ex04_bibliotecas.py
Bibliotecas externas com pip:
- `psutil` — monitoramento de CPU, memória, disco e processos
- `requests` — requisições HTTP e verificação de URLs
- Desafio: relatório completo combinando psutil + requests

---

## 📋 Boas Práticas Adotadas

- `encoding="utf-8"` em todos os `open()` — evita problemas com acentos
- `if __name__ == "__main__"` — separa código executável de módulo importável
- `.gitignore` configurado — arquivos gerados (`.txt`, `.log`) não entram no repositório
- Separação de responsabilidades — funções com responsabilidade única
- `try/except` em operações de I/O e rede
- Commits semânticos: `feat:`, `fix:`, `chore:`

---

## 🔧 Como Rodar

```bash
# Clone o repositório
git clone https://github.com/thiagomw/devops-lab.git
cd devops-lab

# Instale as dependências Python
pip3 install psutil requests

# Execute os exercícios
python3 exercicios_python/ex01_basico.py
python3 exercicios_python/ex02_arquivos.py
python3 exercicios_python/ex03_modulos.py
python3 exercicios_python/ex04_bibliotecas.py

# Execute o monitor de conectividade
python3 cenario-01/check_hosts.py
```

---

## 📚 Recursos de Estudo

- [Linux Journey](https://linuxjourney.com)
- [Pro Git Book (PT-BR)](https://git-scm.com/book/pt-br/v2)
- [Python para Zumbis — YouTube](https://www.youtube.com/playlist?list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc)
- [TechWorld with Nana — Docker, Kubernetes, DevOps](https://www.youtube.com/@TechWorldwithNana)
- [Docker Getting Started](https://docs.docker.com/get-started/)
- [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)
