from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from .base_page import BasePage


class GamePage(BasePage):

    def get_badges(self):
        badges = self.find_elements((By.CSS_SELECTOR, '.readmore__full a'))
        badges_labels = [
            badge.get_attribute('href')
            for badge in badges
        ]
        return badges_labels

    def get_genre(self):
        genre = self.find_element((By.CLASS_NAME, 'game-content-genre'), wait_until_condition=ec.element_to_be_clickable).text
        return genre


class ParadiseIslandPage(GamePage):
    URL = '/en/games/paradise-island-2'
