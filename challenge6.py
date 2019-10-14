import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyscreenshot


# Challenge 6 - Error Handling
# Using a try/catch block can help you catch certain errors that might exist that you weren’t anticipating.
# It can also give you some type of behavior you want to take when something happens.
#
# Let’s say you are running a test script and the 4th step fails.
# At this point, you can decide what you want it to do.
# Do you want to try something else, or take a screenshot, or reset your browser of where you are at for the next step in the script?
#
# Taking a screenshot is a common way to use the try catch block.
# For this challenge, go to copart site, search for nissan, and then for the model, search for “skyline”.
# This is a rare car that might or might not be in the list for models.
# When the link does not exist to click on, your script will throw an exception.
# Catch the exception and take a screenshot of the page of what it looks like.


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_get_page(self):
        self.driver.get("https://www.copart.com")
        sleep(1)

        self.driver.find_element_by_id('input-search').is_displayed()

        self.driver.find_element_by_id('input-search').send_keys("nissan")
        sleep(1)

        self.driver.find_element_by_id('input-search').send_keys(Keys.ENTER)
        sleep(1)

        self.driver.find_element_by_xpath('//*[@data-uname="ModelFilter"]').click()
        sleep(1)

        try:
            self.driver.find_element_by_xpath('(//input[@placeholder="Search"])[4]').send_keys("skyline")
            sleep(1)

            self.driver.find_element_by_xpath('//*[@value="Skyline"][@name="MODL"]').click()
            sleep(1)
        except Exception:
            print("Skyline element does not exist")
            pyscreenshot.grab()


if __name__ == '__main__':
    unittest.main()
