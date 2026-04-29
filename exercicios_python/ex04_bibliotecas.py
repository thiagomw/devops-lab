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
import time

# ------------------------------------------------------------
# BIBLIOTECA psutil — Monitoramento de recursos do sistema
# ------------------------------------------------------------

# Exercício 1.1
# Imprima o uso atual de CPU em percentual.
# Dica: psutil.cpu_percent(interval=1)

# SUA SOLUÇÃO:

uso_cpu = psutil.cpu_percent(interval=1)
print(uso_cpu)

# ------------------------------------------------------------

# Exercício 1.2
# Imprima as informações de memória:
# - Total
# - Disponível
# - Percentual usado
# Dica: psutil.virtual_memory()
# Os valores vêm em bytes — divida por (1024**3) pra converter pra GB

# SUA SOLUÇÃO:

info_memoria = psutil.virtual_memory()
print(f"=== Infomações Memória ===\nTotal: {info_memoria.total / (1024 ** 3):.2f}GB\nDisponível: {info_memoria.available / (1024 ** 3):.2f}GB\nPercentual usado: {info_memoria.percent}%")

# ------------------------------------------------------------

# Exercício 1.3
# Imprima o uso de disco da partição raiz "/":
# - Total
# - Usado
# - Livre
# - Percentual usado
# Dica: psutil.disk_usage('/')

# SUA SOLUÇÃO:

info_disco = psutil.disk_usage('/')
print(f"=== Infomações Disco ===\nTotal: {info_disco.total / (1024 ** 3):.2f}\nUsado: {info_disco.used / (1024 ** 3):.2f}\nLivre: {info_disco.free / (1024 ** 3):.2f}\nPercentual usado: {info_disco.percent}%")

# ------------------------------------------------------------

# Exercício 1.4
# Liste os 5 processos que mais consomem memória.
# Imprima no formato: PID | NOME | MEMÓRIA%
# Dica: psutil.process_iter(['pid', 'name', 'memory_percent'])
# Use sorted() pra ordenar por memória

# SUA SOLUÇÃO:

processos = psutil.process_iter(['pid', 'name', 'memory_percent'])
top_processos = sorted(processos, key=lambda p: p.info['memory_percent'], reverse=True)

print("=== Top 5 processos mais utilizados no momento: ===")
for processo in top_processos[:5]:
    print(f"{processo.info['pid']} | {processo.info['name']} | {processo.info['memory_percent']}%")

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

# SUA SOLUÇÃO:

def snapshot_sistema():

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        uso_cpu = psutil.cpu_percent(interval=1)
        info_memoria = psutil.virtual_memory()
        info_disco = psutil.disk_usage('/')

        with open("snapshots.log", "a", encoding="utf-8") as f:
            f.write(f"[{data_hora}] CPU:{uso_cpu}% | MEM:{info_memoria.percent}% | DISCO:{info_disco.percent}%\n")
    except Exception as e:
        print(f"Erro inesperado: {e}")

snapshot_sistema()
time.sleep(2)
snapshot_sistema()
time.sleep(2)
snapshot_sistema()

# ------------------------------------------------------------
# BIBLIOTECA requests — Fazendo requisições HTTP
# ------------------------------------------------------------

# Exercício 2.1
# Faça uma requisição GET para "https://httpbin.org/get"
# e imprima o status code da resposta.
# Dica: requests.get(url)

# SUA SOLUÇÃO:

url = "https://httpbin.org/get"
try:
    requisicao = requests.get(url)
    print(requisicao.status_code)
except Exception as e:
    print(f"Erro inesperado: {e}")

# ------------------------------------------------------------

# Exercício 2.2
# Faça uma requisição para "https://httpbin.org/get"
# e imprima o campo "origin" do JSON de resposta.
# (Esse campo mostra seu IP público)
# Dica: response.json()

# SUA SOLUÇÃO:

try:
    requisicao_json = requisicao.json()
    print(requisicao_json.get("origin"))
except Exception as e:
    print(f"Erro inesperado: {e}")

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

def checar_url(url):
    try:
        requisicao_urls = requests.get(url)
        if requisicao_urls.status_code == 200:
            print(f"OK")
        else:
            print(f"ERRO: {requisicao_urls.status_code}")
    except Exception as e:
        print(f"INACESSÍVEL: {e}")

for url in urls:
    checar_url(url)

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

def relatorio_completo():

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        url = "https://www.google.com"
        uso_cpu = psutil.cpu_percent(interval=1)
        info_memoria = psutil.virtual_memory()
        info_disco = psutil.disk_usage('/')

        requisicao_url = requests.get(url)
        conectividade = "OK" if requisicao_url.status_code == 200 else "INACESSÍVEL"

        with open("relatorio_final.txt", "a", encoding="utf-8") as f:
            f.write(f"============================================\nRELATÓRIO DO SISTEMA — {data_hora}\n============================================\nCPU: {uso_cpu}%\nMemória: {info_memoria.percent}%\nDisco: {info_disco.percent}%\nConectividade Google: {conectividade}\n============================================")
    except Exception as e:
        print(f"Erro inesperado: {e}")

relatorio_completo()