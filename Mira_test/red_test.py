

from selenium import webdriver


def test():
    browser = webdriver.Chrome()
    browser.get('http://127.0.01:8000/home/')
    print(browser.title)
    assert browser.title == 'Привет,я Мира'



