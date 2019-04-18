import unittest
from selenium import webdriver
from django.urls import resolve




class NewClientTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can(self):
        self.browser.get('http://127.0.01:8000/home/')
        self.assertIn("Привет,я Мира", self.browser.title)



if __name__ == '__main__':
    unittest.main(warnings='ignore')
