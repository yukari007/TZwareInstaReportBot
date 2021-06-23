#just the imports 
from time import time, sleep
from random import choice
from colorama import Fore, Back, Style 
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def Login(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")


def LoginProxy():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


def Banner():
    print(Fore.RED + '''
████████╗███████╗██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
╚══██╔══╝╚══███╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
   ██║     ███╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
   ██║    ███╔╝  ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
   ██║   ███████╗██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
''')


if __name__ == "__main__":
    Banner()
    PrintStatus("Loading users!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Loading Proxes!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("Victims Username:")
    userid = GetInput("Victims ID:")
    useproxy = GetInput("Do you want to use proxy? [Yes No]:")
    if (useproxy == "Yes"):
        useproxy = True
    elif (useproxy == "No"):
        useproxy = False
    else:
        PrintFatalError("Please just enter 'Yes' or 'No'!")
        exit(0)
    usemultithread = GetInput("Would you like multithread? 1[Yes] 2[No][DONT USE IF YOU HAVE A SLOW PC]")
    
    if (usemultithread == "1"):
        usemultithread = True
    elif (usemultithread == "2"):
        usemultithread = False
    else:
        PrintFatalError("Input Error 1 or 2")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Please select one of the reasons for the above complaint (ex: 1 for spam):")

    
    
    
    print("")
    PrintStatus("Reporting Account!")
    print("")

    if (usemultithread == False):
        LoginProxy()
    else:
        for user in USERS:
            procT = Process(target=Login,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            procT.start() 