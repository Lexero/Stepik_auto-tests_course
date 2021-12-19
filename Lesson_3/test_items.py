import time


def test_check_button_add_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    try:
        assert button
    except AssertionError:
        print("На странице нет кнопки")
