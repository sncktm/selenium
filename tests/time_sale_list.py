from selenium.webdriver.common.by import By
import time



def run_test(driver):
   
    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT, "タイムセール管理").click()

    time.sleep(3)

    # タイムセール一覧をクリック
    driver.find_element(By.LINK_TEXT, "タイムセール一覧").click()
    
    time.sleep(3)

    # タイムセール詳細をクリック
    driver.find_element(By.CLASS_NAME, "detail-button").click()

    time.sleep()