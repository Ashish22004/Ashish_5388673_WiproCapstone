import allure
import time
from pages.home_page import HomePage
from config.config import Config
from utilities.logger import get_logger
from utilities.screenshot_utils import take_screenshot

logger = get_logger(__name__)


# ==========================================================
# NEGATIVE TEST 1 — WRONG WEBSITE URL
# ==========================================================
@allure.suite("Negative Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Negative Tests")
@allure.story("Wrong Website URL")
@allure.title("Negative TC01 — Wrong Website URL")
@allure.description("Open misspelled BestBuy URL instead of bestbuy.com — wrong URL verification")
def test_wrong_website_url(setup):

    driver = setup

    logger.info("=" * 60)
    logger.info("NEGATIVE TEST 1 — WRONG WEBSITE URL")
    logger.info("Expected website : https://www.bestbuy.com")
    logger.info("Opening WRONG website: https://www.bastbiy.com")
    logger.info("=" * 60)

    with allure.step("Open WRONG website — misspelled BestBuy URL instead of bestbuy.com"):
        try:
            driver.get("https://www.bastbiy.com")
            time.sleep(3)
        except Exception:
            # Domain does not exist — this is expected for a wrong URL test
            pass
        logger.info("Wrong website attempted: https://www.bastbiy.com")
        logger.info("Page Title : %s", driver.title)

    with allure.step("Take screenshot — Wrong website"):
        screenshot_path = take_screenshot(driver, "negative_test_1_wrong_website_url")
        allure.attach.file(screenshot_path, name="Wrong Website — Misspelled URL", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify bestbuy.com is NOT in URL"):
        is_wrong_website = "bestbuy.com" not in driver.current_url.lower()
        logger.info("Negative verification — bestbuy.com absent from URL: %s", is_wrong_website)
        logger.info("Result : NEGATIVE TEST 1 PASSED — wrong BestBuy URL used instead of bestbuy.com")
        assert is_wrong_website, \
            "Negative test setup error — bestbuy.com found in URL but wrong URL was expected"


# ==========================================================
# NEGATIVE TEST 2 — WRONG COUNTRY SELECTED
# ==========================================================
@allure.suite("Negative Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Negative Tests")
@allure.story("Wrong Country Selected")
@allure.title("Negative TC02 — Wrong Country Selected")
@allure.description("Select Canada instead of United States — wrong country verification")
def test_wrong_country_selected(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("NEGATIVE TEST 2 — WRONG COUNTRY SELECTED")
    logger.info("Opening correct website: %s", config["base_url"])
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])
        logger.info("BestBuy website opened: %s", driver.current_url)

    with allure.step("Select WRONG country — Canada instead of United States"):
        home_page = HomePage(driver)
        home_page.select_canada()
        logger.info("Current URL: %s", driver.current_url)

    with allure.step("Take screenshot — Wrong country"):
        screenshot_path = take_screenshot(driver, "negative_test_2_wrong_country")
        allure.attach.file(screenshot_path, name="Wrong Country — Canada", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify united-states is NOT in URL"):
        is_wrong_country = "united-states" not in driver.current_url.lower()
        logger.info("Negative verification — united-states absent from URL: %s", is_wrong_country)
        logger.info("Result : NEGATIVE TEST 2 PASSED — Canada selected instead of United States")
        assert is_wrong_country, \
            "Negative test setup error — united-states found in URL but Canada was expected"


# ==========================================================
# NEGATIVE TEST 3 — WRONG SECTION CLICKED
# ==========================================================
@allure.suite("Negative Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Negative Tests")
@allure.story("Wrong Section Clicked")
@allure.title("Negative TC03 — Wrong Section Clicked")
@allure.description("Click Deal of the Day instead of Top Deals — wrong section verification")
def test_wrong_section_clicked(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("NEGATIVE TEST 3 — WRONG SECTION CLICKED")
    logger.info("Opening correct website: %s", config["base_url"])
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])
        logger.info("BestBuy website opened: %s", driver.current_url)

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()
        logger.info("United States selected.")

    with allure.step("Click WRONG section — Deal of the Day instead of Top Deals"):
        home_page.click_deal_of_the_day()
        logger.info("Current URL: %s", driver.current_url)

    with allure.step("Take screenshot — Wrong section"):
        screenshot_path = take_screenshot(driver, "negative_test_3_wrong_section")
        allure.attach.file(screenshot_path, name="Wrong Section — Deal of the Day", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify top-deals is NOT in URL"):
        is_wrong_section = "top-deals" not in driver.current_url.lower()
        logger.info("Negative verification — top-deals absent from URL: %s", is_wrong_section)
        logger.info("Result : NEGATIVE TEST 3 PASSED — Deal of the Day opened instead of Top Deals")
        assert is_wrong_section, \
            "Negative test setup error — top-deals found in URL but Deal of the Day was expected"