import unittest
from selenium import webdriver
from time import sleep

# HW3:
# https://www.doterra.com/US/en/product-education-blends
# Figure out how many of the products have the word doTERRA in it, how may are DigestZens and how many fit into a misc category.
# This is the same as challenge 5.


class ChallengeEx1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_HW3(self):
        self.driver.get("https://www.doterra.com/US/en/product-education-blends")
        sleep(1)

        array1 = self.driver.find_elements_by_xpath("//*[@class='title']")
        text = []
        doterra = 0
        digestzen = 0
        misc = 0

        i = 0
        while i < len(array1):
            text.append(array1[i].text)
            i += 1

        x = 0
        while x < len(array1):
            if 'doTERRA' in text[x]:
                doterra += 1
            elif 'DigestZen' in text[x]:
                digestzen += 1
            else:
                misc += 1

            x += 1
        print('doTERRA - ' + str(doterra))
        print('DigestZen - ' + str(digestzen))
        print('Misc - ' + str(misc))


if __name__ == '__main__':
    unittest.main()



