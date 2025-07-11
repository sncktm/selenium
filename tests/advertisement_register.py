from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
def run_test(driver):
    # ActionChains準備
    actions = ActionChains(driver)

    # 「広告管理」の li 要素を取得
    ad_management = driver.find_element(By.XPATH, '//a[text()="広告管理"]/parent::li')

    # マウスを「広告管理」にホバー
    actions.move_to_element(ad_management).perform()

    time.sleep(2)

    # サブメニューが表示されるまで少し待つ（CSSアニメーション対応）
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "広告情報一覧"))
    )

    # 「広告情報一覧」のリンクを取得
    ad_list = driver.find_element(By.LINK_TEXT, "広告情報一覧")

    # ホバーしてからクリック（明示的に move_to_element → click）
    actions.move_to_element(ad_list).click().perform()

    time.sleep(2)

    # 正しいセレクタでボタンを取得
    register_button = driver.find_element(By.CSS_SELECTOR, 'button.button.cancel-button.btn-new')
    actions.move_to_element(register_button).perform()
    time.sleep(2)
    # 通常クリック（disabled でなければ）
    register_button.click()

    time.sleep(2)

    title_input = driver.find_element(By.ID,"ad-title")
    title_input.clear()
    title_input.send_keys("Sample1")
    time.sleep(2)

    #id_input = driver.find_element(By.ID,"ad-type")
    dropdown_element = driver.find_element("id", "ad-type")
    dropdown_element.click()
    time.sleep(1)
    select = Select(dropdown_element)
    select.select_by_index(2)
    time.sleep(1)

    driver.execute_script("""
    window.scrollBy({ top : 250, left: 0, behavior: 'smooth'});
""")
    
    text_input = driver.find_element(By.ID,"ad-text")
    text_input.clear()
    text_input.send_keys("これはテストです")
    time.sleep(1)

    size_element = driver.find_element("id", "ad-priority")
    size_element.click()
    time.sleep(1)
    select = Select(size_element)
    select.select_by_index(1)
    time.sleep(1)

    # ファイルアップロード用のinput要素を取得
    file_input = driver.find_element(By.ID, "file-upload")

    # アップロードしたい画像ファイルの絶対パスを指定
    file_path = r"C:\Users\st20224116\Desktop\workspace\selenium\images\20off.png"

    # inputにファイルパスを送信 → これでファイル選択ダイアログを介さずアップロード完了
    file_input.send_keys(file_path)

    time.sleep(2)

    goods_element = driver.find_element("id", "goods")
    goods_element.click()
    time.sleep(1)
    select = Select(goods_element)
    select.select_by_index(1)
    time.sleep(1)

    register_button = driver.find_element(By.CLASS_NAME, "confirmed-button")
    register_button.click()
    time.sleep(1)

    registerconfirm_button = driver.find_element(By.CLASS_NAME, "button confirmed-button")
    registerconfirm_button.click()
    time.sleep(2)