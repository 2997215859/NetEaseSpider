#coding=utf-8
import string

from Crypto.Cipher import AES
import base64
import requests
import json
import music_mysql
import pymysql
import time
from settings import config
# headers
headers = {
    'Referer': 'http://music.163.com/',
    'Cookie': 'appver=1.5.0.75771;MUSIC_U=e954e2600e0c1ecfadbd06b365a3950f2fbcf4e9ffcf7e2733a8dda4202263671b4513c5c9ddb66f1b44c7a29488a6fff4ade6dff45127b3e9fc49f25c8de500d8f960110ee0022abf122d59fa1ed6a2;',
}


def get_params(first_param, forth_param):
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key.encode(), iv.encode())
    h_encText = AES_encrypt(h_encText.decode(), second_key.encode(), iv.encode())
    return h_encText.decode()

def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text.encode())
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_json(url, data):
    response = requests.post(url, headers=headers, data=data)
    return response.content


def crypt_api(id, offset):
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=" % id
    first_param = "{rid:\"\", offset:\"%s\", total:\"true\", limit:\"100\", csrf_token:\"\"}" % offset
    forth_param = "0CoJUm6Qyw8W8jud"
    params = get_params(first_param, forth_param)
    encSecKey = get_encSecKey()
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    return url, data

def get_love_song(user_id):
    love_songs = []
    # Connect to the database
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = 'SELECT * FROM `love_song` WHERE 1'
    try:
        cursor.execute(sql)
        for song in cursor:
            love_songs.append({'song_id':song['song_id'], 'song_name':song['song_name']})
        db.commit()
        return love_songs
    except Exception as e:
        print('errrorrrr->', e)
        db.rollback()
    db.close()

def get_comment(id, song_name):
    try:
        offset = 0
        url, data = crypt_api(id, offset)
        json_text = get_json(url, data)
        # print json_text
        json_dict = json.loads(json_text.decode("utf-8"))
        comments_sum = json_dict['total']
        for i in range(0, comments_sum, 100):
            offset = i
            url, data = crypt_api(id, offset)
            json_text = get_json(url, data)
            json_dict = json.loads(json_text.decode("utf-8"))
            json_comment = json_dict['comments']
            for json_comment in json_comment:
                user_id = json_comment['user']['userId']
                user_name = json_comment['user']['nickname']
                comment = json_comment['content']
                timestamp = json_comment['time']
                ts = int(timestamp) / 1000
                # 转换成localtime
                time_local = time.localtime(ts)
                # 转换成新的时间格式(2016-05-05 20:28:54)
                dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                # print dt
                music_mysql.insert_comment(user_id, user_name, id, song_name, comment, dt)
                # print('id = ', id)
                # print('user_id=', user_id)
                # print('user_name=', user_name)
                # print(comment)
                # print('Notes have been add to DB!')
            time.sleep(3)

            # time.sleep(1)
    except Exception as e:
        print('errroooo->', e)
        pass

if __name__ == "__main__":
    # songs = get_love_song('268192391')
    songs = []
    # songs.append({'song_id':34923114, 'song_name':'晚安'})
    for song in songs:
        get_comment(song['song_id'], song['song_name'])
