import unittest
from selenium import webdriver
from time import sleep

# Challenge 7 - Array/Dictionary.
# One mistake that many people make is for writing automation is making their script/objects too static.
# This causes a maintenance nightmare when you have 1000 tests that needs to be updated when a value changes or locators change.
# This also posed a challenge when there are multiple languages involved but the page layout stays the same or if the list of elements grows or shrinks.
# Arrays are great to use to create a virtual layout/map on navigation objects like a top menu or multiple links in the footer.
# Rather than locating only one link, why not build a map of all the links on a certain section.
# For this challenge, take a look at https://www.copart.com main page.
# Go to the Makes/Models section of the page.
# Create a 2 dimensional array that stores all the values displayed on the page along w/ the URL for that link.
# Once you have this array, you can verify all the elements in the array navigates to the correct page.
# To get started, inspect the code and notice the section of the page is built using angular.
# There is no static id or element class that identifies each element in this section.
# Everything is generic.
# The only way to build a function/object for this section is to loop through each element.
# Hint: xpath is easiest.


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_get_page(self):
        self.driver.get("https://www.copart.com")
        sleep(1)

        xpath1 = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//li")
        xpath2 = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//li/a")

        array2 = []

        i = 0
        while i < len(xpath1):
            array2.append(xpath1[i].text)
            array2.append(xpath2[i].get_attribute('href'))

            i += 1

        x = 0
        y = 1
        while y < len(xpath1):
            self.driver.get(array2[y])
            sleep(1)

            if array2[x] in self.driver.find_element_by_xpath("//span[@data-uname='lotsearchLotmodel']").text:
            # if "kurtis" in self.driver.find_element_by_xpath("//span[@data-uname='lotsearchLotmodel']").text:
                print(array2[x] + ": Passed")

            else:
                print(array2[x] + ": has Failed")

            x += 2
            y += 2


if __name__ == '__main__':
    unittest.main()