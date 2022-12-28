import unittest
from selenium import webdriver
import tests.latam_airlines_main_page_test as LatamAirlinesMainPageTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class GoogleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LatamAirlinesMainPageTest.LatamAirlinesMainPageTestCase('test_page_title'))
    suite.addTest(GoogleTestCase('test_page_title'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main(verbosity=2)
    # browser = webdriver.Chrome()
    # browser.get('http://www.yahoo.com/')
    # assert 'Yahoo' in browser.title

    # elem = browser.find_element(By.NAME, 'p')
    # elem.send_keys('seleniumhq' + Keys.RETURN)

    # browser.quit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
