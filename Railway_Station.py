from bs4 import BeautifulSoup as Soup
import requests
import csv
import pandas as pd


headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

url = "https://www.cleartrip.com/trains/stations/list"
req = requests.get(url, headers= headers)

content = req.content
my_soup = Soup(content, 'html5lib')

def Scrap():
    station_list = []
    table = my_soup.find("table", class_= 'results')
    data = table.find_all("td", limit= 50000)
    
    for i in range(0, len(data)):
        if i % 4 == 0 or i % 2 == 0:
            station_list.append(data[i].get_text())
    
    print(station_list)

    
Scrap()



