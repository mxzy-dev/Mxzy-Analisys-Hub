import os
import requests as r


def enter():
    input("-Нажмите Enter чтобы продолжить--}")

BLUE = "\033[1;34m"
banner = f"""{BLUE}
╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║            M X Z Y   A N A L I S Y S   H U B                        ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    print(banner)
    url = input("Enter url: https://api.example.com --")
    analisys(url)

def analisys(url):
    response = r.get(url, timeout=15)
    if 200 <= response.status_code < 300:
        clear()
        code = response.status_code
        final_url = response.url
        server = response.headers.get("Server")
        content_type = response.headers.get("Content-Type")
        size = len(response.content)
        cookies = response.cookies
        cookies_count = len(response.cookies)
        redirects = len(response.history)
        print(f"""
┌─────────────────────────┐
│ Analysis                   
│                         
│ Status: {code}             
│ Final URL: {final_url}  
│ Server: {server}           
│ Content-Type: {content_type} 
│ Size: {size}      
│ Cookies: {cookies_count}
│ Cookies content: {cookies}              
│ Redirects: {redirects}            
└─────────────────────────┘
""")
        print("\n")
        enter()
        clear()
        start()
    elif 400 <= response.status_code < 500:
        print("Client Error")
        enter()
        clear()
        start()
    elif 500<= response.status_code < 600:
        print("Server Error")
        enter()
        clear()
        start()

start()