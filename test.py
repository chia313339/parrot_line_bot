from Model.dModel import *
# import Psycopg2
import uuid
import requests
import re
import random
import configparser
from bs4 import BeautifulSoup




# line_keyword = "不是吧"
# line_message = "真的假的"
#
# insert_data = LEARN_WORD(KEYWORD = line_keyword
#                           , MESSAGE = line_message
#                           )
# db.session.add(insert_data)
# db.session.commit()

# content=""
# alldata = db.session.query(LEARN_WORD.KEYWORD).all()
# for somedata in alldata:
#     content += str(somedata)
#     print(somedata)
#
# print(content)

# alldata = LEARN_WORD.query.first()
# print(alldata.KEYWORD)
# for somedata in alldata:
#     print(somedata)

#
#
# def mapping_word(keyword):
#     db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=keyword).first()
#     if not db_MESSAGE:
#         print("沒有資料")
#         return 0
#     else :
#         print("有資料")
#         return 1
#
#
# def learn_word(keyword,message):
#     content = mapping_word(keyword)
#     if content == 0:
#         print("學習新字詞 "+keyword)
#         insert_data = LEARN_WORD(KEYWORD=keyword,MESSAGE=message)
#         db.session.add(insert_data)
#         db.session.commit()
#         print("DONE 已學習新字詞")
#     else :
#         db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=keyword).first()
#         db_MESSAGE.MESSAGE = message
#         db.session.commit()
#         print("DONE 已修改新字詞")


# print(mapping_word('不是吧'))
# print(mapping_word('不吧'))
# learn_word('不會吧','是喔')

# print(mapping_word('不是吧'))
# print(mapping_word('不吧'))
#
# text='不吧'
#
# if mapping_word(text) == 1:
#     print("KEYWORD = " + text)
#     db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=text).first()
#     content = db_MESSAGE.MESSAGE
#     print("MESSAGE = " + content)

#
#
# def mapping_word(keyword):
#     db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=keyword).first()
#     if not db_MESSAGE:
#         print("沒有資料")
#         return 0
#     else :
#         print("有資料")
#         return 1
#
#
# def learn_index(text):
#     if text[0:6] == '小紅學說話;' & text[6:].count(';') == 1:
#         print("開始學說話")
#         return 1
#     else :
#         return 0
#
# def learn_word(keyword,message):
#     content = mapping_word(keyword)
#     if content == 0:
#         print("學習新字詞 "+keyword)
#         insert_data = LEARN_WORD(KEYWORD=keyword,MESSAGE=message)
#         db.session.add(insert_data)
#         db.session.commit()
#         print("DONE 已學習新字詞")
#     else :
#         db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=keyword).first()
#         db_MESSAGE.MESSAGE = message
#         db.session.commit()
#         print("DONE 已修改新字詞")
#
# if learn_index(event.message.text) == 1:
#     keyword = event.message.text[6:].split(';')[0]
#     message = event.message.text[6:].split(';')[1]
#     print("KEYWORD = " + keyword,"MESSAGE = "+ message)
#     learn_word(keyword,message)
#     content = "好喔！我記起來了！！"
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=content))
#     return 0
#
#

def ptt_hot():
    target_url = 'http://disp.cc/b/PttHot'
    print('Start parsing pttHot....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for data in soup.select('#list div.row2 div span.listTitle'):
        title = data.text
        link = "http://disp.cc/b/" + data.find('a')['href']
        if data.find('a')['href'] == "796-59l9":
            break
        content += '{}\n{}\n\n'.format(title, link)
    return content

print(ptt_hot())



print("DONE")


