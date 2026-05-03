import socket
import datetime
import os

hosts = [
    {"name": "Google DNS", "host": "8.8.8.8", "port": 53},
    {"name": "Cloudflare", "host": "1.1.1.1", "port": 53},
    {"name": "GitHub", "host": "github.com", "port": 443},
    {"name": "Oracle Cloud", "host": "oracle.com", "port": 443},
]



def check_hosts(hosts):

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultados = []

    with open ("/home/ubuntu/devops-lab/cenario-01/check_report.log", "a") as f:
        for host in hosts:
            try:
                conexao = socket.create_connection((host["host"], host["port"]), timeout=3)
                conexao.close()
                status, icone = "UP", "✅"
            except Exception:
                status, icone = "DOWN", "❌"

            resultado = f"[{data_hora}] {icone} {host['name']}:{host['port']} — {status}"
            resultados.append(resultado)
            print(resultado)

            f.write(f"{resultado}\n")

if __name__ == "__main__":

    check_hosts(hosts)