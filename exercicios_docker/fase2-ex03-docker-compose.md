# 🐳 EXERCÍCIO 03 — docker-compose
**Fase 2 · Docker · Nível: Intermediário**

---

## 📋 Contexto

Aplicações reais raramente rodam com um container só — geralmente têm a aplicação, um banco de dados, um cache, um proxy. O `docker-compose` permite definir e orquestrar múltiplos containers num único arquivo YAML.

---

## 🎯 Exercícios

### 3.1 — Primeiro docker-compose.yml

Crie um `docker-compose.yml` que sobe sua aplicação do exercício anterior (`minha-app`) e um container Nginx juntos.

**Dicas:**
- Estrutura básica:
```yaml
version: '3.8'
services:
  nome-do-servico:
    image: ou build:
    ports:
      - "local:container"
```
- Use `build: .` pra buildar sua app local
- Use `image: nginx` pro Nginx

<details>
<summary>👀 Ver gabarito</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: minha-app

  nginx:
    image: nginx
    ports:
      - "8080:80"
    container_name: meu-nginx
```

```bash
docker-compose up --build
# Ctrl+C pra parar
docker-compose down
```

</details>

---

### 3.2 — Variáveis de ambiente no compose

Adicione variáveis de ambiente ao serviço `app` no `docker-compose.yml`.

**Dicas:**
- Use a chave `environment` no serviço
- Ou crie um arquivo `.env` e use `env_file`

<details>
<summary>👀 Ver gabarito — com environment</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: minha-app
    environment:
      - AMBIENTE=producao
      - LOG_LEVEL=info

  nginx:
    image: nginx
    ports:
      - "8080:80"
```

</details>

<details>
<summary>👀 Ver gabarito — com .env</summary>

Crie um arquivo `.env`:
```
AMBIENTE=producao
LOG_LEVEL=info
```

No `docker-compose.yml`:
```yaml
services:
  app:
    build: .
    env_file:
      - .env
```

> ⚠️ Adicione `.env` no `.gitignore` — nunca suba variáveis sensíveis pro GitHub.

</details>

---

### 3.3 — Volumes no compose

Adicione um volume ao serviço `app` pra persistir o arquivo de log gerado pela aplicação.

**Dicas:**
- Use a chave `volumes` no serviço
- Formato: `- ./local:./container`
- O log é salvo em `/app/check_report.log` dentro do container

<details>
<summary>👀 Ver gabarito</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: minha-app
    volumes:
      - ./logs:/app/logs
    environment:
      - AMBIENTE=producao
```

</details>

---

### 3.4 — Depends_on e restart

Configure o serviço `app` para:
- Só iniciar depois do Nginx estar pronto
- Reiniciar automaticamente se cair

**Dicas:**
- `depends_on` define ordem de inicialização
- `restart: always` reinicia sempre que o container cair
- `restart: unless-stopped` reinicia exceto se parado manualmente

<details>
<summary>👀 Ver gabarito</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: minha-app
    restart: unless-stopped
    depends_on:
      - nginx
    environment:
      - AMBIENTE=producao

  nginx:
    image: nginx
    ports:
      - "8080:80"
    container_name: meu-nginx
    restart: unless-stopped
```

</details>

---

### 3.5 — Desafio: stack completa

Monte um `docker-compose.yml` com 3 serviços:
1. Sua aplicação Python
2. Nginx como proxy
3. Um container Redis

Configure volumes, variáveis de ambiente e restart policy em todos.

**Dicas:**
- Redis: `image: redis:alpine`
- Redis expõe a porta `6379`

<details>
<summary>👀 Ver gabarito</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: minha-app
    restart: unless-stopped
    depends_on:
      - redis
    environment:
      - AMBIENTE=producao
    volumes:
      - ./logs:/app/logs

  nginx:
    image: nginx
    ports:
      - "8080:80"
    container_name: meu-nginx
    restart: unless-stopped

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    container_name: meu-redis
    restart: unless-stopped
```

```bash
docker-compose up --build -d
docker-compose ps         # verifica status dos serviços
docker-compose logs app   # logs de um serviço específico
docker-compose down       # derruba tudo
```

</details>

---

## ✅ Como saber se concluiu

- [ ] Consegue escrever um `docker-compose.yml` do zero
- [ ] Sabe usar `build`, `image`, `ports`, `volumes`, `environment`
- [ ] Entende `depends_on` e `restart`
- [ ] Consegue subir, verificar e derrubar uma stack completa
