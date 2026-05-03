# ⚙️ EXERCÍCIO 04 — GitHub Actions e CI/CD
**Fase 2 · CI/CD · Nível: Intermediário**

---

## 📋 Contexto

CI/CD automatiza o processo de testar e entregar código. A cada `push` no GitHub, um pipeline roda automaticamente — testa, valida e pode até fazer o deploy. É uma das práticas mais importantes do DevOps moderno.

---

## 🎯 Exercícios

### 4.1 — Primeiro pipeline

Crie um pipeline no GitHub Actions que roda a cada `push` na branch `main` e imprime "Hello DevOps!" no log.

**Dicas:**
- Arquivo em `.github/workflows/ci.yml`
- Estrutura básica:
```yaml
name: Nome do pipeline
on:
  push:
    branches: [ main ]
jobs:
  nome-do-job:
    runs-on: ubuntu-latest
    steps:
      - name: Nome do step
        run: comando
```

<details>
<summary>👀 Ver gabarito</summary>

```yaml
name: Primeiro Pipeline

on:
  push:
    branches: [ main ]

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Hello DevOps
        run: echo "Hello DevOps!"
```

Após o push, acesse seu repositório no GitHub → aba **Actions** → veja o pipeline rodar.

</details>

---

### 4.2 — Pipeline com testes Python

Crie um pipeline que:
1. Faz checkout do código
2. Instala Python 3.11
3. Instala dependências com `pip`
4. Roda os testes com `unittest`

**Dicas:**
- `actions/checkout@v3` para fazer checkout
- `actions/setup-python@v4` para instalar Python
- `python -m unittest discover` para descobrir e rodar todos os testes

<details>
<summary>👀 Ver gabarito</summary>

```yaml
name: CI — Testes Python

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v3

      - name: Instala Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Instala dependências
        run: pip install psutil requests

      - name: Roda os testes
        run: python -m unittest discover -v
```

</details>

---

### 4.3 — Múltiplos jobs

Adicione um segundo job ao pipeline que roda **depois** dos testes passarem e imprime "Deploy simulado com sucesso!".

**Dicas:**
- Use `needs: nome-do-job-anterior` para definir dependência entre jobs
- Jobs sem `needs` rodam em paralelo

<details>
<summary>👀 Ver gabarito</summary>

```yaml
name: CI/CD — Testes e Deploy

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install psutil requests
      - run: python -m unittest discover -v

  deploy:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - name: Deploy simulado
        run: echo "✅ Testes passaram! Deploy simulado com sucesso!"
```

</details>

---

### 4.4 — Secrets no pipeline

Configure o pipeline pra usar um secret do GitHub — simule um token de deploy.

**Dicas:**
- No GitHub: Settings → Secrets and variables → Actions → New repository secret
- No pipeline: `${{ secrets.NOME_DO_SECRET }}`
- Nunca imprima o valor do secret direto — o GitHub mascara automaticamente mas é má prática

<details>
<summary>👀 Ver gabarito</summary>

No GitHub, crie um secret chamado `DEPLOY_TOKEN` com qualquer valor.

No pipeline:
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Usa o token de deploy
        run: |
          if [ -n "${{ secrets.DEPLOY_TOKEN }}" ]; then
            echo "Token configurado — deploy autorizado!"
          else
            echo "Token não encontrado!"
          fi
```

</details>

---

### 4.5 — Desafio: pipeline completo com Docker

Crie um pipeline que:
1. Faz checkout
2. Roda os testes Python
3. Faz build da imagem Docker
4. Verifica que a imagem foi criada com `docker images`

**Dicas:**
- O GitHub Actions já tem Docker disponível no `ubuntu-latest`
- `docker build -t minha-app .` pra buildar
- `docker images` pra listar

<details>
<summary>👀 Ver gabarito</summary>

```yaml
name: CI — Testes + Docker Build

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install psutil requests
      - run: python -m unittest discover -v

  docker-build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v3

      - name: Build da imagem Docker
        run: docker build -t minha-app .

      - name: Verifica imagem criada
        run: docker images minha-app
```

</details>

---

## ✅ Como saber se concluiu

- [ ] Pipeline básico rodando no GitHub Actions
- [ ] Testes Python sendo executados automaticamente a cada push
- [ ] Entende a diferença entre jobs paralelos e sequenciais (`needs`)
- [ ] Sabe configurar e usar secrets no pipeline
- [ ] Pipeline com Docker build funcionando
