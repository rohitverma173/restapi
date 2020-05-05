import requests

payload = {'fname': 'rohit', 'lname': 'verma'}

url = "https://httpbin.org/post"

r = requests.post(url,data=payload)
print(r.content)


print('api authentication example')

url = "https://httpbin.org/basic-auth/admin/PASS"

r = requests.get(url,auth=('admin','PASS'))

print(r)

print('api call with timeout example working case')

r = requests.get('https://httpbin.org/delay/2',timeout=3)
print(r)

print('api call with timeout example timeout case')

r = requests.get('https://httpbin.org/delay/5',timeout=3)
print(r)



