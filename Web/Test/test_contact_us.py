import time

import pytest
import allure

from Web.Pages.contactUs_page import ContactUsPage
from Web.base.test_base import TestBases


class TestContactUs(TestBases):
    @allure.description("contact us test validly")
    @pytest.mark.sanity
    def test_contact_us_validly(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("zemeneab86959t06@gmail.com")
        contactus.contact_us_with_name("Zemene Abinet")
        contactus.contact_us_with_send_message("This system looks like amazon it needs some improvement ")
        contactus.contact_us_page_send_message()
        time.sleep(1)

    @allure.description("contact us test with empty email")
    @pytest.mark.sanity
    def test_contact_us_with_empty_email(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("")
        contactus.contact_us_with_name("Zemene Abinet")
        contactus.contact_us_with_send_message("This system looks like amazon it needs some improvement ")
        contactus.contact_us_page_send_message()
        time.sleep(1)

    @allure.description("contact us test with empty username")
    @pytest.mark.sanity
    def test_contact_us_with_empty_username(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("zemeneabinet06@gmail.com")
        contactus.contact_us_with_name("")
        contactus.contact_us_with_send_message("This system looks like amazon it needs some improvement ")
        contactus.contact_us_page_send_message()
        time.sleep(1)

    @allure.description("contact us test with empty message box")
    @pytest.mark.sanity
    def test_contact_us_with_empty_message_box(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("zemeneabinet06@gmail.com")
        contactus.contact_us_with_name("Zemene Abinet")
        contactus.contact_us_with_send_message(" ")
        contactus.contact_us_page_send_message()
        time.sleep(1)

    @allure.description("contact us test with invalid message box")
    @pytest.mark.sanity
    def test_contact_us_with_invalid_message_box(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("zemeneabinet06@gmail.com")
        contactus.contact_us_with_name("Zemene Abinet")
        contactus.contact_us_with_send_message("5899ourfhg/*jvn xzjudgccxvxvvxvxvxvxvvvxvcvcvvcvcvcvvcvc ")
        contactus.contact_us_page_send_message()
        time.sleep(1)

    @allure.description("contact us test with invalid email")
    @pytest.mark.sanity
    def test_contact_us_with_invalid_email(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("zemeneabinet06mail.com")
        contactus.contact_us_with_name("Zemene Abinet")
        contactus.contact_us_with_send_message("You have a good humanity to the customers ")
        contactus.contact_us_page_send_message()
        time.sleep(2)

    @allure.description("contact us test with invalid email")
    @pytest.mark.sanity
    def test_contact_us_with_invalid_name(self):
        self.driver = super().init()
        contactus = ContactUsPage(self.driver)
        contactus.contact_us_page()
        contactus.contact_us_with_email("zemeneabinet06mail.com")
        contactus.contact_us_with_name("89*+9*")
        contactus.contact_us_with_send_message("You have a good humanity to the customers ")
        contactus.contact_us_page_send_message()
        time.sleep(2)