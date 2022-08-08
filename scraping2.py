from bs4 import BeautifulSoup as Soup
import requests
import csv
import pandas as pd

entry = input("Search: ")
req = requests.get("https://www.flipkart.com/search?q="+str(entry))
content = req.content  # Get the content
soup = Soup(content, 'html.parser')

names = []
descriptions = []
prices = []
original_prices = []
ratings = []
discounts = []
images = []
links = []

name = soup.find_all('div', class_='_4rR01T')
for i in range(len(name)):
    names.append(name[i].text)

desc = soup.find_all('div', class_='fMghEO')
for i in range(len(desc)):
    descriptions.append(desc[i].text)

price = soup.find_all('div', class_='_30jeq3 _1_WHN1')
for i in range(len(price)):
    prices.append(price[i].text)

original_price = soup.find_all('div', class_='_3I9_wc _27UcVY')
for i in range(len(original_price)):
    original_prices.append(original_price[i].text)

rating = soup.find_all('div', class_='_3LWZlK', limit=24)
for i in range(len(rating)):
    ratings.append(rating[i].text)

discount = soup.find_all('div', class_='_3Ay6Sb', limit=24)
for i in range(0, len(discount)):
    p = discount[i].text
    if("% off" in p):
        p = p.replace("% off", "%")
        discounts.append(p)

image = soup.find_all('img', class_='_396cs4 _3exPp9')
for i in range(len(image)):
    p = image[i]
    image_link = p['src']
    images.append(image_link)

link = soup.find_all('a', class_='_1fQZEK')
for i in range(len(link)):
    a = link[i]
    product_link = "flipkart.com"+a['href']
    links.append(product_link)

data = {'Name': names, 'Description': descriptions, 'Ratings': ratings,
        'Price': prices, 'Link': links, 'image_link': images}
dataset = pd.DataFrame(data=data)
print(dataset)
