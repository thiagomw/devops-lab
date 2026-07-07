# 🚀 devops-lab

Repositório de estudos e projetos práticos da minha jornada do Service Desk ao DevOps Engineer.

![Status](https://img.shields.io/badge/status-em%20andamento-yellow)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-E95420?style=flat&logo=linux&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-C74634?style=flat&logo=oracle&logoColor=white)
![Última atualização](https://img.shields.io/github/last-commit/thiagomw/devops-lab)

---

## 📑 Índice

- [👤 Sobre](#-sobre)
- [🗺️ Roadmap](#️-roadmap)
- [📁 Estrutura do Repositório](#-estrutura-do-repositório)
- [🔍 Cenário 01 — Monitor de Conectividade](#-cenário-01--monitor-de-conectividade)
- [🛠️ Exercícios Python](#️-exercícios-python)
- [🧭 Próximos Cenários](#-próximos-cenários)
- [📋 Boas Práticas Adotadas](#-boas-práticas-adotadas)
- [🔧 Como Rodar](#-como-rodar)
- [📚 Recursos de Estudo](#-recursos-de-estudo)

> 📖 **Quer ver o plano de estudos completo?** Confira o [`roadmap_devops.md`](./roadmap_devops.md) — timeline por fases, checklists de habilidades, cheatsheets de Linux/Git/Python e referências pra cada tecnologia.

---

## 👤 Sobre

Service Desk Engineer na LTM, atendendo cliente ADM em ambiente corporativo Microsoft.
Formado em Redes de Computadores pela FIAP, construindo base técnica em Linux, Python, Docker, CI/CD e Observabilidade com foco em DevOps.

**Infraestrutura de estudo:** Oracle Cloud Free Tier · Ubuntu 22.04 LTS · Python 3.11

---

## 🗺️ Roadmap

| Fase   | Conteúdo                                 | Status         |
| ------ | ---------------------------------------- | -------------- |
| Fase 1 | Linux · Git · Python · VM Oracle Cloud   | ✅ Concluída    |
| Fase 2 | Docker · docker-compose · GitHub Actions | 🔄 Em andamento |
| Fase 3 | Prometheus · Grafana · Observabilidade   | ⏳ Pendente     |
| Fase 4 | Kubernetes · Terraform · IaC             | ⏳ Pendente     |

Cada fase tem material de estudo, checklist de habilidades e um cenário prático rodando em VM real. Detalhes completos no [`roadmap_devops.md`](./roadmap_devops.md).

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
├── cenario-02/                  # Em construção — ver "Próximos Cenários" abaixo
├── cenario-03/                  # Planejado — ver "Próximos Cenários" abaixo
├── exercicios_docker/           # Exercícios progressivos de Docker (Fase 2)
├── roadmap_devops.md            # Plano de estudos completo
└── .gitignore
```

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

**Exemplo de execuções encadeadas rodando via cron:**

```
[2025-05-10 14:30:01] ✅ Google DNS:53 — UP
[2025-05-10 14:30:01] ✅ Cloudflare:53 — UP
[2025-05-10 14:35:01] ✅ Google DNS:53 — UP
[2025-05-10 14:35:01] ❌ GitHub:443 — DOWN (timed out)
[2025-05-10 14:40:01] ✅ Google DNS:53 — UP
[2025-05-10 14:40:01] ✅ GitHub:443 — UP
```

> 💡 **Aprendizado:** o `socket.create_connection()` sem `timeout` explícito trava o script por ~30s quando um host não responde. Um `timeout=3` mata rápido e libera o cron pra próxima execução.

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

## 🧭 Próximos Cenários

Em vez de deixar as pastas vazias com "Em breve", segue o escopo concreto planejado para cada uma. O detalhamento completo (com passo a passo e gabarito) vai pra dentro das pastas conforme cada cenário for construído.

### Cenário 02 — Containerização e CI/CD (em construção)

**Objetivo:** empacotar o `check_hosts.py` do Cenário 01 em um container Docker, versionar a imagem e configurar deploy automático via GitHub Actions.

**Escopo planejado:**

- `Dockerfile` multi-stage pro script Python
- `docker-compose.yml` orquestrando app + volume persistente pros logs
- Publicação da imagem no Docker Hub via GitHub Actions
- Deploy automático na VM Oracle via SSH quando merge na `main`
- Testes com `unittest` rodando no pipeline antes do deploy

**O que quero aprender aqui:** `Dockerfile` bem escrito, secrets no GitHub Actions, artefatos entre jobs, e o ciclo real de "código → build → publish → deploy".

### Cenário 03 — Observabilidade (planejado)

**Objetivo:** enxergar o que está acontecendo no ambiente antes que vire problema.

**Escopo planejado:**

- Instrumentar o `check_hosts.py` com `prometheus_client` (métricas: latência TCP, hosts UP/DOWN, taxa de erro)
- Subir stack Prometheus + Grafana via docker-compose na VM
- Dashboards com histórico de conectividade
- Alertas por threshold (ex.: mais de 3 falhas em 5min)

**O que quero aprender aqui:** modelo pull do Prometheus, PromQL básico, montagem de dashboards que dizem algo, e o mindset "métrica antes de log".

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

**Roadmap**

- [roadmap.sh/devops](https://roadmap.sh/devops) — guia oficial de estudos seguido neste lab

**Linux & Git**

- [Linux Journey](https://linuxjourney.com)
- [Pro Git Book (PT-BR)](https://git-scm.com/book/pt-br/v2)

**Python**

- [Python para Zumbis — YouTube](https://www.youtube.com/playlist?list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc)

**Docker & Kubernetes**

- [TechWorld with Nana — Docker, Kubernetes, DevOps](https://www.youtube.com/@TechWorldwithNana)
- [Docker Getting Started](https://docs.docker.com/get-started/)

**Observabilidade**

- [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)

---

## 📄 Licença

Este projeto está sob licença MIT — veja o arquivo [`LICENSE`](./LICENSE) para detalhes. Sinta-se livre pra usar como referência nos seus próprios estudos.
