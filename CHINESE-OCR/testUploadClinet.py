import requests
requests.adapters.DEFAULT_RETRIES = 5
files = {'image01': open('005.jpg', 'rb')}
user_info = {'name': 'letian'}
r = requests.post("http://127.0.0.1:8001/upload", data=user_info, files=files)
#r = requests.get("http://127.0.0.1:5000/json")
print r.text