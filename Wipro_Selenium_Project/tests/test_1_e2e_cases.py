import allure
from pages.home_page import HomePage
from pages.headphones_page import HeadphonesPage
from config.config import Config
from utilities.logger import get_logger
from utilities.screenshot_utils import take_screenshot

logger = get_logger(__name__)


@allure.suite("E2E Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Purchase Flow")
@allure.story("Complete E2E Flow")
@allure.title("Complete Positive Flow — E2E Test")
@allure.description("Full end to end flow from opening BestBuy to Cart Order Summary in ONE browser session")
def test_complete_positive_flow(setup):

    driver = setup
    config = Config.load_config()
    home_page = HomePage(driver)
    headphones_page = HeadphonesPage(driver)

    logger.info("=" * 70)
    logger.info("STARTING COMPLETE POSITIVE FLOW — E2E TEST")
    logger.info("=" * 70)

    with allure.step("POSITIVE TEST 1 — Open BestBuy Website"):
        logger.info("POSITIVE TEST 1 — OPEN BESTBUY WEBSITE")
        driver.get(config["base_url"])
        logger.info("BestBuy website opened: %s", driver.current_url)
        assert "bestbuy" in driver.current_url.lower(), \
            "FAILED — BestBuy website did not open"
        logger.info("PASSED — BestBuy website opened successfully")

    with allure.step("POSITIVE TEST 2 — Select United States"):
        logger.info("POSITIVE TEST 2 — SELECT UNITED STATES")
        home_page.select_country()
        assert "bestbuy.com" in driver.current_url.lower(), \
            "FAILED — United States homepage did not load"
        logger.info("PASSED — United States selected. URL: %s", driver.current_url)

    with allure.step("POSITIVE TEST 3 — Click Top Deals"):
        logger.info("POSITIVE TEST 3 — CLICK TOP DEALS")
        home_page.click_top_deals()
        assert "top-deals" in driver.current_url.lower(), \
            "FAILED — Top Deals page did not load"
        logger.info("PASSED — Top Deals opened. URL: %s", driver.current_url)

    with allure.step("POSITIVE TEST 4 — Click Headphones Category"):
        logger.info("POSITIVE TEST 4 — CLICK HEADPHONES CATEGORY")
        headphones_page.click_headphones_in_deals()
        logger.info("PASSED — Headphones page opened. URL: %s", driver.current_url)

    with allure.step("POSITIVE TEST 5 — Click Random Headphone Category"):
        logger.info("POSITIVE TEST 5 — CLICK RANDOM HEADPHONE CATEGORY")
        selected = headphones_page.click_subcategory()
        logger.info("PASSED — Random category selected: %s. URL: %s", selected, driver.current_url)

    with allure.step("POSITIVE TEST 6 — Add Products to Cart"):
        logger.info("POSITIVE TEST 6 — ADD PRODUCTS TO CART")
        count = headphones_page.get_product_count()
        logger.info("Products found on page: %d", count)
        added = headphones_page.click_add_to_cart_on_listing()
        assert added > 0, "FAILED — No products were added to cart"
        logger.info("PASSED — Products added to cart: %d", added)

    with allure.step("POSITIVE TEST 7 — Open Cart / Order Summary Page"):
        logger.info("POSITIVE TEST 7 — OPEN CART / ORDER SUMMARY PAGE")
        headphones_page.open_cart()
        assert "cart" in driver.current_url.lower(), \
            "FAILED — Cart page did not open"
        logger.info("PASSED — Cart page opened. URL: %s", driver.current_url)
        screenshot_path = take_screenshot(driver, "positive_e2e_test_complete_cart")
        allure.attach.file(screenshot_path, name="Cart Order Summary", attachment_type=allure.attachment_type.PNG)

    logger.info("=" * 70)
    logger.info("ALL 7 POSITIVE TESTS PASSED SUCCESSFULLY")
    logger.info("=" * 70)

    print("=" * 70)
    print("ALL 7 POSITIVE TESTS PASSED")
    print("Random Category Selected :", selected)
    print("Products Found           :", count)
    print("Products Added           :", added)
    print("Final Cart URL           :", driver.current_url)
    print("=" * 70)