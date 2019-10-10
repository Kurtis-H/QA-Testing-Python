import unittest
from selenium import webdriver
from time import sleep

# Here's the last extra challenge.
#
# Requirement list.
# 1. Go to  https://www.youniqueproducts.com/products/view/US-51081-01
# 2. Add the item to the Cart
# 3. Go to the Cart
# 4. Validate the Cart Overview
#
# requirement 4 is vague but I would like a function that can return me any items in the list of values based on whatever, string is displayed.
# I would like requirement 4 to return me $5.50 if I request the value for Shipping:... ie: "assertEqual(' Shipping:', '$5.50').
# Make sure you make your function dynamic that it will work w/ any number of values.


class ChallengeEx4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_HW3(self):
        self.driver.get("https://www.youniqueproducts.com/products/view/US-51081-01")
        sleep(3)

        productAdd = self.driver.find_element_by_xpath("//*[@class='padTB1 addToCartWithQty']//*[@type='button']")
        cart = self.driver.find_element_by_id("miniCart-root")

        productAdd.click()
        sleep(1)

        cart.click()
        sleep(3)

        stuff1 = self.driver.find_elements_by_xpath("//tr[@class='totals groupRow']//*[@class='totalDisplay']")
        stuff2 = self.driver.find_element_by_xpath("//tr[@class='totals groupRow']//*[@class='totalDisplay bold pink-text']")
        array1 = []

        i = 0
        while i < len(stuff1):
            array1.append(stuff1[i].text)
            i += 1

        totalItems = array1[1]
        subtotal = stuff2.text
        tax = array1[2]
        shipping = array1[3]
        estimate = array1[4]

        self.assertEqual(shipping, '$5.50')


if __name__ == '__main__':
    unittest.main()
