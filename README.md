# 🚀 devops-lab

Repositório de estudos e projetos práticos da minha jornada do Service Desk ao DevOps Engineer.

## 👤 Sobre

Formado em Tecnologia de Redes (FIAP), atualmente Service Desk em empresa de IA (LTM/LTIMindTree).  
Construindo base técnica em Linux, Python, Docker, CI/CD e Observabilidade com foco em DevOps.

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
│   └── check_hosts.py          # Verificador de conectividade com cron
├── cenario-02/                  # Em breve — Docker + CI/CD
├── cenario-03/                  # Em breve — Prometheus + Grafana
└── .gitignore
```

---

## 🗺️ Roadmap

| Fase | Conteúdo | Status |
|---|---|---|
| **Fase 1** | Linux · Git · Python · VM Oracle Cloud | ✅ Concluída |
| **Fase 2** | Docker · docker-compose · GitHub Actions | 🔄 Em andamento |
| **Fase 3** | Prometheus · Grafana · Observabilidade | ⏳ Pendente |
| **Fase 4** | Kubernetes · Terraform · IaC | ⏳ Pendente |

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
- Filtrar linhas por nível (`INFO`, `WARNING`, `ERROR`)
- Função `gerar_log()` reutilizável

### ex03_modulos.py
Módulos da biblioteca padrão para automação de infra:
- `os` — manipulação de diretórios e arquivos do sistema
- `subprocess` — execução de comandos do sistema operacional
- `socket` — verificação de conectividade em hosts e portas
- Desafio: relatório de conectividade salvo em arquivo

### ex04_bibliotecas.py
Bibliotecas externas com `pip`:
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
git clone https://github.com/SEU_USUARIO/devops-lab.git
cd devops-lab

# Instale as dependências Python
pip3 install psutil requests

# Execute os exercícios
python3 exercicios_python/ex01_basico.py
python3 exercicios_python/ex02_arquivos.py
python3 exercicios_python/ex03_modulos.py
python3 exercicios_python/ex04_bibliotecas.py
```

---

## 📚 Recursos de Estudo

- [Linux Journey](https://linuxjourney.com)
- [Pro Git Book (PT-BR)](https://git-scm.com/book/pt-br/v2)
- [Python para Zumbis](https://www.youtube.com/watch?v=YO58tXerKDc) — YouTube
- [TechWorld with Nana](https://www.youtube.com/@TechWorldwithNana) — Docker, Kubernetes, DevOps
- [Docker Getting Started](https://docs.docker.com/get-started)
- [Prometheus Docs](https://prometheus.io/docs)

---

*Atualizado em abril de 2026 · Fase 1 concluída*
