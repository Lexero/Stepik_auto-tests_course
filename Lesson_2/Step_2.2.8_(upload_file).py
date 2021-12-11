from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    input1 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div/input[Lesson_3]")
    input3.send_keys("ibba@mail.ru")
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    path = os.getcwd() + '/' + file.name
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(path)

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
