from bs4 import BeautifulSoup as Soup
import requests
import csv
import pandas as pd
import random


class Home_Page:
    def __init__(self):
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

        # cookies = {'session': '17ab96bd8ffbe8ca58a78657a918558'}

        # url1 = 'https://www.amazon.in/s?k='
        # url2 = 'https://www.flipkart.com/search?q='

        """entry = input("Search: ")
        amazon_req = requests.get("https://www.amazon.in/s?k="+str(entry), headers=headers)
        flipkart_req = requests.get("https://www.flipkart.com/search?q="+str(entry), headers=headers)

        amazon_content = amazon_req.content  # Get Amazon content
        flipkart_content = flipkart_req.content  # Get Flipkart content

        self.amzn_soup = Soup(amazon_content, 'html5lib')
        self.flkt_soup = Soup(flipkart_content, 'html5lib')"""
    
    def intialize(self):
        
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
        
        entry_list = ['laptop', 'phone', 'samsung', 'mi', 'oppo', 'realme', 'oneplus', 'lenovolaptop', 'hplaptop', 'delllaptop', 'asuslaptop']
        # entry = random.choice(entry_list)
        
        names = []
        prices = []
        original_prices = []
        ratings = []
        discounts = []
        images = []
        links = []
        
        for i in range(len(entry_list)):
            
            amazon_req = requests.get("https://www.amazon.in/s?k="+str(random.choice(entry_list)), headers=headers)
            flipkart_req = requests.get("https://www.flipkart.com/search?q="+str(random.choice(entry_list)), headers=headers)
            
            print("https://www.amazon.in/s?k="+str(random.choice(entry_list)))
            print("https://www.flipkart.com/search?q="+str(random.choice(entry_list)))

            amazon_content = amazon_req.content  # Get Amazon content
            flipkart_content = flipkart_req.content  # Get Flipkart content

            amzn_soup = Soup(amazon_content, 'html5lib')
            flkt_soup = Soup(flipkart_content, 'html5lib')

            # Amazon - Name
            """name = amzn_soup.find('span', class_='a-size-medium a-color-base a-text-normal')
            names.append(name.text)"""

            # Flipkart - Name
            name = flkt_soup.find('div', class_='_4rR01T')
            names.append(name.text)

             # Price

            # Amazon - Price
            """amzn_price = self.amzn_soup.find('span', class_='a-price-whole')
            prices.append(amzn_price.text)"""

            # Flipkart - Price
            flkt_price = flkt_soup.find('div', class_='_30jeq3 _1_WHN1')
            prices.append(flkt_price.text)

            # Original Price

            # Amazon - Original Price
            """amzn_original_price = self.amzn_soup.find('span', class_='a-offscreen')
            original_prices.append(amzn_original_price.text)"""

            # Flikart - Original Price
            flkt_original_price = flkt_soup.find('div', class_='_3I9_wc _27UcVY')
            original_prices.append(flkt_original_price.text)

            # Ratings

            # Amazon Ratings
            """amzn_rating = self.amzn_soup.find('span', class_='a-icon-alt')
            ratings.append(amzn_rating.text)"""

            # Flipkart Ratings
            flkt_rating = flkt_soup.find('div', class_='_3LWZlK')
            ratings.append(flkt_rating.text)

            # Discount

            # Amazon - Discount
            """amzn_discount = self.amzn_soup.find('a', class_='a-size-mini a-link-normal a-text-normal')
            p = value.find('span', class_=None).text
            if("% off" in p):
                p = p.replace("% off", "%")
                discounts.append(p)"""

            # Flipkart - Discount
            flkt_discount = flkt_soup.find('div', class_='_3Ay6Sb')
            p = flkt_discount.text
            if("% off" in p):
                p = p.replace("% off", "%")
                discounts.append(p)

            # Image-url

            # Amazon - Image-urls
            """amzn_image = self.amzn_soup.find('img', class_='s-image')
            p = amzn_image
            image_link = p['src']
            images.append(image_link)"""

            # Flipkart - Image-urls
            flkt_image = flkt_soup.find('img', class_='_396cs4 _3exPp9')
            p = flkt_image
            image_link = p['src']
            images.append(image_link)

            # link to original product page

            # Amazon - link
            """amzn_link = self.amzn_soup.find('a', class_='a-link-normal a-text-normal', limit=10)
            a = amzn_link
            product_link = "https://amazon.in"+a['href']
            links.append(product_link)"""

            # Flipkart - link
            flkt_link = flkt_soup.find('a', class_='_1fQZEK')
            a = flkt_link
            product_link = "https://www.flipkart.com"+a['href']
            links.append(product_link)

        # Data - Dictionary
        data = {'Name': names, 'Ratings': ratings, 'Price': prices, 'Link': links, 'image_link': images}
        dataset = pd.DataFrame(data=data)

        print(dataset)


if __name__ == "__main__":
    H = Home_Page()
    H.intialize()
