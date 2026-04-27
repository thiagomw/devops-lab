# ============================================================
# EXERCÍCIO 1 — Funções, Listas, Dicionários, Loops, Condições
# Tema: Simulando um inventário de servidores
# ============================================================
# Como usar:
# - Leia o enunciado de cada exercício
# - Escreva sua solução abaixo de cada comentário "# SUA SOLUÇÃO:"
# - Rode o arquivo: python3 ex01_basico.py
# - Suba pro GitHub quando terminar
# ============================================================

# ------------------------------------------------------------
# NÍVEL 1 — Listas e loops
# ------------------------------------------------------------

# Exercício 1.1
# Você tem uma lista de servidores. Percorra a lista e
# imprima o nome de cada um.

servidores = ["web-01", "web-02", "db-01", "db-02", "cache-01"]

# SUA SOLUÇÃO:

for servidor in servidores:
    print(servidor)

# ------------------------------------------------------------

# Exercício 1.2
# Percorra a lista de servidores e imprima só os que
# começam com "web".
# Dica: use o método .startswith()

# SUA SOLUÇÃO:

for servidor in servidores:
    if servidor.startswith('web'):
        print(servidor)

# ------------------------------------------------------------

# Exercício 1.3
# Crie uma nova lista chamada "servidores_db" contendo
# só os servidores que começam com "db".
# Imprima a nova lista.

# SUA SOLUÇÃO:

servidores_db = []

for servidor in servidores:
    if servidor.startswith('db'):
        servidores_db.append(servidor)
        
print(servidores_db)

# ------------------------------------------------------------
# NÍVEL 2 — Dicionários
# ------------------------------------------------------------

# Exercício 2.1
# Você tem um dicionário com informações de um servidor.
# Imprima cada chave e valor no formato:
# "chave: valor"

servidor = {
    "nome": "web-01",
    "ip": "10.0.0.1",
    "status": "offline",
    "cpu_percent": 90,
    "memoria_percent": 90
}

# SUA SOLUÇÃO:

for chave, valor in servidor.items():
    print(f"{chave}: {valor}")

# ------------------------------------------------------------

# Exercício 2.2
# Usando o dicionário acima, verifique:
# - Se o status é "online", imprima "Servidor operacional"
# - Se o cpu_percent for maior que 80, imprima "ALERTA: CPU alta"
# - Se a memoria_percent for maior que 85, imprima "ALERTA: Memória alta"
# - Se nenhum alerta, imprima "Servidor saudável"

# SUA SOLUÇÃO:

tem_alerta = False

if servidor['status'] == "online":
    print("O Servidor está operacional")

if servidor['cpu_percent'] > 80:
    print("ALERTA: Uso de CPU alto!")
    tem_alerta = True

if servidor['memoria_percent'] > 85:
    print("ALERTAL: Uso de memória alto!")
    tem_alerta = True

if not tem_alerta:
    print("Servidor saudável.")

# ------------------------------------------------------------

# Exercício 2.3
# Você tem uma lista de dicionários — cada um representa um servidor.
# Percorra a lista e imprima só os servidores com status "offline".

frota = [
    {"nome": "web-01", "status": "online"},
    {"nome": "web-02", "status": "offline"},
    {"nome": "db-01",  "status": "online"},
    {"nome": "db-02",  "status": "offline"},
    {"nome": "cache-01", "status": "online"},
]

# SUA SOLUÇÃO:

for servidor in frota:
    if servidor['status'] == "offline":
        print(servidor['nome'])

# ------------------------------------------------------------
# NÍVEL 3 — Funções
# ------------------------------------------------------------

# Exercício 3.1
# Crie uma função chamada "checar_status" que recebe
# um dicionário de servidor e retorna:
# - "ALERTA" se o status for "offline"
# - "OK" se o status for "online"
# Teste chamando a função com cada servidor da lista "frota" acima.

# SUA SOLUÇÃO:

def checar_status(dicionario):

    if dicionario['status'] == "offline":
        status = "ALERTA"
    
    else:
        status = "OK"

    return status

for servidor in frota:
    resultado = checar_status(servidor)
    print(f"{servidor['nome']}: {resultado}")
# ------------------------------------------------------------

# Exercício 3.2
# Crie uma função chamada "resumo_frota" que recebe a lista "frota"
# e imprime um resumo no formato:
#
# === Resumo da Frota ===
# Total de servidores: 5
# Online: 3
# Offline: 2
#
# Chame a função passando a lista "frota".

# SUA SOLUÇÃO:

def resumo_frota(servidores):

    total_servidores = len(servidores)
    servidores_online = 0
    servidores_offline = 0

    for servidor in servidores:
        if servidor['status'] == "online":
            servidores_online += 1
        else:
            servidores_offline += 1

    print(f"=== Resumo da Frota ===\nTotal de servidores: {total_servidores}\n Online: {servidores_online}\n Offline: {servidores_offline}")


resultado = resumo_frota(frota)

# ------------------------------------------------------------

# Exercício 3.3 — Desafio
# Crie uma função chamada "checar_recursos" que recebe
# o dicionário "servidor" (do exercício 2.1) e retorna
# uma lista com todos os alertas encontrados.
# Regras:
# - CPU acima de 80% → adiciona "CPU alta" na lista
# - Memória acima de 85% → adiciona "Memória alta" na lista
# - Status offline → adiciona "Servidor offline" na lista
# - Se não houver alertas → retorna lista vazia
#
# Imprima os alertas encontrados ou "Nenhum alerta" se a lista estiver vazia.

# SUA SOLUÇÃO:

def checar_recursos(servidor):

    alertas = []

    if servidor['cpu_percent'] > 80:
        alertas.append("Uso de CPU alto!")
    
    if servidor['memoria_percent'] > 85:
        alertas.append("Uso de memória alto!")
    
    if servidor['status'] == "offline":
        alertas.append("Servidor offline!")

    return alertas

resultado = checar_recursos(servidor)

if not resultado:
    print("Nenhum alerta!")
else:
    for alerta in resultado:
        print(alerta)