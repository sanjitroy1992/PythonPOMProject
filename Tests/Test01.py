from selenium import webdriver
import unittest
import HtmlTestRunner
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Resources.TestData import TestData

class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.get(TestData.App_Url)
        cls.driver.maximize_window()

    def test_01_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(TestData.Username)
        login.enter_password(TestData.Password)
        login.click_login()

        time.sleep(2)
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

    def test_02_login_invalid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(TestData.Invalid_Username)
        login.enter_password(TestData.Password)
        login.click_login()
        msg = login.invalid_username()
        self.assertEqual(msg, TestData.Invalid_Credentials)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=TestData.HTML_Report_Path))