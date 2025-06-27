
from selenium.webdriver.common.by import By
import time

#seleniumのバージョンは４
#店舗ログイン

def run_test(driver):
    # 指定した秒数だけ待つ
    time.sleep(3)


    #email入力
    driver.find_element(By.ID, "email").send_keys("cccc@gmail.com")
    time.sleep(3)

    #IDの中に「PASSWORD」がある場所を取得
    driver.find_element(By.ID, "pass").send_keys("0123")
    time.sleep(3)

    #Submitボタンをクリック
    driver.find_element(By.CLASS_NAME, "confirmed-button").click()
    time.sleep(1)