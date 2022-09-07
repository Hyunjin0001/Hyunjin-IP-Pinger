import os

try:
    import os
    from os import system
    system("title " + "Ip Pinger,   Made By ✦ Hyunjin ✧#0001 ,   Github: github.com/Hyunjin0001")
except:
    pass

print("""                  
(MADE BY HYUNJIN)
______ _                       
| ___ (_)                      
| |_/ /_ _ __   __ _  ___ _ __ 
|  __/| | '_ \ / _` |/ _ \ '__|
| |   | | | | | (_| |  __/ |   
\_|   |_|_| |_|\__, |\___|_|   
                __/ |          
               |___/           """)
ip = input("Enter Ip : ")
while True:
    os.system("ping -n 4 " + ip)
