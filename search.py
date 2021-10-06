#!/usr/bin/python
try:
    import os, time, re
    from crtsh import crtshAPI
    from alive_progress import alive_bar
except ModuleNotFoundError:
    os.system("pip install alive-progress crtsh")

def cari(keyword):
    html = crtshAPI().search(f"{keyword}")
    total = []
    for site in html:
        if site["common_name"] not in total:
            total.append(site["common_name"])

    jumlah = len(total)
    print(f"[!] Found: {jumlah} domain")
    result_name = re.sub("\s", "_", keyword)
    for x in [jumlah]:
        with alive_bar(x) as fuck:
            for i in range(jumlah):
                file = open(f"{result_name}.txt", "a+")
                file.write(total[i] + "\n")
                file.close; time.sleep(.01); fuck()
    print(f"[+] Tersimpan di {result_name}.txt")
if __name__ == '__main__':
    keyword = input("[$] Search: ")
    print("[*] Please wait...")
    cari(keyword)
# code by ./meicookies
