from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import re
import pandas as pd



def get_daraz_title_price(url,driver,*args ,sleep_time =3):
    
    
    driver.get(url)
    time.sleep(sleep_time)
    html_source = driver.page_source
    
    soup = BeautifulSoup(html_source, 'html.parser')

    price_list= [float(span.text.replace('Rs. ', '').replace(',', '')) if span else 0 for span in soup.find_all(args[0], {args[1]: args[2]})]
    title_list= [re.sub(r'\s{2,}',' ',div.text) if div else 'None' for div in soup.find_all(args[3],{args[4]:args[5]})]

        
        
    return create_df_clean_data(title_list, price_list)





def get_ishopping_title_price(url,driver,*args ,sleep_time =3):
    
    
    driver.get(url)
    time.sleep(sleep_time)
    html_source = driver.page_source
    
    soup = BeautifulSoup(html_source, 'html.parser')
    item_soup = soup.find_all(args[0],{args[1]:args[2]})
    final_price_soup = [each_item.find_all(args[3], {args[4]: args[5]}) for each_item in item_soup]

    price_list = [float(span.find(args[6], {args[7]: args[8]}).text.replace('Rs. ', '').replace(',', '')) if span else 0 for final_prices in final_price_soup for span in final_prices]
    
    title_list= [re.sub(r'\s{2,}',' ',a.text) if a else 'None' for each_item in item_soup for a in each_item.find_all(args[9],{args[10]:args[11]})]
    
        
    return create_df_clean_data(title_list, price_list)






def create_df_clean_data(title_list, price_list):
    
    df = pd.DataFrame({'Title': title_list, 'Price': price_list}).drop_duplicates('Title').dropna()
    df.query('Price !=0 and Title !="None"', inplace= True)
    df.reset_index(drop=True, inplace=True)
    
    return df



def get_cheapest_website(url1, url2, key_word, **kwargs):
    driver = webdriver.Chrome()
    
    df1 = get_daraz_title_price(url1, driver, *kwargs['daraz_args'])
    df2 = get_ishopping_title_price(url2, driver, *kwargs['ishopping_args'])
    
    df1_filtered = df1[df1['Title'].str.contains(key_word, case=False, na=False)]
    df2_filtered = df2[df2['Title'].str.contains(key_word, case=False, na=False)]
    
    if df1_filtered.empty:
        print("No results found on Daraz for the given keyword.")
        return
    elif df2_filtered.empty:
        print("No results found on iShopping for the given keyword.")
        return
    
    min_price_df1 = df1_filtered['Price'].min()
    min_price_df2 = df2_filtered['Price'].min()

    if min_price_df1 == min_price_df2:
        print('Both websites have the same minimum price for the given keyword.')
    elif min_price_df1 > min_price_df2:
        print('Follow the link to the cheapest Website Daraz: ', url1)
        print('Cheapest Website 1 Dataframe:')
        print(df1_filtered.head())
    else:
        print('Follow the link to the cheapest Website ishopping: ', url2)
        print('Cheapest Website 2 Dataframe:')
        print(df2_filtered.head())  




daraz_url = "https://www.daraz.pk/catalog/?_keyori=ss&from=input&page=1&q=infinix+note+30&spm=a2a0e.pdp.search.go"
ishopping_url = "https://www.ishopping.pk/catalogsearch/result/?q=Infinix+note+30"

daraz_args= ['span', 'class', 'currency--GVKjl', 'div', 'class', 'title--wFj93']
ishopping_args = ['div','class','product-item-details','span','data-price-type','finalPrice','span','class','price', 'a', 'class', 'product-item-link']


kwargs ={
    'daraz_args': daraz_args,
    'ishopping_args': ishopping_args
}
key_word="infinix note 30"
#get_cheapest_website(daraz_url,ishopping_url,key_word,**kwargs)
