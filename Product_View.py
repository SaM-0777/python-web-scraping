from bs4 import BeautifulSoup
import requests
import json
from Sites import Fetch

class GalleryView(Fetch):
    def __init__(self):
        Fetch.__init__(self)
        
    
    def GoToPage(self):
        F = Fetch()
        links = F.FetchLinks()
        #print(links)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
        link_ = '#'
        Product_Details = {}
        
        # Traverse the links one by one
        for url in links:
            
            # print(url)
            
            page = requests.get(url, headers= headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Main-Section
            main_section = soup.body.find('div', class_ = 'grid-75 tablet-grid-100 grid-parent')
            
            # Prod-view
            main_div = main_section.find('div', id = 'deal-detail-like-dislike-container')
            
            # src-link of prod-img
            prod_img = main_div.find('div', class_ = 'grid-20 tablet-grid-20 grid-parent pr').a.img.get('data-src')
            
            # prod-details-text-section
            prod_deatils_div = main_div.find('div', class_ = 'grid-80 tablet-grid-80 grid-parent pl30 pr20')
            
            # prod-redirect-link
            prod_redirect_link = prod_deatils_div.find_all('div', class_ = 'grid-20 tablet-grid-25 ftr pad-left')
            for _div in prod_redirect_link:
                if _div.a.get('target') == '_blank':
                    link_ = _div.a.get('href')
            # print(link_)
            
            # prod-details
            prod_name = prod_deatils_div.find('h1').get_text()
            
            # try to avoid error
            price_offer_div = prod_deatils_div.find('div', class_ = 'grid-25 tablet-grid-25 fl grid-parent')
            
            if price_offer_div != None:
                prod_price = price_offer_div.find('div', class_ = 'dealprice').get_text()
                prod_offer_percent = price_offer_div.find('div', class_ = 'dealpercent').get_text()
            else:
                prod_price = None
                prod_offer_percent = None
            
            # Prod-Description
            prod_desc_div = main_section.find('div', class_= 'posts_list').find('div', 'wcard brd-t-b-4')
            content_div = prod_desc_div.find('div', class_= 'mainpost postcontent')
            prod_desc = content_div.get_text()
            
            # Create Prod-view dict
            prod_view_desc = {'Name': prod_name, 'Image-url': prod_img, 'Price': prod_price, 'Offer-Details': prod_offer_percent, 'Description': prod_desc, 'Redirect-url': link_}
            
            #print(prod_view_desc)
            
            Product_Details.update(prod_view_desc)
        
        print(Product_Details)
            

if __name__ == "__main__":
    GView = GalleryView()
    GView.GoToPage()
