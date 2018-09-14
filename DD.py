# -*- coding: utf-8 -*-
#DEDE SHOP CENTRE AUTO BOT
#VERSION  : SELFBOT ONLY
#CREATOR : DEDE
#ID LINE : http://line.me/ti/p/~_dede__
#WA         : +6281333833838

from LineAPI.linepy import *
from gtts import gTTS
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import ast, codecs, json, os, pytz, re, random, requests, sys, time, urllib.parse
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests,pytz, pafy, subprocess, six, ast, pytz, urllib, urllib.parse

listApp = ["CHROMEOS", "DESKTOPWIN", "DESKTOPMAC", "IOSIPAD", "WIN10"]
print ("===============[AUTO SELFBOT LOGIN START]===============\n")
client = LINE("Ewq4DBMwrLc3IRG6qro5.m2ME01d3Cv+owt3u6kxuDq.JzuF/poJT7DQSkG4HNY+fxv5HkDmPRAvQONghEOmJmQ=")
print ("===============[AUTO SELFBOT LOGIN SUKSES]==============\n")
ki = LINE("EwiWVuiu6aQh3lepoyKe.1MIYF9X8Puov4JB2doZgxG.+Bfaau3eaFTmicVh2TaDQbWjl7dpqqbQueSxVFsG9Ks=")
print ("==============[ALHAMDULILLAH LOGIN SUKSES]===============\n\n\n\n======================================\n          AUTO SELFBOT LINE\n            CREATOR : DEDE\n           DEDE SHOP CENTRE\n======================================\n\n[SELFBOT SISTEM START]")
KAC = [client]
clientMID = client.profile.mid
kiMID = ki.profile.mid
Bot =[clientMID]
creator = ["u33699ed350f7715fce593dd4e8a5d475"]
owner = ["u33699ed350f7715fce593dd4e8a5d475"]
admin = ["u33699ed350f7715fce593dd4e8a5d475"]
target = []
simisimi = []

clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientStart = time.time()
oepoll = OEPoll(client)
responsename = client.getProfile().displayName

