import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(f):
    return str(math.log(abs(12 * math.sin(int(f)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()

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
