# 🟡 CENÁRIO 2 — Aplicação containerizada com pipeline CI/CD

**O que você vai praticar:** Docker · docker-compose · GitHub Actions · testes com `unittest`

---

## 📋 Contexto

Você vai containerizar uma aplicação Python de monitoramento usando Docker, e criar um pipeline CI/CD no GitHub Actions que roda os testes automaticamente a cada `push` — exatamente como times de DevOps fazem em produção.

---

## 🎯 O que o cenário precisa ter

1. Uma aplicação Python que coleta métricas do sistema (`monitor.py`)
2. Testes automatizados para a aplicação (`test_monitor.py`)
3. Um `Dockerfile` pra containerizar a aplicação
4. Um pipeline no GitHub Actions que roda os testes a cada push

---

## 💡 Dicas

- Use `psutil` pra coletar CPU, memória e disco
- A função principal deve retornar um dicionário com as métricas
- O `Dockerfile` parte de `python:3.11-slim`
- O pipeline usa `ubuntu-latest` como runner
- Testes com `unittest` — métodos começam com `test_`

---

## 🖥️ Passo a Passo na VM

**Passo 1 — Instale Docker**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
exit
# Reconecte na VM para aplicar o grupo docker
ssh ubuntu@SEU_IP -i sua_chave.key
docker --version
docker run hello-world
sudo apt install docker-compose -y
```

**Passo 2 — Prepare o projeto**
```bash
cd ~/devops-lab
mkdir cenario-02
cd cenario-02
```

**Passo 3 — Crie os arquivos**

> Tente fazer você mesmo antes de ver o gabarito!

<details>
<summary>👀 Ver gabarito — monitor.py</summary>

```python
# monitor.py
import psutil
import datetime

def coletar_metricas():
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memoria_percent": psutil.virtual_memory().percent,
        "disco_percent": psutil.disk_usage('/').percent,
    }

if __name__ == "__main__":
    metricas = coletar_metricas()
    for chave, valor in metricas.items():
        print(f"{chave}: {valor}")
```

</details>

<details>
<summary>👀 Ver gabarito — test_monitor.py</summary>

```python
# test_monitor.py
import unittest
from monitor import coletar_metricas

class TestMonitor(unittest.TestCase):
    def test_retorna_dicionario(self):
        self.assertIsInstance(coletar_metricas(), dict)

    def test_chaves_presentes(self):
        resultado = coletar_metricas()
        self.assertIn("cpu_percent", resultado)
        self.assertIn("memoria_percent", resultado)
        self.assertIn("disco_percent", resultado)

    def test_valores_validos(self):
        resultado = coletar_metricas()
        self.assertTrue(0 <= resultado["cpu_percent"] <= 100)
        self.assertTrue(0 <= resultado["memoria_percent"] <= 100)
        self.assertTrue(0 <= resultado["disco_percent"] <= 100)

if __name__ == "__main__":
    unittest.main()
```

</details>

<details>
<summary>👀 Ver gabarito — Dockerfile</summary>

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install psutil
CMD ["python", "monitor.py"]
```

</details>

<details>
<summary>👀 Ver gabarito — .github/workflows/ci.yml</summary>

```yaml
name: CI — Testa o monitor

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install psutil
      - run: python -m unittest test_monitor.py -v
```

</details>

---

**Passo 4 — Build e teste local**
```bash
docker build -t meu-monitor .
docker run meu-monitor
```

**Passo 5 — Versione e veja o pipeline rodar**
```bash
cd ~/devops-lab
git add .
git commit -m "feat: cenario-02 - monitor containerizado com CI/CD"
git push origin main
```

> Acesse seu repositório no GitHub → aba **Actions** → veja o pipeline rodar em tempo real.

---

## ✅ Como saber se concluiu

- [ ] Container buildando e rodando sem erros
- [ ] Testes passando localmente com `python -m unittest test_monitor.py -v`
- [ ] Pipeline verde no GitHub Actions após o push
- [ ] Commit no GitHub com todos os arquivos versionados
