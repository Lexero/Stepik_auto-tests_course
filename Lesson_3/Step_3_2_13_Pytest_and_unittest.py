from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.options import Options


def link_t(link):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    browser.find_element_by_css_selector(".first_block > div.form-group.first_class >input").send_keys("Саня")
    browser.find_element_by_css_selector(".first_block >div.form-group.second_class >input").send_keys("Петров")
    browser.find_element_by_css_selector(".first_block > div.form-group.third_class > input").send_keys(
        "Petrov@mail.ru")
    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class TestsStep(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "Test registration1 failed")

    def test_registration2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "Test registration2 failed")


if __name__ == "__main__":
    unittest.main()
