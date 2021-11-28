from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    find_valuex = browser.find_element_by_id("treasure")
    x = find_valuex.get_attribute("valuex")
    y = calc(x)

    input3 = browser.find_element_by_id("answer")
    input3.send_keys(y)

    option1 = browser.find_element_by_class_name("check-input")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button.click()

finally:
    alert = browser.switch_to.alert
    print(alert.text)

    alert.accept()
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла