# tests/time_sale_register.py
import random
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test(driver):
    wait = WebDriverWait(driver, 10)

    # モーダルが表示されていない状態になるまで待つ
    try:
        wait.until(EC.invisibility_of_element((By.ID, "completionModal")))
        print("✅ completionModal が閉じました。")
    except:
        print("⚠️ モーダルが閉じなかったため、JavaScriptで強制的に閉じます。")
        driver.execute_script("document.getElementById('completionModal').style.display='none'")

    # すでにログイン・遷移済み前提（main.pyで対応）

    # 「タイムセール登録」クリック

    time.sleep(3)
    
    driver.find_element(By.LINK_TEXT, "タイムセール管理").click()

    time.sleep(3)

    driver.find_element(By.LINK_TEXT, "タイムセール登録").click()
    time.sleep(2)

    # タイムセール名
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ts_name = f"TEST_{timestamp}"
    print(f"設定するタイムセール名: {ts_name}")
    driver.find_element(By.ID, "name").send_keys(ts_name)
    time.sleep(1)

    # 「？」クリック
    driver.find_element(By.CLASS_NAME, "tooltip2").click()
    time.sleep(1)

    # 適用チェック
    checkbox = driver.find_element(By.ID, "timesale_Application_Flag")
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(1)

    # 日付の入力
    today = datetime.now().date()
    start_date = today + timedelta(days=random.randint(0, 365))
    end_date = start_date + timedelta(days=random.randint(0, 30))
    formatted_start = "00" + start_date.strftime("%Y/%m/%d")
    formatted_end = "00" + end_date.strftime("%Y/%m/%d")

    driver.find_element(By.NAME, "start_date").clear()
    driver.find_element(By.NAME, "start_date").send_keys(formatted_start, Keys.TAB)
    driver.find_element(By.NAME, "end_date").clear()
    driver.find_element(By.NAME, "end_date").send_keys(formatted_end, Keys.TAB)
    print("日付入力完了")

    # 繰り返しと曜日
    Select(driver.find_element(By.NAME, "repeat")).select_by_value("weekly")
    wednesday = driver.find_element(By.XPATH, "//input[@name='days' and @value='wednesday']")
    if not wednesday.is_selected():
        wednesday.click()
    time.sleep(1)

    # 時間設定
    now = datetime.now()
    start_time = now.strftime("%H:%M")
    end_time = (now + timedelta(minutes=120)).strftime("%H:%M")
    driver.find_element(By.NAME, "start_time").clear()
    driver.find_element(By.NAME, "start_time").send_keys(start_time, Keys.TAB)
    driver.find_element(By.NAME, "end_time").clear()
    driver.find_element(By.NAME, "end_time").send_keys(end_time, Keys.TAB)

    # 商品設定（3つ）
    for i in range(3):
        jan = f"000000000000{i+1}"
        price = "150"
        driver.find_element(By.ID, f"jan_Code{i}").send_keys(jan, Keys.ENTER)
        time.sleep(1)
        driver.find_element(By.ID, f"time_Sales_Prise{i}").send_keys(price)

    # 確認ボタン
    driver.find_element(By.CSS_SELECTOR, "button.btn.confirmed-button").click()

    # 最終確認ボタンを2回押す
    for i in range(2):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.confirmed-button")))
        driver.find_element(By.CSS_SELECTOR, "button.button.confirmed-button").click()
        time.sleep(1)

    print("✅ タイムセール登録完了")
