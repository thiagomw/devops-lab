# ============================================================
# EXERCÍCIO 4 — Instalando e usando bibliotecas com pip
# Tema: Monitoramento de recursos com psutil e requests
# ============================================================
# Como usar:
# 1. Instale as dependências antes de rodar:
#    pip3 install psutil requests
# 2. Leia o enunciado de cada exercício
# 3. Escreva sua solução abaixo de cada "# SUA SOLUÇÃO:"
# 4. Rode o arquivo: python3 ex04_bibliotecas.py
# 5. Suba pro GitHub quando terminar
# ============================================================

import psutil
import requests
import datetime

# ------------------------------------------------------------
# BIBLIOTECA psutil — Monitoramento de recursos do sistema
# ------------------------------------------------------------

# Exercício 1.1
# Imprima o uso atual de CPU em percentual.
# Dica: psutil.cpu_percent(interval=1)

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 1.2
# Imprima as informações de memória:
# - Total
# - Disponível
# - Percentual usado
# Dica: psutil.virtual_memory()
# Os valores vêm em bytes — divida por (1024**3) pra converter pra GB

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 1.3
# Imprima o uso de disco da partição raiz "/":
# - Total
# - Usado
# - Livre
# - Percentual usado
# Dica: psutil.disk_usage('/')

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 1.4
# Liste os 5 processos que mais consomem memória.
# Imprima no formato: PID | NOME | MEMÓRIA%
# Dica: psutil.process_iter(['pid', 'name', 'memory_percent'])
# Use sorted() pra ordenar por memória

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 1.5 — Desafio
# Crie uma função chamada "snapshot_sistema" que coleta
# CPU, memória e disco e retorna um dicionário com essas infos.
# Depois salve o snapshot em um arquivo "snapshots.log" no formato:
#
# [DATA HORA] CPU: X% | MEM: X% | DISCO: X%
#
# Chame a função 3 vezes com um time.sleep(2) entre cada chamada
# pra ver os valores variando.

import time

# SUA SOLUÇÃO:


# ------------------------------------------------------------
# BIBLIOTECA requests — Fazendo requisições HTTP
# ------------------------------------------------------------

# Exercício 2.1
# Faça uma requisição GET para "https://httpbin.org/get"
# e imprima o status code da resposta.
# Dica: requests.get(url)

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.2
# Faça uma requisição para "https://httpbin.org/get"
# e imprima o campo "origin" do JSON de resposta.
# (Esse campo mostra seu IP público)
# Dica: response.json()

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.3
# Crie uma função chamada "checar_url" que recebe uma URL,
# faz uma requisição GET e retorna:
# - "OK" se o status code for 200
# - "ERRO: X" onde X é o status code, se for diferente de 200
# - "INACESSÍVEL" se der exceção de conexão
#
# Teste com as URLs abaixo:
urls = [
    "https://www.google.com",
    "https://github.com",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://url-que-nao-existe-xyz.com",
]

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.4 — Desafio Final
# Combine psutil + requests:
# Crie uma função chamada "relatorio_completo" que:
# 1. Coleta CPU, memória e disco com psutil
# 2. Verifica se "https://www.google.com" está acessível com requests
# 3. Salva tudo em "relatorio_final.txt" no formato:
#
# ========================================
# RELATÓRIO DO SISTEMA — DATA HORA
# ========================================
# CPU: X%
# Memória: X%
# Disco: X%
# Conectividade Google: OK / INACESSÍVEL
# ========================================
#
# Chame a função ao final do script.

# SUA SOLUÇÃO:
