# Task_1 Get_friends_list

# Task_2 Get_friends_friends_list

# Task_3 Get_mutual_ friends

import requests
import time
from urllib.parse import urlencode


AUTHORIZED_URL = 'https://oauth.vk.com/authorize'
APP_ID = '6256742'
VERSION = '5.69'

auth_data = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': VERSION
}


print('?'.join(
    (AUTHORIZED_URL, urlencode(auth_data))
))

TOKEN = '' #  токен убран из открытого доступа

params = {
    'access_token': TOKEN,
    'v': VERSION,
}


response = requests.get('https://api.vk.com/method/friends.get', params)  # Task_1 Get_friends_list
response_json = response.json()


# for person_id in response_json['response']['items']:
#     time.sleep(3)
#     print('FRIEND_ID', person_id)
#
#     params = {
#         'access_token': TOKEN,
#         'v': VERSION,
#         'user_id': person_id,
#     }
#     response = requests.get('https://api.vk.com/method/friends.get', params)  # Task_2 Get_friends_friends_list
#
#
#     response_json = response.json()
#     print(response_json)

for person_id in response_json['response']['items']:
    time.sleep(3)
    print('FRIEND_ID', person_id)

    params = {
        'access_token': TOKEN,
        'v': VERSION,
        'source_uid': person_id,
        'target_uids': person_id,
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)  # Task_3 Get_mutual_ friends

    response_json = response.json()
    print(response_json)





