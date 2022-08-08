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
cookies = {'session': '17ab96bd8ffbe8ca58a78657a918558'}
entry = input("Search: ")
req = requests.get("https://www.amazon.in/s?k="+str(entry), headers= headers)
content = req.content  # Get the content
soup = Soup(content, 'html5lib')

names = []
descriptions = []
prices = []
original_prices = []
ratings = []
discounts = []
images = []
links = []

name = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
for i in range(len(name)):
    names.append(name[i].text)

price = soup.find_all('span', class_='a-price-whole')
for i in range(len(price)):
    prices.append(price[i].text)

original_price = soup.find_all('span', class_= 'a-offscreen')
for i in range(len(original_price)):
    original_prices.append(original_price[i].text)

rating = soup.find_all('span', class_='a-icon-alt', limit= 18)
for i in range(len(rating)):
    ratings.append(rating[i].text)

discount = soup.find_all('a', class_= 'a-size-mini a-link-normal a-text-normal', limit= 18)
for value in discount:
    p = value.find('span', class_=None).text
    if("% off" in p):
        p = p.replace("% off", "%")
        discounts.append(p)

image = soup.find_all('img', class_='s-image')
for i in range(len(image)):
    p = image[i]
    image_link = p['src']
    images.append(image_link)

link = soup.find_all('a', class_= 'a-link-normal a-text-normal')
for i in range(len(link)):
    a = link[i]
    product_link = "amazon.in"+a['href']
    links.append(product_link)

data = {'Name': names, 'Ratings': ratings,
        'Price': prices, 'Link': links, 'image_link': images}
#dataset = pd.DataFrame(data=data)
#print(dataset)

print(f'Name len : {len(names)}')
print(f'Rating len : {len(ratings)}')
print(f'Price len : {len(prices)}')
print(f'Link len : {len(links)}')
print(f'Image len : {len(images)}')

print(f'Prices : \n {prices}')
print(f'Names : \n {names}')

