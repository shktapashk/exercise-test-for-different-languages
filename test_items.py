import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_ProductPage_contains_addToBasketButton(browser):
    browser.get(link)
    time.sleep(30)
    BasketButton = browser.find_elements_by_class_name("btn-add-to-basket")
    assert BasketButton, "кнопка не найдена"
    