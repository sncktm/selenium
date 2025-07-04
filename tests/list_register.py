from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

#リスト登録です
def run_test(driver):
    #ホームへボタンクリック
    home_link = driver.find_element(By.CSS_SELECTOR, "a.button.confirmed-button")
    home_link.click()
    time.sleep(4)

    # 検索メニュー（虫眼鏡のリンク）を探す
    search_menu = driver.find_element(By.XPATH, "//a[text()='検索']")
    time.sleep(3)

    # マウスを hover してメニューを表示
    ActionChains(driver).move_to_element(search_menu).perform()
    time.sleep(3)

    # 「商品検索」が表示されるまで待機してからクリック
    wait = WebDriverWait(driver, 10)
    product_search_link = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='goods']"))
    )
    product_search_link.click()

    time.sleep(3)
    
    # 商品カードのクリック（class="goods" の最初の1つ）
    wait = WebDriverWait(driver, 10)
    goods_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "goods")))
    goods_card.click()

    time.sleep(3)

    # 少し待機してから下にスクロール（詳細表示後）
    
    driver.execute_script("window.scrollBy(0, 500);")

    time.sleep(3)

    # 商品詳細が表示されるまでスクロール（必要に応じて）
    driver.execute_script("window.scrollBy(0, 500);")

    # ボタンがクリック可能になるまで待ってクリック
    wait = WebDriverWait(driver, 10)
    register_button = wait.until(
        EC.element_to_be_clickable((By.ID, "register-button"))
    )
    register_button.click()

    time.sleep(3)

    # 「晩御飯」リストの li をクリック
    wait = WebDriverWait(driver, 10)
    dinner_list = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@data-list-no='00000005']"))
    )
    dinner_list.click()
    time.sleep(3)

   # モーダル全体が表示されるのを待つ
    wait = WebDriverWait(driver, 10)
    modal = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal-content') and contains(@class, 'completion')]"))
    )

    # モーダル内の「閉じる」ボタンを取得してクリック
    close_button = modal.find_element(By.XPATH, ".//button[contains(text(), '閉じる')]")
    close_button.click()
    time.sleep(3)

