import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")   # Хорошая практика отметить в scope="function", хотя это и default значение
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.smoke
    @pytest.mark.skip  # этот маркер означает, что при прогоне этот тест будет скипнут
    def test_guest_should_see_login_link_skipped(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.xfail(reason="fixing this bug right now")  # С этим маркером тест выполнится, но если он не пройдет
    # проверку, то прогон все равно будет зеленым (можно использовать с известными багами, пока их чинят)
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

# чтобы запустить тест введи команду pytest -s -v -m smoke test_fixture5.py
# pytest -s -v -m "not smoke" test_fixture5.py - если хочешь запустить "не smoke" тесты (логическое НЕ)
# pytest -s -v -m "smoke or regression" test_fixture5.py - для запуска тестов с разными метками (логическое ИЛИ)
# pytest -s -v -m "regression and win10" test_fixture5.py - чтобы запустить тесты с несколькими метками (логическое И)
# pytest -rx -v test_fixture5.py запуск с подробной причиной ошибки при xfail из этого маркера (то что указано в скобках)
