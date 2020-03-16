#!/usr/bin/python3
# coding: utf-8

# Contributors:
#---------------
# @Cracked.keys
# @
# @
# @ 

# Colors.
Red = '\033[31m'
Cyan = '\033[36m'
Pink = '\033[95m'
Grey = '\033[90m'
Green = '\033[32m'
White = '\033[37m'
Purple = '\033[35m'
Yellow = '\033[93m'
End = '\033[0m'

# Modules.
try:
    import os
    import sys
    import time
    import random
    import subprocess
    from datetime import date
except ImportError:
    print(Red+ "Failed to import modules")

# Functions.
today = date.today()

def Exe():
    try:
        Banner()
        Main()
    except KeyboardInterrupt:
        subprocess.call('clear', shell=True)
        print(Green + "\n\nExiting....\n")

def Checkroot():
    if os.getuid() != 0:
        print(32 * " " + Red + "You are not root" + White + "!")
    else:
        print(34 * " " + Green + "You are root" + White + " :)")

def Banner():
    subprocess.call('clear', shell=True)
    print("                                                                     ")
    print("                                                                     ")
    print(White + 11 * " " + "██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗  ██╗██╗████████╗") 
    print(White + 11 * " " + "██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║ ██╔╝██║╚══██╔══╝")
    print(White + 11 * " " + "██████╔╝██║     ███████║██║     █████╔╝ █████╔╝ ██║   ██║   ")
    print(White + 11 * " " + "██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔═██╗ ██║   ██║   ") 
    print(White + 11 * " " + "██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██╗██║   ██║   ") 
    print(White + 11 * " " + "╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ")   
    Checkroot()
    print(Grey + 22 * " " + "╔═══════════════════════════════════╗")
    print(Grey + 22 * " " + "║                                   ║")
    print(Grey + 22 * " " + "║                                   ║")
    print(Grey + 22 * " " + "╚═══════════════════════════════════╝      ")
    print(68 * " " + Green + "? " + White + "for help" + Grey + ".")
    print(White + 80 * "═")
    print(White + 80 * "═")

