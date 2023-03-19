# https://fans-vision.wstif3b.id/pages/login.php
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def run_test():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
    listWord = []
    driver.implicitly_wait(5)
    emailOption = ["nkmsabdjas@gmail.com","kahsdkas@gmail.com","","","admin@gmail.com"]
    passwordOption = ["1234567","","kahsdkas","","123"]
    driver.get("https://fans-vision.wstif3b.id/pages/login.php")
    content = driver.page_source

    for emailOpt,passOpt in zip(emailOption,passwordOption):
        inputEmail = driver.find_element(By.NAME,"email")
        inputPassword = driver.find_element(By.NAME,"password")
        inputEmail.send_keys(emailOpt)
        inputPassword.send_keys(passOpt)
        driver.find_element(By.CLASS_NAME,"btn").click()
        time.sleep(2)

    driver.find_element(By.ID,"produk").click()
    driver.find_element(By.ID,"show-login").click()
    driver.find_element(By.NAME,"nama").send_keys("blabla")
    driver.find_element(By.NAME,"harga").send_keys("123")
    driver.find_element(By.NAME,"kecepatan").send_keys("")
    time.sleep(2)
    driver.find_element(By.NAME,"kecepatan").send_keys("123")
    driver.find_element(By.NAME,"stok").send_keys("123")
    driver.find_element(By.ID,"submit").click()
    # print(driver.current_url)


