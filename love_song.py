import re
import requests
from bs4 import BeautifulSoup
from settings import headers
from settings import play_url
from settings import config
from settings import pymysql

def insert_love_song(user_id, song_id, song_name):
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO `love_song`(`user_id`, `song_id`, `song_name`) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (user_id, song_id, song_name))
        db.commit()
    except Exception as e:
        print('errrorrrr->', e)
        db.rollback()
    db.close()

s = requests.session()
r = s.get(play_url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
# print soup.prettify()
main = soup.find('ul', {'class':'f-hide'})
for music in main.find_all('a'):
    #print music
    # /song?id=427016671
    matchObj = re.match(r'.*?song\?id=(\d+)', music['href'], re.M|re.I)
    song_id = matchObj.group(1)
    #print music.text + ':' + matchObj.group(1)
    insert_love_song('268192391', song_id, music.text);
     # print('{} : {}' . format(music.text, music['href']))