languageOpen = codecs.open("language.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("setting.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
creatorOpen = codecs.open("hitcreator.json","r","utf-8")
OwnerOpen = codecs.open("Owner.json","r","utf-8")
AdminOpen = codecs.open("Admin.json","r","utf-8")
language = json.load(languageOpen)
read = json.load(readOpen)
settings = json.load(settingsOpen)
unsend = json.load(unsendOpen)
admin = json.load(AdminOpen)
owner = json.load(OwnerOpen)

def restartBot():
	print ("[ INFO ] BOT RESTARTED")
	python = sys.executable
	os.execl(python, python, *sys.argv)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭════════════════╮ \n┃  MENTION MEMBER : {} \n╰════════════════╯\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n[ SUKSES ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def timeChange(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days, hours = divmod(hours,24)
	weeks, days = divmod(days,7)
	months, weeks = divmod(weeks,4)
	text = ""
	if months != 0: text += "%02d Bulan" % (months)
	if weeks != 0: text += " %02d Minggu" % (weeks)
	if days != 0: text += " %02d Hari" % (days)
	if hours !=  0: text +=  " %02d Jam" % (hours)
	if mins != 0: text += " %02d Menit" % (mins)
	if secs != 0: text += " %02d Detik" % (secs)
	if text[0] == " ":
		text = text[1:]
	return text
	
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Brightly"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def command(text):
	pesan = text.lower()
	if settings["setKey"] == True:
		if pesan.startswith(settings["keyCommand"]):
			cmd = pesan.replace(settings["keyCommand"],"")
		else:
			cmd = "Undefined command"
	else:
		cmd = text.lower()
	return cmd

def backupData():
	try:
		backup = read
		f = codecs.open('read.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = settings
		f = codecs.open('setting.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = unsend
		f = codecs.open('unsend.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except Exception as error:
		pass
		return False
	
def menuSelf():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
		menuSelf =   "╭════════════════╮" + "\n" + \
                "┃HACKERS INC. TEAM BOT" + "\n" + \
                "┃         VERSI : COUPLE" + "\n" + \
                "╰═══════╬╬═══════╯" + "\n" + \
                "╭═══════╬╬═══════╮" + "\n" + \
                "┃       SELFBOT SERVICE" + "\n" + \
		        "┣•━━━━━━━━━━━━━━━━" + "\n" + \
		        "┣│✪│•" + key + "Help\n" + \
                "┣│✪│•" + key + "Setting\n" + \
                "┣│✪│•" + key + "Group\n" + \
		        "┣│✪│•" + key + "Translate\n" + \
		        "┣•━━━━━━━━━━━━━━━━" + "\n" + \
		        "┃       SELFBOT SERVICE" + "\n" + \
		        "┣•━━━━━━━━━━━━━━━━" + "\n" + \
		        "┣│✪│•" + key + "Restart" + "\n" + \
		        "┣│✪│•" + key + "Runtime" + "\n" + \
		        "┣│✪│•" + key + "Speed" + "\n" + \
		        "┣│✪│•" + key + "Self Respon" + "\n" + \
		        "┣│✪│•" + key + "Status" + "\n" + \
		        "┣│✪│•" + key + "Cpp" + "\n" + \
		        "┣│✪│•" + key + "CName: (Text)" + "\n" + \
                "┣│✪│•" + key + "CBio: (Text)" + "\n" + \
                "┣│✪│•" + key + "Me" + "\n" + \
                "┣│✪│•" + key + "MyMid" + "\n" + \
                "┣│✪│•" + key + "MyName" + "\n" + \
                "┣│✪│•" + key + "MyBio" + "\n" + \
                "┣│✪│•" + key + "MyPic" + "\n" + \
                "┣│✪│•" + key + "MyVid" + "\n" + \
                "┣│✪│•" + key + "MyCover" + "\n" + \
                "┣│✪│•" + key + "MyProfile" + "\n" + \
                "┣│✪│•" + key + "GetMid (Tag)" + "\n" + \
                "┣│✪│•" + key + "GetName (Tag)" + "\n" + \
                "┣│✪│•" + key + "GetBio (Tag)" + "\n" + \
                "┣│✪│•" + key + "GetPic (Tag)" + "\n" + \
                "┣│✪│•" + key + "GetVid (Tag)" + "\n" + \
                "┣│✪│•" + key + "GetCover (Tag)" + "\n" + \
                "┣│✪│•" + key + "Clone (Tag)" + "\n" + \
                "┣│✪│•" + key + "Restore" + "\n" + \
                "┣│✪│•" + key + "Mybackup" + "\n" + \
                "┣│✪│•" + key + "Myfriend" + "\n" + \
                "┣│✪│•" + key + "Steal (Nomor)" + "\n" + \
                "┣│✪│•" + key + "Mygroup" + "\n" + \
                "┣│✪│•" + key + "Infogr (Nomor)" + "\n" + \
                "┣│✪│•" + key + "Infomem (Nomor)" + "\n" + \
                "┣│✪│•" + key + "/info" + "\n" + \
                "┣│✪│•" + key + "BlockList" + "\n" + \
                "┣│✪│•" + key + "Fbc (Text)" + "\n" + \
                "┣│✪│•" + key + "Bcg (Text)" + "\n" + \
                "┣│✪│•" + key + "Bcpm Text)" + "\n" + \
                "┣│✪│•" + key + "Mimic (On/Off)" + "\n" + \
                "┣│✪│•" + key + "MicList" + "\n" + \
                "┣│✪│•" + key + "MicAdd (Tag)" + "\n" + \
                "┣│✪│•" + key + "Micdel (Tag)" + "\n" + \
                "┣│✪│•" + key + "Yvideo (Text)" + "\n" + \
                "┣│✪│•" + key + "Smule (ID Smule)" + "\n" + \
                "┣│✪│•" + key + "Gambar (Text)" + "\n" + \
                "┣│✪│•" + key + "Njeplak" + "\n" + \
                "┣│✪│•" + key + "Today" + "\n" + \
                "┣│✪│•" + key + "Errorr boss" + "\n" + \
                "┣•━━━━━━━━━━━━━━━━" + "\n" + \
		        "┃        COUPLE SERVICE" + "\n" + \
		        "┣•━━━━━━━━━━━━━━━━" + "\n" + \
		        "┣│✪│•" + key + "Ay Friend" + "\n" + \
		        "┣│✪│•" + key + "Aysteal (Nomor)" + "\n" + \
		        "┣│✪│•" + key + "Ay blocklist" + "\n" + \
		        "┣│✪│•" + key + "Ay group" + "\n" + \
		        "┣│✪│•" + key + "Ayinfogr (Nomor)" + "\n" + \
		        "┣│✪│•" + key + "Ayinfomem (Nomor)" + "\n" +\
		        "┣│✪│•" + key + "Aygid (Nomor)" + "\n" + \
		        "┣│✪│•" + key + "Takeme (GID)" + "\n" + \
		        "┣│✪│•" + key + "Ay out" + "\n" + \
		        "┣│✪│•" + key + "Ay in" + "\n" + \
                "╰═══════╬╬═══════╯" + "\n" + \
                "╭═══════╬╬═══════╮" + "\n" + \
                "┃       CREATOR : DEDE" + "\n" + \
                "┃    line.me/ti/p/~_dede__" + "\n" + \
                "╰════════════════╯"
	return menuSelf
	
def menuGroup():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
		menuGroup =   "╭════════════════╮" + "\n" + \
		        "┃HACKERS INC. TEAM BOT" + "\n" + \
                "┃       GROUP SERVICE" + "\n" + \
                "╰═══════╬╬═══════╯" + "\n" + \
                "╭═══════╬╬═══════╮" + "\n" + \
                "┣│✪│•" + key + "Read On" + "\n" + \
                "┣│✪│•" + key + "Reader" + "\n" + \
                "┣│✪│•" + key + "Intip/.." + "\n" + \
                "┣│✪│•" + key + "Borgol/..." + "\n" + \
                "┣│✪│•" + key + "Boss/Mention" + "\n" + \
                "┣│✪│•" + key + "Tag Name" + "\n" + \
                "┣│✪│•" + key + "Pendinglist" + "\n" + \
                "┣│✪│•" + key + "Ginfo" + "\n" + \
                "┣│✪│•" + key + "CGName: (Text)" + "\n" + \
                "┣│✪│•" + key + "CGPicture" + "\n" + \
                "┣│✪│•" + key + "GID" + "\n" + \
                "┣│✪│•" + key + "GName" + "\n" + \
                "┣│✪│•" + key + "GPicture" + "\n" + \
                "┣│✪│•" + key + "Naik cg" + "\n" + \
                "┣│✪│•" + key + "Up cg" + "\n" + \
                "╰═══════╬╬═══════╯" + "\n" + \
                "╭═══════╬╬═══════╮" + "\n" + \
                "┃       CREATOR : DEDE" + "\n" + \
                "┃    line.me/ti/p/~_dede__" + "\n" + \
                "╰════════════════╯"
	return menuGroup
	
def menuSetting():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
		menuSetting =   "╭════════════════╮" + "\n" + \
		        "┃HACKERS INC. TEAM BOT" + "\n" + \
                "┃      SETTING SERVICE" + "\n" + \
                "╰═══════╬╬═══════╯" + "\n" + \
                "╭═══════╬╬═══════╮" + "\n" + \
                "┣│✪│•" + key + "Autoadd (On/Off)" + "\n" + \
                "┣│✪│•" + key + "Autojoin (On/Off)" + "\n" + \
                "┣│✪│•" + key + "Jointicket (On/Off)" + "\n" + \
                "┣│✪│•" + key + "Autoread (On/Off)" + "\n" + \
                "┣│✪│•" + key + "Autoadd (On/Off)" + "\n" + \
                "┣│✪│•" + key + "Respon (On/Off)" + "\n" + \
                "┣│✪│•" + key + "Info (On/Off)" + "\n" + \
                "┣│✪│•" + key + "TL (On/Off)" + "\n" + \
                "┣│✪│•" + key + "SMess: (Text)" + "\n" + \
                "┣│✪│•" + key + "SRespon: (Text)" + "\n" + \
                "┣│✪│•" + key + "SJoin: (Text)" + "\n" + \
                "╰═══════╬╬═══════╯" + "\n" + \
                "╭═══════╬╬═══════╮" + "\n" + \
                "┃       CREATOR : DEDE" + "\n" + \
                "┃    line.me/ti/p/~_dede__" + "\n" + \
                "╰════════════════╯"
	return menuSetting
	
def menuTranslate():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	menuTranslate =	"╭════════════════╮" + "\n" + \
	                   "┃HACKERS INC. TEAM BOT" + "\n" + \
	                   "┃      T R A N S L A T O R" + "\n" + \
                       "╰═══════╬╬═══════╯" + "\n" + \
                       "╭═══════╬╬═══════╮" + "\n" + \
                       "┣│✪│•Tr-af : afrikaans" + "\n" + \
                       "┣│✪│•Tr-sq : albanian" + "\n" + \
                       "┣│✪│•Tr-am : amharic" + "\n" + \
                       "┣│✪│•Tr-ar : arabic" + "\n" + \
                       "┣│✪│•Tr-hy : armenian" + "\n" + \
                       "┣│✪│•Tr-az : azerbaijani" + "\n" + \
                       "┣│✪│•Tr-eu : basque" + "\n" + \
                       "┣│✪│•Tr-be : belarusian" + "\n" + \
                       "┣│✪│•Tr-bn : bengali" + "\n" + \
                       "┣│✪│•Tr-bs : bosnian" + "\n" + \
                       "┣│✪│•Tr-bg : bulgarian" + "\n" + \
                       "┣│✪│•Tr-ca : catalan" + "\n" + \
                       "┣│✪│•Tr-ceb : cebuano" + "\n" + \
                       "┣│✪│•Tr-ny : chichewa" + "\n" + \
                       "┣│✪│•Tr-zh-cn : chinese" + "\n" + \
                       "┣│✪│  (Simplified)" + "\n" + \
                       "┣│✪│•Tr-zh-tw : chinese" + "\n" + \
                       "┣│✪│  (Traditional)" + "\n" + \
                       "┣│✪│•Tr-co : corsican" + "\n" + \
                       "┣│✪│•Tr-hr : croatian" + "\n" + \
                       "┣│✪│•Tr-cs : czech" + "\n" + \
                       "┣│✪│•Tr-da : danish" + "\n" + \
                       "┣│✪│•Tr-nl : dutch" + "\n" + \
                       "┣│✪│•Tr-en : english" + "\n" + \
                       "┣│✪│•Tr-eo : esperanto" + "\n" + \
                       "┣│✪│•Tr-et : estonian" + "\n" + \
                       "┣│✪│•Tr-tl : filipino" + "\n" + \
                       "┣│✪│•Tr-fi : finnish" + "\n" + \
                       "┣│✪│•Tr-fr : french" + "\n" + \
                       "┣│✪│•Tr-fy : frisian" + "\n" + \
                       "┣│✪│•Tr-gl : galician" + "\n" + \
                       "┣│✪│•Tr-ka : georgian" + "\n" + \
                       "┣│✪│•Tr-de : german" + "\n" + \
                       "┣│✪│•Tr-el : greek" + "\n" + \
                       "┣│✪│•Tr-gu : gujarati" + "\n" + \
                       "┣│✪│•Tr-ht : haitian creole" + "\n" + \
                       "┣│✪│•Tr-ha : hausa" + "\n" + \
                       "┣│✪│•Tr-haw : hawaiian" + "\n" + \
                       "┣│✪│•Tr-iw : hebrew" + "\n" + \
                       "┣│✪│•Tr-hi : hindi" + "\n" + \
                       "┣│✪│•Tr-hmn : hmong" + "\n" + \
                       "┣│✪│•Tr-hu : hungarian" + "\n" + \
                       "┣│✪│•Tr-is : icelandic" + "\n" + \
                       "┣│✪│•Tr-ig : igbo" + "\n" + \
                       "┣│✪│•Tr-id : indonesian" + "\n" + \
                       "┣│✪│•Tr-ga : irish" + "\n" + \
                       "┣│✪│•Tr-it : italian" + "\n" + \
                       "┣│✪│•Tr-ja : japanese" + "\n" + \
                       "┣│✪│•Tr-jw : javanese" + "\n" + \
                       "┣│✪│•Tr-kn : kannada" + "\n" + \
                       "┣│✪│•Tr-kk : kazakh" + "\n" + \
                       "┣│✪│•Tr-km : khmer" + "\n" + \
                       "┣│✪│•Tr-ko : korean" + "\n" + \
                       "┣│✪│•Tr-ku : kurdish (kurmanji)" + "\n" + \
                       "┣│✪│•Tr-ky : kyrgyz" + "\n" + \
                       "┣│✪│•Tr-lo : lao" + "\n" + \
                       "┣│✪│•Tr-la : latin" + "\n" + \
                       "┣│✪│•Tr-lv : latvian" + "\n" + \
                       "┣│✪│•Tr-lt : lithuanian" + "\n" + \
                       "┣│✪│•Tr-lb : luxembourgish" + "\n" + \
                       "┣│✪│•Tr-mk : macedonian" + "\n" + \
                       "┣│✪│•Tr-mg : malagasy" + "\n" + \
                       "┣│✪│•Tr-ms : malay" + "\n" + \
                       "┣│✪│•Tr-ml : malayalam" + "\n" + \
                       "┣│✪│•Tr-mt : maltese" + "\n" + \
                       "┣│✪│•Tr-mi : maori" + "\n" + \
                       "┣│✪│•Tr-mr : marathi" + "\n" + \
                       "┣│✪│•Tr-mn : mongolian" + "\n" + \
                       "┣│✪│•Tr-my : myanmar (burmese)" + "\n" + \
                       "┣│✪│•Tr-ne : nepali" + "\n" + \
                       "┣│✪│•Tr-no : norwegian" + "\n" + \
                       "┣│✪│•Tr-ps : pashto" + "\n" + \
                       "┣│✪│•Tr-fa : persian" + "\n" + \
                       "┣│✪│•Tr-pl : polish" + "\n" + \
                       "┣│✪│•Tr-pt : portuguese" + "\n" + \
                       "┣│✪│•Tr-pa : punjabi" + "\n" + \
                       "┣│✪│•Tr-ro : romanian" + "\n" + \
                       "┣│✪│•Tr-ru : russian" + "\n" + \
                       "┣│✪│•Tr-sm : samoan" + "\n" + \
                       "┣│✪│•Tr-gd : scots gaelic" + "\n" + \
                       "┣│✪│•Tr-sr : serbian" + "\n" + \
                       "┣│✪│•Tr-st : sesotho" + "\n" + \
                       "┣│✪│•Tr-sn : shona" + "\n" + \
                       "┣│✪│•Tr-sd : sindhi" + "\n" + \
                       "┣│✪│•Tr-si : sinhala" + "\n" + \
                       "┣│✪│•Tr-sk : slovak" + "\n" + \
                       "┣│✪│•Tr-sl : slovenian" + "\n" + \
                       "┣│✪│•Tr-so : somali" + "\n" + \
                       "┣│✪│•Tr-es : spanish" + "\n" + \
                       "┣│✪│•Tr-su : sundanese" + "\n" + \
                       "┣│✪│•Tr-sw : swahili" + "\n" + \
                       "┣│✪│•Tr-sv : swedish" + "\n" + \
                       "┣│✪│•Tr-tg : tajik" + "\n" + \
                       "┣│✪│•Tr-ta : tamil" + "\n" + \
                       "┣│✪│•Tr-te : telugu" + "\n" + \
                       "┣│✪│•Tr-th : thai" + "\n" + \
                       "┣│✪│•Tr-tr : turkish" + "\n" + \
                       "┣│✪│•Tr-uk : ukrainian" + "\n" + \
                       "┣│✪│•Tr-ur : urdu" + "\n" + \
                       "┣│✪│•Tr-uz : uzbek" + "\n" + \
                       "┣│✪│•Tr-vi : vietnamese" + "\n" + \
                       "┣│✪│•Tr-cy : welsh" + "\n" + \
                       "┣│✪│•Tr-xh : xhosa" + "\n" + \
                       "┣│✪│•Tr-yi : yiddish" + "\n" + \
                       "┣│✪│•Tr-yo : yoruba" + "\n" + \
                       "┣│✪│•Tr-zu : zulu" + "\n" + \
                       "┣│✪│•Tr-fil : Filipino" + "\n" + \
                       "┣│✪│•Tr-he : Hebrew" + "\n" + \
                       "╰═══════╬╬═══════╯" + "\n" + \
                       "╭═══════╬╬═══════╮" + "\n" + \
                       "┃       CREATOR : DEDE" + "\n" + \
                       "┃    line.me/ti/p/~_dede__" + "\n" + \
                       "╰════════════════╯"
	return menuTranslate

def clientBot(op):
	try:
		if op.type == 0:
			print ("[ 0 ] END OF OPERATION")
			return

		if op.type == 5:
			print ("[ 5 ] NOTIFIED ADD CONTACT")
			if settings["autoAdd"] == True:
				client.findAndAddContactsByMid(op.param1)
			client.sendMention(op.param1, settings["autoAddMessage"], [op.param1])

		if op.type == 13:
			print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
			if settings["autoJoin"] and clientMID in op.param3:
				client.acceptGroupInvitation(op.param1)
				client.sendMention(op.param1, settings["autoJoinMessage"], [op.param2])
				
		if op.type == 26:
			try:
				print("[ 25 ] SEND MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				cmd = command(text)
				setKey = settings["keyCommand"].title()
				if settings["setKey"] == False:
					setKey = ''
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					if msg.contentType == 0:
						if cmd == "turn off":
							client.sendMessage(to, "➧ Bot Di Nonaktifkan")
							sys.exit("[ INFO ] BOT SHUTDOWN")
							return
						elif cmd == "salam":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Wa alaikum salam kk\n➧ Semoga kk selalu dalam lindungan Allah\n➧ Serta selalu diberikan yg terbaik dr yang\n   paling baik\n\n➧ Amiin yaa robbal alamiin...")
						elif cmd == "assalamualaikum":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Wa alaikum salam kk\n➧ Semoga kk selalu dalam lindungan Allah\n➧ Serta selalu diberikan yg terbaik dr yang\n   paling baik\n\n➧ Amiin yaa robbal alamiin...")
						elif cmd == "assalamu'alaikum":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Wa alaikum salam kk\n➧ Semoga kk selalu dalam lindungan Allah\n➧ Serta selalu diberikan yg terbaik dr yang\n   paling baik\n\n➧ Amiin yaa robbal alamiin...")
						elif cmd == "asalamualaikum":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Wa alaikum salam kk\n➧ Semoga kk selalu dalam lindungan Allah\n➧ Serta selalu diberikan yg terbaik dr yang\n   paling baik\n\n➧ Amiin yaa robbal alamiin...")
						elif cmd == "mikum":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Wa alaikum salam kk\n➧ Semoga kk selalu dalam lindungan Allah\n➧ Serta selalu diberikan yg terbaik dr yang\n   paling baik\n\n➧ Amiin yaa robbal alamiin...")
						elif cmd == "pagi":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Selamat pagi juga kk \n➧ Semoga hari ini bs lbh baik \n   dr hr kemarin\n\n➧ Amiin...")
						elif cmd == "met pagi":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Selamat pagi juga kk \n➧ Semoga hari ini bs lbh baik \n   dr hr kemarin\n\n➧ Amiin...")
						elif cmd == "mat pagi":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Selamat pagi juga kk \n➧ Semoga hari ini bs lbh baik \n   dr hr kemarin\n\n➧ Amiin...")
						elif cmd == "selamat pagi":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Selamat pagi juga kk \n➧ Semoga hari ini bs lbh baik \n   dr hr kemarin\n\n➧ Amiin...")
						elif cmd == "pagi kk":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Selamat pagi juga kk \n➧ Semoga hari ini bs lbh baik \n   dr hr kemarin\n\n➧ Amiin...")
						elif cmd == "siang":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met siang n met beraktifitas kk \n➧ Semoga selalu diberi kelancaran \n   n kemudahan di setiap apa yg kk kerjakan\n\n➧ Amiin...")
						elif cmd == "met siang":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met siang n met beraktifitas kk \n➧ Semoga selalu diberi kelancaran \n   n kemudahan di setiap apa yg kk kerjakan\n\n➧ Amiin...")
						elif cmd == "mat siang":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met siang n met beraktifitas kk \n➧ Semoga selalu diberi kelancaran \n   n kemudahan di setiap apa yg kk kerjakan\n\n➧ Amiin...")
						elif cmd == "selamat siang":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met siang n met beraktifitas kk \n➧ Semoga selalu diberi kelancaran \n   n kemudahan di setiap apa yg kk kerjakan\n\n➧ Amiin...")
						elif cmd == "siang kk":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met siang n met beraktifitas kk \n➧ Semoga selalu diberi kelancaran \n   n kemudahan di setiap apa yg kk kerjakan\n\n➧ Amiin...")
						elif cmd == "sore":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met sore juga kk \n➧ Cepet mandi gih,,,udah sore kk...\n➧ Kk bau banget,,,taukkkkk...\n\n➧ Wakakakakakakakak...")
						elif cmd == "met sore":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met sore juga kk \n➧ Cepet mandi gih,,,udah sore kk...\n➧ Kk bau banget,,,taukkkkk...\n\n➧ Wakakakakakakakak...")
						elif cmd == "mat sore":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met sore juga kk \n➧ Cepet mandi gih,,,udah sore kk...\n➧ Kk bau banget,,,taukkkkk...\n\n➧ Wakakakakakakakak...")
						elif cmd == "selamat sore":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met sore juga kk \n➧ Cepet mandi gih,,,udah sore kk...\n➧ Kk bau banget,,,taukkkkk...\n\n➧ Wakakakakakakakak...")
						elif cmd == "selamat sore semua":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met sore juga kk \n➧ Cepet mandi gih,,,udah sore kk...\n➧ Kk bau banget,,,taukkkkk...\n\n➧ Wakakakakakakakak...")
						elif cmd == "malam":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met malam n met rehat kk \n➧ Semoga yg kita kerjakan hari ini \n   menghasilkan sesuatu yg barokah...\n\n➧ Amiin...")
						elif cmd == "met malam":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met malam n met rehat kk \n➧ Semoga yg kita kerjakan hari ini \n   menghasilkan sesuatu yg barokah...\n\n➧ Amiin...")
						elif cmd == "mat malam":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met malam n met rehat kk \n➧ Semoga yg kita kerjakan hari ini \n   menghasilkan sesuatu yg barokah...\n\n➧ Amiin...")
						elif cmd == "selamat malam":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met malam n met rehat kk \n➧ Semoga yg kita kerjakan hari ini \n   menghasilkan sesuatu yg barokah...\n\n➧ Amiin...")
						elif cmd == "met malam semua":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Met malam n met rehat kk \n➧ Semoga yg kita kerjakan hari ini \n   menghasilkan sesuatu yg barokah...\n\n➧ Amiin...")
						elif cmd == "sepi":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Iya nih,,,sepi amat room nya...\n➧ Kali ajja dah pada kojom ama anuhnya\n➧ Makanya jangan ngejomblo teruss....\n➧ Biar ada temennya...")
						elif cmd == "sepi amat":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Iya nih,,,sepi amat room nya...\n➧ Kali ajja dah pada kojom ama anuhnya\n➧ Makanya jangan ngejomblo teruss....\n➧ Biar ada temennya...")
						elif cmd == "sepi amat roomnya":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Iya nih,,,sepi amat room nya...\n➧ Kali ajja dah pada kojom ama anuhnya\n➧ Makanya jangan ngejomblo teruss....\n➧ Biar ada temennya...")
						elif cmd == "sepi roomya":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Iya nih,,,sepi amat room nya...\n➧ Kali ajja dah pada kojom ama anuhnya\n➧ Makanya jangan ngejomblo teruss....\n➧ Biar ada temennya...")
						elif cmd == "anjay":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Dihhh.... Ngomongnya yg sopan dong\n➧ Kagak malu apa di baca banyak orang")
						elif cmd == "anjayy":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Dihhh.... Ngomongnya yg sopan dong\n➧ Kagak malu apa di baca banyak orang")
						elif cmd == "njay":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Dihhh.... Ngomongnya yg sopan dong\n➧ Kagak malu apa di baca banyak orang")
						elif cmd == "njir":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Dihhh.... Ngomongnya yg sopan dong\n➧ Kagak malu apa di baca banyak orang")
						elif cmd == "njirr":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Dihhh.... Ngomongnya yg sopan dong\n➧ Kagak malu apa di baca banyak orang")
						elif cmd == "njirrr":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Dihhh.... Ngomongnya yg sopan dong\n➧ Kagak malu apa di baca banyak orang")
						elif cmd == "sue":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Apamu yg sueek kk...???\n➧ Atw sue ora jamu..??? Xixixixi")
						elif cmd == "suee":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Apamu yg sueek kk...???\n➧ Atw sue ora jamu..??? Xixixixi")
						elif cmd == "sueee":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Apamu yg sueek kk...???\n➧ Atw sue ora jamu..??? Xixixixi")
						elif cmd == "suek":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Apamu yg sueek kk...???\n➧ Atw sue ora jamu..??? Xixixixi")
						elif cmd == "suekk":
							client.sendMention(to, "@!", [sender])
							client.sendMessage(to, "➧ Apamu yg sueek kk...???\n➧ Atw sue ora jamu..??? Xixixixi")
			except Exception as error:
				pass
				
		if op.type == 25:
			try:
				print("[ 25 ] SEND MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				cmd = command(text)
				setKey = settings["keyCommand"].title()
				if settings["setKey"] == False:
					setKey = ''
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					if msg.contentType == 0:
						if cmd == "turn off":
							client.sendMessage(to, "➧ Bot Di Nonaktifkan")
							sys.exit("[ INFO ] BOT SHUTDOWN")
							return
						elif cmd == "restart":
							client.sendMessage(to, "➧ Restarting Dots System\n➧ Tunggu 30 Detik")
							restartBot()
						elif cmd == "speed":
							start = time.time()
							client.sendMessage(to, "➧ Checking Dots Speed")
							elapsed_time = time.time() - start
							client.sendMessage(to, "➧ Speed Result : \n   {} Detik".format(str(elapsed_time)))
						elif cmd == "self respon":
							get_profile_time_start = time.time()
							get_profile = client.getProfile()
							get_profile_time = time.time() - get_profile_time_start
							get_group_time_start = time.time()
							get_group = client.getGroupIdsJoined()
							get_group_time = time.time() - get_group_time_start
							get_contact_time_start = time.time()
							get_contact = client.getContact(sender)
							get_contact_time = time.time() - get_contact_time_start
							client.sendMessage(msg.to,"╭════════════════╮\n┃      SELFBOT RESPON\n╰════════════════╯\n     ➧ Get Profile Respon :\n        %.10f\n     ➧ Get Contact Respon :\n        %.10f\n     ➧ Get Group Respon :\n        %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3) + "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
						elif cmd == "runtime":
							timeNow = time.time()
							runtime = timeNow - clientStart
							runtime = timeChange(runtime)
							client.sendMessage(to, "╭════════════════╮\n┃   SELFBOT ACTIVE TIME\n╰════════════════╯\n   ➧ Status : Aktif\n   ➧ Sistem : Normal\n   ➧ Activ Time :  \n      {}".format(str(runtime)) + "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
						elif cmd.startswith("setkey: "):
							sep = text.split(" ")
							key = text.replace(sep[0] + " ","")
							if " " in key:
								client.sendMessage(to, "➧ Jangan menggunakan spasi")
							else:
								settings["keyCommand"] = str(key).lower()
								client.sendMessage(to, "➧ Success Changing Set Ket To : \n   {} ".format(str(key).lower()))
						elif cmd == "help":
							helpSelf = menuSelf()
							contact = client.getContact(sender)
							icon = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
							name = contact.displayName
							link = "https://timeline.line.me/post/_dZNo9tm3E3PH0dURm6N9Rf_pYxmFJO2uASn_y7Q/1153217318709030407"
							client.sendFooter(to, helpSelf, icon, name, link)
						elif cmd == "group":
							helpGroup = menuGroup()
							contact = client.getContact(sender)
							icon = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
							name = contact.displayName
							link = "https://timeline.line.me/post/_dZNo9tm3E3PH0dURm6N9Rf_pYxmFJO2uASn_y7Q/1153217318709030407"
							client.sendFooter(to, helpGroup, icon, name, link)
						elif cmd == "setting":
							helpSetting = menuSetting()
							contact = client.getContact(sender)
							icon = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
							name = contact.displayName
							link = "https://timeline.line.me/post/_dZNo9tm3E3PH0dURm6N9Rf_pYxmFJO2uASn_y7Q/1153217318709030407"
							client.sendFooter(to, helpSetting, icon, name, link)
						elif cmd == "translate":
							helpTranslate = menuTranslate()
							contact = client.getContact(sender)
							icon = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
							name = contact.displayName
							link = "https://timeline.line.me/post/_dZNo9tm3E3PH0dURm6N9Rf_pYxmFJO2uASn_y7Q/1153217318709030407"
							client.sendFooter(to, helpTranslate, icon, name, link)
						elif cmd == "check":
							if msg._from in creator:
								client.sendMessage(to, "➧ H.I.T SB On")
						elif cmd == "self status":
							try:
								ret_ = "╭════════════════╮\n┃       SELFBOT STATUS\n┣•━━━━━━━━━━━━━━━━"
								if settings["autoAdd"] == True: ret_ += "\n┣• Auto Add : ON"
								else: ret_ += "\n┣• Auto Add : OFF"
								if settings["autoJoin"] == True: ret_ += "\n┣• Auto Join : ON"
								else: ret_ += "\n┣• Auto Join : OFF"
								if settings["autoJoin"] == True: ret_ += "\n┣• Join Ticket : ON"
								else: ret_ += "\n┣• Join Ticket : OFF"
								if settings["autoRead"] == True: ret_ += "\n┣• Auto Read : ON"
								else: ret_ += "\n┣• Auto Read : OFF"
								if settings["autoRespon"] == True: ret_ += "\n┣• Auto Respon : ON"
								else: ret_ += "\n┣• Auto Respon : OFF"
								if settings["checkContact"] == True: ret_ += "\n┣• Check Contact : ON"
								else: ret_ += "\n┣• Check Contact : OFF"
								if settings["checkPost"] == True: ret_ += "\n┣• Check Post : ON"
								else: ret_ += "\n┣• Check Post : OFF"
								if settings["checkSticker"] == True: ret_ += "\n┣• Check Sticker : ON"
								else: ret_ += "\n┣• Check Sticker : OFF"
								ret_ +="\n┣•━━━━━━━━━━━━━━━━\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
								client.sendMessage(to, str(ret_))
							except Exception as error:
								pass
						elif cmd == "autoadd on":
							if settings["autoAdd"] == True:
								client.sendMessage(to, "➧ Auto add aktif")
							else:
								settings["autoAdd"] = True
								client.sendMessage(to, "➧ Auto add aktif")
						elif cmd == "autoadd off":
							if settings["autoAdd"] == False:
								client.sendMessage(to, "➧ Auto add nonaktif")
							else:
								settings["autoAdd"] = False
								client.sendMessage(to, "➧ Auto add nonaktif")
						elif cmd == "autojoin on":
							if settings["autoJoin"] == True:
								client.sendMessage(to, "➧ Auto join aktif")
							else:
								settings["autoJoin"] = True
								client.sendMessage(to, "➧ Auto join aktif")
						elif cmd == "autojoin off":
							if settings["autoJoin"] == False:
								client.sendMessage(to, "➧ Auto join nonaktif")
							else:
								settings["autoJoin"] = False
								client.sendMessage(to, "➧ Auto join nonaktif")
						elif cmd == "jointicket on":
							if settings["autoJoinTicket"] == True:
								client.sendMessage(to, "➧ Auto join ticket aktif")
							else:
								settings["autoJoinTicket"] = True
								client.sendMessage(to, "➧ Auto join ticket aktif")
						elif cmd == "jointicket off":
							if settings["autoJoinTicket"] == False:
								client.sendMessage(to, "➧ Auto join ticket nonaktif")
							else:
								settings["autoJoinTicket"] = False
								client.sendMessage(to, "➧ Auto join ticket nonaktif")
						elif cmd == "autoread on":
							if settings["autoRead"] == True:
								client.sendMessage(to, "➧ Auto read aktif")
							else:
								settings["autoRead"] = True
								client.sendMessage(to, "➧ Auto read aktif")
						elif cmd == "autoread off":
							if settings["autoRead"] == False:
								client.sendMessage(to, "➧ Auto read nonaktif")
							else:
								settings["autoRead"] = False
								client.sendMessage(to, "➧ Auto read nonaktif")
						elif cmd == "respon on":
							if settings["autoRespon"] == True:
								client.sendMessage(to, "➧ Auto respon tag aktif")
							else:
								settings["autoRespon"] = True
								client.sendMessage(to, "➧ Auto respon tag aktif")
						elif cmd == "respon off":
							if settings["autoRespon"] == False:
								client.sendMessage(to, "➧ Auto respon tag nonaktif")
							else:
								settings["autoRespon"] = False
								client.sendMessage(to, "➧ Auto respon tag nonaktif")
						elif cmd == "info on":
							if settings["checkContact"] == True:
								client.sendMessage(to, "➧ Check details contact aktif")
							else:
								settings["checkContact"] = True
								client.sendMessage(to, "➧ Check details contact aktif")
						elif cmd == "info off":
							if settings["checkContact"] == False:
								client.sendMessage(to, "➧ Check details contact nonaktif")
							else:
								settings["checkContact"] = False
								client.sendMessage(to, "➧ Check details contact nonaktif")
						elif cmd == "tl on":
							if settings["checkPost"] == True:
								client.sendMessage(to, "➧ Check details post aktif")
							else:
								settings["checkPost"] = True
								client.sendMessage(to, "➧ Check details post aktif")
						elif cmd == "tl off":
							if settings["checkPost"] == False:
								client.sendMessage(to, "➧ Check details post nonaktif")
							else:
								settings["checkPost"] = False
								client.sendMessage(to, "➧ Check details post nonaktif")
						elif cmd == "cst on":
							if settings["checkSticker"] == True:
								client.sendMessage(to, "➧ Check details sticker aktif")
							else:
								settings["checkSticker"] = True
								client.sendMessage(to, "➧ Check details sticker aktif")
						elif cmd == "cst off":
							if settings["checkSticker"] == False:
								client.sendMessage(to, "➧ Check details sticker nonaktif")
							else:
								settings["checkSticker"] = False
								client.sendMessage(to, "➧ Check details sticker nonaktif")
						elif cmd.startswith("smess: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							try:
								settings["autoAddMessage"] = txt
								client.sendMessage(to, "➧ Success changing to : \n   {}".format(txt))
							except:
								client.sendMessage(to, "➧ Failed")
						elif cmd.startswith("setrespon: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							try:
								settings["autoResponMessage"] = txt
								client.sendMessage(to, "➧ Success changing to : \n   {}".format(txt))
							except:
								client.sendMessage(to, "➧ Failed")
						elif cmd.startswith("setjoin: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							try:
								settings["autoJoinMessage"] = txt
								client.sendMessage(to, "➧ Success changing to : \n   {}".format(txt))
							except:
								client.sendMessage(to, "➧ Failed")
						elif cmd == "gpicture":
							if msg.toType == 2:
								group = client.getGroup(to)
								groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
								client.sendImageWithURL(to, groupPicture)
						elif cmd == "cpp":
							settings["changePictureProfile"] = True
							client.sendMessage(to, "➧ Silahkan Kirim Fotonya")
						elif cmd == "cgp":
							if msg.toType == 2:
								if to not in settings["changeGroupPicture"]:
									settings["changeGroupPicture"].append(to)
								client.sendMessage(to, "➧ Silahkan Kirim Fotonya")
							
						elif cmd.startswith("cname: "):
							sep = text.split(" ")
							name = text.replace(sep[0] + " ","")
							if len(name) <= 20:
								profile = client.getProfile()
								profile.displayName = name
								client.updateProfile(profile)
								client.sendMessage(to, "➧ Success changing name to :\n   {}".format(name))
						elif cmd.startswith("cbio: "):
							sep = text.split(" ")
							bio = text.replace(sep[0] + " ","")
							if len(bio) <= 500:
								profile = client.getProfile()
								profile.statusMessage = bio
								client.updateProfile(profile)
								client.sendMessage(to, "➧ Success changing bio to :\n   {}".format(bio))
						elif cmd == "me":
							client.sendMention(to, "@!", [sender])
							client.sendContact(to, sender)
							contact = client.getContact(sender)
							cover = client.getProfileCoverURL(sender)
							client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
							client.sendImageWithURL(to, cover)
						elif cmd == "myprofile":
							contact = client.getContact(sender)
							cover = client.getProfileCoverURL(sender)
							result = "╭════════════════╮\n┃       DETAIL PROFILE\n╰════════════════╯"
							result += "\n ➧  Display Name : \n   @!"
							result += "\n ➧  Status Message : \n   {}".format(contact.statusMessage)
							result += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
							client.sendMention(to, result, [sender])
							client.sendMessage(to, "➧ Profil Picture")
							client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
							client.sendMessage(to, "➧ Cover Picture")
							client.sendImageWithURL(to, cover)
						elif cmd == "mymid":
							contact = client.getContact(sender)
							client.sendMention(to, "@!\n➧ Your Mid :\n   {}".format(contact.mid), [sender])
						elif cmd == "myname":
							contact = client.getContact(sender)
							client.sendMention(to, "@!\n➧ Your display name :\n   {}".format(contact.displayName), [sender])
						elif cmd == "mybio":
							contact = client.getContact(sender)
							client.sendMention(to, "➧ @!\n➧ Your Status Message :\n   {}".format(contact.statusMessage), [sender])
						elif cmd == "mypic":
							contact = client.getContact(sender)
							client.sendMessage(to, "➧ Your Picture Covet :")
							client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
						elif cmd == "myvid":
							contact = client.getContact(sender)
							if contact.videoProfile == None:
								return client.sendMessage(to, "➧ Anda tidak menggunakan video profile")
							client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
						elif cmd == "mycover":
							cover = client.getProfileCoverURL(sender)
							client.sendMessage(to, "➧ Your Cover Picture :")
							client.sendImageWithURL(to, str(cover))
						elif cmd.startswith("getmid "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									client.sendMention(to, "@! \n➧ Mid :\n   {}".format(ls), [ls])
						elif cmd.startswith("getname "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									client.sendMention(to, "@! \n➧ Display Name :\n   {}".format(contact.displayName), [ls])
						elif cmd.startswith("getbio "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									client.sendMention(to, "@! \n➧ Status Message :\n   {}".format(contact.statusMessage), [ls])
						elif cmd.startswith("getpic "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									client.sendMessage(to, "➧ Picture Profile :")
									client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
						elif cmd.startswith("getvid "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									if contact.videoProfile == None:
										return client.sendMention(to, "@!\n➧ Tidak menggunakan video profile", [ls])
									client.sendMessage(to, "➧ Video Profil :")
									client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
						elif cmd.startswith("getcover "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									cover = client.getProfileCoverURL(ls)
									client.sendMessage(to, "➧ Picture Cover :")
									client.sendImageWithURL(to, str(cover))
						elif cmd.startswith("clone "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									client.cloneContactProfile(ls)
									client.sendContact(to, sender)
									client.sendMessage(to, "➧ Berhasil clone profile")
						elif cmd == "restore":
							try:
								clientProfile = client.getProfile()
								clientProfile.displayName = str(settings["myProfile"]["displayName"])
								clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
								clientPictureStatus = client.downloadFileURL("http://dl.profile.line-cdn.net/{}".format(str(settings["myProfile"]["pictureStatus"])), saveAs="LineAPI/tmp/backupPicture.bin")
								coverId = str(settings["myProfile"]["coverId"])
								client.updateProfile(clientProfile)
								client.updateProfileCoverById(coverId)
								client.updateProfilePicture(clientPictureStatus)
								client.sendMessage(to, "➧ Berhasil restore profile")
								client.sendContact(to, sender)
								client.deleteFile(clientPictureStatus)
							except Exception as error:
								pass
								client.sendMessage(to, "➧ Gagal restore profile")
						elif cmd == "mybackup":
							try:
								clientProfile = client.getProfile()
								settings["myProfile"]["displayName"] = str(clientProfile.displayName)
								settings["myProfile"]["statusMessage"] = str(clientProfile.statusMessage)
								settings["myProfile"]["pictureStatus"] = str(clientProfile.pictureStatus)
								coverId = client.getProfileDetail()["result"]["objectId"]
								settings["myProfile"]["coverId"] = str(coverId)
								client.sendMessage(to, "➧ Berhasil backup profile")
							except Exception as error:
								pass
								client.sendMessage(to, "➧ Gagal backup profile")
						elif cmd == "myfriend":
							contacts = client.getAllContactIds()
							num = 0
							result = "╭════════════════╮\n┃        F R I E N D L I S T\n┣•━━━━━━━━━━━━━━━━"
							for listContact in contacts:
								contact = client.getContact(listContact)
								num += 1
								result += "\n┣ {}. {}".format(num, contact.displayName)
							result += "\n┣•━━━━━━━━━━━━━━━━\n┃  Total  Friend : {} ".format(len(contacts)) + "\n╰════════════════╯"
							client.sendMessage(to, result)
						elif cmd.startswith("steal "):
							sep = text.split(" ")
							query = text.replace(sep[0] + " ","")
							contacts = client.getAllContactIds()
							try:
								listContact = contacts[int(query)-1]
								contact = client.getContact(listContact)
								cover = client.getProfileCoverURL(listContact)
								result = "╭════════════════╮\n┃         DETAIL PROFILE\n╰════════════════╯"
								result += "\n ➧  Display Name : \n   @!"
								result += "\n ➧  Mid : \n   {}".format(contact.mid)
								result += "\n ➧  Status Message : \n   {}".format(contact.statusMessage)
								result += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
								client.sendMention(to, result, [contact.mid])
							except Exception as error:
								pass
						
						elif cmd == "blocklist":
							blockeds = client.getBlockedContactIds()
							num = 0
							result = "╭════════════════╮\n┃     BLOCKED ACCOUNT\n┣•━━━━━━━━━━━━━━━━"
							for listBlocked in blockeds:
								contact = client.getContact(listBlocked)
								num += 1
								result += "\n┣ {}. {}".format(num, contact.displayName)
							result += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Blocked :  {} ".format(len(blockeds)) + "\n╰════════════════╯"
							client.sendMessage(to, result)
						elif cmd == "ay blocklist":
							blockeds = ki.getBlockedContactIds()
							num = 0
							result = "╭════════════════╮\n┃     BLOCKED ACCOUNT\n┣•━━━━━━━━━━━━━━━━"
							for listBlocked in blockeds:
								contact = ki.getContact(listBlocked)
								num += 1
								result += "\n┣ {}. {}".format(num, contact.displayName)
							result += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Blocked :  {} ".format(len(blockeds)) + "\n╰════════════════╯"
							ki.sendMessage(to, result)
						elif cmd.startswith("fbc "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							contacts = client.getAllContactIds()
							for contact in contacts:
								client.sendMessage(contact, "[ D'SHOP SELFBOT BROADCAST ]\n{}".format(str(txt)))
							client.sendMessage(to, "➧ Berhasil broadcast ke {} teman".format(str(len(contacts))))
						elif cmd.startswith("cgname: "):
							if msg.toType == 2:
								sep = text.split(" ")
								groupname = text.replace(sep[0] + " ","")
								if len(groupname) <= 20:
									group = client.getGroup(to)
									group.name = groupname
									client.updateGroup(group)
									client.sendMessage(to, "➧ Berhasil mengubah nama group menjadi : \n   {}".format(groupname))
						elif cmd == "oqr":
							if msg.toType == 2:
								group = client.getGroup(to)
								group.preventedJoinByTicket = False
								client.updateGroup(group)
								groupUrl = client.reissueGroupTicket(to)
								client.sendMessage(to, "➧ Berhasil membuka QR Group\n\nGroupURL : line://ti/g/{}".format(groupUrl))
						elif cmd == "cqr":
							if msg.toType == 2:
								group = client.getGroup(to)
								group.preventedJoinByTicket = True
								client.updateGroup(group)
								client.sendMessage(to, "➧ Berhasil menutup QR Group")
						elif cmd == "gpic":
							if msg.toType == 2:
								group = client.getGroup(to)
								groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
								client.sendMessage(to, "➧ Group Cover :")
								client.sendImageWithURL(to, groupPicture)
						elif cmd == "gname":
							if msg.toType == 2:
								group = client.getGroup(to)
								client.sendMessage(to, "➧ Nama Group : {}".format(group.name))
						elif cmd == "gid":
							if msg.toType == 2:
								group = client.getGroup(to)
								client.sendMessage(to, "➧ Group ID :\n   {}".format(group.id))
						elif cmd == "mygroup":
							groups = client.getGroupIdsJoined()
							ret_ = "╭════════════════╮\n┃         M Y    G R O U P\n┣•━━━━━━━━━━━━━━━━"
							no = 0
							for gid in groups:
								group = client.getGroup(gid)
								no += 1
								ret_ += "\n┣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
							ret_ += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Groups : {} ".format(str(len(groups))) + "\n╰════════════════╯"
							client.sendMessage(to, str(ret_))
						
						elif cmd == "tag name":
							if msg.toType == 2:
								group = client.getGroup(to)
								num = 0
								ret_ = "╭════════════════╮\n┃          TAG BY NAME\n┣•━━━━━━━━━━━━━━━━"
								for contact in group.members:
									num += 1
									ret_ += "\n┣ {}. {}".format(num, contact.displayName)
								ret_ += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Members : {} ".format(len(group.members)) + "\n╰════════════════╯"
								client.sendMessage(to, ret_)
						elif cmd == "pendinglist":
							if msg.toType == 2:
								group = client.getGroup(to)
								ret_ = "╭════════════════╮\n┃         PENDING LIST\n┣•━━━━━━━━━━━━━━━━"
								no = 0
								if group.invitee is None or group.invitee == []:
									return client.sendMessage(to, "➧ Tidak ada pendingan")
								else:
									for pending in group.invitee:
										no += 1
										ret_ += "\n┣ {}. {}".format(str(no), str(pending.displayName))
									ret_ += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Pending : {} ".format(str(len(group.invitee))) + "\n╰════════════════╯"
									client.sendMessage(to, str(ret_))
						
						elif cmd == "ginfo":
							group = client.getGroup(to)
							try:
								try:
									groupCreator = group.creator.mid
								except:
									groupCreator = "   Tidak Ada (Hapus Akun)"
								if group.invitee is None:
									groupPending = "0"
								else:
									groupPending = str(len(group.invitee))
								if group.preventedJoinByTicket == True:
									groupQr = "   Tertutup"
									groupTicket = "   Tidak Ada"
								else:
									groupQr = "Terbuka"
									groupTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
								ret_ = "╭════════════════╮\n┃            GROUP INFO\n╰════════════════╯"
								ret_ += "\n ➧ Nama Group : \n   {}".format(group.name)
								ret_ += "\n ➧ Pembuat : \n   @!"
								ret_ += "\n ➧ Jumlah Member : {}".format(str(len(group.members)))
								ret_ += "\n ➧ Jumlah Pending : {}".format(groupPending)
								ret_ += "\n ➧ Group Qr : {}".format(groupQr)
								ret_ += "\n ➧ Group ID : \n   {}".format(group.id)
								ret_ += "\n ➧ Group Ticket : \n   {}".format(groupTicket)
								ret_ += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
								client.sendMention(to, str(ret_), [groupCreator])
								client.sendMessage(to, "➧ Group Cover Picture")
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus))
							except:
								pass
								
						elif cmd.startswith("bcg "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							groups = client.getGroupIdsJoined()
							for group in groups:
								client.sendMessage(group, "[ D'SHOP SELFBOT BROADCAST ]\n\n   {}".format(str(txt)))
							client.sendMessage(to, "➧ Berhasil broadcast ke : {} group".format(str(len(groups))))
						
						
						elif cmd == "cctv on":
							tz = pytz.timezone("Asia/Jakarta")
							timeNow = datetime.now(tz=tz)
							day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
							hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
							bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
							hr = timeNow.strftime("%A")
							bln = timeNow.strftime("%m")
							for i in range(len(day)):
								if hr == day[i]: hasil = hari[i]
							for k in range(0, len(bulan)):
								if bln == str(k): bln = bulan[k-1]
							readTime = "➧ " + hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n➧ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
							if to in settings['readPoint']:
								try:
									del settings['readPoint'][to]
									del settings['readMember'][to]
								except:
									pass
								settings['readPoint'][to] = msg_id
								settings['readMember'][to] = []
								client.sendMessage(to, "➧ Cctv Aktif")
							else:
								try:
									del settings['readPoint'][to]
									del settings['readMember'][to]
								except:
									pass
								settings['readPoint'][to] = msg_id
								settings['readMember'][to] = []
								client.sendMessage(to, "➧ Set reading point : \n{}".format(readTime))
						elif cmd == "cctv off":
							tz = pytz.timezone("Asia/Jakarta")
							timeNow = datetime.now(tz=tz)
							day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
							hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
							bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
							hr = timeNow.strftime("%A")
							bln = timeNow.strftime("%m")
							for i in range(len(day)):
								if hr == day[i]: hasil = hari[i]
							for k in range(0, len(bulan)):
								if bln == str(k): bln = bulan[k-1]
							readTime = "➧ " + hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n➧ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
							if to not in settings['readPoint']:
								client.sendMessage(to,"➧ Cctv Nonaktif")
							else:
								try:
									del settings['readPoint'][to]
									del settings['readMember'][to]
								except:
									pass
								client.sendMessage(to, "➧ Delete reading point : \n{}".format(readTime))
						elif cmd == "ciduk":
							if to in settings['readPoint']:
								if settings["readMember"][to] == []:
									return client.sendMessage(to, "➧ Tidak Ada Sider")
								else:
									no = 0
									result = "╭════════════════╮\n┃            LIST SIDER\n┣•━━━━━━━━━━━━━━━━"
									for dataRead in settings["readMember"][to]:
										no += 1
										result += "\n┣ {}. @!".format(str(no))
									result += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Sider : {} ".format(str(len(settings["readMember"][to]))) + "\n╰════════════════╯"
									client.sendMention(to, result, settings["readMember"][to])
									settings['readMember'][to] = []
						elif cmd == "mimic on":
							if settings["mimic"]["status"] == True:
								client.sendMessage(to, "➧ Reply message aktif")
							else:
								settings["mimic"]["status"] = True
								client.sendMessage(to, "➧ Berhasil mengaktifkan reply message")
						elif cmd == "mimic off":
							if settings["mimic"]["status"] == False:
								client.sendMessage(to, "➧ Reply message nonaktif")
							else:
								settings["mimic"]["status"] = False
								client.sendMessage(to, "➧ Berhasil menonaktifkan reply message")
						elif cmd == "miclist":
							if settings["mimic"]["target"] == {}:
								client.sendMessage(to, "➧ Tidak Ada Target")
							else:
								no = 0
								result = "╭════════════════╮\n┃          MIMIC LIST\n┣•━━━━━━━━━━━━━━━━"
								target = []
								for mid in settings["mimic"]["target"]:
									target.append(mid)
									no += 1
									result += "\n┣ {}. @!".format(no)
								result += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Mimic : {} ".format(str(len(target))) + "\n╰════════════════╯"
								client.sendMention(to, result, target)
						elif cmd.startswith("micadd "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									try:
										if ls in settings["mimic"]["target"]:
											client.sendMessage(to, "➧ Target sudah ada dalam list")
										else:
											settings["mimic"]["target"][ls] = True
											client.sendMessage(to, "➧ Berhasil menambahkan target")
									except:
										client.sendMessage(to, "➧ Gagal menambahkan target")
						elif cmd.startswith("micdel "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									try:
										if ls not in settings["mimic"]["target"]:
											client.sendMessage(to, "➧ Target sudah tidak didalam list")
										else:
											del settings["mimic"]["target"][ls]
											client.sendMessage(to, "➧ Berhasil menghapus target")
									except:
										client.sendMessage(to, "➧ Gagal menghapus target")

						elif cmd.startswith("instainfo "):
							sep = text.split(" ")
							search = text.replace(sep[0] + " ","")
							url = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
							data = url.json()
							icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/599px-Instagram_icon.png"
							name = "Instagram"
							link = "https://www.instagram.com/{}".format(data["result"]["username"])
							result = "╭════════════════╮\n┃   INSTAGRAM INFO\n╰════════════════╯"
							result += "\n ➧ Name : {}".format(data["result"]["name"])
							result += "\n ➧ Username : {}".format(data["result"]["username"])
							result += "\n ➧ Bio : {}".format(data["result"]["bio"])
							result += "\n ➧ Follower : {}".format(data["result"]["follower"])
							result += "\n ➧ Following : {}".format(data["result"]["following"])
							result += "\n ➧ Private : {}".format(data["result"]["private"])
							result += "\n ➧ Post : {}".format(data["result"]["mediacount"])
							result += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
							client.sendImageWithURL(to, data["result"]["url"])
							client.sendFooter(to, result)
						elif cmd.startswith("instastory "):
							sep = text.split(" ")
							query = text.replace(sep[0] + " ","")
							cond = query.split(" ")
							search = str(cond[0])
							if len(cond) == 2:
								url = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
								data = url.json()
								num = int(cond[1])
								if num <= len(data["url"]):
									search = data["url"][num - 1]
									if search["tipe"] == 1:
										client.sendImageWithURL(to, str(search["link"]))
									elif search["tipe"] == 2:
										client.sendVideoWithURL(to, str(search["link"]))
						elif cmd.startswith("insta "):
							sep = text.split(" ")
							search = text.replace(sep[0] + " ","")
							r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
							data = r.text
							data = json.loads(data)
							if data != []:
								ret_ = "âââ[ Profile Instagram ]"
								ret_ += "\nâ  Nama : {}".format(str(data["full_name"]))
								ret_ += "\nâ  Username : {}".format(str(data["username"]))
								ret_ += "\nâ  Bio : {}".format(str(data["biography"]))
								ret_ += "\nâ  Pengikut : {}".format(str(data["edge_followed_by"]["count"]))
								ret_ += "\nâ  Diikuti : {}".format(str(data["edge_follow"]["count"]))
								if data["is_verified"] == True:
								    ret_ += "\nâ  Verifikasi : Belum"
								if data["is_private"] == True:
									ret_ += "\nâ  Akun Pribadi : Iya"
								else:
								    ret_ += "\nâ  Akun Pribadi : Tidak"
								ret_ += "\nâ  Total Post : {}".format(str(data["edge_owner_to_timeline_media"]["count"]))
								ret_ += "\nâââ[ https://www.instagram.com/{} ]".format(search)
								path = data["profile_pic_url_hd"]
								client.sendImageWithURL(to, str(path))
								client.sendMessage(to, str(ret_))
						elif cmd == "quotes":
							url = requests.get("https://botfamily.faith/api/quotes/?apikey=beta")
							data = url.json()
							result = "╭════════════════╮\n┃             Q U O T E S\n╰════════════════╯"
							result += "\n ➧ Author : {}".format(data["result"]["author"])
							result += "\n ➧ Category : {}".format(data["result"]["category"])
							result += "\n ➧ Quote : {}".format(data["result"]["quote"])
							result += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
							client.sendMessage(to, result)
						elif cmd.startswith("say-"):
							sep = text.split("-")
							sep = sep[1].split(" ")
							lang = sep[0]
							if settings["setKey"] == False:
								txt = text.lower().replace("say-" + lang + " ","")
							else:
								txt = text.lower().replace(settings["keyCommand"] + "say-" + lang + " ","")
							if lang not in language["gtts"]:
								return client.sendMessage(to, "➧ Bahasa {} tidak ditemukan".format(lang))
							tts = gTTS(text=txt, lang=lang)
							tts.save("line/tmp/tts-{}.mp3".format(lang))
							client.sendAudio(to, "line/tmp/tts-{}.mp3".format(lang))
							client.deleteFile("line/tmp/tts-{}.mp3".format(lang))
						elif cmd.startswith("yvideo "):
							try:
								sep = msg.text.split(" ")
								textToSearch = msg.text.replace(sep[0] + " ","")
								query = urllib.parse.quote(textToSearch)
								search_url="https://www.youtube.com/results?search_query="
								mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
								sb_url = search_url + query
								sb_get = requests.get(sb_url, headers = mozhdr)
								soupeddata = BeautifulSoup(sb_get.content, "html.parser")
								yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
								x = (yt_links[1])
								yt_href =  x.get("href")
								yt_href = yt_href.replace("watch?v=", "")
								qx = "https://youtu.be" + str(yt_href)
								vid = pafy.new(qx)
								stream = vid.streams
								best = vid.getbest()
								best.resolution, best.extension
								for s in stream:
									me = best.url
									vin = s.url
									hasil = ""
									title = "╭════════════════╮\n┃           DETAIL VIDEO\n╰════════════════╯\n  ➧ Judul : " + vid.title
									author = '\n  ➧ Author : ' + str(vid.author)
									durasi = '\n  ➧ Duration : ' + str(vid.duration)
									suka = '\n  ➧ Likes : ' + str(vid.likes)
									dislike = '\n  ➧ Dislikes : ' + str(vid.dislikes)
									rating = '\n  ➧ Rating : ' + str(vid.rating)
								client.sendMessage(to,title+ author+ durasi+ suka+dislike+ rating+"\n  ➧ Source : Youtube\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
								
								client.sendVideoWithURL(to, me)
								client.sendMessage(to, "➧ Enjoy it.....\n\n➧ By : D'SHOP SELFBOT")
							except Exception as e:
								client.sendMessage(msg.to,str(e))
						elif cmd.startswith("gambar "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							url = requests.get("https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q={}".format(txt))
							data = url.json()
							client.sendImageWithURL(to, random.choice(data["result"]))
						elif cmd.startswith("play "):
							sep = text.split("|")
							query = text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							url = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
							data = url.json()
							if len(cond) == 1:
								num = 0
								ret_ = "╭════════════════╮\n┃        MUSIC RESULT\n╰════════════════╯"
								for music in data["result"]:
									num += 1
									ret_ += "\n ➧ {}. {}".format(str(num), str(music["single"]))
								ret_ += "\n╭════════════════╮\n┃       Total Music : {} ".format(str(len(data["result"])) + " \n╰════════════════╯")
								ret_ += "\n\n➧ Untuk memutar music : \n➧ Silahkan ketik :  {} {}|_(Nomor)".format(str(setKey), str(search))
								client.sendMessage(to, str(ret_))
							elif len(cond) == 2:
								num = int(cond[1])
								if num <= len(data["result"]):
									music = data["result"][num - 1]
									url = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
									data = url.json()
									ret_ = "╭════════════════╮\n┃          DETAIL MUSIC\n╰════════════════╯"
									ret_ += "\n ➧ Title : {}".format(str(data["result"]["song"]))
									ret_ += "\n ➧ Album : {}".format(str(data["result"]["album"]))
									ret_ += "\n ➧ Size : {}".format(str(data["result"]["size"]))
									ret_ += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
									client.sendImageWithURL(to, str(data["result"]["img"]))
									client.sendMessage(to, str(ret_))
									client.sendMessage(to, "➧ Downloading Audio...")
									client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
									client.sendMessage(to, "➧ Selamat Mendengarkan")
								                   
						elif cmd.startswith("lyric "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							cond = txt.split("|")
							query = cond[0]
							with requests.session() as web:
								web.headers["user-agent"] = "Mozilla/5.0"
								url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
								data = BeautifulSoup(url.content, "html.parser")
								result = []
								for trackList in data.findAll("ul", {"class":"tracks list"}):
									for urlList in trackList.findAll("a"):
										title = urlList.text
										url = urlList["href"]
										result.append({"title": title, "url": url})
								if len(cond) == 1:
									ret_ = "╭════════════════╮\n┃           MUSIC RESULT\n┣•━━━━━━━━━━━━━━━━"
									num = 0
									for title in result:
										num += 1
										ret_ += "\n┣ {}. {}".format(str(num), str(title["title"]))
									ret_ += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Lyric : {} ".format(str(len(result)) + " \n╰════════════════╯")
									ret_ += "\n\n➧ Untuk melihat liriknya : \n➧ Silahkan ketik : {}Lyric {}|_(Nomor)".format(str(setKey), str(query))
									client.sendMessage(to, ret_)
								elif len(cond) == 2:
									num = int(cond[1])
									if num <= len(result):
										data = result[num - 1]
										with requests.session() as web:
											web.headers["user-agent"] = "Mozilla/5.0"
											url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
											data = BeautifulSoup(url.content, "html5lib")
											for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
												lyric = lyricContent.text
												client.sendMessage(to, lyric)
						elif cmd.startswith("tr-"):
							sep = text.split("-")
							sep = sep[1].split(" ")
							lang = sep[0]
							if settings["setKey"] == False:
								txt = text.lower().replace("tr-" + lang + " ","")
							else:
								txt = text.lower().replace(settings["keyCommand"] + "tr-" + lang + " ","")
							if lang not in language["googletrans"]:
								return client.sendMessage(to, "➧ Bahasa {} tidak ditemukan".format(lang))
							translator = Translator()
							result = translator.translate(txt, dest=lang)
							client.sendMessage(to, result.text)
						if text.lower() == "mykey":
							client.sendMessage(to, "➧ Keycommand yang diset saat ini : \n   {}".format(str(settings["keyCommand"])))
						elif text.lower() == "setkey on":
							if settings["setKey"] == True:
								client.sendMessage(to, "➧ Setkey telah aktif")
							else:
								settings["setKey"] = True
								client.sendMessage(to, "➧ Berhasil mengaktifkan setkey")
						elif text.lower() == "/info":
							if settings["checkContact"] == True:
								client.sendMessage(to, "➧ Kirim Kontaknya")
							else:
								settings["checkContact"] = True
								client.sendMessage(to, "➧ Kirim Kontaknya")
						elif text.lower() == "setkey off":
							if settings["setKey"] == False:
								client.sendMessage(to, "➧ Setkey telah nonaktif")
							else:
								settings["setKey"] = False
								client.sendMessage(to, "➧ Berhasil menonaktifkan setkey")
						elif cmd == "detectunsend on":
							if settings["detectUnsend"] == True:
								client.sendMessage(to, "Detect unsend telah aktif")
							else:
								settings["detectUnsend"] = True
								client.sendMessage(to, "Berhasil mengaktifkan detect unsend")
						elif cmd == "boss" or text.lower() == 'mention':
							group = client.getGroup(msg.to)
							nama = [contact.mid for contact in group.members]
							nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
							if jml <= 20:
								mentionMembers(msg.to, nama)
							if jml > 20 and jml < 40:
								for i in range (0, 20):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
							if jml > 40 and jml < 60:
								for i in range (0, 20):
									nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (20, 40):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
								for k in range (40, len(nama)-1):
									nm3 += [nama[k]]
								mentionMembers(msg.to, nm3)
							if jml > 60 and jml < 80:
								for i in range (0, 20):
									nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (20, 40):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
								for k in range (40, 60):
									nm3 += [nama[k]]
								mentionMembers(msg.to, nm3)
								for l in range (80, len(nama)-1):
									nm4 += [nama[l]]
								mentionMembers(msg.to, nm4)
							if jml > 80 and jml < 100:
								for i in range (0, 20):
									nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (20, 40):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
								for k in range (40, 60):
									nm3 += [nama[k]]
								mentionMembers(msg.to, nm3)
								for l in range (60, 80):
									nm4 += [nama[l]]
								mentionMembers(msg.to, nm4)
								for m in range (80, len(nama)-1):
									nm5 += [nama[m]]
								mentionMembers(msg.to, nm4)
						elif cmd == "read on":
							try:
								del settings['cctv']['point'][receiver]
								del settings['cctv']['sidermem'][receiver]
								del settings['cctv']['cyduk'][receiver]
							except:
								pass
							settings['cctv']['point'][receiver] = msg.id
							settings['cctv']['sidermem'][receiver] = "[°PENGINTIP TERCYDUK°]\n"
							settings['cctv']['cyduk'][receiver]=True
							client.sendMessage(receiver, "➧ Sider 1 Active")
						elif cmd == "reader":
							if msg.to in cctv['point']:
								settings['cctv']['cyduk'][receiver]=False
								client.sendMessage(receiver, settings['cctv']['sidermem'][msg.to])
						elif cmd == ".." or text.lower() == 'intip':
							try:
								del settings['cctv3']['point3'][receiver]
								del settings['cctv3']['sidermem3'][receiver]
								del settings['cctv3']['cyduk3'][receiver]
							except:
								pass
							settings['cctv3']['point3'][receiver] = msg.id
							settings['cctv3']['sidermem3'][receiver] = "[°PENGINTIP TERCYDUK°]\n"
							settings['cctv3']['cyduk3'][receiver]=True
							settings['cctv3']['cyduk'][receiver]=False
						elif cmd == "..." or text.lower() == 'borgol':
							if msg.to in settings['cctv3']['point3']:
								settings['cctv3']['cyduk3'][receiver]=False
								client.sendMessage(receiver, settings['cctv3']['sidermem3'][msg.to])
							else:
								client.sendMessage(receiver, "➧ Nyalain sider dulu")
						elif cmd == "errorr boss":
							client.sendMessage(msg.to,"➧ Waduh......hp aim error..!!!\n\n\n69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69.69")
						elif cmd == "njeplak":
							jomblo = ['Istri yang baik itu istri yang mengizinkan suaminya untuk poligami kak...','Kakak ingin membahagiakan suami...???\nKuncinya cuma satu kakak..\nIzinkan suamimu untuk selingkuh...\nItu sajja.... ','Kunci kebahagiaan itu dari hati bos...\nBukan dr materi atw fisik... Ye kan.??','Meminta maaf jika kita salah\nbukan berarti merendahkan diri sendiri lho kak...','Selalu bersyukur ya kak...\nBar hidup kita lbh tenang n damai... Amiiinnnn....','Jangan sampai edan krn cinta dunia maya ya kak...\nApalagi sampai lupa ama keluarga...\nSadarlah,,,bahwa dunia maya hanyalah hal yg gak jelas n gak pasti ajja kak']
							psn = random.choice(jomblo)
							client.sendMessage(msg.to,"➧ " + psn)
						elif cmd == "naik cg":
							group = client.getGroup(msg.to)
							members = [mem.mid for mem in group.members]
							jmlh = int(settings["anuh1"])
							if jmlh <= 100:
								for x in range(jmlh):
									try:
										client.acquireGroupCallRoute(msg.to)
										client.inviteIntoGroupCall(msg.to, contactIds=members)
									except:
										pass
						elif cmd == "up cg":
							group = client.getGroup(msg.to)
							members = [mem.mid for mem in group.members]
							jmlh = int(settings["anuh2"])
							if jmlh <= 100:
								for x in range(jmlh):
									try:
										client.acquireGroupCallRoute(msg.to)
										client.inviteIntoGroupCall(msg.to, contactIds=members)
									except:
										pass
						elif cmd == "((":
							group = client.getGroup(msg.to)
							members = [mem.mid for mem in group.members]
							jmlh = int(settings["anuh3"])
							if jmlh <= 100:
								for x in range(jmlh):
									try:
										client.acquireGroupCallRoute(msg.to)
										client.inviteIntoGroupCall(msg.to, contactIds=members)
									except:
										pass
						elif cmd == "(((":
							group = client.getGroup(msg.to)
							members = [mem.mid for mem in group.members]
							jmlh = int(settings["anuh4"])
							if jmlh <= 1000:
								for x in range(jmlh):
									try:
										client.acquireGroupCallRoute(msg.to)
										client.inviteIntoGroupCall(msg.to, contactIds=members)
									except:
										pass
						elif cmd == "today":
							tz = pytz.timezone("Asia/Jakarta")
							timeNow = datetime.now(tz=tz)
							day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
							hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
							bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
							hr = timeNow.strftime("%A")
							bln = timeNow.strftime("%m")
							for i in range(len(day)):
								if hr == day[i]: hasil = hari[i]
							for k in range(0, len(bulan)):
								if bln == str(k): bln = bulan[k-1]
							readTime = "╭════════════════╮\n┃       K A L E N D E R\n╰════════════════╯\n  ➧ Hari        : "+hasil + "\n  ➧ Tanggal : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n  ➧ Jam       : " + timeNow.strftime('%H:%M:%S')
							client.sendMessage(msg.to, readTime)
#COUPLE BOT START
						elif cmd == "ay friend":
							contacts = ki.getAllContactIds()
							num = 0
							result = "╭════════════════╮\n┃        F R I E N D L I S T\n┣•━━━━━━━━━━━━━━━━"
							for listContact in contacts:
								contact = ki.getContact(listContact)
								num += 1
								result += "\n┣ {}. {}".format(num, contact.displayName)
							result += "\n┣•━━━━━━━━━━━━━━━━\n┃  Total  Friend : {} ".format(len(contacts)) + "\n╰════════════════╯"
							ki.sendMessage(to, result)
						elif cmd.startswith("aysteal "):
							sep = text.split(" ")
							query = text.replace(sep[0] + " ","")
							contacts = ki.getAllContactIds()
							try:
								listContact = contacts[int(query)-1]
								contact = ki.getContact(listContact)
								cover = ki.getProfileCoverURL(listContact)
								result = "╭════════════════╮\n┃         DETAIL PROFILE\n╰════════════════╯"
								result += "\n ➧  Display Name : \n   @!"
								result += "\n ➧  Mid : \n   {}".format(contact.mid)
								result += "\n ➧  Status Message : \n   {}".format(contact.statusMessage)
								result += "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
								ki.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
								ki.sendMention(to, result, [contact.mid])
							except Exception as error:
								pass
						elif cmd == "ay group":
							groups = ki.getGroupIdsJoined()
							ret_ = "╭════════════════╮\n┃         M Y    G R O U P\n┣•━━━━━━━━━━━━━━━━"
							no = 0
							for gid in groups:
								group = ki.getGroup(gid)
								no += 1
								ret_ += "\n┣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
							ret_ += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Groups : {} ".format(str(len(groups))) + "\n╰════════════════╯"
							ki.sendMessage(to, str(ret_))
						elif cmd.startswith("ayinfogr "):
							separate = text.split(" ")
							number = text.replace(separate[0] + " ","")
							groups = ki.getGroupIdsJoined()
							ret_ = ""
							try:
								group = groups[int(number)-1]
								G = ki.getGroup(group)
								try:
									gCreator = G.creator.displayName
								except:
									gCreator = "Hapus Akun"
								if G.invitee is None:
									gPending = "0"
								else:
									gPending = str(len(G.invitee))
								if G.preventedJoinByTicket == True:
									gQr = "Tertutup"
									gTicket = "Tertutup"
								else:
									gQr = "Terbuka"
									gTicket = "https://line.me/R/ti/g/{}".format(str(ki.reissueGroupTicket(G.id)))
								timeCreated = []
								timeCreated.append(time.strftime("%d-%m-%Y •• %H:%M:%S ", time.localtime(int(G.createdTime) / 1000)))
								ret_ += "╭════════════════╮\n┃           GROUP INFO\n╰════════════════╯\n"
								ret_ += "\n  ➧ NAME        : \n     {}".format(G.name)
								ret_ += "\n  ➧ CREATOR : \n     {}".format(gCreator)
								ret_ += "\n  ➧ CEATED    : \n     {}".format(str(timeCreated))
								ret_ += "\n  ➧ MEMBER  : \n     ( {} ) Orang".format(str(len(G.members)))
								ret_ += "\n  ➧ PENDING : \n     ( {} ) Orang".format(gPending)
								ret_ += "\n  ➧ QR              : \n     {}".format(gQr)
								ret_ += "\n  ➧ TICKET     : \n     {}".format(gTicket)
								ret_ += ""
								ki.sendMessage(to, str(ret_) + "\n\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
							except:
								pass
						elif cmd.startswith("ayinfomem "):
							separate = msg.text.split(" ")
							number = msg.text.replace(separate[0] + " ","")
							groups = ki.getGroupIdsJoined()
							ret_ = ""
							try:
								group = groups[int(number)-1]
								G = ki.getGroup(group)
								no = 0
								ret_ = ""
								for mem in G.members:
									no += 1
									ret_ += "\n  ➧ "+ str(no) + ". " + mem.displayName
								ki.sendMessage(to,"╭════════════════╮\n┃        INFO MEMBER\n╰════════════════╯\n  [ " + str(G.name) + " ]\n" + ret_ + "\n\n  [ JUMLAH :  %i MEMBERS ]" % len(G.members) + "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
							except:
								pass
						elif cmd == 'ay gid':
							if msg.toType == 2:
								group = ki.getGroupIdsJoined()
								no = 0
								ret_ = ""
								for gid in group:
									group = ki.getGroup(gid)
									no += 1
									ret_ += "\n➧  {}. {} | {}".format(str(no), str(group.name), str(group.id))
									ki.sendMessage(to, str(ret_))
						elif cmd.startswith("takeme "):
							separate = msg.text.split(" ")
							gid = text.replace(separate[0] + " ","")
							groups = ki.getGroupIdsJoined()
							if gid == "":
								ki.sendText(msg.to,"➧ Invalid Group Id")
							else:
								try:
									ki.findAndAddContactsByMid(sender)
									ki.inviteIntoGroup(gid,[sender])
								except:
									pass
						elif cmd.startswith("ayout "):
							separate = msg.text.split(" ")
							gid = text.replace(separate[0] + " ","")
							groups = ki.getGroupIdsJoined()
							if gid == "":
								ki.sendMessage(msg.to,"➧ Invalid Group Id")
							else:
								try:
									ki.leaveGroup(gid,[sender])
									ki.sendMessage(msg.to,"➧ Success")
								except:
									pass
						elif cmd == 'ay in':
							G = client.getGroup(msg.to)
							ginfo = client.getGroup(msg.to)
							G.preventJoinByTicket = False
							client.updateGroup(G)
							invsend = 0
							Ticket = client.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.001)
							G = client.getGroup(msg.to)
							ginfo = client.getGroup(msg.to)
							G.preventJoinByTicket = True
							client.updateGroup(G)
						elif cmd == 'ay out':
							if msg.toType == 2:
								ginfo = client.getGroup(msg.to)
								try:
									ki.leaveGroup(msg.to)
									ki.sendMessage(msg.to,"➧ Pamit dulu ya... \n➧ Aim Diminta Keluar Oleh Ayank Bebekk")
								except:
									pass

						elif cmd == 'clean up':
							#if msg._from in owner:
								if msg.toType == 2:
									print ("[ 19 ] KICK ALL MEMBER")
									_name = msg.text.replace("clean up","")
									gs = client.getGroup(msg.to)
									targets = []
									for g in gs.members:
										if _name in g.displayName:
											targets.append(g.mid)
										if targets == []:
											client.sendMessage(msg.to,"➧ Not Found")
										else:
											for target in targets:
												if not target in Bots:
													if not target in Owner:
														if not target in admin:
															try:
																client.kickoutFromGroup(msg.to,[target])
																print (msg.to,[g.mid])
															except:
																client.sendMessage(msg.to,"➧ Auto Cleaning Up Member")
						elif cmd == 'memlist':
							kontak = client.getGroup(msg.to)
							group = kontak.members
							num=1
							msgs="╭════════════════╮\n┃        GROUP MEMBER\n╰════════════════╯\n [ " + str(G.name) + " ]\n  "
							for ids in group:
								msgs+="\n  ➧ [%i]• %s" % (num, ids.displayName) 
								num=(num+1)
							msgs+="\n\n [ Total Members : %i  ]"% len(group) + "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯"
							client.sendMessage(receiver, msgs)
						elif cmd.startswith("infomem "):
							separate = msg.text.split(" ")
							number = msg.text.replace(separate[0] + " ","")
							groups = client.getGroupIdsJoined()
							ret_ = ""
							try:
								group = groups[int(number)-1]
								G = client.getGroup(group)
								no = 0
								ret_ = ""
								for mem in G.members:
									no += 1
									ret_ += "\n  ➧ "+ str(no) + ". " + mem.displayName
								client.sendMessage(to,"╭════════════════╮\n┃        INFO MEMBER\n╰════════════════╯\n  [ " + str(G.name) + " ]\n" + ret_ + "\n\n  [ JUMLAH :  %i MEMBERS ]" % len(G.members) + "\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
							except:
								pass
						elif cmd.startswith("aygid "):
							separate = msg.text.split(" ")
							number = msg.text.replace(separate[0] + " ","")
							groups = ki.getGroupIdsJoined()
							ret_ = ""
							for gid in groups:
								groups = groups[int(number)-1]
								groups = ki.getGroup(gid)
								ret_ += "➧ GID : {}\n{}".format(str(groups.name), str(groups.id))
								ki.sendMessage(to, str(ret_))
						elif cmd.startswith("aypendinglist "):
							separate = msg.text.split(" ")
							number = msg.text.replace(separate[0] + " ","")
							groups = ki.getGroupIdsJoined()
							ret_ = ""
							if msg.toType == 2:
								try:
									group = groups[int(number)-1]
									group = ki.getGroup(pending)
									ret_ = "╭════════════════╮\n┃         PENDING LIST\n┣•━━━━━━━━━━━━━━━━"
									no = 0
									if group.invitee is None or group.invitee == []:
										return ki.sendMessage(to, "➧ Tidak ada pendingan")
									else:
										for pending in group.invitee:
											no += 1
											ret_ += "\n┣ {}. {}".format(str(no), str(pending.displayName))
										ret_ += "\n┣•━━━━━━━━━━━━━━━━\n┃ Total Pending : {} ".format(str(len(group.invitee))) + "\n╰════════════════╯"
										ki.sendMessage(to, str(ret_))
								except:
									pass
						elif cmd.startswith("infogr "):
							separate = text.split(" ")
							number = text.replace(separate[0] + " ","")
							groups = client.getGroupIdsJoined()
							ret_ = ""
							try:
								group = groups[int(number)-1]
								G = client.getGroup(group)
								try:
									gCreator = G.creator.displayName
								except:
									gCreator = "Hapus Akun"
								if G.invitee is None:
									gPending = "0"
								else:
									gPending = str(len(G.invitee))
								if G.preventedJoinByTicket == True:
									gQr = "Tertutup"
									gTicket = "Tertutup"
								else:
									gQr = "Terbuka"
									gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
								timeCreated = []
								timeCreated.append(time.strftime("%d-%m-%Y •• %H:%M:%S ", time.localtime(int(G.createdTime) / 1000)))
								ret_ += "╭════════════════╮\n┃           GROUP INFO\n╰════════════════╯\n"
								ret_ += "\n  ➧ NAME        : \n     {}".format(G.name)
								ret_ += "\n  ➧ CREATOR : \n     {}".format(gCreator)
								ret_ += "\n  ➧ CEATED    : \n     {}".format(str(timeCreated))
								ret_ += "\n  ➧ MEMBER  : \n     ( {} ) Orang".format(str(len(G.members)))
								ret_ += "\n  ➧ PENDING : \n     ( {} ) Orang".format(gPending)
								ret_ += "\n  ➧ QR              : \n     {}".format(gQr)
								ret_ += "\n  ➧ TICKET     : \n     {}".format(gTicket)
								ret_ += ""
								client.sendMessage(to, str(ret_) + "\n\n╭════════════════╮\n┃HACKERS INC.TEAM BOT \n╰════════════════╯")
							except:
								pass
						
						elif cmd.startswith("smule "):
							try:
								separate = msg.text.split(" ")
								smule = msg.text.replace(separate[0] + " ","")
								links = ("https://smule.com/"+smule)
								ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
								client.sendMessage(msg.to,"➧ Searching")
								time.sleep(1)
								client.sendMessage(msg.to,"➧ ID Smule : "+smule+"\n➧ Link : "+links)
								client.sendImageWithURL(msg.to, ss)
							except:
								pass
						elif cmd.startswith("gambar "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							url = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(txt))
							data = url.json()
							client.sendImageWithURL(to, random.choice(data["result"]))
			except Exception as error:
				pass
				
		if op.type == 26:
			try:
				print("[ 26 ] RECEIVE MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
						if msg.contentType == 0:
							client.sendMessage(to, text)
						elif msg.contentType == 1:
							path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-mimic.bin".format(time.time()))
							client.sendImage(to, path)
							client.deleteFile(path)
					if msg.contentType == 0:
						if settings["autoRead"] == True:
							client.sendChatChecked(to, msg_id)
						if sender not in clientMID:
							if msg.toType != 0 and msg.toType == 2:
								if 'MENTION' in msg.contentMetadata.keys()!= None:
									names = re.findall(r'@(\w+)', text)
									mention = ast.literal_eval(msg.contentMetadata['MENTION'])
									mentionees = mention['MENTIONEES']
									for mention in mentionees:
										if clientMID in mention["M"]:
											if settings["autoRespon"] == True:
												dots = "➧ Yes bos...\n➧ Pasti mau ngajakin kojom yaa....","➧ Oittt,,,hadir bos\n➧ Ada apa ya..??","➧ Aim masih di sini setia menemanimu","➧ Mau minta jatah lagi ya","➧ Ingat bos\n➧ Harga tag sudah naik..!!!!","➧ Ada apa bos\n➧ Bikin kaget ajjah...","➧ Sudah dulu tag nya bos \n➧ Besok ajja tag aim lagi gpp....","➧ Selow ajja bos\n➧ Aim kagak akan nikung bebebzmu koq..."
												pilih = random.choice(dots)
												client.sendMention(sender, pilih)
											break
					if msg.contentType == 0:
						if settings["autoRead"] == True:
							if msg.to in simisimi:
								try:
									if msg.text is not None:
										simi = msg.text
										r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
										data = r.text
										data = json.loads(data)
										if data["status"] == 200:
											client.sendMessage(msg.to, str(data["answer"]))
								except Exception as error:
									pass
						if text is None: return
					if msg.contentType == 16:
						url = msg.contentMetadata["postEndUrl"]
						client.like(url[25:58], url[66:], likeType=1001)
						client.comment(url[25:58], url[66:], settings["comment"])
						
						if "/ti/g/" in msg.text.lower():
							if settings["autoJoinTicket"] == True:
								link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
								links = link_re.findall(text)
								n_links = []
								for l in links:
									if l not in n_links:
										n_links.append(l)
								for ticket_id in n_links:
									group = client.findGroupByTicket(ticket_id)
									client.acceptGroupInvitationByTicket(group.id,ticket_id)
									client.sendMessage(to, "➧ Berhasil masuk ke group %s" % str(group.name))
					elif msg.contentType == 1:
						if settings["changePictureProfile"] == True:
							path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
							settings["changePictureProfile"] = False
							client.updateProfilePicture(path)
							client.sendMessage(to, "➧ Berhasil Mengganti PP")
							client.deleteFile(path)
					if msg.toType == 2:
						if to in settings["changeGroupPicture"]:
							path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
							settings["changeGroupPicture"].remove(to)
							client.updateGroupPicture(to, path)
							client.sendMessage(to, "➧ Berhasil Mengganti Cover Group")
							client.deleteFile(path)
					elif msg.contentType == 7:
						if settings["checkSticker"] == True:
							stk_id = msg.contentMetadata['STKID']
							stk_ver = msg.contentMetadata['STKVER']
							pkg_id = msg.contentMetadata['STKPKGID']
							ret_ = "╭━━━━━━━━━━━━━━━━╮\n┃        DETAIL STICKER\n╰━━━━━━━━━━━━━━━━╯"
							ret_ += "\n  ➧ STK_ID : {}".format(stk_id)
							ret_ += "\n  ➧ STK_PKG : {}".format(pkg_id)
							ret_ += "\n  ➧ STK_VER : {}".format(stk_ver)
							ret_ += "\n  ➧ STK_URL : \n   line://shop/detail/{}".format(pkg_id)
							ret_ += "\n╭━━━━━━━━━━━━━━━━╮\n┃HACKERS INC.TEAM BOT \n╰━━━━━━━━━━━━━━━━╯"
							client.sendMessage(to, str(ret_))
					elif msg.contentType == 13:
						if settings2["checkContact"] == True:
							try:
								contact = client.getContact(msg.contentMetadata["mid"])
								cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
								ret_ = "╭━━━━━━━━━━━━━━━━╮\n┃       DETAIL CONTACT\n╰━━━━━━━━━━━━━━━━╯"
								ret_ += "\n ➧ Nama : {}".format(str(contact.displayName))
								ret_ += "\n ➧ Bio : \n   {}".format(str(contact.statusMessage))
								ret_ += "\n╭━━━━━━━━━━━━━━━━╮\n┃HACKERS INC.TEAM BOT \n╰━━━━━━━━━━━━━━━━╯"
								client.sendMessage(to, str(ret_))
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus)))
								client.sendImageWithURL(to, cover)
							except:
								client.sendMessage(to, "➧ Kontak tidak valid")
					elif msg.contentType == 16:
						if settings2["checkPost"] == True:
							try:
								ret_ = "╭━━━━━━━━━━━━━━━━╮\n┃          DETAIL POST\n╰━━━━━━━━━━━━━━━━╯"
								if msg.contentMetadata["serviceType"] == "GB":
									contact = client.getContact(sender)
									auth = "\n ➧ Penulis : {}".format(str(contact.displayName))
								else:
									auth = "\n ➧ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
								purl = "\n ➧ URL : \n   {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
								ret_ += auth
								ret_ += purl
								if "mediaOid" in msg.contentMetadata:
									object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
									if msg.contentMetadata["mediaType"] == "V":
										if msg.contentMetadata["serviceType"] == "GB":
											ourl = "\n ➧ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
											murl = "\n ➧ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
										else:
											ourl = "\n ➧ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
											murl = "\n ➧ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
										ret_ += murl
									else:
										if msg.contentMetadata["serviceType"] == "GB":
											ourl = "\n ➧ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
										else:
											ourl = "\n ➧ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
									ret_ += ourl
								if "stickerId" in msg.contentMetadata:
									stck = "\n ➧ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
									ret_ += stck
								if "text" in msg.contentMetadata:
									text = "\n ➧ Tulisan : {}".format(str(msg.contentMetadata["text"]))
									ret_ += text
								ret_ += "\n╭━━━━━━━━━━━━━━━━╮\n┃HACKERS INC.TEAM BOT \n╰━━━━━━━━━━━━━━━━╯"
								client.sendMessage(to, str(ret_))
								client.sendMessage(to, "➧ Like Success")
							except:
								client.sendMessage(to, "➧ Post tidak valid")
			except Exception as error:
				pass
		elif op.type == 55:
			try:
				if settings['cctv']['cyduk'][op.param1]==True:
					if op.param1 in settings['cctv']['point']:
						Name = client.getContact(op.param2).displayName
						dots = client.getContact(op.param2).picturePath
						if Name in settings['cctv']['sidermem'][op.param1]:
							pass
						else:
							settings['cctv']['sidermem'][op.param1] += "\n➧  °" + Name
							pref=['➧ Ngintip mele kerjaannya \n➧ ','➧ Disini kagak ada mangsa yg bisa di intip...\n➧ ','➧ Nah loh...Main ML ajja sono drpd ngintip mele..\n➧ ','➧ Di gaji berapa buat jadi pengintip bos....\n➧ ','➧ Beranimu cuma ngintip ajjah.\n➧ ','➧ Woiiiii....Pengen bisulan ya bos...\n➧ ','➧ Awas ketangkap Satpol PP lho bos....\n➧ ','➧ Biasa kalo jones itu sukanya ngintip ajjah...\n➧ ','➧ Semoga idungmu kejedot pintu bos....\n➧ ']
							client.sendMessage(op.param1, str(random.choice(pref))+Name)
							client.sendImageWithURL(op.param1, 'http://dl.profile.line.naver.jp'+dots)
				if settings['cctv3']['cyduk3'][op.param1]==True:
					if op.param1 in settings['cctv3']['point3']:
						Name = client.getContact(op.param2).displayName
						if Name in settings['cctv3']['sidermem3'][op.param1]:
							pass
						else:
							settings['cctv3']['sidermem3'][op.param1] += "\n➧ " + Name
							anuh=['➧ Orang koq sukanya ngintip ajjah to kak\n➧ '+Name+'\n➧ Awas bisulan lho ya....hikz\n➧ Ikut ngobrol di room ngapa sih...','➧ Idihhh,,,bos '+Name+'\n➧ Kenapa sukanya intip2 ajjah..??\n➧ Ayo masuk ke room,,,kita bercanda....','➧ Kenapa ngintip ajjah kak \n➧ '+Name+'\n➧ Padahal masuk ke room gratis lho...\n➧ Lebih asyik juga,,,kan banyak temennya...']
							ginfo = client.getGroup(op.param1)
							client.sendMessage(op.param2,str(random.choice(anuh))+"\n\n➧ Room : "+str(ginfo.name))
			except Exception as error:
				pass
		if op.type == 55:
			print ("[ 55 ] NOTIFIED READ MESSAGE")
			if op.param1 in settings["readPoint"]:
				if op.param2 not in settings["readMember"][op.param1]:
					settings["readMember"][op.param1].append(op.param2)
				if settings['cctv']['cyduk'][op.param1]==True:
					if op.param1 in settings['cctv']['point']:
						Name = client.getContact(op.param2).displayName
						if Name in settings['cctv']['sidermem'][op.param1]:
							pass
						else:
							settings['cctv']['sidermem'][op.param1] += "\n➧ " + Name
							siderMembers(op.param1, [op.param2])
	except Exception as error:
		pass
def NOTIFIED_INVITE_INTO_GROUP(op):
	try:
		client.acceptGroupInvitation(op.param1)
	except Exception as e:
		client.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
def run():
	while True:
		ops = oepoll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				try:
					clientBot(op)
				except Exception as error:
					pass
				oepoll.setRevision(op.revision)

if __name__ == "__main__":
	run()
