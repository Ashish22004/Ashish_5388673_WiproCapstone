from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Base class with reusable methods for all page classes
class BasePage:

    # Store driver and set 30 sec wait time
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # Wait until element is clickable then click it
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # Wait for element, clear existing text, type new text
    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        element.clear()
        element.send_keys(text)

    # Wait for element to be visible and return its text
    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    # Wait and return list of all matching elements
    def get_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # Return True if element visible, False if not found within wait time
    def is_element_visible(self, locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False