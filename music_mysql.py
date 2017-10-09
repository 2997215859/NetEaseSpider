# coding = utf-8
import pymysql
from settings import config

def insert_comment(user_id, user_name, song_id, song_name, comment, time):
    # Connect to the database
    db = pymysql.connect(**config)
    cursor = db.cursor()
    # sql = "INSERT INTO `user_comment`(`user_id`, `name`, `comment`) VALUES (%s, %s, %s)"
    sql = "INSERT INTO `user_comment`(`user_id`, `user_name`, `song_id`, `song_name`, `comment`, `time`) VALUES (%s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, (user_id, user_name, song_id, song_name, comment, time))
        db.commit()
    except Exception as e:
        print('errrorrrr->', e)
        db.rollback()
    db.close()

def get_user_id_mysql():
    user_data = []
    # Connect to the database
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = 'SELECT * FROM `user_comment` WHERE 1'
    try:
        cursor.execute(sql)
        for user in cursor:
            user_id_name = {'id': '0', 'name': '0'}
            id = user['id']
            name = user['name']
            user_id_name['id'] = id
            user_id_name['name'] = name
            if user_id_name not in user_data:
                user_data.append(user_id_name)
        db.commit()
        return user_data
    except Exception as e:
        print('errrorrrr->', e)
        db.rollback()
    db.close()


def insert_user(id, name, data):
    # Connect to the database
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO `user_love_songs`(`id`,`name`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90`, `91`, `92`, `93`, `94`, `95`, `96`, `97`, `98`, `99`, `100`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, (id, name, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], data[29], data[30], data[31], data[32], data[33], data[34], data[35], data[36], data[37], data[38], data[39], data[40], data[41], data[42], data[43], data[44], data[45], data[46], data[47], data[48], data[49], data[50], data[51], data[52], data[53], data[54], data[55], data[56], data[57], data[58], data[59], data[60], data[61], data[62], data[63], data[64], data[65], data[66], data[67], data[68], data[69], data[70], data[71], data[72], data[73], data[74], data[75], data[76], data[77], data[78], data[79], data[80], data[81], data[82], data[83], data[84], data[85], data[86], data[87], data[88], data[89], data[90], data[91], data[92], data[93], data[94], data[95], data[96], data[97], data[98], data[99],
))
        db.commit()
        print('id = ', id)
        print('name = ', name)
        print('Data has has been add to user_love_songs')
    except pymysql.err.IntegrityError:
        print('id = ', id)
        print('Data has has been add to user_love_songs')
    except IndexError:
        print('id = ', id)
        print('uses song doesnot exceed 100')
    except Exception as e:
        print('errorrrrr -> ', e)
        db.rollback()
    db.close()