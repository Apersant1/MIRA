
import pytest
from django.urls import resolve
from django.test import TestCase
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test(browser):
    browser.get('http://127.0.01:8000/home/')
    assert browser.title == 'Привет,я Мира'

class HomePageTest(TestCase):
    def Test_When_open_home_page(self):
        response = self.client.get('/home/')
        self.assertTemplateUsed(response, "home/home.html")



