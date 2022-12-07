class Locators:

    # Login page objects
    username_textbox_name = "username"
    password_textbox_name = "password"
    login_button_xpath = "//button[@type='submit']"
    invalid_msg_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"

    # Home page objects
    menu_xpath = "//div[@id='app']/descendant::header/descendant::div[3]/descendant::span"
    logout_xpath = "//div[@id='app']/descendant::header/descendant::div[3]/descendant::ul[2]/descendant::li[4]"
