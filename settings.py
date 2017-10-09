import pymysql
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'netease',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
headers = {
    "Referer":"http://music.163.com",
    "Host":"music.163.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

play_url = 'http://music.163.com/playlist?id=366673743' # song list id


