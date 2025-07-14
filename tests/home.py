from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

#リスト登録です
def run_test(driver):

    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT, "ホーム").click()


    # 「店舗広告」タブをクリック
    store_tab = driver.find_element(By.XPATH, "//button[contains(text(), '店舗広告')]")
    store_tab.click()
    time.sleep(4)

    # 「商品広告」タブをクリック
    product_tab = driver.find_element(By.XPATH, "//button[contains(text(), '商品広告')]")
    product_tab.click()
    time.sleep(4)

    # 「タイムセール」タブをクリック
    timesale_tab = driver.find_element(By.XPATH, "//button[contains(text(), 'タイムセール')]")
    timesale_tab.click()
    time.sleep(4)
