from selenium.webdriver.common.by import By
import time

def run_test(driver):

    time.sleep(3)



    header_link = driver.find_element(By.XPATH, "//a[@href='MyPageServlet']")
    header_link.click()
    time.sleep(4)

    list_link = driver.find_element(By.XPATH, "//a[@href='ListViewServlet']")
    list_link.click()
    time.sleep(4)





    def collect_forms():
        forms = driver.find_elements(
            By.XPATH,
            "//form[input[@type='hidden' and @name='List_No']]"
        )

        form_info = []
        for form in forms:
            list_no_input = form.find_element(By.XPATH, ".//input[@type='hidden' and @name='List_No']")
            list_no = int(list_no_input.get_attribute("value"))
            form_info.append((list_no, form))  # ボタンではなく form を返す
        form_info.sort(key=lambda x: x[0])
        return form_info

    # 最初の一覧収集
    form_list = collect_forms()

    for List_no, form in form_list:
        print(f"Submitting List_No: {List_no}")
        form.submit()  # ← ここで form を直接 submit する
        time.sleep(3)

        driver.back()  # 戻る
        time.sleep(3)

        # ページが変わるので再取得
        form_list = collect_forms()
