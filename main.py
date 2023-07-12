import requests, re 
from colorama import Fore, Back
from user_agent import generate_user_agent as RandomUserAgent
from concurrent.futures import ThreadPoolExecutor

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Cache-Control": "max-age=0", "Connection": "keep-alive", "Host": "www.insecam.org", "Upgrade-Insicure-Requests": "1", "User-Agent": RandomUserAgent()}

def scrape(url):
    request = requests.get(url, headers=headers)
    return request

for key, value in requests.get("http://www.insecam.org/en/jsoncountries/", headers=headers).json()['countries'].items():
    print('Country:', value['country'], '|', 'Country Code:', key, '(x' + str(value['count']) + ')')
for x in range(1): print('\n')

country = input("( ! ) What's the Country Code you'd like to Scan? >> ")
result = requests.get('http://www.insecam.org/en/bycountry/' + country, headers=headers)
    
bold, green, white, reset, back_reset, back_black = '\033[1m', Fore.LIGHTGREEN_EX, Fore.WHITE, Fore.RESET, Back.RESET, Back.BLACK

with ThreadPoolExecutor(max_workers=100) as execute:
    results, addresses = execute.map(scrape, ['http://www.insecam.org/en/bycountry/' + country + '/?page=' + str(page) for page in range(int(re.findall(r'pagenavigator\("\?page=", (\d+)', result.text)[0]))]), []
    for result in results: 
        for IP_ADDRESS in re.findall(r"http://\d+.\d+.\d+.\d+:\d+", result.text): 
            print(bold, back_black, green + '( + ) Live Stream:', IP_ADDRESS, '|', 'IP & Port:', IP_ADDRESS.split('//')[1], reset, back_reset)
            addresses.append(IP_ADDRESS)
            
    with open(country + '.txt', 'w') as file:
        file.truncate(0)
        for link in addresses:
            file.write(link + '\n')
    print(bold + white + '( ! ) Successfully scraped', len(addresses), 'Live Streams & IP Addresses and saved them in', country + '.txt.', reset)
                

