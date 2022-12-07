from selenium.webdriver.common.by import By
from Locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.menu_xpath = Locators.Locators.menu_xpath
        self.logout_xpath = Locators.Locators.logout_xpath

    def click_menu(self):
        self.driver.find_element(By.XPATH, self.menu_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
