import unittest
from selenium import webdriver
from time import sleep

# HW1:
# https://www.doterra.com/US/en/using-essential-oils
# There is a section on the homepage ( Here are the 10 most popular essential oils: ) that has a URL that goes to a dead page.


class ChallengeEx1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_HW1(self):
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")
        sleep(1)

        array1 = self.driver.find_elements_by_xpath("//div[@id='long-form-text']//ol//li//a")
        text = []
        href = []

        i = 0
        while i < len(array1):
            text.append(array1[i].text)
            href.append(array1[i].get_attribute('href'))
            i += 1

        x = 0
        while x < len(array1):
            try:
                self.driver.get(href[x])
                test = self.driver.find_element_by_xpath("//*[@itemprop='name']")

                try:
                    self.assertTrue(text[x] != test.get_attribute('content'))
                    print(text[x] + " - " + href[x] + ' - Passed')
                except False:
                    print(text[x] + " - " + href[x] + ' - FAILED')
            except Exception:
                print(text[x] + " - " + href[x] + ' - FAILED')
            x += 1


if __name__ == '__main__':
    unittest.main()
