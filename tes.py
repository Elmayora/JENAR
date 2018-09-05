# -*- coding: utf-8 -*-

import JENAR
from JENAR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,re,os,json,subprocess,codecs,threading,glob


me = JENAR.LINE() 
me.login(token="you token")
me.loginResult()

k1 = JENAR.LINE() 
k1.login(token="k1 token")
k1.loginResult()

k2 = JENAR.LINE() 
k2.login(token="k2 token")
k2.loginResult()

k3 = JENAR.LINE() 
k3.login(token="k3 token")
k3.loginResult()

k4 = JENAR.LINE() 
k4.login(token="k4 token")
k4.loginResult()

k5 = JENAR.LINE() 
k5.login(token="k5 token")
k5.loginResult()

#k6 = JENAR.LINE() 
#k6.login(token="k6 token")
#k6.loginResult()

#k7 = JENAR.LINE() 
#k7.login(token="k7 token")
#k7.loginResult()

#k8 = JENAR.LINE() 
#k8.login(token="k9 token")
#k8.loginResult()

#k9 = JENAR.LINE() 
#k9.login(token="k9 token")
#k9.loginResult()

#k10 = JENAR.LINE() 
#k10.login(token="k10 token")
#k10.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
KAC=[me,k1,k2,k3,k4,k5]
mid = me.getProfile().mid
ki1mid = k1.getProfile().mid
k2mid = k2.getProfile().mid
k3mid = k3.getProfile().mid
k4mid = k4.getProfile().mid
k5mid = k5.getProfile().mid
#k6mid = k6.getProfile().mid
#k7mid = k7.getProfile().mid
#k8mid = k8.getProfile().mid
#k9mid = k9.getProfile().mid
#k10mid = k10.getProfile().mid

Bots=[mid,k1mid,k2mid,k3mid,k4mid,k5mid]
panel = "u0ac948397fbc732bd3bc5ca273faa698"
Response = "\nrunnerBot\nline://nv/connectedDevices/"
LineBots = "https://github.com/Elmayora/JENAR"
wait = {
    "contact":False,
    "autoJoin":False,
    "leaveRoom":False,
    "respon":"http://line.me/ti/p/~sangreck",
    "timeline":False,
    "autoAdd":True,
    'message':"""❂••••GRACIAS••••❂""",
    "lang":"JP",
    "comment1":"❂••••GRACIAS••••❂",
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "stiles":"⪡❂⪢✪ŤÉŇĞĢĚŖ✪⪡❂⪢",
    "blacklist":{},
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
setTime = {}
setTime = wait2['setTime']
contact = me.getProfile()
backup = me.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    me.acceptGroupInvitation(op.param1)
                else:
                    pass
            else:
                pass
        if op.type == 22:
            if wait["leaveRoom"] == True:
                me.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                me.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    me.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                me.like(url[25:58], url[66:], likeType=1001)
                k1.like(url[25:58], url[66:], likeType=1001)
                k2.like(url[25:58], url[66:], likeType=1001)
                me.comment(url[25:58], url[66:], wait["comment1"])
                k1.comment(url[25:58], url[66:], wait["comment1"])
                k2.comment(url[25:58], url[66:], wait["comment1"])
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["contact"] == True:
                    msg.contentType = 0
                    me.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = me.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = me.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        me.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = me.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = me.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        me.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    me.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","help"]:
                if wait["lang"] == "JP":
                    md = "••statusBots••"
                    if wait["contact"] == True: md+="\n• Contact:on"
                    else: md+="\n• Contact:off"
                    if wait["timeline"] == True: md+="\n• Share:on"
                    else: md+="\n• Share:off"
                    if wait["leaveRoom"] == True: md+="\n• Autoleave:on"
                    else: md+="\n• Autoleave:off"
                    if wait["autoAdd"] == True: md+="\n• Autoadd:on"
                    else: md+="\n• autoAdd:off"
                    if wait["autoJoin"] == True: md+="\n• Autojoin:on"
                    else: md+="\n• Autojoin:off"
                    helpMessage = wait["stiles"] + "\n• Restart\n• Me\n• Speed\n• Gift\n• Halo\n• Allbot\n• Alljoin\n• Allout\n• Allname *nama\n• Myname *nama\n• Gurl\n• Curl\n• Cancel\n• Kickall \n• Kick @tag member\n" + md + "\n•Creator script•\n•••---------------•••\n" + wait["respon"]
                    me.sendText(msg.to,helpMessage)
                    me.findAndAddContactsByMid(panel)
                    me.sendText(panel,Response)
                else:
                    me.findAndAddContactsByMid(panel)
                    me.sendText(panel,Response)
                    me.sendText(msg.to,helpMessage)
            elif "Stiles " in msg.text:
                c = msg.text.replace("Stiles ","")
                if c in [""," ","\n",None]:
                    me.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["stiles"] = c
                    me.sendText(msg.to,"✨Di terapkan ✔✨\n" + c + "\nSilahkan ketik help untuk cek")
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                me.sendMessage(msg)
                me.findAndAddContactsByMid(panel)
                me.sendText(panel,Response)
            elif "Restart" == msg.text:
                    print "[Command]Like executed"
                    try:
                        me.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        me.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif "Allbot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                me.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                me.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                me.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                me.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                me.sendMessage(msg) 
                msg.contentType = 13
#                msg.contentMetadata = {'mid': k6mid}
#               me.sendMessage(msg) 
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': k7mid}
#                me.sendMessage(msg) 
#               msg.contentType = 13
#                msg.contentMetadata = {'mid': k8mid}
#                me.sendMessage(msg)
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': k9mid}
#                me.sendMessage(msg) 
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': k10mid}
#                me.sendMessage(msg) 
#                msg.contentType = 13
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                me.sendMessage(msg)
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = me.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    me.updateGroup(group)
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"URL close")
                    else:
                        me.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        me.sendText(msg.to,"Can not be used for groups other than")
            elif "Allname " in msg.text:
                string = msg.text.replace("Allname ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"Update name\n👉 " + string + "👈")
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"Update name\n👉 " + string + "👈")
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"Update name\n👉 " + string + "👈")
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"Update name\n👉 " + string + "👈")
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"Update name\n👉 " + string + "👈")
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k6.getProfile()
#                    profile.displayName = string
#                    k6.updateProfile(profile)
#                    k6.sendText(msg.to,"Update name\n👉 " + string + "👈")
#                if len(string.decode('utf-8')) <= 20:
 #                   profile = k7.getProfile()
