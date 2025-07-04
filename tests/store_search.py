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

    # --- 並び替え ---
    print("ステップ2: 並び替えを確認します。")
    sort_values = ["name-asc", "name-desc", "price-asc"]
    for value in sort_values:
        print(f"-> 並び替え: {value}")
        before = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-grid .goods")))
        Select(driver.find_element(By.ID, "sort-select")).select_by_value(value)
        wait.until(EC.staleness_of(before))
        time.sleep(2)

    # --- 商品詳細ページへ遷移 ---
    print("ステップ3: 商品詳細ページに遷移します。")
    first_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".goods-grid .goods:first-child")))
    first_item.click()
    wait.until(EC.visibility_of_element_located((By.ID, "details-container")))
    time.sleep(2)

    # --- 検索 "卵" ---
    print("ステップ4: '卵' で検索します。")
    # 一番上までスクロール（navの本来の位置まで）
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    # キーワードを入力
    search_box = driver.find_element(By.NAME, "keyword")
    search_box.clear()
    search_box.send_keys("卵")
    time.sleep(1)
    before = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-grid .goods")))
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-form button[type='submit']")))
    search_button.click()
    wait.until(EC.staleness_of(before))
    time.sleep(2)

    # --- 現在地から近い順 ---
    print("ステップ5: 距離順に並び替えます。")
    Select(driver.find_element(By.ID, "sort-select")).select_by_value("distance-asc")
    wait.until_not(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".goods-grid .goods:first-child .distance"), "距離計算中..."
    ))
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
    time.sleep(2)


    # --- 商品詳細を再確認 ---
    print("ステップ8: フィルタ後の商品詳細を確認します。")
    driver.find_element(By.CSS_SELECTOR, ".goods-grid .goods:first-child").click()
    wait.until(EC.visibility_of_element_located((By.ID, "details-container")))
    print("-> 商品詳細が表示されました。テスト完了。")
    time.sleep(2)
