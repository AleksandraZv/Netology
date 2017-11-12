#part_1 VK_API

import requests
from urllib.parse import urlencode


AUTHORIZED_URL = 'https://oauth.vk.com/authorize'
APP_ID = '6256742'
VERSION = '5.69'

auth_data = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'status, friends',
    'response_type': 'token',
    'v': VERSION
}


print('?'.join(
    (AUTHORIZED_URL, urlencode(auth_data))
))

TOKEN = ''

params = {
    'access_token': TOKEN,
    'v': VERSION,
}


response = requests.get('https://api.vk.com/method/status.get', params)
print(response.text)
# response_text = response.text
# print (response.text, type(response.text))
# response_text['response']
# response_json = response.json()
# print(response_json, type(response_json))
# response_json['response']
# print(response.status_code)

# params['text'] = 'set status from python'
#                  ''
# responce = requests.get('', params)
# responce_json = responce.json()
# print(responce_json, type(responce_json))
