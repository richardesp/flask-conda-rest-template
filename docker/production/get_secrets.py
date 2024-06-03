import os
import requests

def get_secret(secret_name):
    url = f"https://api.digitalocean.com/v2/secrets/{secret_name}"
    headers = {
        "Authorization": f"Bearer {os.environ['DIGITALOCEAN_ACCESS_TOKEN']}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['value']

cert = get_secret("my_cert_secret")
key = get_secret("my_key_secret")

with open("/etc/nginx/certs/server.crt", "w") as cert_file:
    cert_file.write(cert)

with open("/etc/nginx/certs/server.key", "w") as key_file:
    key_file.write(key)
