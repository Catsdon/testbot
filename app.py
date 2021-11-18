# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第三章 互動回傳功能
推播push_message與回覆reply_message
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
from linebot.models import (
    MessageEvent,VideoMessage,TextMessage, StickerMessage, StickerSendMessage, ConfirmTemplate, TemplateSendMessage, MessageAction, URIAction, LocationMessage
 )
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('6LtqwU4k493Gys589ikza9GzxWgrHjJFIcDGc21+JcMAALUjLd2xLzGRJft575QbIOeaUEedDr6QMf4mormSu0bCA8QuUTGj0kC0Im1qNsovhsMLv8tHwJjE2PkLvA44E8ckPuLRtWlTu3sNq+rNmwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('62fedcb34c8415668774fd2ccdb5d73c')

line_bot_api.push_message('U738f70cb25916b736d9abe88f11d01f2', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('看評論',message):
         flex_message = TextSendMessage(text='以下有雷，請小心',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(label="PTT", text="https://www.ptt.cc/bbs/movie/index.html")),
                                    QuickReplyButton(action=MessageAction(label="DCARD", text="https://www.dcard.tw/f/movie")),
                                    
                                ]))
         line_bot_api.reply_message(event.reply_token, flex_message)


    elif message == 'test':
        user_camera_open(event)
    elif re.match('你誰',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('我誰~~~！'))
    elif re.match('你是誰',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('我誰~~~！當然是你的電影大幫手'))
        
    elif re.match('Hi',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('安安'))
    elif re.match('hi',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('尼好 肥宅'))
        
    elif re.match('哈囉',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('哈囉肥宅'))
    elif re.match('你好',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('哈囉肥宅'))
    elif re.match('你好阿',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('哈囉肥宅'))

    elif re.match('摸',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('東踏取蜜!'))

    elif re.match('幹',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('沒禮貌! '))
    elif re.match('三小',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('沒禮貌! '))
    elif re.match('87',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('沒禮貌! '))
    elif re.match('我愛你',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('我也愛你 '))
    elif re.match('愛你',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('我也愛你 '))
    elif re.match('你好帥',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('你現在才知道哦 '))
    elif re.match('我好帥',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('你說付錢的時候嗎?真的滿帥的 '))
        
    elif re.match('我帥嗎',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('滿帥的，只不過差我一點')) 
    elif re.match('好餓',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('我也很餓'))
    elif re.match('餓',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('我也很餓'))
    elif re.match('早安',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('早安！今天真是美好的一天'))
    elif re.match('早',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('早安！今天真是美好的一天'))
    elif re.match('想睡了',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('晚安，祝你有個好夢~!'))
    elif re.match('晚安',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('晚安，祝你有個好夢~!'))

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('哈哈，你沒猜中關鍵字'))


@handler.add(MessageEvent,message=(VideoMessage))
def handle_content_message(event):
    static_tmp_path=''
    if isinstance(event.message,VideoMessage):
        ext='mp4'
    else:
        return

    message_content=line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path,prefix=ext+'-',delete=False) as tf:
        for chunk in message_content.iter_content():
            print(chunk)
            tf.write(chunk)
        tempfile_path=tf.name

    dist_path=tempfile_path+'.'+ext
    dist_name=os.path.basename(dist_path)
    os.rename(tempfile_path,dist_path)

    line_bot_api.reply_message(
        event.reply_token,[
            TextSendMessage(text='成功搜集人臉特徵'),
            TextSendMessage(text=request.host_url+os.path.join('static','tmp',dist_name))
        ]


    )




#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)