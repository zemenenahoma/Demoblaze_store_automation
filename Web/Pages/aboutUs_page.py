from selenium.webdriver.common.by import By

from Web.Locators.aboutUsLocators import AboutUsLocators


class AboutUsPage(AboutUsLocators):
    def __init__(self, driver):
        self.driver = driver

    def about_us_page(self):
        about = self.driver.find_element(By.XPATH, self.about_us_page_xpath)
        about.click()

    def about_us_page_video(self):
        video = self.driver.find_element(By.XPATH, self.about_us_video_element_xpath)
        video.click()

    def about_us_page_video_maximize(self):
        video_maximaize = self.driver.find_element(By.XPATH, self.maximize_window)
        video_maximaize.click()
        video_maximaize.click()

    def stop_vidio(self):
        vid = self.driver.find_element(By.XPATH, self.stop_playing_xpath)
        vid.click()

    def sound_volume_silent(self):
        sond = self.driver.find_element(By.XPATH, self.sound_volume)
        sond.click()

    def close_videos(self):
        clos = self.driver.find_element(By.XPATH, self.close_vidio)
        clos.click()
