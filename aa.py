
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#seleniumのバージョンは４

#ChromeDriveのパスを指定
chrome_driver_path = r"C:\Users\st20224116\Desktop\workspace\selenium\chromedriver.exe"

#Chromeを起動
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service)

try:
    #全画面表示(ウィンドウを最大化)
    driver.maximize_window()


    #指定URLへアクセス
    driver.get("http://moodle/loginform/")


    # 指定した秒数だけ待つ
    time.sleep(3)
    
    #ログインをクリック(Selenium 4)
    login_link = driver.find_element(By.LINK_TEXT, "LOGIN")
    login_link.click()

    # 指定した秒数だけ待つ
    time.sleep(3)

    #画面をスクロール
    driver.execute_script("""
        window.scrollBy({top: 250, left: 0, behavior: 'smooth'})
      """)
    
    # 指定した秒数だけ待つ
    time.sleep(3)

    #IDの中に「EMAIL」がある場所を取得
    email_input = driver.find_element(By.ID, "email")

    #指定したメールアドレスを指定
    email_input.send_keys("test@gmail.com")

    # 指定した秒数だけ待つ
    time.sleep(3)

    #IDの中に「PASSWORD」がある場所を取得
    pass_input = driver.find_element(By.ID, "password")

    #指定したパスワードを指定
    pass_input.send_keys("pass")

    # 指定した秒数だけ待つ
    time.sleep(3)

    #Submitボタンをクリック
    submit_button = driver.find_element(By.CLASS_NAME, "ipt-button")
    submit_button.click()

    #スクショを保存
    driver.save_screenshot(r"C:\Users\st20224116\Documents\Selenium\01.png")

    # 指定した秒数だけ待つ
    time.sleep(10)

finally:
    #ブラウザを閉じる
    driver.quit()