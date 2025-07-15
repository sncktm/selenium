from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def run_test(driver):
    time.sleep(3)
    # 一覧画面：2番目の削除ボタンをクリック
    delete_buttons = driver.find_elements(By.CLASS_NAME, "delete-button")
    if len(delete_buttons) < 2:
        print("⚠️ 2個目の削除ボタンが見つかりません。")
        return

    # JavaScriptで2個目をクリック（onclickが発火しない問題を回避）
    driver.execute_script("arguments[0].click();", delete_buttons[1])
    print("🖱️ 2個目の削除ボタンをクリックしました。")

    # --- 詳細画面の削除フォームのボタンを待機
    try:
        delete_confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form#deleteForm button.delete-button"))
        )
        print("✅ 詳細画面の削除ボタンを検出しました。クリックします。")
        delete_confirm_button.click()
    except TimeoutException:
        print("❌ 詳細画面の削除ボタンが表示されませんでした。")
        return
    time.sleep(3)
    # --- JavaScriptアラートが表示されたら受け入れる
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        print(f"⚠️ アラート検出: {alert.text}")
        alert.accept()
        print("✅ アラートを受け入れました。")
    except TimeoutException:
        print("⚠️ アラートが表示されなかったため、スキップします。")

    time.sleep(3)
     # モーダルが表示されるまで最大10秒待機
    wait = WebDriverWait(driver, 10)
    # モーダルが表示されたことを確認
    wait.until(EC.visibility_of_element_located((By.ID, "completionModal")))
    # 「閉じる」ボタンをクリック
    close_button = driver.find_element(By.XPATH, "//div[@id='completionModal']//button[contains(text(), '閉じる')]")
    close_button.click()

    time.sleep(3)