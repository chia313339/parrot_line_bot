import os
import sys
from Model.dModel import *

chatbot_name =['小紅','李小紅','阿紅']

weather_word = ['天氣','氣象','天候','氣溫','weather']
news_word = ['新聞','新知','新消息','news','想看','有沒有','推薦','最近','來個','來點','什麼']
technews_word = ['新聞','新知','新消息','news','想看','有沒有','推薦','最近','來個','來點','科技','新報','什麼']
hello_word = ['HI','Hello','你好','嗨','哈囉','嗨嗨','妳好','您好','安安','早安','午安','hi','hello','HELLO','Hi']
movie_word =['電影','想看','有沒有','推薦','好看','最近','精彩','介紹','來個','什麼']

def text_match(text,key_word):
    matching_degree=0
    for word in key_word:
        #print(word)
        if text.find(word)!= -1:
            #print('get it!!!')
            matching_degree+=1
    return matching_degree



def mapping_word(keyword):
    db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=keyword).first()
    if not db_MESSAGE:
        print("沒有資料")
        return 0
    else :
        print("有資料")
        return 1

def learn_index(text):
    if (text[0:6] == '小紅學說話;') & (text[6:].count(';') == 1):
        print("開始學說話")
        return 1
    else :
        return 0


def learn_word(keyword,message):
    content = mapping_word(keyword)
    if content == 0:
        print("學習新字詞 "+keyword)
        insert_data = LEARN_WORD(KEYWORD=keyword,MESSAGE=message)
        db.session.add(insert_data)
        db.session.commit()
        print("DONE 已學習新字詞")
    else :
        db_MESSAGE = LEARN_WORD.query.filter_by(KEYWORD=keyword).first()
        db_MESSAGE.MESSAGE = message
        db.session.commit()
        print("DONE 已修改新字詞")
