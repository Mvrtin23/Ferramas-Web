import requests

def get_dolar_value():
    url = 'https://mindicador.cl/api/dolar'
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        # El valor más reciente está en data['serie'][0]['valor']
        return data['serie'][0]['valor']
    except Exception as e:
        print("Error consultando mindicador:", e)
        return None