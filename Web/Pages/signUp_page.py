
import allure
from selenium.webdriver.common.by import By

from Web.Locators.signUp_locators import SignUpLocators


class SignUpPage(SignUpLocators):
    def __init__(self, driver):
        self.driver = driver

    def sign_up_page(self):
        sign_up = self.driver.find_element(By.XPATH, self.sign_up_xpath)
        sign_up.click()
    @allure.step("enter valid user name as {0}")
    def sign_up_user_name(self, name):
        username = self.driver.find_element(By.ID, self.username_Id)
        username.clear()
        username.send_keys(name)

    def sign_up_user_password(self, password):
        passwords = self.driver.find_element(By.ID, self.password_Id)
        passwords.clear()
        passwords.send_keys(password)

    def click_sign_up_button(self):
        sign_up_button = self.driver.find_element(By.XPATH, self.sign_up_button_xpath)
        sign_up_button.click()



