# Ten program printuje twoje IP tylko, nic groźnego, heh..

import requests

def get_public_ip():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify=True)
    if response.status_code != 200:
        return 'Problem with the request. Exiting.'
    data = response.json()
    return data['ip']

my_ip = get_public_ip()
print(f"haha twoje ip zostalo zlekowane, o to one: {my_ip}")

input("skibidi")
