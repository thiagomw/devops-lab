# 🔴 CENÁRIO 3 — Stack completa de monitoramento na VM

**O que você vai praticar:** `prometheus_client` · docker-compose · Grafana na prática

---

## 📋 Contexto

Você vai subir uma stack completa de observabilidade na VM: uma aplicação Python expondo métricas no formato Prometheus, o Prometheus coletando essas métricas, e o Grafana visualizando tudo em dashboards — exatamente o que empresas usam em produção.

---

## 🎯 O que o cenário precisa ter

1. Uma aplicação Python que expõe métricas de CPU, memória e disco via HTTP no formato Prometheus
2. Um `Dockerfile` pra containerizar a aplicação
3. Um `docker-compose.yml` subindo app + Prometheus + Grafana
4. Um `prometheus.yml` configurando o scraping da aplicação
5. Dashboard configurado no Grafana com as métricas

---

## 💡 Dicas

- Biblioteca: `prometheus_client` — instale com `pip3 install prometheus_client psutil`
- Use `Gauge` para métricas que sobem e descem (CPU, memória, disco)
- `start_http_server(8000)` expõe as métricas em `http://localhost:8000/metrics`
- O Prometheus usa modelo **pull** — ele que vai buscar as métricas na aplicação
- No `docker-compose`, o Prometheus acessa a app pelo nome do serviço (`app:8000`), não por `localhost`
- Lembre de abrir as portas `8000`, `9090` e `3000` no firewall da Oracle Cloud e na VM

---

## 🖥️ Passo a Passo na VM

**Passo 1 — Prepare o projeto**
```bash
cd ~/devops-lab
mkdir cenario-03
cd cenario-03
pip3 install prometheus_client psutil
```

**Passo 2 — Abra as portas no firewall da Oracle Cloud**

Na Oracle Cloud: **Networking → VCN → Security Lists → Ingress Rules**  
Adicione regras TCP para as portas `8000`, `9090` e `3000` com source `0.0.0.0/0`

Na própria VM:
```bash
sudo iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 9090 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
```

**Passo 3 — Crie os arquivos**

> Tente fazer você mesmo antes de ver o gabarito!

<details>
<summary>👀 Ver gabarito — app_metricas.py</summary>

```python
# app_metricas.py
from prometheus_client import start_http_server, Gauge
import psutil
import time

cpu_gauge   = Gauge('vm_cpu_percent',     'Uso de CPU da VM em %')
mem_gauge   = Gauge('vm_memoria_percent', 'Uso de memória da VM em %')
disco_gauge = Gauge('vm_disco_percent',   'Uso de disco da VM em %')

def coletar():
    cpu_gauge.set(psutil.cpu_percent(interval=1))
    mem_gauge.set(psutil.virtual_memory().percent)
    disco_gauge.set(psutil.disk_usage('/').percent)

if __name__ == '__main__':
    start_http_server(8000)
    print("📊 Métricas disponíveis em http://localhost:8000/metrics")
    while True:
        coletar()
        time.sleep(5)
```

</details>

<details>
<summary>👀 Ver gabarito — Dockerfile</summary>

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app_metricas.py .
RUN pip install prometheus_client psutil
CMD ["python", "app_metricas.py"]
```

</details>

<details>
<summary>👀 Ver gabarito — docker-compose.yml</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    container_name: app-metricas

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    container_name: prometheus

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin123
    container_name: grafana
```

</details>

<details>
<summary>👀 Ver gabarito — prometheus.yml</summary>

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'app-metricas'
    static_configs:
      - targets: ['app:8000']
```

</details>

---

**Passo 4 — Suba a stack**
```bash
docker-compose up --build -d
```

**Passo 5 — Verifique**

Acesse pelo browser:
- Métricas brutas: `http://SEU_IP:8000/metrics`
- Prometheus: `http://SEU_IP:9090`
- Grafana: `http://SEU_IP:3000` (admin / admin123)

**Passo 6 — Configure o Grafana**

1. Acesse o Grafana no browser
2. Vá em **Configuration → Data Sources → Add data source**
3. Escolha **Prometheus**
4. URL: `http://prometheus:9090`
5. Clique em **Save & Test**
6. Vá em **Dashboards → New Dashboard → Add visualization**
7. No campo de query, digite: `vm_cpu_percent`
8. Repita para `vm_memoria_percent` e `vm_disco_percent`

**Passo 7 — Versione**
```bash
cd ~/devops-lab
git add .
git commit -m "feat: cenario-03 - stack prometheus + grafana na VM"
git push origin main
```

---

## ✅ Como saber se concluiu

- [ ] Stack subindo sem erros com `docker-compose up`
- [ ] Métricas acessíveis em `http://SEU_IP:8000/metrics`
- [ ] Prometheus coletando as métricas (`http://SEU_IP:9090`)
- [ ] Dashboard no Grafana exibindo CPU, memória e disco em tempo real
- [ ] Commit no GitHub com todos os arquivos versionados
