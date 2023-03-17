from selenium import webdriver
from bs4 import BeautifulSoup
import pandas


driver = webdriver.Chrome("/home/mhmmdadi21/Development/Python/Scrapping/chromedriver")
names = []
driver.get("https://www.instagram.com/m_adi_sptro/followers/")
driver.add_cookie(cookie_dict={'name':'sessionid','value':'9025245204%3AD3NNPAaUw5nmUT%3A14%3AAYcXwjZaUndWDibhlwdNzzvECYddP7G5lZhTtD2aEQ'})
driver.get("https://www.instagram.com/m_adi_sptro/followers/")

content = driver.page_source
soup = BeautifulSoup(content,features="lxml")
for a in soup.find_all('div',attrs={'class':'_aacl _aaco _aacw _aacx _aad7 _aade'}):
    print(a)
    name = a.find('div',attrs={'class':' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm'})

    names.append(name.text)

data = pandas.DataFrame({"Username":names})
data.to_csv("data/instagram.csv",encoding='utf-8',index=False)

#  _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm
#   _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm

#   _aacl _aaco _aacw _aacx _aad7 _aade
#   _aacl _aaco _aacw _aacx _aad7 _aade