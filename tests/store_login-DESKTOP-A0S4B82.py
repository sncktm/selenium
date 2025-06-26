
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#seleniumのバージョンは４
#店舗ログイン


def run_test():
    #ChromeDriveのパスを指定
    chrome_driver_path = r"C:\Users\snckt\OneDrive\デスクトップ\workspace\selenium\chromedriver.exe"

    #Chromeを起動
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service = service)

    try:
        #全画面表示(ウィンドウを最大化)
        driver.maximize_window()


        #指定URLへアクセス
        driver.get("http://10.24.108.179:8080/PurchasingSupportStoreSystem/StoreLogin.jsp")


        # 指定した秒数だけ待つ
        time.sleep(3)


        #IDの中に「no」がある場所を取得
        email_input = driver.find_element(By.ID, "no")

        #指定した店舗番号を指定
        email_input.send_keys("000001")

        # 指定した秒数だけ待つ
        time.sleep(3)

        #IDの中に「PASSWORD」がある場所を取得
        pass_input = driver.find_element(By.ID, "pass")

        #指定したパスワードを指定
        pass_input.send_keys("abcd")

        # 指定した秒数だけ待つ
        time.sleep(3)

        #Submitボタンをクリック
        submit_button = driver.find_element(By.CLASS_NAME, "confirmed-button")
        submit_button.click()


        # 指定した秒数だけ待つ
        time.sleep(10)

    finally:
        #ブラウザを閉じる
        driver.quit()