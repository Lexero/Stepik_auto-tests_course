from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    find_num1 = browser.find_element_by_id("num1")
    num1 = find_num1.text
    find_num2 = browser.find_element_by_id("num2")
    num2 = find_num2.text
    summa = (str(int(num1)+int(num2)))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summa)
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    alert = browser.switch_to.alert
    print(alert.text)

    alert.accept()
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
