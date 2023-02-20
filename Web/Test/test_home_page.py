import pytest
import allure

from Web.Pages.homepage import HomePage
from Web.base.test_base import TestBases


class TestHomepage(TestBases):
    @allure.description("home end to end test ")
    @pytest.mark.sanity
    def test_homepage(self):
        self.driver = super().init()
        home = HomePage(self.driver)
        home.log_check()
        home.category_phone()
        home.samsung_click()
        home.samsung_add_cart()
        home.category_laptop()
        home.del_laptop_click()
        home.del_lap_top_add_cart()
        home.category_monitor()
        home.apple_monitor()
        home.apple_monitor_add_to_card()
        home.goto_cart_page_to_fill_forms()




