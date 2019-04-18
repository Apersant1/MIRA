
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test(browser):
    browser.get('http://127.0.01:8000/home/')
    assert browser.title == 'Привет,я Мира'



