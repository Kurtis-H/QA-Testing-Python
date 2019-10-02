import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_get_page(self):
        self.driver.get("https://www.copart.com")
        sleep(3)

        array1 = self.driver.find_elements_by_xpath("//*[@ng-if = 'popularSearches']//li//a")
        print(len(array1))

        i = 0
        while i < len(array1):
            print(array1[i].text + " - " + array1[i].get_attribute('href'))
            i += 1


if __name__ == '__main__':
    unittest.main()