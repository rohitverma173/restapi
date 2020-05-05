import requests
from requests.auth import HTTPBasicAuth

import json

# URL to access
#url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
url = "https://172.28.28.74/dna/system/api/v1/auth/token"

#res = requests.post(url, auth=HTTPBasicAuth('devnetuser', 'Cisco123!'))
res = requests.post(url, auth=HTTPBasicAuth('admin', 'Maglev123'))
#print(res.text)

#convert response to json dict
token = res.json()
#print(type(token))
token_val = token['Token']

# Fill in header
headers = {'x-auth-token': token_val}

#url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
url = "https://172.28.28.74/dna/system/api/v1/auth/token"

# params
my_filter = {'type': "Cisco Catalyst 9300 Switch"}

res = requests.get(url, headers=headers, params=my_filter)

#convert response to json dict
res_dict = res.json()

# print IP and MAC of all the 9300 devices.
print("print IP and MAC of all the 9300 devices")
count = 0
while(count<len(res_dict['response'])):
    mac = res_dict['response'][count]['macAddress']
    ip =  res_dict['response'][count]['managementIpAddress']
    print(f"IP: {ip} , MAC: {mac}")
    count = count+1

