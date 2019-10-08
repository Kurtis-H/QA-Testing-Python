import unittest
from selenium import webdriver
from time import sleep

# HW2:
# Validate all the URLs in the footer


class ChallengeEx1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_HW2(self):
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")
        sleep(1)

        array1 = self.driver.find_elements_by_xpath("//*[@class='footer__links__groups']//a")
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
                sleep(1)
                # self.assertIn(href[x], self.driver.current_url)
                self.assertTrue('page-notFound' in self.driver.page_source)
                # print(text[x] + " - " + href[x] + ' - Passed')
                print(text[x] + " - " + href[x] + ' - FAILED')

            except Exception:
                print(text[x] + " - " + href[x] + ' - Passed')
                # print(text[x] + " - " + href[x] + ' - FAILED')
            x += 1


if __name__ == '__main__':
    unittest.main()