import unittest
from time import sleep
from selenium import webdriver

# Challenge 3 - Loops:
# Loops can be used to write your own wait statements.
# They can also be used to iteration through a list of items.
#
# For this challenge, go to copart and print a list of all the “Popular Items” of vehicle Make/Models on the home page and the URL/href for each type.
# This list can dynamically change depending on what is authored by the content creator but using a loop will make sure that everything will be displayed regardless of the list size.
#
# Your output in the console would look like:
# IMPREZA - https://www.copart.com/popular/model/impreza
# CAMRY - https://www.copart.com/popular/model/camry
# ELANTRA - https://www.copart.com/popular/model/elantra
# SONATA - https://www.copart.com/popular/model/sonata
# COROLLA - https://www.copart.com/popular/model/corolla
# ALTIMA - https://www.copart.com/popular/model/altima
# FORESTER - https://www.copart.com/popular/model/forester
# OPTIMA - https://www.copart.com/popular/model/optima
# IMPALA - https://www.copart.com/popular/model/impala
# PRIUS - https://www.copart.com/popular/model/prius
# FORD - https://www.copart.com/popular/make/ford
# TOYOTA - https://www.copart.com/popular/make/toyota
# CHEVROLET - https://www.copart.com/popular/make/chevrolet
# DODGE - https://www.copart.com/popular/make/dodge
# HONDA - https://www.copart.com/popular/make/honda
# NISSAN - https://www.copart.com/popular/make/nissan
# SUBARU - https://www.copart.com/popular/make/subaru


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