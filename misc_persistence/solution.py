# write a program that sends a get request to the url and prints the response

""" import requests
for i in range(1000):
    print(i,end=" ")
    url = "http://46.101.95.78:30638/flag"
    r=requests.get(url)
    if r.text[0:3]=='HTB':
        print(r.text)
        break
 """

import requests
import concurrent
from concurrent.futures import ThreadPoolExecutor
characters = range(1, 1000)
base_url = 'http://46.101.95.78:30638/flag'
threads = 20
def get_character_info(character):
    r = requests.get(f'{base_url}')
    return r.text
with ThreadPoolExecutor(max_workers=threads) as executor:
    future_to_url = {executor.submit(get_character_info, char)
    for char in characters}
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
            if data[0:3]=='HTB':
                print(data)
        except Exception as e:
            print('Looks like something went wrong:', e)