from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def run_test(driver):
    wait = WebDriverWait(driver, 10)

    time.sleep(3)

    # driver.find_element(By.LINK_TEXT, "広告管理").click()
    # time.sleep(2)
    # driver.find_element(By.LINK_TEXT, "広告情報一覧").click()
    # time.sleep(3)

    # --- ページ遷移後、「変更」ボタンの1つ目が表示されるまで待つ
    edit_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirmed-button")))

    # 一番上の広告の「変更」ボタンをクリック
    edit_buttons = driver.find_elements(By.CLASS_NAME, "confirmed-button")
    edit_buttons[0].click()
    time.sleep(2)

    # === 説明文の上書き ===
    text_input = driver.find_element(By.ID, "ad-text")
    text_input.clear()
    text_input.send_keys("夏のセール実施中！全商品30％オフ！")
    time.sleep(3)

    # === 画像アップロード ===
    image_path = r"C:\Users\st20224116\Desktop\selenium\images\30off.png"
    assert os.path.exists(image_path), "画像ファイルが見つかりません"
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys(image_path)
    time.sleep(3)

    # === 「変更」ボタンをクリック ===
    driver.find_element(By.CLASS_NAME, "confirmed-button").click()
    time.sleep(3)

    
    # モーダルが表示されるまで最大10秒待機
    wait = WebDriverWait(driver, 10)
    # モーダルが表示されたことを確認
    wait.until(EC.visibility_of_element_located((By.ID, "completionModal")))
    # 「閉じる」ボタンをクリック
    close_button = driver.find_element(By.XPATH, "//div[@id='completionModal']//button[contains(text(), '閉じる')]")
    close_button.click()

    time.sleep(3)

