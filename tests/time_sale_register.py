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
    wait = WebDriverWait(driver, 20) # 待機時間を少し長めに設定 (念のため)
 
    # モーダルが表示されていない状態になるまで待つ
    try:
        wait.until(EC.invisibility_of_element((By.ID, "completionModal")))
        print("✅ completionModal が閉じました。")
    except:
        print("⚠️ モーダルが閉じなかったため、JavaScriptで強制的に閉じます。")
        driver.execute_script("document.getElementById('completionModal').style.display='none'")
    time.sleep(2) # モーダル閉鎖後の待機
 
    # すでにログイン・遷移済み前提（main.pyで対応）
 
    print("--- タイムセール登録テスト開始 ---")
 
    # 「タイムセール管理」リンクをクリック
    print("「タイムセール管理」をクリックします。")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "タイムセール管理"))).click()
    time.sleep(3) # 画面遷移の待機
 
    # 「タイムセール登録」リンクをクリック
    print("「タイムセール登録」をクリックします。")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "タイムセール登録"))).click()
    time.sleep(3) # 画面遷移の待機
 
    # タイムセール名を入力
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ts_name = f"TEST_{timestamp}_AUTO"
    print(f"設定するタイムセール名: {ts_name}")
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(ts_name)
    time.sleep(2) # 入力後の待機
 
    # 「？」ボタンをクリック（ツールチップ表示確認）
    print("「？」ボタンをクリックしてツールチップを表示します。")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tooltip2"))).click()
    time.sleep(3) # ツールチップ表示の待機
 
    # 適用チェックボックスの状態を確認し、チェックを入れる
    print("「適用」チェックボックスを確認し、チェックを入れます。")
    checkbox = driver.find_element(By.ID, "timesale_Application_Flag")
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(2) # チェックボックス操作の待機
 
    # --- 日付の入力 (2025/01/01 から 2025/12/31 に固定) ---
    print("開始日: 2025/01/01, 終了日: 2025/12/31 を設定します。")         # ここに "00" を追加します   
    formatted_start = "00" + "2025/01/01"   
    formatted_end = "00" + "2025/12/31"    
    start_date_input = driver.find_element(By.NAME, "start_date")    
    start_date_input.clear()   
    start_date_input.send_keys(formatted_start, Keys.TAB) # formatted_start を使用   
    time.sleep(1) # 入力後の待機    
    end_date_input = driver.find_element(By.NAME, "end_date")
    end_date_input.clear()
    end_date_input.send_keys(formatted_end, Keys.TAB) # formatted_end を使用
    time.sleep(1) # 入力後の待機 
    print(f"✅ 日付入力完了: 開始日 '{formatted_start}', 終了日 '{formatted_end}'")
    time.sleep(2)
 
    # --- 繰り返し設定と曜日の選択 ---
    print("繰り返し設定を「毎週」にし、水、木、金曜日を選択します。")
    Select(driver.find_element(By.NAME, "repeat")).select_by_value("weekly")
    time.sleep(1) # ドロップダウン選択後の待機
 
    # 水曜日
    wednesday = driver.find_element(By.XPATH, "//input[@name='days' and @value='wednesday']")
    if not wednesday.is_selected():
        wednesday.click()
        print("水曜日をチェックしました。")
    time.sleep(1)
 
    # 木曜日
    thursday = driver.find_element(By.XPATH, "//input[@name='days' and @value='thursday']")
    if not thursday.is_selected():
        thursday.click()
        print("木曜日をチェックしました。")
    time.sleep(1)
 
    # 金曜日
    friday = driver.find_element(By.XPATH, "//input[@name='days' and @value='friday']")
    if not friday.is_selected():
        friday.click()
        print("金曜日をチェックしました。")
    time.sleep(2) # 曜日選択後の待機
 
    # --- 時間設定 (00:00 から 23:59 に固定) ---
    print("開始時間: 00:00, 終了時間: 23:59 を設定します。")
   
    start_time_input = driver.find_element(By.NAME, "start_time")
    start_time_input.clear()
    start_time_input.send_keys("00:00", Keys.TAB)
    time.sleep(1) # 入力後の待機
 
    end_time_input = driver.find_element(By.NAME, "end_time")
    end_time_input.clear()
    end_time_input.send_keys("23:59", Keys.TAB)
    time.sleep(1) # 入力後の待機
    print("✅ 時間設定完了")
    time.sleep(2)
 
    # 商品設定（3つ）
    print("商品を3つ設定します。")
    for i in range(3):
        jan = f"000000000000{i+1}" # 例: 0000000000001, 0000000000002, 0000000000003
        price = "150"
       
        jan_code_input = wait.until(EC.visibility_of_element_located((By.ID, f"jan_Code{i}")))
        jan_code_input.send_keys(jan, Keys.ENTER)
        print(f"商品 {i+1} のJANコード {jan} を入力しました。")
        time.sleep(2) # JANコード入力後の待機
 
        time_sales_price_input = wait.until(EC.visibility_of_element_located((By.ID, f"time_Sales_Prise{i}")))
        time_sales_price_input.send_keys(price)
        print(f"商品 {i+1} のタイムセール価格 {price} を入力しました。")
        time.sleep(2) # 価格入力後の待機
 
    # 確認ボタンをクリック
    print("「確認」ボタンをクリックします。")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.confirmed-button"))).click()
    time.sleep(3) # 確認画面への遷移待機
 
    # 最終確認ボタンを2回押す
    print("最終確認ボタンを2回クリックして登録を完了します。")
    for i in range(2):
        confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.confirmed-button")))
        confirm_button.click()
        print(f"最終確認ボタン {i+1} 回目をクリックしました。")
        time.sleep(3) # クリック後の待機
 
    print("✅ タイムセール登録完了")
    print("--- タイムセール登録テスト終了 ---")