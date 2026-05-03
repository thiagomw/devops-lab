# 🐳 EXERCÍCIO 02 — Dockerfile
**Fase 2 · Docker · Nível: Intermediário**

---

## 📋 Contexto

Escrever um `Dockerfile` é a habilidade central do Docker — é como você define o ambiente da sua aplicação de forma reproduzível. Qualquer máquina que tenha Docker consegue rodar sua aplicação exatamente igual.

---

## 🎯 Exercícios

### 2.1 — Dockerfile básico

Crie um `Dockerfile` que:
- Parte da imagem `python:3.11-slim`
- Define `/app` como diretório de trabalho
- Copia todos os arquivos para o container
- Instala o `psutil`
- Roda um script `app.py` ao iniciar

Crie também um `app.py` que imprime CPU, memória e disco usando `psutil`.

**Dicas:**
- Instruções: `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`
- `CMD ["python", "app.py"]`
- Build: `docker build -t minha-app .`
- Run: `docker run --rm minha-app`

<details>
<summary>👀 Ver gabarito — Dockerfile</summary>

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install psutil
CMD ["python", "app.py"]
```

</details>

<details>
<summary>👀 Ver gabarito — app.py</summary>

```python
import psutil

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disco = psutil.disk_usage('/').percent

print(f"CPU: {cpu}%")
print(f"Memória: {mem}%")
print(f"Disco: {disco}%")
```

</details>

---

### 2.2 — Layers e cache

O Docker usa cache de layers pra builds mais rápidos. A ordem das instruções importa.

Compare essas duas versões e responda: qual é mais eficiente e por quê?

**Versão A:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install psutil requests
CMD ["python", "app.py"]
```

**Versão B:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

<details>
<summary>👀 Ver resposta</summary>

A **Versão B** é mais eficiente.

Na Versão A, qualquer mudança em qualquer arquivo invalida o cache do `COPY . .` e força o `pip install` a rodar de novo — mesmo que as dependências não tenham mudado.

Na Versão B, o `requirements.txt` é copiado primeiro e as dependências instaladas. O Docker só reinstala as dependências se o `requirements.txt` mudar. Mudanças no código da aplicação não afetam essa layer.

Em projetos reais com muitas dependências, isso economiza minutos a cada build.

</details>

---

### 2.3 — Dockerfile com requirements.txt

Refaça o exercício 2.1 usando a Versão B — com `requirements.txt` separado.

**Dicas:**
- Crie um arquivo `requirements.txt` com `psutil` dentro
- Siga a estrutura da Versão B do exercício anterior

<details>
<summary>👀 Ver gabarito</summary>

`requirements.txt`:
```
psutil
```

`Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

```bash
docker build -t minha-app-v2 .
docker run --rm minha-app-v2
```

</details>

---

### 2.4 — Desafio: variável de ambiente no Dockerfile

Adicione ao `Dockerfile` uma variável de ambiente `AMBIENTE` com valor padrão `"producao"`.  
No `app.py`, imprima o valor dessa variável.  
Rode o container sobrescrevendo o valor para `"desenvolvimento"`.

**Dicas:**
- Instrução `ENV` no Dockerfile define variável padrão
- `os.environ.get("VARIAVEL")` pra ler no Python
- Flag `-e` no `docker run` pra sobrescrever

<details>
<summary>👀 Ver gabarito — Dockerfile</summary>

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV AMBIENTE="producao"
CMD ["python", "app.py"]
```

</details>

<details>
<summary>👀 Ver gabarito — app.py</summary>

```python
import psutil
import os

ambiente = os.environ.get("AMBIENTE", "nao definido")
print(f"Ambiente: {ambiente}")

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disco = psutil.disk_usage('/').percent

print(f"CPU: {cpu}%")
print(f"Memória: {mem}%")
print(f"Disco: {disco}%")
```

</details>

<details>
<summary>👀 Ver gabarito — como rodar</summary>

```bash
# Roda com o valor padrão (producao)
docker run --rm minha-app-v2

# Sobrescreve pra desenvolvimento
docker run --rm -e AMBIENTE="desenvolvimento" minha-app-v2
```

</details>

---

## ✅ Como saber se concluiu

- [ ] Consegue escrever um `Dockerfile` do zero
- [ ] Entende a ordem das instruções e o impacto no cache
- [ ] Sabe usar `requirements.txt` separado
- [ ] Consegue passar e sobrescrever variáveis de ambiente
