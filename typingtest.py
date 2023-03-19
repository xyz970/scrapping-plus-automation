import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
listWord = []
driver.implicitly_wait(5)
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
        time.sleep(0.1)
    inputField.send_keys(' ')
    # inputField.send_keys(word)
    # inputField.send_keys(' ')


