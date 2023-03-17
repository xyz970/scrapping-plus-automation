from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome("/home/mhmmdadi21/Development/Python/Scrapping/chromedriver")
listWord = []
driver.get("https://10fastfingers.com/typing-test/english")
content = driver.page_source
maximum = 100
soup = BeautifulSoup(content,features="lxml")
for i in range(maximum):
    listEl = driver.find_element(By.CSS_SELECTOR,"span[wordnr*='"+str(i)+"']")
    inputField = driver.find_element(By.ID,"inputfield")
    word = listEl.text
    listLetter = [x for x in word]
    for letter in word:
        inputField.send_keys(letter)
    inputField.send_keys(' ')
    # inputField.send_keys(word)
    # inputField.send_keys(' ')


