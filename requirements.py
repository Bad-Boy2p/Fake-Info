import os
from time import sleep
import random



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

version="1.1"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

os.system("clear")

print(blue + """ /$$$$$$$                                    /$$                           /$$      
| $$__  $$                                  | $$                          | $$      
| $$  \ $$  /$$$$$$  /$$  /$$  /$$ /$$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$      
| $$  | $$ /$$__  $$| $$ | $$ | $$| $$__  $$| $$ /$$__  $$ |____  $$ /$$__  $$      
| $$  | $$| $$  \ $$| $$ | $$ | $$| $$  \ $$| $$| $$  \ $$  /$$$$$$$| $$  | $$      
| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$      
| $$$$$$$/|  $$$$$$/|  $$$$$/$$$$/| $$  | $$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$      
|_______/  \______/  \_____/\___/ |__/  |__/|__/ \______/  \_______/ \_______/      
                                                                                    
                                                                                    
                                                                                    """)

def s() :
	print("")
print(info2 + "requirements")

s()
print(info+ "update and upgrade termux ")
print(info + "install  module")
print(info + "building tool fille ")
sleep(1)

s()
s()
print(info2 + "update termux .........")
s()
s()
os.system("apt update -y")
os.system("apt upgrade -y")
s()
s()
print(info2 + "install module")
os.system("pip install faker")
os.system("pip install platform")
os.system("pip install subprocess")
os.system("pip install socket")
os.system("pip install requests")
s()
s()
print(info2 + "building tool fille")
s()
s()
sleep(2)
try :
	print(green + "plase wait ..................................")
	sleep(2)
	os.system("mkdir /sdcard/fake_info")
	os.system("mkdir /sdcard/fake_info/address")
	os.system("mkdir /sdcard/fake_info/email_password")
	os.system("mkdir /sdcard/fake_info/login_information")
	os.system("mkdir /sdcard/fake_info/name")
	os.system("mkdir /sdcard/fake_info/private_ip")
	os.system("mkdir /sdcard/fake_info/public_ip")
except :
	print(error + "here some problem ")
sleep(1)
os.system("clear")
print(blue + """ /$$$$$$$                                    /$$                           /$$      
| $$__  $$                                  | $$                          | $$      
| $$  \ $$  /$$$$$$  /$$  /$$  /$$ /$$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$      
| $$  | $$ /$$__  $$| $$ | $$ | $$| $$__  $$| $$ /$$__  $$ |____  $$ /$$__  $$      
| $$  | $$| $$  \ $$| $$ | $$ | $$| $$  \ $$| $$| $$  \ $$  /$$$$$$$| $$  | $$      
| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$      
| $$$$$$$/|  $$$$$$/|  $$$$$/$$$$/| $$  | $$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$      
|_______/  \______/  \_____/\___/ |__/  |__/|__/ \______/  \_______/ \_______/      
                                                                                    
                                                                                    
                                                                                    """)
                                                                                    

print(success + "requirements successfly !!!")
s()
print(success+ "update and upgrade termux successfly !!!")
print(success + "install  module successfly !!!")
print(success + "building tool fille successfly !!!")
s()
os.system("clear")

random_num = random.randint(5, 10)
def countdown(t): 
    """
    Countdown Timer
    """
    while t:
        # Divmod takes only two arguments so
        # you'll need to do this for each time
        # unit you need to add
        mins, secs = divmod(t, 60) 
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        days, month = divmod(days, 30)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format( days, hours, mins, secs) 
        print( red  + "              "  +  timer, end="\r") 
        sleep(1) 
        t -= 1

   # os.system("rm requirements.py")

t = random_num


print(info + "file well remove after "  )
countdown(int(t))
print(info2 + "to run the tool write ( python3 fake-info.py )")
