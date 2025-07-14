from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def run_test(driver):
    # 削除ボタンをクリック
    delete_button = driver.find_element(By.CLASS_NAME, "delete-button")
    delete_button.click()
    time.sleep(1)

    # アラートが表示されるのを最大5秒待つ
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        print(f"アラート検出: {alert.text}")
        alert.accept()
        print("✅ アラートを受け入れました。")
    except TimeoutException:
        print("⚠️ アラートが表示されなかったため、スキップします。")

    time.sleep(1)

    # 確認ボタンをクリック
    deleteconfirm_button = driver.find_element(By.CLASS_NAME, "confirmed-button")
    deleteconfirm_button.click()
    time.sleep(2)
