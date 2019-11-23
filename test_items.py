import time


def test_find_add_cart_button(browser):
    time.sleep(10)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), 'No button'

