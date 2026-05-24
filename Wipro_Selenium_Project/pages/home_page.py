from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from pages.base_page import BasePage
from utilities.logger import get_logger
from utilities.screenshot_utils import take_screenshot

logger = get_logger(__name__)


class HomePage(BasePage):

    # --- Locators (merged from locators/home_locators.py) ---
    UNITED_STATES_BUTTON = (By.CSS_SELECTOR, "a.us-link")
    TOP_DEALS_LINK = (
        By.XPATH,
        '//a[@data-lid="ubr_td"] | //a[contains(@href,"top-deals")]'
    )

    def _wait_for_page_load(self):
        # Wait until browser reports page completely loaded
        WebDriverWait(self.driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def select_country(self):
        # Clicks United States on country selection popup
        logger.info("=== SELECT UNITED STATES: Clicking United States on popup ===")
        try:
            country = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.UNITED_STATES_BUTTON)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", country
            )
            time.sleep(0.5)
            logger.info("Clicking United States button...")
            ActionChains(self.driver).move_to_element(country).click().perform()
            logger.info("United States button CLICKED")
            WebDriverWait(self.driver, 60).until(
                lambda d: "Best Buy International" not in d.title
            )
            self._wait_for_page_load()
            logger.info("US Homepage loaded: %s", self.driver.title)
        except TimeoutException:
            logger.info("Country popup not shown — already on US homepage")
            self._wait_for_page_load()

    def click_top_deals(self):
        # Clicks Top Deals link in navigation bar
        logger.info("=== CLICK TOP DEALS: Finding Top Deals link in navigation ===")
        xpaths = [
            '//a[@data-lid="ubr_td"]',
            '//a[contains(@href,"top-deals")]',
            '//a[normalize-space(text())="Top Deals"]',
            '//a[contains(text(),"Top Deals")]',
        ]
        for xpath in xpaths:
            try:
                deals = WebDriverWait(self.driver, 8).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", deals
                )
                time.sleep(1)  # Kept at 1 — needed for Top Deals to navigate correctly
                logger.info("Top Deals link found — clicking...")
                ActionChains(self.driver).move_to_element(deals).click().perform()
                logger.info("Top Deals CLICKED")
                self._wait_for_page_load()
                # Wait until URL actually contains top-deals
                WebDriverWait(self.driver, 15).until(
                    lambda d: "top-deals" in d.current_url.lower()
                )
                logger.info("Top Deals page URL: %s", self.driver.current_url)
                return True
            except Exception:
                logger.warning("XPath not found, trying next: %s", xpath)
                continue
        take_screenshot(self.driver, "top_deals_not_found")
        raise Exception("Top Deals link not found after trying all XPaths.")

    def select_canada(self):
        # Clicks Canada on country popup — WRONG country intentionally for negative test
        logger.info("=== NEGATIVE TEST 2: Clicking Canada (wrong country) ===")
        time.sleep(2)
        try:
            canada = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "canada-link"))
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", canada
            )
            time.sleep(1)
            logger.info("Clicking Canada button...")
            canada.click()
            logger.info("Canada CLICKED — URL will now be bestbuy.ca")
            self._wait_for_page_load()
            logger.info("After Canada click — URL: %s", self.driver.current_url)
        except Exception as e:
            logger.warning("Canada button not found: %s", str(e))
            self._wait_for_page_load()

    def click_deal_of_the_day(self):
        # Clicks Deal of the Day instead of Top Deals — WRONG section intentionally for negative test
        logger.info("=== NEGATIVE TEST 3: Clicking Deal of the Day (wrong section) ===")
        deal_xpaths = [
            '//a[contains(@class,"bottom-left-links") and contains(@href,"deal-of-the-day")]',
            '//a[contains(@href,"deal-of-the-day")]',
            '//a[normalize-space(text())="Deal of the Day"]',
            '//a[contains(text(),"Deal of the Day")]',
        ]
        for xpath in deal_xpaths:
            try:
                deal = WebDriverWait(self.driver, 8).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", deal
                )
                time.sleep(1)
                logger.info("Deal of the Day link found — clicking...")
                self.driver.execute_script("arguments[0].click();", deal)
                logger.info("Deal of the Day CLICKED")
                self._wait_for_page_load()
                logger.info("Deal of the Day URL: %s", self.driver.current_url)
                return True
            except Exception:
                logger.warning("XPath not found, trying next: %s", xpath)
                continue
        logger.warning("Deal of the Day link not found — using direct URL as fallback")
        self.driver.get(
            "https://www.bestbuy.com/site/misc/deal-of-the-day/"
            "pcmcat248000050016.c?id=pcmcat248000050016"
        )
        self._wait_for_page_load()
        logger.info("Deal of the Day URL via direct navigation: %s", self.driver.current_url)