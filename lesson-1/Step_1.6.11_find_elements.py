from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first_block > div.form-group.first_class >input")
    input1.send_keys("Саня")
    input2 = browser.find_element_by_css_selector(".first_block >div.form-group.second_class >input")
    input2.send_keys("Петров")
    input3 = browser.find_element_by_css_selector(".first_block > div.form-group.third_class > input")
    input3.send_keys("Petrov@mail.ru")
    input4 = browser.find_element_by_css_selector(".second_block >div.form-group.first_class > input")
    input4.send_keys("+79000000000")
    input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Москва, Красная площадь, Д.1")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
