import random
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector

def get_data_from_mysql():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="mysql",
            database="purchasing_support_system_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT JAN_code FROM sales")
        rows = cursor.fetchall()
        print("MySQLデータベースから取得したJANコード:")
        for row in rows:
            print(f"JANコード: {row[0]}")
        return [row[0] for row in rows]
    except mysql.connector.Error as err:
        print(f"MySQLデータベースエラー: {err}")
        return []
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQLデータベース接続を閉じました。")

def run_test(driver):
    wait = WebDriverWait(driver, 20)

    driver.maximize_window()
    driver.get("http://localhost:8080/PurchasingSupportStoreSystem/StoreLogin.jsp")

    input_element = driver.find_element(By.CLASS_NAME, "group")
    input_element.click()
    driver.find_element(By.ID, "no").send_keys("000001")
    driver.find_element(By.ID, "pass").send_keys("abcd")
    driver.find_element(By.CLASS_NAME, "confirmed-button").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "タイムセール管理").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "タイムセール登録").click()
    wait.until(EC.visibility_of_element_located((By.ID, "name")))
    print("タイムセール登録画面に遷移し、要素がロードされました。")

    ts_name = f"TEST_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    print(f"設定するタイムセール名: {ts_name}")
    driver.find_element(By.ID, "name").send_keys(ts_name)

    driver.find_element(By.CLASS_NAME, "tooltip2").click()
    checkbox = driver.find_element(By.ID, "timesale_Application_Flag")
    if not checkbox.is_selected():
        checkbox.click()

    today = datetime.now().date()
    start_date = today + timedelta(days=random.randint(0, 365))
    end_date = start_date + timedelta(days=random.randint(0, 30))
    formatted_start_date = "00" + start_date.strftime("%Y/%m/%d")
    formatted_end_date = "00" + end_date.strftime("%Y/%m/%d")

    driver.find_element(By.NAME, "start_date").send_keys(formatted_start_date, Keys.TAB)
    driver.find_element(By.NAME, "end_date").send_keys(formatted_end_date, Keys.TAB)

    Select(driver.find_element(By.NAME, "repeat")).select_by_value("weekly")
    wed_checkbox = driver.find_element(By.XPATH, "//input[@name='days' and @value='wednesday']")
    if not wed_checkbox.is_selected():
        wed_checkbox.click()

    now = datetime.now()
    driver.find_element(By.NAME, "start_time").send_keys(now.strftime("%H:%M"), Keys.TAB)
    driver.find_element(By.NAME, "end_time").send_keys((now + timedelta(minutes=120)).strftime("%H:%M"), Keys.TAB)

    all_jan_codes = get_data_from_mysql()
    selected_jan_codes = random.sample(all_jan_codes, min(len(all_jan_codes), 3))
    print(f"選択されたJANコード: {selected_jan_codes}")

    for i, jan in enumerate(selected_jan_codes):
        jan_input = wait.until(EC.element_to_be_clickable((By.ID, f"jan_Code{i}")))
        jan_input.send_keys(jan, Keys.ENTER)
        price_input = wait.until(EC.element_to_be_clickable((By.ID, f"time_Sales_Prise{i}")))
        price_input.send_keys("150")
        time.sleep(1)

    # 確認→確定→確定
    driver.find_element(By.CSS_SELECTOR, "button.btn.confirmed-button").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.confirmed-button"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.confirmed-button"))).click()

if __name__ == "__main__":
    chrome_driver_path = r"C:\Users\st20224137\Documents\Selenium\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        run_test(driver)
    finally:
        driver.quit()
