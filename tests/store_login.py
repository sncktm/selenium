
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#seleniumのバージョンは４
#店舗ログイン

def run_test(driver):

    time.sleep(3)

    #IDの中に「no」がある場所を取得
    driver.find_element(By.ID, "no").send_keys("000001")
    time.sleep(3)

    #IDの中に「PASSWORD」がある場所を取得
    driver.find_element(By.ID, "pass").send_keys("abcd")
    time.sleep(3)

    #Submitボタンをクリック
    driver.find_element(By.CLASS_NAME, "confirmed-button").click()
    time.sleep(1)