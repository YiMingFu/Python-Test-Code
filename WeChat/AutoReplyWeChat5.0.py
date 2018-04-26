#coding=utf8
import itchat,time
import threading
from enum import Enum
import sys
import datetime
import requests
import sqlite3

#-----------智能回复-------------
KEY = 'ed4bb0eb8090408ba5cb43aab63bbffc'
# '''创建一个数据库，文件名'''
sqldb = sqlite3.connect('./MsgQA.db')
# '''创建游标'''
sqlMsg = sqldb.cursor()
# '''执行语句'''
sql = '''create table MsgQA(
        Q text,
        A text,
        ID text
        )'''
try:
    sqlMsg.execute(sql)
except :
    print ''
sqldb.commit()
def get_response(msg):  
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {  
        'key': KEY,  
        'info': msg,  
        'userid': 'AI鹿鹿',  
    }  
    try:  
        r = requests.post(apiUrl, data=data).json()  
        return r.get('text')  
    except:  
        return  
#-----------智能回复-------------

itchat.auto_login(enableCmdQR=2)
itchat.auto_login(enableCmdQR=True)
reload(sys)
sys.setdefaultencoding("utf-8")
systemencoding=sys.getfilesystemencoding()
class ReplyTimeType(Enum):
  ImmediateRep =1
  DelayRep = 2
class ReplyBodyType(Enum):
  ImmediateRep =1
  DelayRep = 2
class ReplyBodyType(Enum):
  Myself =1
  Robot = 2
staticRepMsg = {
                "hiMsg":u'*****',
                "reqList":u'****',
                "goodNigth":u'*****',
                "tel":u'*****\n*****：00',
                } 
CurReplyTimeType = ReplyTimeType.DelayRep
CurReplyMainType = None
delayRepTime = 600#回复间隔／秒
lastTime = 0
myUserName = 'myName'
toReplyDict = {}
userNameLabel = 'RemarkName'
unknownUser = ''
replyMsg = False
replyTimeDelta = 660
realHandleMsg = True
users = itchat.search_friends(name = 'Cindy')
usersManger = itchat.search_friends(name = 'Milu')
admin1 = users[0]['UserName']#发给Cindy
admin2 = usersManger[0]['UserName']#发给波哥
def realHandleRecvMsg(msg):
    global realHandleMsg
    if msg['User']['RemarkName'] =='':
        userNameLabel = 'NickName'
    else:
        userNameLabel = 'RemarkName'
    fromUserName = msg["FromUserName"]
    if(fromUserName == myUserName):
        if msg['Text'] == 'ShutDownAutoMsg':
            realHandleMsg = False
            itchat.send('关闭夜间自动回复❌',toUserName='filehelper')
            itchat.send_msg(u"[%s]%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),'\n 关闭夜间自动回复❌'), admin1)
        elif msg['Text'] == 'OpenAutoMsg':
            realHandleMsg = True
            itchat.send('开启夜间自动回复✅',toUserName='filehelper')
            itchat.send_msg(u"[%s]%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),'\n 开启夜间自动回复✅'), admin1)
    if realHandleMsg ==True:   
        now = datetime.datetime.now()
        if now.hour<8 and now.hour>1:
            autoReplayMsg(staticRepMsg["goodNigth"],msg.fromUserName)
            autoReplayMsg(staticRepMsg["reqList"],msg.fromUserName)
            autoReplayMsg(staticRepMsg["tel"],msg.fromUserName)
        else:
            realHandleMsg = True
            autoReplayMsg(staticRepMsg["hiMsg"],msg.fromUserName)
            autoReplayMsg(staticRepMsg["reqList"],msg.fromUserName)
        itchat.send_msg(u"[%s]%s@%s的信息%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),'\n ⚠️系统已自动回复⚠️ ',msg['User'][userNameLabel],''), admin1)

def handleRecvMsg(msg):
    global replyMsg 
    lastTime = time.time()
    now = datetime.datetime.now()
    if now.hour<8 and now.hour>1:
        CurReplyTimeType = ReplyTimeType.ImmediateRep
    else:
        CurReplyTimeType = ReplyTimeType.DelayRep
    if(CurReplyTimeType == ReplyTimeType.ImmediateRep):
        realHandleRecvMsg(msg)
        replyMsg = True
    elif(CurReplyTimeType == ReplyTimeType.DelayRep):
        HandleDelayRep(msg)
        replyMsg = True
def HandleDelayRep(msg):
    fromUserName = msg["FromUserName"]
    toUserName = msg["ToUserName"]
    if(fromUserName == myUserName):
        if(toReplyDict.has_key(toUserName)):
            data = toReplyDict[toUserName]
            data["msg"] = None
            data["sendTime"] = None
            data["reply"] = time.time()
        return   
    if(toReplyDict.has_key(fromUserName)):
        temp = toReplyDict[fromUserName]
        temp["sendTime"] = time.time()
        temp["msg"] = msg
        return   
    temp = {}
    toReplyDict[fromUserName] = temp
    temp["sendTime"] = time.time()
    temp["msg"] = msg
    temp["AutoMsg"] = False

def autoReplayMsg(msg,toUser):
    itchat.send_msg(msg,toUser)

def loopHandleDelayMsg(arg,):
    global replyMsg
    while True:
        if replyMsg == True:
            for user,temp in toReplyDict.items():
                curTime = time.time()
                if(temp.has_key("reply") and ((curTime -temp["reply"]) < replyTimeDelta)):
                    continue
                if(not temp.has_key("sendTime") or not temp["sendTime"]):
                    continue
                if(temp["AutoMsg"] == True):
                    continue
                sendTime = temp["sendTime"]
                if(curTime - sendTime >delayRepTime):
                    msg = temp["msg"]
                    temp["AutoMsg"] =True
                    realHandleRecvMsg(msg)
                    temp["msg"] = None
                    temp["sendTime"] = None
                    temp["reply"] = time.time()
                    replyMsg = False
        time.sleep(1)

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video','Text','Map', 'Card', 'Note', 'Sharing'])
def text_client(msg): 
if __name__ == '__main__':
    myUserName = itchat.get_friends(update=True)[0]["UserName"] 
    threading.Thread(target=loopHandleDelayMsg,args=("xx",)).start()
    itchat.run()