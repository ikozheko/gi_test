from selenium.webdriver.common.by import By

from .base_page import BasePage
    

class MainPage(BasePage):

    def get_games(self):
        games = self.find_element((By.CLASS_NAME, 'plate_theme_games')).find_elements(By.CLASS_NAME, 'plate__item')
        games_labels = [
            li.find_element_by_class_name('plate__title').text
            for li in games
        ]
        return games_labels

