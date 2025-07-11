from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test(driver):
    wait = WebDriverWait(driver, 10)

    # 検索メニューをクリック
    search_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='検索']")))
    search_menu.click()
    time.sleep(1.5)

    # 「店舗検索」をクリック
    store_search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "店舗検索")))
    store_search_link.click()
    time.sleep(2.0)

    # 店舗一覧が表示されるまで待機
    first_store = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".store-list .store")))
    time.sleep(1.5)

    # 最初の店舗をクリックして詳細を表示
    first_store.click()
    time.sleep(2.5)

    # ページを最上部にスクロール
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2.0)

    # 並び替えのセレクトボックスを変更（時間を長めに確保）
    sort_select = wait.until(EC.presence_of_element_located((By.ID, "sort-select")))
    select = Select(sort_select)

    sort_values = ["name-asc", "name-desc", "opening-asc", "closing-desc", "distance"]
    for value in sort_values:
        select.select_by_value(value)
        time.sleep(2.5)  # ソートによる画面変化を目視できるように

    # 営業中のみ表示をチェック
    available_checkbox = driver.find_element(By.ID, "showOnlyAvailable")
    if not available_checkbox.is_selected():
        available_checkbox.click()
        time.sleep(1.5)

    # 「タイヨー」と入力
    keyword_input = driver.find_element(By.ID, "keyword")
    keyword_input.clear()
    keyword_input.send_keys("タイヨー")
    time.sleep(1.5)

    # 検索ボタンをクリック
    search_button = driver.find_element(By.CSS_SELECTOR, "#search-form button[type='submit']")
    search_button.click()
    time.sleep(2.5)

    # 結果の店舗名が表示されるまで待機
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".store-name")))
    time.sleep(3.0)  # 最後に結果を確認しやすく

    for i in range(10):  # 10回に分けて100pxずつスクロール
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(0.5)  # ゆっくり下がっていく感じ
    time.sleep(1.0)  # 最下部で停止
