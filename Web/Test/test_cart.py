import pytest
import allure
from time import sleep

from selenium.webdriver.common.by import By

from Web.Pages.cart_page import CartPage
from Web.base.test_base import TestBases


class TestCartPage(TestBases):
    @allure.description(" test cart with correct information")
    @pytest.mark.sanity
    def test_cart_page_validly(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        sleep(2)
        cart.click_ok_buttons()

    @allure.description("Empty user name test")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_name(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        alt = self.driver.switch_to.alert.text
        assert alt == "Please fill out Name and Creditcard."
        sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.description("empty country")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_country(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        # drive = self.driver.find_element(By.XPATH, "/html/body/div[10]/h2").text
        assert self.driver.title == "login"

    @allure.description("empty city")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_city(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "Login"

    @allure.description("empty card")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_credit_card(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty month")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_month(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("55553210256")
        cart.fill_month_to_purchase("")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty year")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_year(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("55553210256")
        cart.fill_month_to_purchase("september")
        cart.fill_year_to_purchase("")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty invalid year")
    @pytest.mark.sanity
    def test_cart_page_with_invalid_year(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("55553210256")
        cart.fill_month_to_purchase("september")
        cart.fill_year_to_purchase("120")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty invalid month")
    @pytest.mark.sanity
    def test_cart_page_with_invalid_month(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("55553210256")
        cart.fill_month_to_purchase("sep")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty invalid credit_card")
    @pytest.mark.sanity
    def test_cart_page_with_invalid_credit_card(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("po")
        cart.fill_month_to_purchase("september")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty invalid name")
    @pytest.mark.sanity
    def test_cart_page_with_invalid_name(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemen89")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("78524526")
        cart.fill_month_to_purchase("september")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty invalid city name")
    @pytest.mark.sanity
    def test_cart_page_with_city_name(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemen89")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("/*")
        cart.fill_credit_card_to_purchase("266699995632")
        cart.fill_month_to_purchase("september")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description("empty invalid country name")
    @pytest.mark.sanity
    def test_cart_page_with_country_name(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemen89")
        cart.fill_country_to_purchase("7*")
        cart.fill_city_to_purchase("gondar")
        cart.fill_credit_card_to_purchase("po")
        cart.fill_month_to_purchase("september")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
        assert self.driver.title == "STORE"

    @allure.description(" all empty field")
    @pytest.mark.sanity
    def test_cart_page_with_all_fields_empty(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("")
        cart.fill_country_to_purchase("")
        cart.fill_city_to_purchase("")
        cart.fill_credit_card_to_purchase("")
        cart.fill_month_to_purchase("")
        cart.fill_year_to_purchase("")
        cart.click_to_purchase()

        alt = self.driver.switch_to.alert.text
        assert alt == "Please fill out Name and Creditcard."
        self.driver.switch_to.alert.accept()

    @allure.description(" all empty field")
    @pytest.mark.sanity
    def test_cart_page_with_all_fields_empty_except_country(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("")
        cart.fill_country_to_purchase("")
        cart.fill_city_to_purchase("")
        cart.fill_credit_card_to_purchase("")
        cart.fill_month_to_purchase("")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()

        alt = self.driver.switch_to.alert.text
        assert alt == "Please fill out Name and Creditcard."
        self.driver.switch_to.alert.accept()
