from selenium import webdriver
from bs4 import BeautifulSoup
import pandas


driver = webdriver.Chrome("/home/mhmmdadi21/Development/Python/Scrapping/chromedriver")
products = []
prices = []

driver.get("https://shopee.co.id/flash_sale?categoryId=0&promotionId=105932505956352")

content = driver.page_source
soup = BeautifulSoup(content,features="lxml")
for a in soup.find_all('a',href=True,attrs={'class':'PMpbYz'}):
    product = a.find('div',attrs={'class':'OHv6Qr'})
    price = a.find('span',attrs={'class':'i25Yvf'})

    products.append(product.text)
    prices.append(price.text)

data = pandas.DataFrame({"Nama Produk":products,"Harga":prices})
data.to_csv("data/shopeeFlash.csv",encoding='utf-8',index=False)