def Main():
    inp = input(Green + " [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
    if inp == "?":
        Help()
    elif inp == "q":
        sys.exit()
        subprocess.call('clear', shell=True)
    elif inp == "r":
        os.system("clear && ./BlackKit.py")
    elif inp == "ping":
        Ping()
    elif inp == "wifi":
        Wifi()
    elif inp == "recon":
        Recon()
    elif inp == "tools":
        Tools()
    elif inp == "other":
        Other()
    elif inp == "whoami":
        Whoami() 
    elif inp == "evasion":
        Evasion()
    elif inp == "payload":
        Payload()
    elif inp == "database":
        Database()
    elif inp == "firewall":
        Firewall()
    elif inp == "sniffing":
        Sniffing()
    elif inp == "localchat":
        Localchat()
    elif inp == "bruteforce":
        Bruteforce()
    elif inp == "hashcracker":
        Hashcracker()
    else:
        Exe()
    
def Help():
        subprocess.call('clear', shell=True)
        print(White + """ 
            > Here are a list of commands to use for this script <

     command                     info 
--------------------------------------------------------------------------------  
        q               - Will quit the script.
        r               - Will restart the script.
        ping            - Ping a host to see if it's online.
        wifi            - Assorted wifi tools for recon and attcking.
        recon           - Different type of nmap scans for recon.
        tools           - Different tools that will work with this script.
        other           - Various options for different uses.
        whoami          - Gives you system info.              
        evasion         - Technique's and spoofing.
        payload         - Automated payloads for attacking.
    ^   database        - Configure options for database directory.
    |   sniffing        - Wireshark or tcpdump for sniffing. 
    |   localchat       - Chat to another system via ncat.
    |   bruteforce      - Bruteforcing options.
    |   hashcracker     - Uses John to crack hashes.
    """)
        print("Would you like to " + Red + "restart" + White + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
        else:
            Help()

def Ping():
    subprocess.call('clear', shell=True)
    target = input(Grey + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
    print("                  ")
    os.system("ping " + target)
    print("                  ")
    print(80 * "═")
    print("Would you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
    YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
    if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
        Exe()
    elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
        sys.exit()
        subprocess.call('clear', shell=True)
    else:
        Ping()

def Wifi():
    # Work in progress.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " ")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " ")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Wifi()

def Recon():
    # Needs work.
    subprocess.call('clear', shell=True)
    print(80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " OS Scan          ")        
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Port Scan        ")        
    print(Grey + "[" + White + "3" + Grey + "]" + White + " Active Scan      ")
    print(Grey + "[" + White + "4" + Grey + "]" + White + " Network Scan     ")
    print(Grey + "[" + White + "5" + Grey + "]" + White + " Service Scan     ")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu        ")
    filename = str(today) + "results.txt"
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        target = input(Grey + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("sudo nmap -O " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "2":
        target = input(Grey + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -p- " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "3":
        target = input(Grey + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -A " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "4":
        target = input(Grey + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -sS -Pn -n --disable-arp-ping " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "5":
        target = input(Grey + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -sV --script=banner " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    else:
        Recon()

def Tools():
    # Finish.
    subprocess.call('clear', shell=True)
    print("Here's a list of tools to install...\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " Anonsurf")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Anonsurf")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " Anonsurf")
    print(Grey + "[" + White + "4" + Grey + "]" + White + " Anonsurf")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Tools()

def Other():
    # Work in prgress.
    subprocess.call('clear', shell=True)
    print(" ")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " Whois")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Wafw00f")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " IP lookup")
    print(Grey + "[" + White + "4" + Grey + "]" + White + " DNS lookup")
    print(Grey + "[" + White + "5" + Grey + "]" + White + " What's my IP?")
    print(Grey + "[" + White + "6" + Grey + "]" + White + " Identify hash")
    print(Grey + "[" + White + "7" + Grey + "]" + White + " Reverse IP lookup")
    print(Grey + "[" + White + "8" + Grey + "]" + White + " Active interface's")
    print(Grey + "[" + White + "9" + Grey + "]" + White + " Reverse DNS lookup")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        target = input(Grey + "\nEnter domain\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("whois " + target)
    elif inp == "2":
        target = input(Grey + "\nEnter domain\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("wafw00f " + target)
    elif inp == "4":
        target = input(Grey + "\nEnter domain\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nslookup " + target)
        print( Grey + 80 * "-" + End)
        os.system("dig " + target)
    elif inp == "5":
        print(80 * "═")
        print("\nPublic IP\n" + 25 * "-")
        os.system("dig +short myip.opendns.com @resolver1.opendns.com")
        print("\nIPv4 Address\n" + 25 * "-")
        os.system("ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'")
        print("\nIPv6 Address\n" + 25 * "-")
        os.system("ip addr | grep 'state UP' -A4 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'")
        print("\n" + 80 * "═")
        print("Would you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
    elif inp == "6":
        dahash = input("\nEnter Hash" + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("hashid " + dahash)
    elif inp == "7":
        os.system(" ")
    elif inp == "8":
        print(Green + " ")
        os.system("ifconfig")
        print("\n" + End + 80 * "=")
        print("Would you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
    elif inp == "9":
        os.system("dig -x " + target)
    else:
        Other()

def Whoami():
    print(White + 80 * "═")
    Checkroot()
    print(White + 80 * "═")
    print("\nCurrent user.\n" + Green + 25 * "-" + End)
    os.system("whoami")
    print("\nCurrent logged on users.\n" + Green + 25 * "-" + End)
    os.system("w")
    print("\nLast logged on users.\n" + Green + 25 * "-" + End)
    os.system("last -a")
    print(White + 80 * "═")
    print("Kernal info.\n" + Green + 25 * "-" + End)
    os.system("uname -a")
    os.system("cat /proc/version")
    print(White + 80 * "═")
    print("Operating system info.\n" + Green + 25 * "-" + End)
    os.system("cat /etc/issue")
    os.system("cat /etc/*release*")
    print(White + 80 * "═")
    if os.getuid() != 0:
        os.system(Green + " You are not root!" + End)
        print(White + 80 * "═")
    else:
        os.system("cat /etc/shadow")
        print(White + 80 * "═")
    print("Would you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
    YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
    if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
        Exe()
    elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
        sys.exit()
        subprocess.call('clear', shell=True)

def Evasion():
    # Start.)
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " ")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " ")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Evasion()

def Payload():
    # Finish.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " TCP Payload for MacOS")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " TCP Payload for Linux")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " TCP Payload for Android")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " TCP Payload for Windows")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " HTTP Payload for Windows")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " ")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " ")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " ")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        os.system("")
    else:
        Payload()


def Database():
    # Work in progress.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " Show Database.")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Gen Atomic Dir.")
    print(Grey + "[" + White + "?" + Grey + "]" + White + " Show help.")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu.")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        print("\n" + 80 * "═")
        os.system("ls Database/")        
        print("\nWould you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
    elif inp == "2":
        print(" ")
    elif inp == "?":
        print("""\n
            > Here are a list of commands to use for this script <

     command                     info 
--------------------------------------------------------------------------------
        q               - Will quit the script
        r               - Will restart Database option.
        l               - 
        c               - 
        """)
    else:
        Database()

def Firewall():
    # Work in progress.
    print("")

def Sniffing():
    # Work in progress.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " TCPdump")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Wireshark")
    print(Grey + "[" + White + "x" + Grey + "]" + White + " Main menu")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        os.system("")
    elif inp == "tcpdump":
        os.system("sudo wireshark > /dev/null 2>&1")
    else:
        Sniffing()

def Localchat():
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " Open Netcat Window for chatting.")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Connect to host to chat using Netcat.")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "1":
        port = input(End + "\nEnter " + Green + "port" + White + " to connect to" + Grey + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nc -lp " + port)
        print("\nWould you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
    elif inp == "2":
        ipadd = input(End + "\nEnter " + Green + "IP address" + White + " to connect to" + Grey + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        port = input(End + "\nEnter " + Green + "port" + White + " to connect to" + Grey + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nc " + ipadd + " -p " + port)
        print("\nWould you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
    else:
        Localchat()

def Bruteforce():
    # Finish Medusa option.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Grey + "[" + White + "1" + Grey + "]" + White + " Hydra")
    print(Grey + "[" + White + "2" + Grey + "]" + White + " Medusa")
    print(Grey + "[" + White + "3" + Grey + "]" + White + " Main menu")
    inp = str(input(Grey + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "1":
        print(Green + "\nSpawning the Hydra... >" + White + ":)")
        time.sleep(2)
        print(Green + "\nHydra spawned........\n" + Grey + "\n       (" + White + "Ctrl+c to quit" + Green + "!!" + Grey + ")" + End)
        os.system("xhydra > /dev/null 2>&1")
        print("\nWould you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
    elif inp == "2":
        print("")
    else:
        Bruteforce()

def Hashcracker():
    # Fix/work on.
    print("Enter hash in nano file then 'Ctrl-x' to quit ")
    time.sleep(1.5)
    filename = str(input(Grey + "\nName file." + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    os.system("nano " + filename)
    os.system("john " + filename)
    os.system("mv " + filename + " Database/Other/Hashes/")

Exe()