"""
Esse script serve como auxiliar para popular a API do produtor de eventos.
Ele faz requisições POST a cada 2 minutos para gerar eventos de equipamentos
e enviá-los ao Databricks através do endpoint de sql.
"""

import time
import requests

if __name__ == "__main__":
    while True:
        try:
            response = requests.post("http://api:8000/produce", timeout=10)
            if response.status_code == 200:
                print("feito")
            else:
                print(f"Failed to produce event. Status code: {response.status_code}")
            time.sleep(120)
        except Exception as e:
            print(f"Error producing event: {e}")
            time.sleep(10)
            continue
