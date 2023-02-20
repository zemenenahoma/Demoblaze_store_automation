from selenium.webdriver.common.by import By
from Web.Locators.login_locator import Locators


class LoginPages(Locators):
    def __init__(self, driver):
        self.driver = driver

    def click_on_login_text(self):
        tru = self.driver.find_element(By.XPATH, self.login_text)
        tru.click()

    def set_user_name(self, username):
        user_name_txt = self.driver.find_element(By.ID, self.login_user_name)
        user_name_txt.clear()
        user_name_txt.send_keys(username)

    def set_user_password(self, password):
        user_password_txt = self.driver.find_element(By.ID, self.login_user_password)
        user_password_txt.clear()
        user_password_txt.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
