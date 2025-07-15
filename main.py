# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from tests import goods_search, store_search, store_login, member_login, time_sale_list, list_view, advertisement_update, home, list_register, advertisement_register, advertisement_delete, time_sale_register

chrome_driver_path = r"C:\Users\st20224116\Desktop\selenium\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()

    # --- 会員用ログインページ（最初のタブ）
    driver.get("https://21d418823a6f.ngrok-free.app/PurchasingSupportUserSystem/MemberLogin.jsp")
    member_tab = driver.current_window_handle
    member_login.run_test(driver)

    # ---検索して、そのままリスト登録（卵）
    store_search.run_test(driver)
    # goods_search.run_test(driver)

    # list_view.run_test(driver)

    # list_register.run_test(driver)
    # list_view.run_test(driver)

    # home.run_test(driver)


    # --- 新しいタブで店舗用ログインページを開く
    driver.execute_script("window.open('https://21d418823a6f.ngrok-free.app/PurchasingSupportStoreSystem/StoreLogin.jsp', '_blank');")
    time.sleep(3)

    # --- タブハンドル再取得・切り替え
    handles = driver.window_handles
    store_tab = [h for h in handles if h != member_tab][0]
    driver.switch_to.window(store_tab)

    # --- 店舗ログイン
    store_login.run_test(driver)

    # --- 広告登録、変更、削除(変更後、ホームに遷移して確認)
    # advertisement_register.run_test(driver)
    # advertisement_update.run_test(driver)
    # advertisement_delete.run_test(driver)
    driver.switch_to.window(member_tab)
    home.run_test(driver)

    driver.switch_to.window(store_tab)
    # --- タイムセール一覧に遷移
    time_sale_register.run_test(driver)
    time_sale_list.run_test(driver)

    driver.switch_to.window(member_tab)
    goods_search.run_test(driver)

    time.sleep(3)

finally:
    driver.quit()
