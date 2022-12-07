from selenium.webdriver.common.by import By
from Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = Locators.Locators.username_textbox_name
        self.password_textbox_name = Locators.Locators.password_textbox_name
        self.login_button_xpath = Locators.Locators.login_button_xpath
        self.invalid_credentials_msg_xpath = Locators.Locators.invalid_msg_xpath

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_username(self, msg):
        return str(msg) == self.driver.find_element(By.XPATH, self.invalid_credentials_msg_xpath).text

    def check_invalid_password(self, msg):
        return str(msg) == self.driver.find_element(By.XPATH, self.invalid_credentials_msg_xpath).text