import requests

def fetch_cnc_data():
    try:
        res = requests.get("https://api.mocki.io/v1/0a1b2c3d")
        d = res.json()
        return [d["speed"], d["feed"], d["depth"], d["temperature"], d["vibration"]]
    except:
        return None
