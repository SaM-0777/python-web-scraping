from bs4 import BeautifulSoup
import requests
import re

class Fetch:
    def __init__(self):
        self.sites = ['boAt', 'AmazonFashion', 'Amazon', 'Flipkart', 'Myntra', 'Tata', 'CLIQ' 'Ajio']
        # Initialize Beautifulsoup
        self.url = 'https://www.desidime.com'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
        page = requests.get(self.url, headers=headers)
        self.soup = BeautifulSoup(page.content, 'html.parser')
    
    def FetchLinks(self):
        prod_links = []
        try:
            main_list = self.soup.body.find('ul', class_='cf').find_all('li', class_='padfix grid-20 tablet-grid-25')
        except:
            print("Error")
        else:
            for li in main_list:
                deal_div = li.find('div', class_= 'deal-box shadow').find('div', class_ = 'deal-box-head cf')
                pr_div = li.find('div', class_= 'deal-box shadow').find('div', class_ = 'pr')
                if pr_div != None:
                    if len(pr_div.find_all('div')) == 1:
                        if deal_div:
                            link_div = deal_div.find('div', class_= 'ftr flex')
                            if link_div:
                                prod_links.append(self.url + link_div.a.get('href'))

                                        

        return prod_links
        """for url in prod_links:
            print(url, end="\n\n")"""
        
    
"""if __name__ == "__main__":
    F = Fetch()
    F.FetchLinks()"""
    