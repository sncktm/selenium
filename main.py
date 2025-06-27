# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from tests import store_login, member_login, time_sale_list

chrome_driver_path = r"C:\Users\st20224116\Desktop\workspace\selenium\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()

    # --- 会員用ログインページ（最初のタブ）
    driver.get("http://10.24.108.179:8080/PurchasingSupportUserSystem/MemberLogin.jsp")
    member_tab = driver.current_window_handle
    member_login.run_test(driver)

    # --- 新しいタブで店舗用ログインページを開く
    driver.execute_script("window.open('http://10.24.108.179:8080/PurchasingSupportStoreSystem/StoreLogin.jsp', '_blank');")
    time.sleep(3)

    # --- タブハンドル再取得・切り替え
    handles = driver.window_handles
    store_tab = [h for h in handles if h != member_tab][0]
    driver.switch_to.window(store_tab)

    # --- 店舗ログイン
    store_login.run_test(driver)

    # --- タイムセール一覧に遷移
    time_sale_list.run_test(driver)

    time.sleep(3)

finally:
    driver.quit()
