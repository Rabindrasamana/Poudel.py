#THIS 
#CODE
#IS
#WRITEEN
#BY
#BISHESH
import random
import requests
import os
from colorama import Fore, Style, init
os.system("clear")
logo=(f"""
\033[1;37m
 _________                     _          
|  _   _  |                   (_)         
|_/ | | \_|.---.  _ .--.      __   .--.   
    | |   / /__\\[ `.-. |    [  |/ .'`\ \ 
   _| |_  | \__., | | | |  _  | || \__. | 
  |_____|  '.__.'[___||__][ \_| | '.__.'  
                           \____/                                   
                           
               \033[1;37mOWNER •->  \033[1;92mZAMAN
               \033[1;37mVERSION •->  \033[1;92m0.1
               \033[1;37mTOOL •->  \033[1;92mAUTO UA MAKE
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def S1():
    one = str(random.randint(101,303))
    two = str(random.randint(101,303))
    U_V1 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097196;FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_GB;FBCR/IND airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 4i;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V2 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454129;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/airtel;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/A0001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V3 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_GB;FBCR/Reliance;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1033;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V4 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20748104;FBDM/{{density=1.5,width=540,height=960}};FBLC/en_US;FBCR/XL Axiata;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A33w;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V5 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454026;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V6 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097172;FBDM/{{density=1.5,width=540,height=960}};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V7 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748054;FBDM/{{density=2.0,width=720,height=1280}};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    U_V8 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748051;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
    U_V9 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    U_V10 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20453986;FBDM/{{density=1.5,width=480,height=854}};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y511-U251;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
    ua = random.choice([U_V1, U_V2, U_V3, U_V4, U_V5, U_V6, U_V7, U_V8, U_V9, U_V10])
    return ua
def check_ua_active(ua):
    urls = ["https://google.com", "https://facebook.com", "https://amazon.com", 
            "https://twitter.com", "https://instagram.com", "https://youtube.com",
            "https://reddit.com", "https://netflix.com", "https://linkedin.com", "https://bing.com"]
    headers = {'User-Agent': ua}

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=3)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            continue
    return False
def main():
    print(logo)
    limit = int(input("Enter the number of User-Agents to generate : "))
    
    for _ in range(limit):
        ua = S1()
        is_active = check_ua_active(ua)

        if is_active:
            print(Fore.GREEN + "Active UA: " + ua)
            print(f"\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        else:
            print(Fore.RED + "Dead UA: " + ua)

if __name__ == "__main__":
    main()

S1()
