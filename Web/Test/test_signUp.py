import time

import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Web.Pages.signUp_page import SignUpPage
from Web.base.test_base import TestBases


# @allure.severity(allure.severity_level.CRITICAL)
class TestSignUp(TestBases):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("test valid information")
    @pytest.mark.sanity
    def test_sign_up(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()
        sign_up.sign_up_user_name("zemeneabinet06@gmail.com")
        sign_up.sign_up_user_password("nm182551")
        sign_up.click_sign_up_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")

        assert alt == "Please fill all the registration forms"

        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("test empty user name")
    @pytest.mark.sanity
    def test_sign_up_with_empty_username(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()
        time.sleep(4)
        sign_up.sign_up_user_name("")
        time.sleep(4)
        sign_up.sign_up_user_password("7820315429")
        time.sleep(4)
        sign_up.click_sign_up_button()
        time.sleep(4)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")
        assert alt == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("test empty password")
    @pytest.mark.sanity
    def test_sign_up_with_empty_password(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()
        sign_up.sign_up_user_name("nahom1221@gmail.com")
        sign_up.sign_up_user_password("")
        sign_up.click_sign_up_button()
        time.sleep(2)
        we = self.driver.switch_to.alert.text
        assert we == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Invalid email")
    @pytest.mark.sanity
    def test_sign_up_with_invalid_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("nahom1221mail.com")

        sign_up.sign_up_user_password("jhkhhbbh")

        sign_up.click_sign_up_button()
        time.sleep(2)
        we = self.driver.switch_to.alert.text
        assert we == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Invalid password")
    @pytest.mark.sanity
    def test_sign_up_with_invalid_password(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("nahom1221@gmail.com")

        sign_up.sign_up_user_password("08")

        sign_up.click_sign_up_button()
        time.sleep(1)
        alt = self.driver.switch_to.alert.text
        assert alt == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Invalid password and email")
    @pytest.mark.sanity
    def test_sign_up_with_invalid_password_and_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("nahom122mail.com")

        sign_up.sign_up_user_password("0/")

        sign_up.click_sign_up_button()
        time.sleep(1)
        dm = self.driver.switch_to.alert.text
        assert dm == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Empty password and email")
    @pytest.mark.sanity
    def test_sign_up_with_empty_password_and_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("")

        sign_up.sign_up_user_password("0/")

        sign_up.click_sign_up_button()
        time.sleep(1)

        dm = self.driver.switch_to.alert.text

        assert dm == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("empty password and invalid email")
    @pytest.mark.sanity
    def test_sign_up_with_empty_password_and_invalid_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("zkmfho@gmal.com")

        sign_up.sign_up_user_password("")

        sign_up.click_sign_up_button()
        time.sleep(1)

        dm = self.driver.switch_to.alert.text

        assert dm == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("invalid password and empty email")
    @pytest.mark.sanity
    def test_sign_up_with_invalid_password_and_empty_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("zkmfho@gmal.com")

        sign_up.sign_up_user_password("")

        sign_up.click_sign_up_button()

        time.sleep(1)

        dm = self.driver.switch_to.alert.text
        assert dm == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("invalid password and invalid email")
    @pytest.mark.sanity
    def test_sign_up_with_invalid_password_and_invalid_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("zkmfho@gmal.com")

        sign_up.sign_up_user_password("44kdjfhhhf")

        sign_up.click_sign_up_button()

        time.sleep(1)

        dm = self.driver.switch_to.alert.text
        assert dm == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("invalid password and empty email")
    @pytest.mark.sanity
    def test_sign_up_with_empty_password_and_empty_email(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("")

        sign_up.sign_up_user_password("")

        sign_up.click_sign_up_button()

        time.sleep(1)

        dm = self.driver.switch_to.alert.text
        assert dm == "Please fill out all the registration forms"
        self.driver.switch_to.alert.accept()
