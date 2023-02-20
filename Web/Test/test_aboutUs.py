import time

import pytest
import allure

from Web.Pages.aboutUs_page import AboutUsPage
from Web.base.test_base import TestBases


class TestAboutUsPage(TestBases):
    @allure.description("about us test ")
    @pytest.mark.sanity
    def test_about_us_page(self):
        self.driver = super().init()
        about = AboutUsPage(self.driver)
        time.sleep(1)
        about.about_us_page()
        time.sleep(1)
        about.about_us_page_video()
        time.sleep(2)
        about.about_us_page_video_maximize()
        time.sleep(3)
        about.stop_vidio()
        time.sleep(3)
        about.sound_volume_silent()
        time.sleep(5)
        about.close_videos()
        assert self.driver.title == "STORE"
