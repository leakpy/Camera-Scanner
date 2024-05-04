import fade
import requests
import re
import random
from requests.structures import CaseInsensitiveDict



text = """


████████╗██████╗ ██╗   ██╗███████╗████████╗██╗   ██╗
╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
   ██║   ██████╔╝██║   ██║███████╗   ██║    ╚████╔╝ 
   ██║   ██╔══██╗██║   ██║╚════██║   ██║     ╚██╔╝  
   ██║   ██║  ██║╚██████╔╝███████║   ██║      ██║   
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   
                                                    
| GITHUB: TRUUSTY | DISCORD: TRUSTY.PY | TELEGRAM: TRUUSTYLOL | 
| Github repo: https://github.com/truusty/Camera-Scanner |
"""
print(fade.purplepink(text))

url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


resp = requests.get(url, headers=headers)

data = resp.json()
countries = data['countries']

for key, value in countries.items():
    print(f'({key}) - {value["country"]}')

try:
    print("")
    country = input("Country Code: ")
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass

