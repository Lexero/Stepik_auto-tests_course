import pytest
from selenium import webdriver
import time
import math

final = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(final)


@pytest.mark.parametrize('stepick', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestsStep:
    def test_guest_should_see_login_link(self, browser, stepick):
        global final
        link = f"https://stepik.org/lesson/{stepick}/step/1"
        browser.implicitly_wait(10)
        browser.get(link)
        answer = str(math.log(int(time.time())))
        input = browser.find_element_by_css_selector(".textarea")
        input.send_keys(answer)
        browser.find_element_by_css_selector(".submit-submission").click()
        answer_good = browser.find_element_by_class_name("smart-hints__hint").text
        try:
            assert 'Correct!' == answer_good
        except AssertionError:
            final += answer_good
