import urllib.parse
import functools

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    DOMAIN = 'https://www.game-insight.com'
    URL = '/en'

    def __init__(self, driver):
        self.driver = driver

    def get_active_page_name(self):
        menu_item = self.find_element((By.XPATH, '//div[@class="header-nav-item active"]'))
        return menu_item.find_element(By.TAG_NAME, 'a').text

    def click_on_menu(self, menu_id):
        item = self.find_element((By.XPATH, f'//div[@data-menuid="{menu_id}"]'))
        item.click()

    def find_element(self, locator, time=10, wait_until_condition=None):
        if wait_until_condition is None:
            wait_until_condition = ec.presence_of_element_located
        return WebDriverWait(self.driver, time).until(wait_until_condition(locator),
                                                      message=f"Can't find element by locator {locator}")

    find_elements = functools.partialmethod(find_element, wait_until_condition=ec.presence_of_all_elements_located)

    def go_to_site(self):
        self.driver.get(urllib.parse.urljoin(self.DOMAIN, self.URL))
