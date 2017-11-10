#part_1 VK_API

AUTORIZED_URL = ''
CLIENT_ID = ''

auth_data = {

    'client_id': APP_ID,
    'redirect_uri': '',
    'display':'page',
    'scope': 'status,friends',
    'responce_type':'token',
    'v': VESION
}


# print('?'.join(
#     (AUTORIZED_URL,urlencode(auth_data))
# ))

TOKEN = ''

params = {
    'access_token': TOKEN,
    'v': VERSION
}


# responce = requests.get('', params)
# responce_text = responce.text
# print (responce.text, type(responce.text))
# responce_text['responce']
# responce_json = responce.json()
# print(responce_json, type(responce_json))
# responce_json['responce']
# print(responce.status_code)

perams['text'] = 'set status from python'
                 ''
responce = requests.get('', params)
responce_json = responce.json()
print(responce_json, type(responce_json))
