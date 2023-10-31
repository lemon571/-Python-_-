from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def get_text(self, locator):
        return self.find_element(locator).text
