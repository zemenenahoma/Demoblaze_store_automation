from Web.Locators.contact_locators import ContactUsLocators
from selenium.webdriver.common.by import By


class ContactUsPage(ContactUsLocators):

    def __init__(self, driver):
        self.driver = driver

    def contact_us_page(self):
        contact = self.driver.find_element(By.XPATH, self.contact_us_xpath)
        contact.click()

    def contact_us_with_email(self, email):
        emails = self.driver.find_element(By.ID, self.contact_email_id)
        emails.send_keys(email)

    def contact_us_with_name(self, name):
        names = self.driver.find_element(By.ID, self.contact_name_id)
        names.send_keys(name)

    def contact_us_with_send_message(self, message):
        messages = self.driver.find_element(By.ID, self.contact_us_message_box_id)
        messages.send_keys(message)

    def contact_us_page_send_message(self):
        send = self.driver.find_element(By.XPATH, self.send_message_xpath)
        send.click()

        alt = self.driver.switch_to.alert.text

        print("Anyways", alt, "Thanks!!!")
        assert alt == "Thanks for the message!!"

