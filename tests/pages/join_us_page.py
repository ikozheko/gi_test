import time

from .base_page import BasePage
from selenium.webdriver.common.by import By


class JoinUsPage(BasePage):

    def go_to_site(self):
        super().go_to_site()
        self.click_on_menu('1ec2e3b6')

    def submit(self):
        button = self.find_element((By.CLASS_NAME, 'form-submit'))
        button.click()

    def get_validation_errors(self):
        error_blocks = self.find_elements((By.CLASS_NAME, 'form__item-error-text'))
        error_blocks = {
            visible_block.get_attribute('id')
            for visible_block in error_blocks
            if (
                    visible_block.get_attribute('style') == 'display: block;'
                    and visible_block.get_attribute('id') != 'application_components_GIFormJoin_captcha'
            )
        }
        return error_blocks

    def _get_field_text(self, locator):
        return self.find_element(locator).text

    def _set_field_text(self, locator, value):
        self.find_element(locator).send_keys(value)

    @property
    def username(self):
        return self._get_field_text((By.ID, 'application_components_GIFormJoin_name'))

    @username.setter
    def username(self, value):
        self._set_field_text((By.ID, 'application_components_GIFormJoin_name'), value)

    @property
    def contact_email(self):
        return self._get_field_text((By.ID, 'application_components_GIFormJoin_email'))

    @contact_email.setter
    def contact_email(self, value):
        self._set_field_text((By.ID, 'application_components_GIFormJoin_email'), value)

    def switch_accept(self):
        self.find_element((By.ID, 'application_components_GIFormJoin_accept')).click()
