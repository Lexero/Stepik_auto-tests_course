import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('stepick', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestsStep:
    def test_guest_should_see_login_link(self, browser, stepick):
        link = f"https://stepik.org/lesson/{stepick}/step/1"
        browser.get(link)
        time.sleep(5)
        input = browser.find_element_by_css_selector(".textarea")
        answer = str(math.log(int(time.time())))
        input.send_keys(answer)
        time.sleep(1)
        browser.find_element_by_css_selector(".submit-submission").click()
        time.sleep(1)
        answer_good = browser.find_element_by_class_name("smart-hints__hint").text
        time.sleep(10)
        print(answer_good)
        assert answer_good == "Correct!", "Not our page"

