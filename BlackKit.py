#!/usr/bin/python3
# coding: utf-8



# Contributors:
#---------------
# @Cracked.keys
# @inc0gnit0
# @
# @ 



# Colors.
Red = '\033[91m'
Cyan = '\033[96m'
Pink = '\033[95m'
Green = '\033[92m'
White = '\033[97m'
Purple = '\033[95m'
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
    Banner()
    Main()
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
    print(Green + 11 * " " + "██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗  ██╗██╗████████╗") 
    print(Green + 11 * " " + "██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║ ██╔╝██║╚══██╔══╝")
    print(Green + 11 * " " + "██████╔╝██║     ███████║██║     █████╔╝ █████╔╝ ██║   ██║   ")
    print(Green + 11 * " " + "██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔═██╗ ██║   ██║   ") 
    print(Green + 11 * " " + "██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██╗██║   ██║   ") 
    print(Green + 11 * " " + "╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ")   
    Checkroot()
    print(Green + 22 * " " + "╔═══════════════════════════════════╗")
    print(Green + 22 * " " + "║                                   ║")
    print(Green + 22 * " " + "║                                   ║")
    print(Green + 22 * " " + "╚═══════════════════════════════════╝      ")
    print(68 * " " + Green + "? " + White + "for help" + Green + ".")
    print(White + 80 * "═")
    print(White + 80 * "═")



