#!/usr/bin/python3
# coding: utf-8



# Contributors:
# ---------------
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
    print(Red + "Failed to import modules")



# Functions.
today = date.today()



def Checkroot():
    if os.getuid() != 0:
        print(32 * " " + Red + "You are not root" + White + "!")
    else:
        print(34 * " " + Green + "You are root" + White + " :)")



def Exe():
    if os.getuid() != 0:
        subprocess.call('clear', shell=True)
        print(Red + "\nPlease run BlackKit with sudo privledges.\n")
        time.sleep(3)
        subprocess.call('clear', shell=True)
    else:
        Banner()
        Main()



def Banner():
    subprocess.call('clear', shell=True)
    print(" ")
    print(Green + 11 * " " + "██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗  ██╗██╗████████╗") 
    print(Green + 11 * " " + "██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║ ██╔╝██║╚══██╔══╝")
    print(Green + 11 * " " + "██████╔╝██║     ███████║██║     █████╔╝ █████╔╝ ██║   ██║   ")
    print(Green + 11 * " " + "██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔═██╗ ██║   ██║   ") 
    print(Green + 11 * " " + "██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██╗██║   ██║   ") 
    print(Green + 11 * " " + "╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ")   
    print(" ")
    print(White + 22 * " " + "╔═══════════════════════════════════╗")
    print(White + 22 * " " + "║                                   ║")
    print(White + 22 * " " + "║                                   ║")
    print(White + 22 * " " + "╚═══════════════════════════════════╝      ")
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
    elif inp == "sniffing":
        Sniffing()
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
════════════════════════════════════════════════════════════════════════════════
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
        sniffing        - Wireshark or tcpdump for sniffing. 
        bruteforce      - Bruteforcing options.
        hashcracker     - Uses John to crack hashes.""")
        print(White + 80 * "═")

        Main()



def Ping():
    subprocess.call('clear', shell=True)
    target = input(Green + "\nEnter IP\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
    print("                  ")
    os.system("ping " + target)
    print("                  ")
    print(White + 80 * "═")
    Main()



def Wifi():
    # Work in progress.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(White + "[" + Green + "1" + White + "]" + Green + " ")
    print(White + "[" + Green + "x" + White + "]" + Green + " Main menu")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Wifi()



def Recon():
    # Needs work.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(White + "[" + Green + "1" + White + "]" + Green + " OS Scan          ")        
    print(White + "[" + Green + "2" + White + "]" + Green + " Port Scan        ")        
    print(White + "[" + Green + "3" + White + "]" + Green + " Active Scan      ")
    print(White + "[" + Green + "4" + White + "]" + Green + " Network Scan     ")
    print(White + "[" + Green + "5" + White + "]" + Green + " Service Scan     ")
    print(White + "[" + Green + "x" + White + "]" + Green + " Main menu        ")
    
    filename = str(today) + "results.txt"
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("nmap -O " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "2":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("nmap -p- " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "3":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("nmap -A " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "4":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("nmap -sS -Pn -n --disable-arp-ping " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    elif inp == "5":
        target = input(Green + "\nEnter IP\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("nmap -sV --script=banner " + target + " -oG " + filename)
        os.system("mv " + filename + " Database/Recon_scans/")
    else:
        Recon()



def Tools():
    # Finish.
    subprocess.call('clear', shell=True)
    print("Here's a list of tools to install...\n")
    print(White + "[" + Green + "1" + White + "]" + Green + " Anonsurf")
    print(White + "[" + Green + "2" + White + "]" + Green + "         ")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Tools()



def Other():
    # Work in progress.
    subprocess.call('clear', shell=True)
    print(" ")
    print(White + "[" + Green + "1" + White + "]" + Green + " Whois")
    print(White + "[" + Green + "2" + White + "]" + Green + " Wafw00f")
    print(White + "[" + Green + "3" + White + "]" + Green + " IP lookup")
    print(White + "[" + Green + "4" + White + "]" + Green + " DNS lookup")
    print(White + "[" + Green + "5" + White + "]" + Green + " What's my IP?")
    print(White + "[" + Green + "6" + White + "]" + Green + " Identify hash")
    print(White + "[" + Green + "7" + White + "]" + Green + " Reverse IP lookup")
    print(White + "[" + Green + "8" + White + "]" + Green + " Active interface's")
    print(White + "[" + Green + "9" + White + "]" + Green + " Reverse DNS lookup")
    print(White + "[" + Green + "x" + White + "]" + Green + " Main menu")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        target = input(Green + "\nEnter domain\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("whois " + target)
    elif inp == "2":
        target = input(Green + "\nEnter domain\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("wafw00f " + target)
    elif inp == "4":
        target = input(Green + "\nEnter domain\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("nslookup " + target)
        print( Green + 80 * "-" + End)
        os.system("dig " + target)
    elif inp == "5":
        print(White + 80 * "═")
        print(Green + "\nPublic IP\n" + White + 25 * "-" + End)
        os.system("sudo curl icanhazip.com")
        print(Green + "\nIPv4 Address\n" + White + 25 * "-" + End)
        os.system("ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'")
        print(Green + "\nIPv6 Address\n" + White + 25 * "-" + End)
        os.system("ip addr | grep 'state UP' -A4 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'")
        print(White + "\n" + 80 * "═")
        Main()
    elif inp == "6":
        Thehash = input("\nEnter Hash" + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
        os.system("hashid " + Thehash)
    elif inp == "7":
        os.system(" ")
    elif inp == "8":
        print(Green + " ")
        os.system("ifconfig")
        print("\n" + White + 80 * "=")
        Main()
    elif inp == "9":
        os.system("dig -x " + target)
    else:
        Other()



def Whoami():
    print(White + 80 * "═")
    Checkroot()
    print(White + 80 * "═")
    print(Green + "\nCurrent user.\n" + White + 25 * "-" + End)
    os.system("whoami")
    print(Green + "\nCurrent logged on users.\n" + White + 25 * "-" + End)
    os.system("w")
    print(Green + "\nLast logged on users.\n" + White + 25 * "-" + End)
    os.system("last -a")
    print(White + 80 * "═")
    print(Green + "Kernal info.\n" + White + 25 * "-" + End)
    os.system("uname -a")
    os.system("cat /proc/version")
    print(White + 80 * "═")
    print(Green + "Operating system info.\n" + White + 25 * "-" + End)
    os.system("cat /etc/issue")
    os.system("cat /etc/*release*")
    print(White + 80 * "═")
    Main()
        


def Evasion():
    # Work in progress
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(White + "[" + Green + "1" + White + "]" + Green + " ")
    print(White + "[" + Green + "2" + White + "]" + Green + " ")
    print(White + "[" + Green + "x" + White + "]" + Green + " Main menu")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    else:
        Evasion()



def Payload():
    # Work on.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(White + "[" + Green + "3" + White + "]" + Green + " TCP Payload for MacOS")
    print(White + "[" + Green + "3" + White + "]" + Green + " TCP Payload for Linux")
    print(White + "[" + Green + "3" + White + "]" + Green + " TCP Payload for Android")
    print(White + "[" + Green + "1" + White + "]" + Green + " TCP Payload for Windows")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
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
    print(White + "[" + Green + "1" + White + "]" + Green + " Create Database.")
    print(White + "[" + Green + "2" + White + "]" + Green + " Show databases")
    print(White + "[" + Green + "x" + White + "]" + Green + " Main menu.")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        print(" ")    
    elif inp == "2":
        print(" ")
    else:
        Database()




def Sniffing():
    # TCPdump needs to be finsihed
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(White + "[" + Green + "1" + White + "]" + Green + " TCPdump")
    print(White + "[" + Green + "2" + White + "]" + Green + " Wireshark")
    print(White + "[" + Green + "x" + White + "]" + Green + " Main menu")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "x":
        Exe()
    elif inp == "1":
        os.system("")
    elif inp == "":
        os.system("sudo wireshark > /dev/null 2>&1")
    else:
        Sniffing()



def Bruteforce():
    # Finish Medusa option.
    subprocess.call('clear', shell=True)
    print(White + 80 * "═" + "\n")
    print(White + "[" + Green + "1" + White + "]" + Green + " Hydra")
    print(White + "[" + Green + "2" + White + "]" + Green + " Medusa")
    print(White + "[" + Green + "3" + White + "]" + Green + " Main menu")
    
    inp = str(input(Green + "\nChoose a option" + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    if inp == "1":
        print(Green + "\nSpawning the Hydra... >" + White + ":)")
        time.sleep(2)
        print(Green + "\nHydra spawned........\n" + Green + "\n       (" + White + "Ctrl+c to quit" + Green + "!!" + Green + ")" + End)
        os.system("xhydra > /dev/null 2>&1")
        print("\nWould you like to " + Red + "restart" + End + " the script?\n" + 80 * "═")
        
        YesNo = input(Green + "Y" + End + " / " + Red + "N\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End)
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
    # Work in progress
    filename = str(input(Green + "\nFirst enter a name for the file you'll be using." + Green + ".\n" + White + 80 * "═" + White + "\n[" + Green + "BlackKit" + White + "]" + Green + "\n  ╚═> " + End))
    # Will add a function to check if filename is in use
    time.sleep(1.5)
    print("Enter the hash in nano file then do 'Ctrl-x' and 'Y' to quit and save.")
    time.sleep(1.5)
    os.system("nano " + filename)
    print(Green + "Good!")
    time.sleep(1)
    os.system("john " + filename)
    os.system("mv " + filename + " Database/Hashes/")



# Error Handling
try:
    if '__name__' == '__name__':
        Exe()

except KeyboardInterrupt:
    subprocess.call('clear', shell=True)
    print(White + 80 * "═")
    print(Red + "\nControl + C Detected\n")
    print(Red + "Exiting\n" + End)
    print(White + 80 * "═")
    time.sleep(1)
    subprocess.call('clear', shell=True)