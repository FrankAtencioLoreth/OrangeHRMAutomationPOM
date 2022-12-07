from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # config webdriver
        print("Test start")
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_01_login_valid(self):
        self.driver.implicitly_wait(10)
        loging = LoginPage(self.driver)
        loging.enter_username("Admin")
        loging.enter_password("admin123")
        loging.click_login_button()
        time.sleep(4)
        home = HomePage(self.driver)
        home.click_menu()
        time.sleep(4)
        home.click_logout()

    def test_02_login_invalid_username(self):
        self.driver.implicitly_wait(10)
        loging = LoginPage(self.driver)
        loging.enter_username("Admin123")
        loging.enter_password("admin123")
        time.sleep(4)
        loging.click_login_button()
        time.sleep(4)
        assert loging.check_invalid_username("Invalid credentials"), "Username is incorrect"
        time.sleep(5)

    def test_03_login_invalid_password(self):
        self.driver.implicitly_wait(10)
        loging = LoginPage(self.driver)
        loging.enter_username("Admin")
        loging.enter_password("admin1234")
        loging.click_login_button()
        assert loging.check_invalid_password("Invalid credentials"), "Password is incorrect"
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        print("Test finish")
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
