from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input3 = browser.find_element_by_class_name("form-control")
    input3.send_keys(y)

    option1 = browser.find_element_by_class_name("form-check-input")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    alert = browser.switch_to.alert
    print(alert.text)

    alert.accept()
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла