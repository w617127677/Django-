import requests
import json
data = {

"username":"a",

"password":"zxc123456"

}
# print(data.json())
response = requests.post('http://127.0.0.1:8000/api-token-auth/',data=data)
print(response.text)
# headers = {
# 'Authorization': 'Token 7b5a6f2ac1e43dc9dde4a756a0e02e2a94540820'
# }
# # for i in range(10):
# response = requests.get('http://cchh.natapp1.cc/snippets',headers=headers)
# print(response.text)
