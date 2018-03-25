#coding:utf8
import itchat
import time
import re
from itchat.content import *
from wechat_search import getPackage
# 登录

# itchat.login()
# #  发送消息
# itchat.send(u'你好', 'filehelper')

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if msg['Type'] == 'Text':
        if '快递' in msg['Content']:
            bill_num = re.search(r"(快递)(\+)([0-9]+)", msg['Content']).group(3)
            reply_info = getPackage.getPackage(bill_num)
            itchat.send(reply_info, toUserName=msg['FromUserName'])
        else:
            reply_info = '查询请输入:快递+运单号,如快递+123456789'
            itchat.send(reply_info, toUserName=msg['FromUserName'])

# itchat.login()
# friends = itchat.get_friends()
# for friend in friends:
#     print(friend)
#     if friend['Signature'].strip() =='长路多艰险 誓死不弯腰 野火烧不尽 芳草碧连天':
#         print(friend)

itchat.auto_login(hotReload=True)

itchat.run()