import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, ctime


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_get_page(self):
        self.driver.get("https://www.copart.com")
        sleep(1)

        self.driver.find_element_by_id('input-search').is_displayed()

        self.driver.find_element_by_id('input-search').send_keys("Exotics")
        sleep(1)

        self.driver.find_element_by_id('input-search').send_keys(Keys.ENTER)
        sleep(1)

        assert self.driver.find_elements_by_xpath("//*[contains(text(),'PORSCHE')]")


if __name__ == '__main__':
    unittest.main()
