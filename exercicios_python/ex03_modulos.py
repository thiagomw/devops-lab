# ============================================================
# EXERCÍCIO 3 — Módulos os, subprocess e socket
# Tema: Automação e verificação de infraestrutura
# ============================================================
# Como usar:
# - Leia o enunciado de cada exercício
# - Escreva sua solução abaixo de cada comentário "# SUA SOLUÇÃO:"
# - Rode o arquivo: python3 ex03_modulos.py
# - Suba pro GitHub quando terminar
# ============================================================

import os
import subprocess
import socket

# ------------------------------------------------------------
# MÓDULO os — Interagindo com o sistema de arquivos
# ------------------------------------------------------------

# Exercício 1.1
# Imprima o diretório atual onde o script está rodando.
# Dica: os.getcwd()

# SUA SOLUÇÃO:

diretorio_atual = os.getcwd()
# print(diretorio_atual)

# ------------------------------------------------------------

# Exercício 1.2
# Crie uma estrutura de diretórios chamada:
# logs/2026/abril
# Usando os.makedirs() com exist_ok=True

# SUA SOLUÇÃO:

diretorio = "logs/2026/abril"

# os.makedirs(diretorio, exist_ok=True)
# print(f"Diretório {diretorio} já existe.")

# ------------------------------------------------------------

# Exercício 1.3
# Liste todos os arquivos do diretório atual e imprima
# só os que terminam com ".py" ou ".txt"
# Dica: os.listdir()

# SUA SOLUÇÃO:

arquivos = os.listdir(diretorio_atual)
# for arquivo in arquivos:
#     if arquivo.endswith('.py') or arquivo.endswith('.txt'):
#         print(arquivo)

# ------------------------------------------------------------

# Exercício 1.4
# Verifique se o diretório "logs/2026/abril" existe.
# Se existir, imprima "Diretório encontrado"
# Se não existir, imprima "Diretório não encontrado"
# Dica: os.path.exists()

# SUA SOLUÇÃO:

diretorio_existe = os.path.exists(diretorio)

if diretorio_existe:
    print("Diretório encontrado")
else:
    print("Diretório não encontrado")

# ------------------------------------------------------------
# MÓDULO subprocess — Rodando comandos do sistema
# ------------------------------------------------------------

# Exercício 2.1
# Use subprocess para rodar o comando "uname -a" e
# imprima o resultado.
# Dica: subprocess.run() com capture_output=True e text=True

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.2
# Use subprocess para rodar o comando "df -h" (uso de disco)
# e imprima a saída completa.

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.3
# Use subprocess para rodar o comando "free -h" (uso de memória)
# e imprima só a linha que contém "Mem:"
# Dica: percorra as linhas da saída com .splitlines()

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.4 — Desafio
# Crie uma função chamada "rodar_comando" que:
# - Recebe um comando como string (ex: "ls -la")
# - Roda o comando com subprocess
# - Retorna a saída se der certo
# - Retorna a mensagem de erro se falhar
# - Trate exceções com try/except
#
# Teste com pelo menos 3 comandos, incluindo um inválido.

# SUA SOLUÇÃO:


# ------------------------------------------------------------
# MÓDULO socket — Verificando conectividade
# ------------------------------------------------------------

# Exercício 3.1
# Verifique se o host "8.8.8.8" na porta 53 está acessível.
# Imprima "Acessível" ou "Inacessível".
# Dica: socket.create_connection() com timeout=3

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 3.2
# Crie uma função chamada "checar_host" que recebe
# host e porta, tenta conectar com timeout de 3 segundos
# e retorna True se acessível ou False se não.

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 3.3 — Desafio Final
# Usando a função "checar_host" do exercício anterior,
# verifique todos os hosts abaixo e gere um relatório
# salvo em "relatorio_conectividade.txt" no formato:
#
# [DATA HORA] HOST:PORTA — STATUS
#
# hosts = [
#     ("8.8.8.8", 53),
#     ("1.1.1.1", 53),
#     ("github.com", 443),
#     ("localhost", 80),
#     ("oracle.com", 443),
# ]

hosts = [
    ("8.8.8.8", 53),
    ("1.1.1.1", 53),
    ("github.com", 443),
    ("localhost", 80),
    ("oracle.com", 443),
]

# SUA SOLUÇÃO:
