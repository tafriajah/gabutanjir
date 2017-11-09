# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from googletrans import Translator
import time,random,sys,json,codecs,threading,glob,re
import json,urllib2,urllib
import requests
import shutil
import tempfile
from bs4 import BeautifulSoup
import wikipedia


#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = LINETCR.LINE()
cl.login(token="Em0HGqyS7rNdWW9VVT5a.FbyMj6PnEZEI8qZ4zwXRoG.WMHcW7THVka4x6Pfu3lYE5NcEzTqsAXKds2uhPCOlQw=")
cl.loginResult()

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.loginResult()

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

#kc = LINETCR.LINE()
#kc.login(qr=True)
#kc.loginResult()

#ks = LINETCR.LINE()
#ks.login(qr=True)
#ks.loginResult()

#ka = LINETCR.LINE()
#ka.login(qr=True)
#ka.loginResult()

#kb = LINETCR.LINE()
#kb.login(qr=True)
#kb.loginResult()

#ko = LINETCR.LINE()
#ko.login(qr=True)
#ko.loginResult()

#ke = LINETCR.LINE()
#ke.login(qr=True)
#ke.loginResult()

#ku = LINETCR.LINE()
#ku.login(qr=True)
#ku.loginResult()

ki = kk = kc = ks = ka = kb = ko = ke = ku = cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""🌼 ᴀɪ•бот соɴтяоʟ•ɪᴀ 🌼

Command In Group
[🍁] /Gname:
[🍁] /Ginfo
[🍁] /Id Group
[🍁] /Cancel
[🍁] /Gurl
[🍁] /All Group Cancel
[🍁] /Protect
[🍁] Group id
[🍁] Link Open ~ Link Close

Command Kicker In Group
[🍒] Inv: 「Mid」
[🍒] Sayonara: 「Mid」
[🍒] /AI「@TagTarget」
[🍒] /Blacklist 「@TagTarget」
[🍒] /Ban ~ Banned 「@TagTarget」
[🍒] /Unban ~ Unban 「@TagTarget」

Command Plus
[🍙] /Wikipedia:
[🍙] /Lurking
[🍙] /Mention
[🍙] /Check
[🍙] /Me
[🍙] /Mycontact
[🍙] /MyMid
[🍙] /Mid AI ~ /Mid IA
[🍙] /ChangeMessage: ~ /AddMessage:
[🍙] /Comment: ~ /AddComment:
[🍙] Dp「@TagTarget」
[🍙] Team AI/Team IA
"""

Setgroup ="""Command BOT
[🎒] /Contact:on ~ /Contact:off
[🎒] /AutoJoin:on ~ /AutoJoin:off
[🎒] /AutoLeave:on ~ /AutoLeave:off
[🎒] /Share:on ~ /Share:off
[🎒] /Add:on ~ /Add:off
[🎒] /Comment:on ~ /Comment:off

Command Protect
[🌸] /Join:on ~ /Join:off
[🌸] /NoInvite:on ~ /NoInvite:off
[🌸] /GProtect:on ~ /GProtect:off
"""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF=[ka,kb,ko,ke,ku]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ku.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,"u7c162627aa4d7b37a2f10cf8656c6b3a"]
admin=["u7c162627aa4d7b37a2f10cf8656c6b3a"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"""Thanks For Add me:

→ G͍̗ͥ͗ͯ͢҉ę̶̴͎̲̘̱͐͋͗ͫn̴̵̷̶̢̒ͪ̏ͩ̑ͤ͊̀̿͢͡ͅȩ̸̵̷̻̯͕̼̤̪͉̣̰͌̌͆ͩ̀͛̚͟͞͏̸̴r̷̢̥̍͆͌ͯ͌͟͜͢͏a̢͈̳͙̯̪̠͕̹ͥͫͭͫ̅͏̴̡̛̕̕̕͢͞͝ț̴̡̯͋̾̋̒́ͮ͌́̕͝ī̡̢̹̳͈̘̜̺͓̗̖̄́ͫ̐̋̈̈̃̑̚͢͠o̷̴̢̨̡̕͠͝n̷̴̢̨̡̕͠͝ ̷̴̷̴̢̨̡̢̨̡̕̕͠͝͠͝B̡̯̤̣̈́̎ŏ͓ͦͭͤ̆̍͛͒͑͡҉̴̢̀͝t͖̺̥̞͚̂̓ͦͮͅ͏̷̸̨́͟͜s̷̴̢̨̡ͭ̋͌̐̊ͨ̄̏̋̕͠͝
→ ᴀɪ•ᴛᴇᴀᴍ•ɪᴀ бот соɴтяоʟ""",
    'AddMessage':"",
    "lang":"JP",
    "comment":"""Thanks For Add me:

