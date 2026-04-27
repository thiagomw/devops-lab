# ============================================================
# EXERCÍCIO 2 — Ler e Escrever Arquivos
# Tema: Geração e leitura de logs de sistema
# ============================================================
# Como usar:
# - Leia o enunciado de cada exercício
# - Escreva sua solução abaixo de cada comentário "# SUA SOLUÇÃO:"
# - Rode o arquivo: python3 ex02_arquivos.py
# - Suba pro GitHub quando terminar
# ============================================================

import datetime

# ------------------------------------------------------------
# NÍVEL 1 — Escrita de arquivos
# ------------------------------------------------------------

# Exercício 1.1
# Crie um arquivo chamado "servidores.txt" e escreva
# um servidor por linha:
# web-01
# web-02
# db-01
# db-02
# cache-01

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 1.2
# Crie um arquivo chamado "log.txt" e escreva 5 linhas de log
# no formato: [DATA HORA] INFO mensagem
# Use datetime.datetime.now() pra pegar a data/hora atual
# Exemplo: [2026-04-23 21:00:00] INFO Servidor web-01 iniciado

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 1.3
# Abra o arquivo "log.txt" que você criou e ADICIONE
# (sem apagar o que já tem) mais 3 linhas de log com
# nível "WARNING".
# Dica: use o modo "a" no open()

# SUA SOLUÇÃO:


# ------------------------------------------------------------
# NÍVEL 2 — Leitura de arquivos
# ------------------------------------------------------------

# Exercício 2.1
# Leia o arquivo "servidores.txt" que você criou
# e imprima cada linha sem o \n no final.
# Dica: use .strip()

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.2
# Leia o arquivo "log.txt" e imprima só as linhas
# que contêm a palavra "WARNING".

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 2.3
# Leia o arquivo "log.txt" e conte quantas linhas
# têm nível "INFO" e quantas têm nível "WARNING".
# Imprima o resultado no formato:
# INFO: X ocorrências
# WARNING: X ocorrências

# SUA SOLUÇÃO:


# ------------------------------------------------------------
# NÍVEL 3 — Combinando leitura e escrita
# ------------------------------------------------------------

# Exercício 3.1
# Leia o arquivo "servidores.txt" e crie um novo arquivo
# chamado "relatorio.txt" com o seguinte formato pra cada servidor:
#
# Servidor: web-01 | Status: verificado | Data: 2026-04-23

# SUA SOLUÇÃO:


# ------------------------------------------------------------

# Exercício 3.2 — Desafio
# Crie uma função chamada "gerar_log" que recebe:
# - nivel: "INFO", "WARNING" ou "ERROR"
# - mensagem: texto da mensagem
# E escreve uma linha no arquivo "sistema.log" no formato:
# [DATA HORA] NIVEL mensagem
#
# Chame a função pelo menos 6 vezes com níveis e mensagens variados.
# Depois leia o arquivo e imprima só as linhas de ERROR.

# SUA SOLUÇÃO:
