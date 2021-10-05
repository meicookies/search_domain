#!/usr/bin/python
try:
    import requests, re, validators, os, time
    from bs4 import BeautifulSoup
    from alive_progress import alive_bar
except ModuleNotFoundError:
    os.system("pip install requests validators bs4 alive-progress")

curl = requests.Session()
curl.trust_env = False
print("""

    search domain by name

""")
keyword = input("[$] Search: ")
print("[*] Please wait...")

sites = "https://crt.sh/"
source = curl.get(f"{sites}?q={keyword}").content
html = re.sub("<BR>", "\n", source.decode('UTF-8'))

pocket = set()
counter = 0
saved_result = re.sub("\s", "_", keyword)
for site in BeautifulSoup(html, "html.parser").find_all("td"):
    if validators.domain(site.text):
        with open(f"{saved_result}.txt", "a+") as fuck:
            if site.text not in pocket:
                counter += 1
                pocket.add(site.text)
                fuck.write(re.sub("$", "\n", site.text))
                fuck.close
result = [counter]
print(f"[!] Found: {result} domain")
for x in result:
    with alive_bar(x) as bar:
        for i in range(x):
            time.sleep(.01)
            bar()
print(f"[+] Tersimpan di {saved_result}.txt")
# coded by ./meicookies
