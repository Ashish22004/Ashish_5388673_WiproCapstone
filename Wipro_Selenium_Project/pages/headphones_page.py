from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from pages.base_page import BasePage
from utilities.logger import get_logger
from utilities.excel_utils import get_random_category

logger = get_logger(__name__)


class HeadphonesPage(BasePage):

    # --- Locators ---
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "li.sku-item")
    ALL_ADD_TO_CART_BUTTONS = (
        By.XPATH,
        '//button[contains(@data-testid,"plp-add-to-cart")]'
    )

    def _wait_for_page_load(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        time.sleep(1)

    # ================================================================
    # POSITIVE TEST 4 — CLICK HEADPHONES CATEGORY
    # ================================================================
    def click_headphones_in_deals(self):
        logger.info("=== POSITIVE TEST 4: CLICK HEADPHONES CATEGORY ===")
        try:
            link = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    '//a[contains(@href,"headphones-on-sale")]'
                ))
            )
            ActionChains(self.driver).move_to_element(link).perform()
            time.sleep(1)
            logger.info("Headphones link found — clicking...")
            self.driver.execute_script("arguments[0].click();", link)
            logger.info("Headphones CLICKED")
            self._wait_for_page_load()
            logger.info("Headphones On Sale page: %s", self.driver.current_url)
            return True
        except Exception as e:
            logger.warning("Headphones link not found: %s", str(e)[:60])
        raise Exception("Headphones link not found on Top Deals page.")

    # ================================================================
    # POSITIVE TEST 5 — CLICK RANDOM HEADPHONE CATEGORY FROM EXCEL
    # ================================================================
    def click_subcategory(self):
        logger.info("=== POSITIVE TEST 5: CLICK RANDOM HEADPHONE CATEGORY ===")

        # Get random category from Excel file
        selected_category = get_random_category()
        logger.info("Selected category from Excel: %s", selected_category)

        # Build XPaths to find the selected category on page
        xpaths = [
            f'//a[normalize-space(text())="{selected_category}"]',
            f'//p[normalize-space(text())="{selected_category}"]/ancestor::a',
            f'//a[contains(text(),"{selected_category}")]',
            f'//span[normalize-space(text())="{selected_category}"]/ancestor::a',
        ]

        for xpath in xpaths:
            try:
                links = self.driver.find_elements(By.XPATH, xpath)
                if links:
                    link = links[0]
                    ActionChains(self.driver).move_to_element(link).perform()
                    time.sleep(1)
                    logger.info("%s link found — clicking...", selected_category)
                    self.driver.execute_script("arguments[0].click();", link)
                    logger.info("%s CLICKED", selected_category)
                    self._wait_for_page_load()
                    logger.info("Category page URL: %s", self.driver.current_url)
                    return selected_category
            except Exception:
                continue

        # If selected category not found on page — fallback to Wireless
        logger.warning(
            "%s not found on page — falling back to Wireless", selected_category
        )
        fallback_xpaths = [
            '//a[normalize-space(text())="Wireless"]',
            '//a[contains(text(),"Wireless")]',
            '//a[contains(@href,"wireless-headphones")]',
        ]
        for xpath in fallback_xpaths:
            try:
                links = self.driver.find_elements(By.XPATH, xpath)
                if links:
                    link = links[0]
                    self.driver.execute_script("arguments[0].click();", link)
                    logger.info("Fallback Wireless CLICKED")
                    self._wait_for_page_load()
                    logger.info("Fallback URL: %s", self.driver.current_url)
                    return "Wireless"
            except Exception:
                continue

        raise Exception("No headphone category found on page.")

    # ================================================================
    # COUNT PRODUCTS ON LISTING PAGE — FIXED
    # ================================================================
    def get_product_count(self):
        logger.info("Counting products on listing page...")

        # Dismiss any popup before counting
        try:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(1)
        except Exception:
            pass

        try:
            self.driver.execute_script(
                "document.querySelectorAll('[class*=\"overlay\"],[class*=\"modal\"],"
                "[class*=\"survey\"],[class*=\"drawer\"]')"
                ".forEach(function(el){"
                "  el.style.display='none';"
                "  el.style.visibility='hidden';"
                "  el.style.pointerEvents='none';"
                "});"
                "document.body.style.overflow='auto';"
            )
            time.sleep(1)
        except Exception:
            pass

        # Try all known product selectors one by one
        selectors = [
            ('css', 'li.sku-item'),
            ('css', '[class*="sku-item"]'),
            ('css', '[data-testid*="product-list-item"]'),
            ('css', '[class*="product-item"]'),
            ('css', '[class*="list-item"]'),
            ('xpath', '//button[contains(@data-testid,"plp-add-to-cart")]'),
        ]

        for selector_type, selector in selectors:
            try:
                if selector_type == 'css':
                    products = self.driver.find_elements(By.CSS_SELECTOR, selector)
                else:
                    products = self.driver.find_elements(By.XPATH, selector)

                if products:
                    count = len(products)
                    logger.info(
                        "Found %d products using selector: %s", count, selector
                    )
                    return count
            except Exception:
                continue

        # Last fallback — count Add to Cart buttons = number of products
        try:
            buttons = self.driver.find_elements(*self.ALL_ADD_TO_CART_BUTTONS)
            if buttons:
                logger.info(
                    "Found %d products via Add to Cart buttons (last fallback).",
                    len(buttons)
                )
                return len(buttons)
        except Exception:
            pass

        logger.warning("No products found on listing page.")
        return 0

    # ================================================================
    # DISMISS POPUP AFTER ADD TO CART
    # ================================================================
    def _dismiss_popup(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(1)
        except Exception:
            pass
        try:
            self.driver.execute_script(
                "document.querySelectorAll('[class*=\"overlay\"],[class*=\"modal\"],"
                "[class*=\"drawer\"],[class*=\"cart-con\"]')"
                ".forEach(function(el){"
                "  el.style.display='none';"
                "  el.style.visibility='hidden';"
                "  el.style.pointerEvents='none';"
                "});"
                "document.body.style.overflow='auto';"
                "document.documentElement.style.overflow='auto';"
            )
        except Exception:
            pass
        time.sleep(1)

    # ================================================================
    # COLLECT VALID ADD TO CART BUTTON IDs
    # ================================================================
    def _collect_valid_button_ids(self):
        valid_ids = []
        seen_ids = set()
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(1)
            all_buttons = self.driver.find_elements(*self.ALL_ADD_TO_CART_BUTTONS)
            logger.info("Total Add to Cart buttons found: %d", len(all_buttons))
            for btn in all_buttons:
                try:
                    btn_id = btn.get_attribute("data-testid") or ""
                    if not btn_id or btn_id in seen_ids:
                        continue
                    if btn.get_attribute("disabled"):
                        continue
                    btn_text = (btn.text or "").strip().lower()
                    aria_label = (btn.get_attribute("aria-label") or "").lower()
                    if "sold out" in aria_label or "unavailable" in aria_label:
                        continue
                    if "sold out" in btn_text or "unavailable" in btn_text:
                        continue
                    if (
                        "add to cart" in btn_text
                        or "add to cart" in aria_label
                        or "add" in btn_text
                    ):
                        valid_ids.append(btn_id)
                        seen_ids.add(btn_id)
                        logger.info("Valid Add to Cart button: %s", btn_id)
                except Exception:
                    continue
        except Exception as e:
            logger.warning("Error collecting buttons: %s", e)
        return valid_ids

    # ================================================================
    # POSITIVE TEST 6 — ADD PRODUCTS TO CART
    # ================================================================
    def click_add_to_cart_on_listing(self):
        logger.info("=== POSITIVE TEST 6: ADD PRODUCTS TO CART ===")

        added_count = 0
        max_to_add = 2
        clicked_ids = set()

        valid_ids = self._collect_valid_button_ids()
        logger.info("Valid buttons ready to click: %d", len(valid_ids))

        if not valid_ids:
            logger.warning("No valid Add to Cart buttons found!")
            return 0

        for btn_id in valid_ids:
            if added_count >= max_to_add:
                break
            if btn_id in clicked_ids:
                continue
            try:
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(1)

                btn = WebDriverWait(self.driver, 8).until(
                    EC.presence_of_element_located((
                        By.XPATH, '//button[@data-testid="%s"]' % btn_id
                    ))
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", btn
                )
                time.sleep(1)

                btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((
                        By.XPATH, '//button[@data-testid="%s"]' % btn_id
                    ))
                )
                ActionChains(self.driver).move_to_element(btn).perform()
                time.sleep(1)

                logger.info(
                    "Clicking Add to Cart for product %d: %s",
                    added_count + 1, btn_id
                )
                self.driver.execute_script("arguments[0].click();", btn)
                logger.info("Add to Cart clicked!")

                self._dismiss_popup()

                clicked_ids.add(btn_id)
                added_count += 1
                logger.info("Product %d added to cart successfully.", added_count)

            except Exception as e:
                logger.warning("Could not add %s: %s", btn_id, str(e)[:60])
                clicked_ids.add(btn_id)
                self._dismiss_popup()
                continue

        logger.info("Total products added to cart: %d", added_count)
        return added_count

    # ================================================================
    # POSITIVE TEST 7 — OPEN CART PAGE
    # ================================================================
    def open_cart(self):
        logger.info("=== POSITIVE TEST 7: OPEN CART PAGE ===")
        self.driver.get("https://www.bestbuy.com/cart")
        self._wait_for_page_load()
        logger.info("Cart page loaded: %s", self.driver.current_url)
        try:
            cart_items = self.driver.find_elements(
                By.CSS_SELECTOR,
                '.fluid-large-view__list-item, '
                '[data-testid="cartItem"], '
                '[class*="cart-item"]'
            )
            logger.info("Cart items visible: %d", len(cart_items))
        except Exception:
            logger.info("Could not count cart items.")
        time.sleep(1)