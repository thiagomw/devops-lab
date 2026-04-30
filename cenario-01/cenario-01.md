# 🟢 CENÁRIO 1 — Verificador de conectividade rodando na VM

**O que você vai praticar:** Linux na VM · Python com `socket` · Git · `cron`

---

## 📋 Contexto

Você tem uma VM rodando na Oracle Cloud. O objetivo é criar um script Python que verifica se uma lista de hosts está respondendo, salva um relatório em arquivo e roda automaticamente de tempos em tempos via `cron`.

---

## 🎯 O que o script precisa fazer

1. Ter uma lista de hosts com nome, endereço e porta
2. Tentar conectar em cada host com timeout de 3 segundos
3. Registrar se cada host está `UP` ou `DOWN`
4. Salvar o resultado em `check_report.txt` com timestamp
5. Imprimir o resultado no terminal também

---

## 💡 Dicas

- Módulo: `socket` — função `socket.create_connection((host, porta), timeout=3)`
- Se conectar → `UP`, se lançar exceção → `DOWN`
- Use `datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")` pro timestamp
- Abra o arquivo com modo `"a"` e `encoding="utf-8"`
- Trate exceções com `try/except`

---

## 🖥️ Passo a Passo na VM

**Passo 1 — Conecte na VM**
```bash
ssh ubuntu@SEU_IP_PUBLICO -i sua_chave.key
```

**Passo 2 — Prepare o projeto**
```bash
cd ~/devops-lab
mkdir cenario-01
cd cenario-01
nano check_hosts.py
```

**Passo 3 — Escreva o script**

> Tente fazer você mesmo antes de ver o gabarito!

<details>
<summary>👀 Ver gabarito — clique só se precisar</summary>

```python
# check_hosts.py
import socket
import datetime
import os

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

log_file = os.path.join(os.path.dirname(__file__), "check_report.txt")
with open(log_file, "a", encoding="utf-8") as f:
    f.write("\n".join(results) + "\n\n")
```

</details>

---

**Passo 4 — Rode e teste**
```bash
python3 check_hosts.py
cat check_report.txt
```

**Passo 5 — Agende com cron**
```bash
crontab -e
```

<details>
<summary>👀 Ver configuração do cron — clique só se precisar</summary>

Adicione essa linha no arquivo:
```
*/5 * * * * python3 /home/ubuntu/devops-lab/cenario-01/check_hosts.py
```

Isso roda o script a cada 5 minutos automaticamente.

Confirme o agendamento:
```bash
crontab -l
```

Aguarde 5 minutos e verifique:
```bash
cat ~/devops-lab/cenario-01/check_report.txt
```

</details>

---

**Passo 6 — Versione no GitHub**
```bash
cd ~/devops-lab
git add .
git commit -m "feat: cenario-01 - verificador de conectividade com cron"
git push origin main
```

---

## ✅ Como saber se concluiu

- [ ] Script rodando e imprimindo resultado no terminal
- [ ] Arquivo `check_report.txt` sendo gerado com timestamp
- [ ] Cron agendado e acumulando novas entradas a cada 5 minutos
- [ ] Commit no GitHub com o script versionado
