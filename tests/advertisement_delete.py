from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import time
def run_test(driver):

    # 削除ボタンをクリック
    delete_button = driver.find_element(By.CLASS_NAME, "delete-button")
    delete_button.click()
    time.sleep(2)

    # JavaScriptのconfirmダイアログを受け取って「OK」を押す
    alert = Alert(driver)
    alert.accept()  # 「OK」を押す（「キャンセル」は alert.dismiss()
    time.sleep(2)

    deleteconfirm_button = driver.find_element(By.CLASS_NAME, "confirmed-button")
    deleteconfirm_button.click()
    time.sleep(2)
