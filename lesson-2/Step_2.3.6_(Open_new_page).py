from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def calc(f):
    return str(math.log(abs(12 * math.sin(int(f)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

finally:
    alert = browser.switch_to.alert
    print(alert.text)

    alert.accept()
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
