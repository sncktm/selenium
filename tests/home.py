from selenium.webdriver.common.by import By
import time

def run_test(driver):
   
    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT, "ホーム").click()
    time.sleep(3)
