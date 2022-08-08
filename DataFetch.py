from bs4 import BeautifulSoup as Soup
import requests
import csv
import pandas as pd

class Fetch_Data:
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
        
        cookies = {'session': '17ab96bd8ffbe8ca58a78657a918558'}
        
        url1 = 'https://www.amazon.in/s?k='
        url2 = 'https://www.flipkart.com/search?q='
        
        entry = input("Search: ")
        amazon_req = requests.get("https://www.amazon.in/s?k="+str(entry), headers= headers)
        flipkart_req = requests.get("https://www.flipkart.com/search?q="+str(entry), headers= headers)
        
        amazon_content = amazon_req.content  # Get Amazon content
        flipkart_content = flipkart_req.content  # Get Flipkart content
        
        self.amzn_soup = Soup(amazon_content, 'html5lib')
        self.flkt_soup = Soup(flipkart_content, 'html5lib')

        
    def Scrap(self):
        
        # Data from Amazon
        names = []
        prices = []
        original_prices = []
        ratings = []
        discounts = []
        images = []
        links = []
        
        # Product Details
        
        
        # Name
        
        # Amazon-Name
        amzn_name = self.amzn_soup.find_all('span', class_='a-size-medium a-color-base a-text-normal', limit= 10)
        for i in range(len(amzn_name)):
            names.append(amzn_name[i].text)
            
        # Flipkart-Name
        flkt_name = self.flkt_soup.find_all('div', class_='_4rR01T')
        for i in range(len(flkt_name)):
            names.append(flkt_name[i].text)


        # Price
        
        # Amazon - Price
        amzn_price = self.amzn_soup.find_all('span', class_= 'a-price-whole', limit= 10)
        for i in range(len(amzn_price)):
            prices.append(amzn_price[i].text)
            
        # Flipkart - Price
        flkt_price = self.flkt_soup.find_all('div', class_='_30jeq3 _1_WHN1')
        for i in range(len(flkt_price)):
            prices.append(flkt_price[i].text)


        # Original Price
        
        # Amazon - Original Price
        amzn_original_price = self.amzn_soup.find_all('span', class_='a-offscreen', limit= 10)
        for i in range(len(amzn_original_price)):
            original_prices.append(amzn_original_price[i].text)
            
        # Flikart - Original Price
        flkt_original_price = self.flkt_soup.find_all('div', class_='_3I9_wc _27UcVY')
        for i in range(len(flkt_original_price)):
            original_prices.append(flkt_original_price[i].text)
        

        # Ratings
        
        # Amazon Ratings
        amzn_rating = self.amzn_soup.find_all('span', class_='a-icon-alt', limit=10)
        for i in range(len(amzn_rating)):
            ratings.append(amzn_rating[i].text)
            
        # Flipkart Ratings
        flkt_rating = self.flkt_soup.find_all('div', class_='_3LWZlK', limit=24)
        for i in range(len(flkt_rating)):
            ratings.append(flkt_rating[i].text)
            

        # Discount
        
        # Amazon - Discount
        amzn_discount = self.amzn_soup.find_all('a', class_='a-size-mini a-link-normal a-text-normal', limit=10)
        for value in amzn_discount:
            p = value.find('span', class_=None).text
            if("% off" in p):
                p = p.replace("% off", "%")
                discounts.append(p)
                
        # Flipkart - Discount
        flkt_discount = self.flkt_soup.find_all('div', class_='_3Ay6Sb', limit=24)
        for i in range(0, len(flkt_discount)):
            p = flkt_discount[i].text
            if("% off" in p):
                p = p.replace("% off", "%")
                discounts.append(p)
        
        
        # Image-url
        
        # Amazon - Image-urls
        amzn_image = self.amzn_soup.find_all('img', class_='s-image', limit=10)
        for i in range(len(amzn_image)):
            p = amzn_image[i]
            image_link = p['src']
            images.append(image_link)
            
        # Flipkart - Image-urls
        flkt_image = self.flkt_soup.find_all('img', class_='_396cs4 _3exPp9')
        for i in range(len(flkt_image)):
            p = flkt_image[i]
            image_link = p['src']
            images.append(image_link)


        # link to original product page
        
        # Amazon - link
        amzn_link = self.amzn_soup.find_all('a', class_='a-link-normal a-text-normal', limit= 10)
        for i in range(len(amzn_link)):
            a = amzn_link[i]
            product_link = "amazon.in"+a['href']
            links.append(product_link)
            
        # Flipkart - link
        flkt_link = self.flkt_soup.find_all('a', class_='_1fQZEK')
        for i in range(len(flkt_link)):
            a = flkt_link[i]
            product_link = "https://www.flipkart.com"+a['href']
            links.append(product_link)

        # Data - Dictionary
        data = {'Name': names, 'Ratings': ratings,
                'Price': prices, 'Link': links, 'image_link': images}
        dataset = pd.DataFrame(data=data)
        
        print(dataset)


if __name__ == "__main__":
    F = Fetch_Data()
    F.Scrap()


