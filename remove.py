import os
from time import sleep
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

banner = red + """                                                               
@@@@@@@   @@@@@@@@  @@@@@@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  
@@!  @@@  @@!       @@! @@! @@!  @@!  @@@  @@!  @@@  @@!       
!@!  @!@  !@!       !@! !@! !@!  !@!  @!@  !@!  @!@  !@!       
@!@!!@!   @!!!:!    @!! !!@ @!@  @!@  !@!  @!@  !@!  @!!!:!    
!!@!@!    !!!!!:    !@!   ! !@!  !@!  !!!  !@!  !!!  !!!!!:    
!!: :!!   !!:       !!:     !!:  !!:  !!!  :!:  !!:  !!:       
:!:  !:!  :!:       :!:     :!:  :!:  !:!   ::!!:!   :!:       
::   :::   :: ::::  :::     ::   ::::: ::    ::::     :: ::::  
 :   : :  : :: ::    :      :     : :  :      :      : :: ::   
                                                               """
                                                               
                                                               
                                                               
 
os.system("clear")
print(banner)
print(info + "start removing  ...............")
sleep(2)
print(info + "remove files ")
os.system("rm fake-info.py")
os.system("rm remove.py")

os.system("cd ..")
os.system("rm -rf Fake _Info")
sleep(1)
print(info + "remove data files")
os.system("rm -rf /sdcard/fake_info")
print(success + "removing succsefly ")

print(green + "good bye :-)")

