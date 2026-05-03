# 🐳 EXERCÍCIO 01 — Docker Básico
**Fase 2 · Docker · Nível: Iniciante**

---

## 📋 Contexto

Antes de containerizar aplicações reais, você precisa dominar os comandos básicos do Docker — rodar containers, inspecionar, parar, remover e entender o que está acontecendo.

---

## 🎯 Exercícios

### 1.1 — Primeiro container

Rode um container Ubuntu interativo, execute `uname -a` dentro dele e saia.

**Dicas:**
- Flag `-it` para modo interativo
- Flag `--rm` para remover o container ao sair
- Comando `bash` para abrir o shell

<details>
<summary>👀 Ver gabarito</summary>

```bash
docker run -it --rm ubuntu bash
# dentro do container:
uname -a
exit
```

</details>

---

### 1.2 — Container em background

Rode um container Nginx em background e confirme que está rodando.

**Dicas:**
- Flag `-d` para rodar em background (detached)
- Flag `-p` para mapear porta: `-p 8080:80`
- `docker ps` para listar containers rodando

<details>
<summary>👀 Ver gabarito</summary>

```bash
docker run -d -p 8080:80 --name meu-nginx nginx
docker ps
```

Acesse `http://localhost:8080` no browser para ver o Nginx rodando.

</details>

---

### 1.3 — Inspecionar e parar

Inspecione o container do Nginx, pare ele e remova.

**Dicas:**
- `docker logs` para ver os logs do container
- `docker stop` para parar
- `docker rm` para remover
- `docker images` para listar imagens

<details>
<summary>👀 Ver gabarito</summary>

```bash
docker logs meu-nginx
docker stop meu-nginx
docker rm meu-nginx
docker images
```

</details>

---

### 1.4 — Variáveis de ambiente

Rode um container passando uma variável de ambiente e imprima ela dentro do container.

**Dicas:**
- Flag `-e` para passar variável de ambiente
- Use a imagem `ubuntu` com o comando `bash -c "echo $VARIAVEL"`

<details>
<summary>👀 Ver gabarito</summary>

```bash
docker run --rm -e MEU_NOME="devops-lab" ubuntu bash -c 'echo $MEU_NOME'
```

</details>

---

### 1.5 — Volume

Rode um container Ubuntu, monte uma pasta local dentro dele e crie um arquivo lá dentro. Confirme que o arquivo aparece na pasta local.

**Dicas:**
- Flag `-v` para montar volume: `-v /caminho/local:/caminho/container`
- Crie uma pasta local antes: `mkdir ~/teste-volume`

<details>
<summary>👀 Ver gabarito</summary>

```bash
mkdir ~/teste-volume
docker run -it --rm -v ~/teste-volume:/dados ubuntu bash
# dentro do container:
echo "arquivo criado no container" > /dados/teste.txt
exit
# de volta na VM:
cat ~/teste-volume/teste.txt
```

</details>

---

## ✅ Como saber se concluiu

- [ ] Conseguiu rodar, inspecionar, parar e remover containers
- [ ] Entende a diferença entre `-it`, `-d`, `-p`, `-e` e `-v`
- [ ] Sabe usar `docker ps`, `docker logs`, `docker images`
