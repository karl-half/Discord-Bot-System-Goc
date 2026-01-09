import pymysql

def get_connection():
    return pymysql.connect(host="localhost", user="root", password="", database="globalna_koalicja_okultystyczna_db", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)