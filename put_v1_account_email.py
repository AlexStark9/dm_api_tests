import requests
import json

url = "http://localhost:5051/v1/account/email"

payload = json.dumps({
  "login": "User_1",
  "email": "User_1@mail.ru",
  "password": "qwerty12345"
})
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
