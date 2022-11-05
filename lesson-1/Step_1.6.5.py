import math
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
link = "http://suninjuly.github.io/find_link_text"

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    input666 = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    input666.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    alert = browser.switch_to.alert
    print(alert.text)

    alert.accept()
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
