from bs4 import BeautifulSoup as Soup
import requests
import csv
import pandas as pd


class Get_Deals:
    def __init__(self):
        """self.headers = {
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
        }"""
        
        """self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip',
            'DNT': '1',  # Do Not Track Request Header
            'Connection': 'close'
        }"""
        
        self.cookies = {'session': '17ab96bd8ffbe8ca58a78657a918558'}
        
        self.amzn_url = "https://www.amazon.in"
        self.flkt_url = "https://www.flipkart.com"

        amazon_req = requests.get(self.amzn_url, headers=self.headers)
        flipkart_req = requests.get(self.flkt_url, headers=self.headers)

        amazon_content = amazon_req.content  # Get Amazon content
        flipkart_content = flipkart_req.content  # Get Flipkart content

        self.amzn_soup = Soup(amazon_content, 'html5lib')
        self.flkt_soup = Soup(flipkart_content, 'html5lib')


    def Get_Link(self):

        amzn_todays_deal_link = self.amzn_soup.find('a', class_='a-link-normal as-title-block-right see-more truncate-1line').get('href')
        amzn_deal_page_link = str(self.amzn_url)+amzn_todays_deal_link
        
        flkt_todays_deal_link = self.flkt_soup.find('a', class_= '_2KpZ6l _3dESVI').get('href')
        flkt_deal_page_link = str(self.flkt_url)+flkt_todays_deal_link
        
        # print(amzn_deal_page_link)
        # print('\n\n', flkt_deal_page_link)
        
        self.Get_Data(amzn_deal_page_link, flkt_deal_page_link)


    def Get_Data(self, amzn_url, flkt_url):
        
        amzn_page = requests.get(amzn_url, headers=self.headers)
        amzn_soup = Soup(amzn_page.content, 'html5lib')
        
        flkt_page = requests.get(flkt_url, headers=self.headers)
        flkt_soup = Soup(flkt_page.content, 'html5lib')
        
        """print(amzn_soup.prettify())
        print('\n\n\n\n\n', flkt_soup.prettify())"""
        
        
        names = []
        discounts = []
        images = []
        links = []
        
        # Amazon - Name
        name = amzn_soup.find_all('a', class_='a-link-normal  a-color-base a-text-normal')
        for i in range(len(name)):
            names.append(name[i].text)
            
        # Flipkart - Name
        name = flkt_soup.find_all('div', class_='_3LU4EM')
        for i in range(len(name)):
            names.append(name[i].text)
        
        print(name)
            
        # Amazon = Discount
        discount = amzn_soup.find_all('span', class_= 'a-size-medium a-color-price')
        for value in discount:
            p = value.text
            if("% off" in p):
                p = p.replace("% off", "%")
                discounts.append(p)
                
        # Flipkart - Price
        price = flkt_soup.find_all('div', class_='_2tDhp2')
        for i in range(len(price)):
            discounts.append(price[i].text)
         
        # Amazon - Images
        image = amzn_soup.find_all('div', class_='a-image-container a-dynamic-image-container aok-align-center-horizontally DealImage-module__image_1aM-S1pMSsajamWgCRXa6y DealImage-module__imageAspectRatioFix_DJdrM5BSpMhSiPB6czCA4')
        for i in range(len(image)):
            p = image[i]
            image_tag = p.img
            images.append(image_tag.get('src'))
            
        # Flipkart - Images
        image = flkt_soup.find_all('img', class_='_396cs4 _3exPp9')
        for i in range(len(image)):
            p = image[i]
            image_link = p['src']
            images.append(image_link)
            
        # Amazon = link 
        link = amzn_soup.find_all('a', class_='a-link-normal')
        for i in range(len(link)):
            a = link[i]
            product_link = self.url+a['href']
            links.append(product_link)
            
        # Flipkart - link
        link = flkt_soup.find_all('a', class_='_6WQwDJ')
        for i in range(len(link)):
            a = link[i]
            product_link = self.flkt_url+a['href']
            links.append(product_link)

        
        # Data - Dictionary
        data = {'Name': names, 'Discount': discounts, 'Link': links, 'image_link': images}
        dataset = pd.DataFrame(data=data)

        print(dataset)
    


if __name__ == "__main__":
    G = Get_Deals()
    G.Get_Link()
    