→ G͍̗ͥ͗ͯ͢҉ę̶̴͎̲̘̱͐͋͗ͫn̴̵̷̶̢̒ͪ̏ͩ̑ͤ͊̀̿͢͡ͅȩ̸̵̷̻̯͕̼̤̪͉̣̰͌̌͆ͩ̀͛̚͟͞͏̸̴r̷̢̥̍͆͌ͯ͌͟͜͢͏a̢͈̳͙̯̪̠͕̹ͥͫͭͫ̅͏̴̡̛̕̕̕͢͞͝ț̴̡̯͋̾̋̒́ͮ͌́̕͝ī̡̢̹̳͈̘̜̺͓̗̖̄́ͫ̐̋̈̈̃̑̚͢͠o̷̴̢̨̡̕͠͝n̷̴̢̨̡̕͠͝ ̷̴̷̴̢̨̡̢̨̡̕̕͠͝͠͝B̡̯̤̣̈́̎ŏ͓ͦͭͤ̆̍͛͒͑͡҉̴̢̀͝t͖̺̥̞͚̂̓ͦͮͅ͏̷̸̨́͟͜s̷̴̢̨̡ͭ̋͌̐̊ͨ̄̏̋̕͠͝
→ ᴀɪ•ᴛᴇᴀᴍ•ɪᴀ бот соɴтяоʟ""",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"ᴀɪ•бот соɴтяоʟ•ɪᴀ",
    "cName2":"ᴀɪ•бот-ᴏɴᴇ",
    "cName3":"ᴀɪ•бот-ᴛᴡᴏ",
    "cName4":"ᴀɪ•бот-ᴛʜяᴇᴇ",
    "cName5":"ᴀɪ•бот-ғᴏᴜʀ",
    "cName6":"ᴀɪ•бот-ғɪvᴇ",
    "cName7":"ᴀɪ•бот-sɪx",
    "cName8":"ᴀɪ•бот-sᴇvᴇɴ",
    "cName9":"ᴀɪ•бот-ᴇɪɢʜᴛ",
    "cName10":"ᴀɪ•бот-ɴɪɴᴇ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in admin and Bots:
                   G = ka.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in admin and Bots:
                  group = ka.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in admin and Bots:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#
        
        if op.type == 19:
           if op.param2 not in admin and Bots:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
           else: 
               pass

        if op.type == 19:
           if op.param3 in admin and Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,admin)
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
 
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True        
                    
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
#        if op.type == 26 or op.type == 25:
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#==================================================================
# COMMAND Help + Set Group
#==================================================================
            elif msg.text in ["/Menu"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,helpMessage)
                    else:
                        cl.sendText(msg.to,helpt)

            elif msg.text in ["/Protect"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,Setgroup)
                    else:
                        cl.sendText(msg.to,Sett)

#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Group Name
#==================================================================
            elif ("/Gname: " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("/Gname: ","")
                    grup = cl.getGroup(msg.to)
                    cl.updateGroup(X)
                    cl.sendText(msg.to, "Update Group Name to →" + grup)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")

            elif ("Gname: " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    grup = cl.getGroup(msg.to)
                    ki.updateGroup(X)
                    ki.sendText(msg.to, "Group Name Change→" + grup)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Kick By Mid
#==================================================================
            elif "/Matane: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("/Matane: ","")
                ki.kickoutFromGroup(msg.to,[midd])

            elif "Sayonara: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Sayonara: ","")
                kk.kickoutFromGroup(msg.to,[midd])
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Invite By Mid
#==================================================================
            elif "/Inv: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("/Inv: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "Inv: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Inv: ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Bot Contact
#==================================================================
            elif msg.text in ["Team AI"]:
              if msg.from_ in admin:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': mid}
                  cl.sendMessage(msg)

                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Amid}
                  cl.sendMessage(msg)

                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Bmid}
                  cl.sendMessage(msg)

                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Cmid}
                  cl.sendMessage(msg)
                
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Dmid}
                  cl.sendMessage(msg)
                
            elif msg.text in ["Team IA"]:
              if msg.from_ in admin:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Emid}
                  cl.sendMessage(msg)
                
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Fmid}
                  cl.sendMessage(msg)
                
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Gmid}
                  cl.sendMessage(msg)
                
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Hmid}
                  cl.sendMessage(msg)

                  msg.contentType = 13
                  msg.contentMetadata = {'mid': Imid}
                  cl.sendMessage(msg)                  
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Send Contact
#==================================================================
            elif msg.text in ["/Me"]:
              if msg.from_ in admin:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': msg.from_}
                  cl.sendMessage(msg)

            elif msg.text in ["/Mycontact"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ki.sendMessage(msg)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Gift
#==================================================================
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '5'}
#                msg.text = None
#                cl.sendMessage(msg)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Cancel Invitation
# Admin
#==================================================================
            elif msg.text in ["/Cancel"]:
              if msg.from_ in admin:
                  if msg.toType == 2:
                      X = cl.getGroup(msg.to)
                      if X.invitee is not None:
                          gInviMids = [contact.mid for contact in X.invitee]
                          cl.cancelGroupInvitation(msg.to, gInviMids)
                      else:
                          if wait["lang"] == "JP":
                              cl.sendText(msg.to,"No one is inviting")
                          else:
                              cl.sendText(msg.to,"Sorry, nobody absent")
                  else:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Can not be used outside the group")
                      else:
                          cl.sendText(msg.to,"Not for use less than group")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Cancel Invitation
# Assist
#==================================================================
            elif msg.text in ["Cancel"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
#==================================================================
# COMMAND Fnish
#==================================================================
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
#==================================================================
# COMMAND Open QR Group
#==================================================================
            elif msg.text in ["/Link Open","/Open Url"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Group Open")
                    else:
                        cl.sendText(msg.to,"Link Already Open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Link Open","Open Url"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Link Group Open")
                    else:
                        ki.sendText(msg.to,"Link Already Open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Close QR Group
#==================================================================
            elif msg.text in ["/Link Close","/Close Url"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Group Close")
                    else:
                        cl.sendText(msg.to,"Link Already Close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Link Close","Close Url"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Link Group Close")
                    else:
                        ki.sendText(msg.to,"Link Already Close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Join Ticket
#==================================================================
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))

            elif msg.text == "/Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "Close"
                        else:
                            u = "Open"
                        cl.sendText(msg.to,"「Group Name」\n" + str(ginfo.name) + "\n\n「Group ID」\n" + msg.to + "\n\n「Group Creator」\n→" + gCreator + "\nMembers Joined: " + str(len(ginfo.members)) + " Members\nMembers Pending: " + sinvitee + " people\nGroup Url: " + u + " it is Inside")
                    else:
                        cl.sendText(msg.to,"「Group Name」\n" + str(ginfo.name) + "\n\n「Group ID」\n" + msg.to + "\n\n「Group Creator」\n→" + gCreator)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND ID Group + Mid
#==================================================================
            elif "/Id Group" == msg.text:
                ki.sendText(msg.to,msg.to)

            elif "/MyMid" == msg.text:
                ki.sendText(msg.to, msg.from_)

            elif "/Mid AI" == msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to, "My Mid →" + mid)
                  cl.sendText(msg.to, "ᴀɪ•бот-ᴏɴᴇ →" + Amid)
                  cl.sendText(msg.to, "ᴀɪ•бот-ᴛᴡᴏ →" + Bmid)
                  cl.sendText(msg.to, "ᴀɪ•бот-ᴛʜяᴇᴇ →" + Cmid)
                  cl.sendText(msg.to, "ᴀɪ•бот-ғᴏᴜʀ →" + Dmid)

            elif "/Mid IA" == msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to, "ᴀɪ•бот-ғɪvᴇ →" + Emid)
                  cl.sendText(msg.to, "ᴀɪ•бот-sɪx →" + Fmid)
                  cl.sendText(msg.to, "ᴀɪ•бот-sᴇvᴇɴ →" + Gmid)
                  cl.sendText(msg.to, "ᴀɪ•бот-ᴇɪɢʜᴛ →" + Hmid)
                  cl.sendText(msg.to, "ᴀɪ•бот-ɴɪɴᴇ →" + Imid)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Chat Sticker
#==================================================================
#            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "100",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                cl.sendMessage(msg)
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Post Timeline
#==================================================================
#            elif msg.text in ["/Timeline:"]:
#                tl_text = msg.text.replace("/Timeline:","")
#                post = "line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"]
#                cl.sendText(msg.to, "Success Update Timeline\n\n→" + post)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Mc
#==================================================================
#            elif msg.text in ["Mc "]:
#                mmid = msg.text.replace("Mc ","")
#                msg.contentType = 13
#                msg.contentMetadata = {"mid":mmid}
#                cl.sendMessage(msg)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Protect Join
#==================================================================
            elif msg.text in ["/Join:on","/KickJoin:on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Member Joined Group On")
                    else:
                        cl.sendText(msg.to,"KickJoin Already On")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Member Joined Group On")
                    else:
                        cl.sendText(msg.to,"KickJoin Already On")

            elif msg.text in ["/Join:off","/KickJoin:off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Member Joined Group Off")
                    else:
                        cl.sendText(msg.to,"KickJoin Already Off")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Member Joined Group Off")
                    else:
                        cl.sendText(msg.to,"KickJoin Already Off")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Protect Invite
#==================================================================
            elif msg.text in ["/NoInvite:on","/Noinvite:on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel User Invited On")
                    else:
                        cl.sendText(msg.to,"Cancel Already On")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel User Invited On")
                    else:
                        cl.sendText(msg.to,"Cancel Already On")

            elif msg.text in ["/NoInvite:off","/Noinvite:off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel User Invited Off")
                    else:
                        cl.sendText(msg.to,"Cancel Already Off")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel User Invited Off")
                    else:
                        cl.sendText(msg.to,"Cancel Already Off")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Protect Group
#==================================================================
            elif msg.text in ["/GProtect:on","/Gprotect:on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["/GProtect:off","/Gprotect:off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Info Contact
#==================================================================
            elif msg.text in ["/Contact:On","/Contact:on","/contact:on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["/Contact:Off","/Contact:off","/contact:off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Auto Join ON
#==================================================================
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","/AutoJoin:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoJoin Already On")
                    else:
                        cl.sendText(msg.to,"Auto Join On")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoJoin Already On")
                    else:
                        cl.sendText(msg.to,"Auto Join On")
#==================================================================
# COMMAND Auto Join OFF
#==================================================================                        
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","/AutoJoin:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoJoin Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join Off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoJoin Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join Off")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Gcancel
#==================================================================
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Auto Leave ON
#==================================================================
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","/AutoLeave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Already On")
                    else:
                        cl.sendText(msg.to,"AutoLeave On")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoLeave On")
                    else:
                        cl.sendText(msg.to,"Auto Leave Already On")
#==================================================================
# COMMAND Auto Leave OFF
#==================================================================                        
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","/AutoLeave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Already Off")
                    else:
                        cl.sendText(msg.to,"AutoLeave Off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoLeave Off")
                    else:
                        cl.sendText(msg.to,"Auto Leave Already Off")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Share ON
#==================================================================
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","/Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Link Post Already On")
                    else:
                        cl.sendText(msg.to,"Share Link Post On")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Link Post On")
                    else:
                        cl.sendText(msg.to,"Share Link Post Already On")
#==================================================================
# COMMAND Share OFF
#==================================================================                        
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","/Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Link Post Already Off")
                    else:
                        cl.sendText(msg.to,"Share Link Post Off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Link Post Off")
                    else:
                        cl.sendText(msg.to,"Share Link Post Already Off")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Set View
#==================================================================
            elif msg.text in ["Set View"]:
                md = ""
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Album Merit
#==================================================================                
            elif "album merit:" in msg.text:
                gid = msg.text.replace("album merit:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
#==================================================================
# COMMAND Album
#==================================================================
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
#==================================================================
# COMMAND Album
#==================================================================
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Group ID
#==================================================================
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
#==================================================================
# COMMAND Cancell All
#==================================================================
            elif msg.text in ["/All Group Cancel"]:
              if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                      cl.rejectGroupInvitation(i)
                  if wait["lang"] == "JP":
                      cl.sendText(msg.to,"All invitations have been refused")
                  else:
                      cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
#==================================================================
# COMMAND Album Removeat
#==================================================================                      
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
#==================================================================
# COMMAND Auto Add ON
#==================================================================
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","/Add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoAdd Already On")
                    else:
                        cl.sendText(msg.to,"AutoAdd On")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoAdd On")
                    else:
                        cl.sendText(msg.to,"AutoAdd Already On")
#==================================================================
# COMMAND Auto Add OFF
#==================================================================
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","/Add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoAdd Already Off")
                    else:
                        cl.sendText(msg.to,"AutoAdd Off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"AutoAdd Off")
                    else:
                        cl.sendText(msg.to,"AutoAdd Already Off")
#==================================================================
# COMMAND Finsih
#==================================================================


#==================================================================
# COMMAND Auto Add Message
#==================================================================
            elif "/ChangeMessage:" in msg.text:
                wait["message"] = msg.text.replace("/ChangeMessage:","")
                cl.sendText(msg.to,"Auto Add Message Already Change")

            elif "/AddMessage:" in msg.text:
                wait["AddMessage"] = msg.text.replace("/AddMessage:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Message Change")
                else:
                    cl.sendText(msg.to,"Done")

            elif msg.text in ["/Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Auto Add Message\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Comment Add
#==================================================================
            elif "/Comment:" in msg.text:
                c = msg.text.replace("/Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Message Changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Change\n\n→" + c)

            elif "/AddComment:" in msg.text:
                c = msg.text.replace("AddComment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Changed\n\n→" + c)

            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"Comment\n\n→" + str(wait["comment"]))
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Comment ON
#==================================================================

            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","/Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment On")
                    else:
                        cl.sendText(msg.to,"Comment Already On")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment On")
                    else:
                        cl.sendText(msg.to,"Comment Already On")
#==================================================================
# COMMAND Comment OFF
#==================================================================
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","/Comment:off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Off")
                    else:
                        cl.sendText(msg.to,"Comment Already Off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Off")
                    else:
                        cl.sendText(msg.to,"Comment Already Off")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Gurl
#==================================================================
            elif msg.text in ["/Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Group Link\n\n→ line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"Group Link\n\n→ line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Wikipedia
#==================================================================
            elif msg.text in ["/Wiki: "]:
                wikisearch = msg.text.replace("/Wiki: ","")
                cl.sendText(msg.to,wikipedia.summary(wikisearch))
#==================================================================
# COMMAND Finish
#==================================================================

	    elif "Dp @" in msg.text:
		print "[Command Steal Dp Sedang Berjalan]"
		_name = msg.text.replace("Dp @","")
		_nametarget = _name.rstrip('  ')
		gs = cl.getGroup(msg.to)
		targets = []
		for g in gs.members:
		    if _nametarget == g.displayName:
			targets.append(g.mid)
		if targets == []:
		    ki.sendText(msg.to,"Can't Steal...")
		else:
		    for target in targets:
			try:
			    contact = cl.getContact(target)
			    path ="http://dl.profile.line-cdn.net/" + contact.pictureStatus
			    cl.sendImageWithURL(msg.to, path)
			except Exception as e:
			    raise e
		print "[Command Steal Dp Berhasil]"
#==================================================================
# COMMAND Comment Bl
#==================================================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#==================================================================
# COMMAND FInish
#==================================================================
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           
         
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
              if msg.form_ in admin:
                  if wait["clock"] == True:
                      now2 = datetime.now()
                      nowT = datetime.strftime(now2,"(%H:%M)")
                      profile = kc.getProfile()
                      profile.displayName = wait["cName4"] + nowT
                      kc.updateProfile(profile)
                      kc.sendText(msg.to,"Sukses update")
                  else:
                      kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#

         #-----------------------------------------------
            elif msg.text in ["/Lurking","/lurking"]:
                if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        chiya = ""
                    else:
                        chiya = ""
                        for rom in wait2["ROM"][msg.to].items():
                            print rom
                            chiya += rom[1] + "\n"
                    cl.sendText(msg.to, "╔═════{Silent Reader}═════╗%s\n\n╚═════[X]═════╝\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                    print "Read Point Set"
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait
                    cl.sendText(msg.to, "Read Point Set Automatically....")
#                else:
#                    cl.sendText(msg.to, "Read Point Set Automatically....")
#                    print "Read Point Set"
#                    try:
#                        del wait2['readPoint'][msg.to]
#                        del wait2['readMember'][msg.to]
#                   except:
#                        pass
#                    wait2['readPoint'][msg.to] = msg.id
#                   wait2['readMember'][msg.to] = ""
#                   wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#                    wait2['ROM'][msg.to] = {}
#                    print wait
#                    cl.sendText(msg.to, "Read Point Set Automatically....")
         #-----------------------------------------------
#==================================================================
# COMMAND All Join
#==================================================================
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["/All in"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = ku.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ku.updateGroup(G)
                        print "Semua Bot Sudah Join"
                        G.preventJoinByTicket(G)
                        ku.updateGroup(G)
#==================================================================
# COMMAND Bot Join by Command
#==================================================================
            elif msg.text in ["/2in"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["/3in"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["/4in"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#
#==================================================================
# COMMAND Finish
#==================================================================


#==================================================================
# COMMAND Bye All
#==================================================================
    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["/All out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Gomenne, Matane "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                    except:
                        pass
#==================================================================
# COMMAND Out by Command
#==================================================================
            elif msg.text in ["/2out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Arigatou Gozaimasu"  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["/3out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.sendText(msg.to,"Arigatou Gozaimasu"  +  str(ginfo.name)  + "")
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["/4out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.sendText(msg.to,"Arigatou Gozaimasu"  +  str(ginfo.name)  + "")
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#==================================================================
# COMMAND 
#==================================================================                        
#            elif msg.text in ["Cv1 @bye"]:
#                if msg.toType == 2:
#                    ginfo = cl.getGroup(msg.to)
#                    try:
#                        ki.leaveGroup(msg.to)
#                    except:
#                        pass
#            elif msg.text in ["Cv2 @bye"]:
#                if msg.toType == 2:
#                    ginfo = cl.getGroup(msg.to)
#                    try:
#                        kk.leaveGroup(msg.to)
#                    except:
#                        pass
#            elif msg.text in ["Cv3 @bye"]:
#                if msg.toType == 2:
#                    ginfo = cl.getGroup(msg.to)
#                    try:
#                        kc.leaveGroup(msg.to)
#                    except:
#                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
#==================================================================
# COMMAND Tag All
#==================================================================
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["/Mention"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)
                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "🌸 @nrik \n"
                      cb = (cb[:int(len(cb)-1)])
                      msg.contentType = 0
                      msg.text = cb2
                      msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                      try:
                       cl.sendMessage(msg)
                      except Exception as error:
                       print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
#            elif msg.text in ["Kill "]:
#              if msg.from_ in admin:
#                if msg.toType == 2:
#                    group = ki.getGroup(msg.to)
#                    gMembMids = [contact.mid for contact in group.members]
#                    matched_list = []
#                    for tag in wait["blacklist"]:
#                        matched_list+=filter(lambda str: str == tag, gMembMids)
#                    if matched_list == []:
#                        kk.sendText(msg.to,"Selamat tinggal")
#                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
#                        return
#                    for jj in matched_list:
#                        try:
#                            klist=[ki,kk,kc]
#                            kicker=random.choice(klist)
#                            kicker.kickoutFromGroup(msg.to,[jj])
#                            print (msg.to,[jj])
#                        except:
#                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                
            elif "/Re" in msg.text:
              if msg.from_ in admin and Bots:
                if msg.toType == 2:
                    print "Cleanse"
                    _name = msg.text.replace("/Re","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"??")
                    kk.sendText(msg.to,"Nande??")
                    kc.sendText(msg.to,"Daijoubu..")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,ks,ka]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "/AI " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("/AI ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"No Comment")
                                    kc.sendText(msg.to,"Hidoii~")
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "/Blacklist @" in msg.text:
              if msg.from_ in admin:
                  _name = msg.text.replace("Blacklist @","")
                  _kicktarget = _name.rstrip(' ')
                  gs = ki2.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                      if _kicktarget == g.displayName:
                          targets.append(g.mid)
                          if targets == []:
                              cl.sendText(msg.to,"Not found")
                          else:
                              for target in targets:
                                  try:
                                      wait["blacklist"][target] = True
                                      f=codecs.open('st2__b.json','w','utf-8')
                                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                      k3.sendText(msg.to,"Succes Cv")
                                  except:
                                      ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                ki.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["/UpChat"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"Total: 26")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "/Say:" in msg.text:
              if msg.from_ in admin:
				  bctxt = msg.text.replace("/Say:","")
				  ki.sendText(msg.to,(bctxt))
       #--------------Fungsi Broadcast Finish-----------#
            elif msg.text in ["Hai"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

            elif msg.text in ["AI"]:
                ki.sendText(msg.to,"🍌 Berisik Ah Lu Tuh Makan Pisang Dulu")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                ki.sendText(msg.to, text)

                profile = kk.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                kk.sendText(msg.to, text)

                profile = kc.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                kc.sendText(msg.to, text)

                profile = ks.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                ks.sendText(msg.to, text)

                profile = ka.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                ka.sendText(msg.to, text)

                profile = kb.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                kb.sendText(msg.to, text)

                profile = ko.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                ko.sendText(msg.to, text)

                profile = ke.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                ke.sendText(msg.to, text)

                profile = ku.getProfile()
                text = profile.displayName + "\n\nYoroshiku~"
                ku.sendText(msg.to, text)
      #-------------Fungsi Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speedbot","speedbot"]:
              if msg.from_ in admin:
                  start = time.time()
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["/Ban"]:
              if msg.from_ in admin:
                  wait["wblacklist"] = True
                  cl.sendText(msg.to,"send contact")
            elif msg.text in ["/Unban"]:
              if msg.from_ in admin:
                  wait["dblacklist"] = True
                  cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["/Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing in Blacklist")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "Blacklist User\n\n→" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["/Check"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")

            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist User Kickout From Group")

            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")

            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")

            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")

            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
