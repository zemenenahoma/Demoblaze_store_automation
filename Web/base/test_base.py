from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestBases:
    driver = webdriver.Chrome()

    def init(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.demoblaze.com/ ")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        return self.driver

    def teardown(self):
        self.driver.quit()
