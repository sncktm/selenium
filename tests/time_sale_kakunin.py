# tests/store_search.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def run_test(driver):
    wait = WebDriverWait(driver, 20)

    time.sleep(3)
    # 商品検索ページへ遷移
    driver.find_element(By.LINK_TEXT, "検索").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "商品検索").click()
    time.sleep(3)

    # --- 全件検索 ---
    print("ステップ1: 全件検索を実行します。")
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-form button[type='submit']")))
    search_button.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-grid .goods")))
    print("-> 全件検索が完了しました。")
    time.sleep(2)

    
    time.sleep(2)

    # --- 販売中のみ表示 ---
    print("ステップ6: '販売中のみ' チェックします。")

    available_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "showOnlyAvailable")))
    if not available_checkbox.is_selected():
        available_checkbox.click()
    # 一番上にスクロール
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    # 検索ボタンをクリック（クリック直前に取得して確実にクリック可能な状態にする）
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-form button[type='submit']")))
    search_button.click()
    # 検索結果が更新されるまで待機（staleness_ofは使わず、新しい要素の出現を待つ）
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-grid .goods")))

    time.sleep(2)


    # --- セール中のみ表示 ---
    print("ステップ7: 'セール中のみ' チェックします。")
    sale_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "showOnlySale")))
    if not sale_checkbox.is_selected():
        sale_checkbox.click()
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-form button[type='submit']")))
    search_button.click()
    # staleness_of はやめて、新しい商品要素の出現を待つ
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-grid .goods")))
    print("-> 'セール中のみ' 絞り込み完了。")
    time.sleep(5)


    driver.find_element(By.LINK_TEXT, "ホーム").click()
    time.sleep(3)
    # 「タイムセール」タブをクリック
    timesale_tab = driver.find_element(By.XPATH, "//button[contains(text(), 'タイムセール')]")
    timesale_tab.click()
    time.sleep(4)