def Main():
    inp = input(White + "[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
    if inp == "?":
        Help()
    elif inp == "x":
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

\033[92m     Command                     Description\033[97m
═════════════════════════════════════════════════════════════════════════════════  
\033[92m        x               - Will quit the script.
        r               - Will restart the script.
        ping            - Ping a host to see if it's online.
        wifi            - Assorted wifi tools for recon and attcking.
        recon           - Different type of nmap scans for recon.
        tools           - Different tools that will work with this script.
        other           - Various options for different uses.
        whoami          - Gives you system info.              
        evasion         - Technique's and spoofing.
        payload         - Automated payloads for attacking.
        database        - Configure options for database directory.
        sniffing        - Wireshark or tcpdump for sniffing. 
        localchat       - Chat to another system via ncat.
        bruteforce      - Bruteforcing options.
        hashcracker     - Uses John to crack hashes.""")
        print(White + 80 * "═" + "\n")
        Main()



def Ping():
    subprocess.call('clear', shell=True)
    target = input(Green + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
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
    print(Green + "[" + White + "1" + Green + "]" + White + " ")
    print(Green + "[" + White + "2" + Green + "]" + White + " ")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Wifi()



def Recon():
    # Needs work.
    subprocess.call('clear', shell=True)
    print(80 * "═" + "\n")
    print(Green + "[" + White + "1" + Green + "]" + White + " OS Scan          ")        
    print(Green + "[" + White + "2" + Green + "]" + White + " Port Scan        ")        
    print(Green + "[" + White + "3" + Green + "]" + White + " Active Scan      ")
    print(Green + "[" + White + "4" + Green + "]" + White + " Network Scan     ")
    print(Green + "[" + White + "5" + Green + "]" + White + " Service Scan     ")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu        ")
    filename = str(today) + "results.txt"
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("sudo nmap -O " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "2":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -p- " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "3":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -A " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "4":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -sS -Pn -n --disable-arp-ping " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "5":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nmap -sV --script=banner " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    else:
        Recon()



def Tools():
    # Finish.
    subprocess.call('clear', shell=True)
    print("Here's a list of tools to install...\n")
    print(Green + "[" + White + "1" + Green + "]" + White + " Anonsurf")
    print(Green + "[" + White + "2" + Green + "]" + White + " Anonsurf")
    print(Green + "[" + White + "3" + Green + "]" + White + " Anonsurf")
    print(Green + "[" + White + "4" + Green + "]" + White + " Anonsurf")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Tools()



def Other():
    # Work in prgress.
    subprocess.call('clear', shell=True)
    print(" ")
    print(Green + "[" + White + "1" + Green + "]" + White + " Whois")
    print(Green + "[" + White + "2" + Green + "]" + White + " Wafw00f")
    print(Green + "[" + White + "3" + Green + "]" + White + " IP lookup")
    print(Green + "[" + White + "4" + Green + "]" + White + " DNS lookup")
    print(Green + "[" + White + "5" + Green + "]" + White + " What's my IP?")
    print(Green + "[" + White + "6" + Green + "]" + White + " Identify hash")
    print(Green + "[" + White + "7" + Green + "]" + White + " Reverse IP lookup")
    print(Green + "[" + White + "8" + Green + "]" + White + " Active interface's")
    print(Green + "[" + White + "9" + Green + "]" + White + " Reverse DNS lookup")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    
    if inp == "x":
        Exe()
        
    elif inp == "1":
        target = input(Green + "\nEnter domain\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("whois " + target)
        
    elif inp == "2":
        target = input(Green + "\nEnter domain\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("wafw00f " + target)
        
    elif inp == "4":
        target = input(Green + "\nEnter domain\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nslookup " + target)
        print( Green + 80 * "-" + End)
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
    print(Green + "[" + White + "1" + Green + "]" + White + " ")
    print(Green + "[" + White + "2" + Green + "]" + White + " ")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    
    if inp == "x":
        Exe()
        
    else:
        Evasion()



def Payload():
    # Finish.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(Green + "[" + White + "3" + Green + "]" + White + " TCP Payload for MacOS")
    print(Green + "[" + White + "3" + Green + "]" + White + " TCP Payload for Linux")
    print(Green + "[" + White + "3" + Green + "]" + White + " TCP Payload for Android")
    print(Green + "[" + White + "1" + Green + "]" + White + " TCP Payload for Windows")
    print(Green + "[" + White + "2" + Green + "]" + White + " HTTP Payload for Windows")
    print(Green + "[" + White + "3" + Green + "]" + White + " ")
    print(Green + "[" + White + "3" + Green + "]" + White + " ")
    print(Green + "[" + White + "3" + Green + "]" + White + " ")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    
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
    print(Green + "[" + White + "1" + Green + "]" + White + " Show Database.")
    print(Green + "[" + White + "2" + Green + "]" + White + " Gen Atomic Dir.")
    print(Green + "[" + White + "?" + Green + "]" + White + " Show help.")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu.")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    
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
    print(Green + "[" + White + "1" + Green + "]" + White + " TCPdump")
    print(Green + "[" + White + "2" + Green + "]" + White + " Wireshark")
    print(Green + "[" + White + "x" + Green + "]" + White + " Main menu")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
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
    print(Green + "[" + White + "1" + Green + "]" + White + " Open Netcat Window for chatting.")
    print(Green + "[" + White + "2" + Green + "]" + White + " Connect to host to chat using Netcat.")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    if inp == "1":
        port = input(End + "\nEnter " + Green + "port" + White + " to connect to" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        os.system("nc -lp " + port)
        print("\nWould you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        
        if YesNo == "Y" or YesNo == "y" or YesNo == "Yes" or YesNo == "yes":
            Exe()
            
        elif YesNo == "N" or YesNo == "n" or YesNo == "No" or YesNo == "no":
            sys.exit()
            subprocess.call('clear', shell=True)
            
    elif inp == "2":
        ipadd = input(End + "\nEnter " + Green + "IP address" + White + " to connect to" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
        port = input(End + "\nEnter " + Green + "port" + White + " to connect to" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End)
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
    print(Green + "[" + White + "1" + Green + "]" + White + " Hydra")
    print(Green + "[" + White + "2" + Green + "]" + White + " Medusa")
    print(Green + "[" + White + "3" + Green + "]" + White + " Main menu")
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    
    if inp == "1":
        print(Green + "\nSpawning the Hydra... >" + White + ":)")
        time.sleep(2)
        print(Green + "\nHydra spawned........\n" + Green + "\n       (" + White + "Ctrl+c to quit" + Green + "!!" + Green + ")" + End)
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
    filename = str(input(Green + "\nName file." + Green + ".\n" + White + 80 * "═" + Green + "\n [" + White + "*" + Green + "]" + "\n  ╚═> " + End))
    os.system("nano " + filename)
    os.system("john " + filename)
    os.system("mv " + filename + " Database/Other/Hashes/")



# Error Handling
try:
    if '__name__' == '__name__':
        Exe()

except KeyboardInterrupt:
    print(Red + "\n\nControl + C Detected!")
    print("Exiting" + End)