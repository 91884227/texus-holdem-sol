import Hand
import itertools
import random
import pymysql

# generate all card
value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] + ['J', 'Q', 'K']
suits = ['s', 'h', 'd', 'c']
all_cards = [ i[0] + i[1] for i in list(itertools.product(value, suits)) ]

# generate all hand
all_hands = [ list(i) for i in list(itertools.combinations(all_cards, 5)) ]

# write to mysql
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "GIT@91884",
    "db": "texus_holdem",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
except Exception as ex:
    print(ex)

with conn.cursor() as cursor:
    # 新增資料SQL語法
    command = "INSERT INTO all_hands (hands, card_value) VALUES(%s, %s)"
    for h in all_hands:
        print(h)
        cursor.execute(
            command, (' '.join(h), Hand.Hand(h).value)
        )
    # 儲存變更
    conn.commit()