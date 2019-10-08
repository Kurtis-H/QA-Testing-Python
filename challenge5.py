import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Challenge 5 - If/Else/Switch
# For this challenge, go to https://www.copart.com and do a search for “porsche” and change the  drop down for “Show Entries” to 100 from 20.
# Count how many different models of porsche is in the results on the first page and return in the terminal how many of each type exists.
#
# Possible values can be “CAYENNE S”, “BOXSTER S”, etc.
#
# For the 2nd part of this challenge, create a switch statement to count the types of damages.
# Here’s the types:
# REAR END
# FRONT END
# MINOR DENT/SCRATCHES
# UNDERCARRIAGE
# And any other types can be grouped into one of MISC.


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/khook/PycharmProjects/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test(self):
        self.driver.get("https://www.copart.com")
        sleep(1)

        search = self.driver.find_element_by_id('input-search')

        search.is_displayed()

        search.send_keys("porsche")
        sleep(1)

        search.send_keys(Keys.ENTER)
        sleep(2)

        elem = self.driver.find_element_by_xpath('//select[@name="serverSideDataTable_length"]')

        elem.click()
        elem.send_keys("100")
        elem.send_keys(Keys.ENTER)
        elem.click()
        sleep(2)

        array1 = self.driver.find_elements_by_xpath('//tr[@class="odd"] | //tr[@class="even"]')
        array2 = self.driver.find_elements_by_xpath('//table//span[@data-uname="lotsearchLotmodel"]')
        array3 = self.driver.find_elements_by_xpath('//table//span[@data-uname="lotsearchLotdamagedescription"]')
        models = []
        damage = []
        rear = 0
        front = 0
        minor = 0
        under = 0
        misc = 0

        i = 0
        while i < len(array1):
            models.append(array2[i].text)
            damage.append(array3[i].text)
            i += 1

        uniqueModels = list(dict.fromkeys(models))
        modelsList = list(models)

        # print(len(models))
        print('----- Different Model Types -----')
        y = 0
        while y < len(uniqueModels):
            print(uniqueModels[y] + ': ' + str(modelsList.count(uniqueModels[y])))
            y += 1

        x = 0
        while x < len(array1):
            if 'REAR END' in damage[x]:
                rear += 1
            elif 'FRONT END' in damage[x]:
                front += 1
            elif 'MINOR DENT/SCRATCHES' in damage[x]:
                minor += 1
            elif 'UNDERCARRIAGE' in damage[x]:
                under += 1
            else:
                misc += 1

            x += 1
        print('----- Damage Types -----')
        print('REAR END: ' + str(rear))
        print('FRONT END: ' + str(front))
        print('MINOR DAMAGE: ' + str(minor))
        print('UNDERCARRIAGE: ' + str(under))
        print('MISC: ' + str(misc))


if __name__ == '__main__':
    unittest.main()