#                    profile.displayName = string
 #                   k7.updateProfile(profile)
 #                   k7.sendText(msg.to,"Update name\n👉 " + string + "👈")
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k8.getProfile()
#                    profile.displayName = string
#                    k8.updateProfile(profile)
 #                   k8.sendText(msg.to,"Update name\n👉 " + string + "👈")
#                if len(string.decode('utf-8')) <= 20:
 #                   profile = k9.getProfile()
#                    profile.displayName = string
#                    k9.updateProfile(profile)
#                    k9.sendText(msg.to,"Update name\n👉 " + string + "👈")
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k10.getProfile()
#                    profile.displayName = string
#                    k10.updateProfile(profile)
#                    k10.sendText(msg.to,"Update name\n👉 " + string + "👈")
            elif "Myname " in msg.text:
                string = msg.text.replace("Myname ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = me.getProfile()
                    profile.displayName = string
                    me.updateProfile(profile)
                    me.sendText(msg.to,"Update Name👉 " + string + "👈")
            elif msg.text in ["Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Sudah On")
                    else:
                        me.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"already on👈")
                    else:
                        me.sendText(msg.to,"It is already open")
            elif msg.text in ["Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"sudah off")
                    else:
                        me.sendText(msg.to,"It is already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"off already")
                    else:
                        me.sendText(msg.to,"already off")
            elif msg.text in ["Autojoin:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Ini sudah on 👈")
                    else:
                        me.sendText(msg.to,"already on 👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"already ON")
                    else:
                        me.sendText(msg.to,"It is already On")
            elif msg.text in ["Autojoin:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Auto Join Already Off")
                    else:
                        me.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"already off")
                    else:
                        me.sendText(msg.to,"It is already off👈")
            elif msg.text in ["Autoleave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"on👈")
                    else:
                        me.sendText(msg.to,"already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"already on")
                    else:
                        me.sendText(msg.to,"Is already aktif")
            elif msg.text in ["Autoleave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"off")
                    else:
                        me.sendText(msg.to,"already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Done off")
                    else:
                        me.sendText(msg.to,"Is already off")
            elif msg.text in ["Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"ready")
                    else:
                        me.sendText(msg.to,"Hal ini sudah on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"on👈")
                    else:
                        me.sendText(msg.to,"on👈")
            elif msg.text in ["Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"off")
                    else:
                        me.sendText(msg.to,"It is already turned off👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Off👈")
                    else:
                        me.sendText(msg.to,"Off👈")
            elif msg.text in ["Autoadd:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Already On")
                    else:
                        me.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Already On👈")
                    else:
                        me.sendText(msg.to,"Already On👈")
            elif msg.text in ["Autoadd:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        me.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Already Off👈")
                    else:
                        me.sendText(msg.to,"Untuk mengaktifkan-off👈")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = me.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        me.updateGroup(x)
                    gurl = me.reissueGroupTicket(msg.to)
                    me.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        me.sendText(msg.to,"Can't be used outside the group")
                    else:
                        me.sendText(msg.to,"Not for use less than group")
            elif "K1 " in msg.text:
                       nk0 = msg.text.replace("K1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = me.getGroup(msg.to)
                       ginfo = me.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       me.updateGroup(gs)
                       invsend = 0
                       Ticket = me.reissueGroupTicket(msg.to)
                       kicker1.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
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
                                    k1.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    k1.leaveGroup(msg.to)
                                    gs = me.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    me.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           prankbot = [k1,k2,k3,k4,k5me]
                           kikil = random.choice(prankbot)
                           kikil.kickoutFromGroup(msg.to,[target])
                       except:
                           me.sendText(msg.to,"Error")
            elif msg.text in ["Halo"]:
                profile = k1.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                k1.sendText(msg.to, text)
                profile = k2.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                k2.sendText(msg.to, text)
#---------------------- = NUKE = ------------------
            elif "Kickall" in msg.text:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Kickall","")
                    gs = me.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        me.sendText(msg.to,"LIMIT.!!!")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[me,k1,k2,k3,k4,k5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = me.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        me.cancelGroupInvitation(msg.to,[_mid])
                    me.sendText(msg.to,"I pretended to cancel and canceled👈")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                me.sendText(msg.to, "Processing Request..")
                elapsed_time = time.time() - start
                me.sendText(msg.to, "%sseconds" % (elapsed_time))
                k1.sendText(msg.to, "%sseconds" % (elapsed_time))
                k2.sendText(msg.to, "%sseconds" % (elapsed_time))
#-----------------------------------------------
            elif msg.text in ["Alljoin"]:
                        G = me.getGroup(msg.to)
                        ginfo = me.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        me.updateGroup(G)
                        invsend = 0
                        Ticket = me.reissueGroupTicket(msg.to)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = me.getGroup(msg.to)
                        ginfo = me.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
            elif msg.text in ["Allout"]:
                if msg.toType == 2:
                    ginfo = me.getGroup(msg.to)
                    try:
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                    except:
                        pass
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        me.acceptGroupInvitation(op.param1)
                    else:
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        me.acceptGroupInvitation(op.param1)
                if k1mid in op.param3:
                    if op.param2 in Bots:
                        k2.findAndAddContactsByMid(op.param3)
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    else:
                        k2.findAndAddContactsByMid(op.param3)
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        me.kickoutFromGroup(op.param1,[op.param2])
                        k1.acceptGroupInvitation(op.param1)
                if k2mid in op.param3:
                    if op.param2 in Bots:
                        k3.findAndAddContactsByMid(op.param3)
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        kicker2.acceptGroupInvitation(op.param1)
                    else:
                        k3.findAndAddContactsByMid(op.param3)
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k2.acceptGroupInvitation(op.param1)
                 if k3mid in op.param3
                     if op.param2 in Bots:
                        me.findAndAddContactsByMid(op.param3)
                        me.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    else:
                        me.findAndAddContactsByMid(op.param3)
                        me.inviteIntoGroup(op.param1,[op.param3])
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k3.acceptGroupInvitation(op.param1)
    if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    me.sendText(op.param1,str(wait["message"]))
                    kicker1.sendText(op.param1,str(wait["message"]))
                    kicker2.sendText(op.param1,str(wait["message"]))
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
                profile = me.getProfile()
                profile.displayName = wait["cName"] + nowT
                me.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = me.fetchOps(me.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(me.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            me.Poll.rev = max(me.Poll.rev, Op.revision)
            bot(Op)


