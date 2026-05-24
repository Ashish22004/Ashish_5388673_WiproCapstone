import allure
from pages.home_page import HomePage
from pages.headphones_page import HeadphonesPage
from config.config import Config
from utilities.logger import get_logger
from utilities.screenshot_utils import take_screenshot

logger = get_logger(__name__)


# ==========================================================
# POSITIVE TEST 1 — OPEN BESTBUY WEBSITE
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Open BestBuy Website")
@allure.title("Positive TC01 — Open BestBuy Website")
@allure.description("Open BestBuy website and verify it loads correctly")
def test_01_open_bestbuy_website(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 1 — OPEN BESTBUY WEBSITE")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])
        logger.info("Website opened: %s", driver.current_url)
        logger.info("Page Title    : %s", driver.title)
        assert "bestbuy" in driver.current_url.lower(), \
            "FAILED — BestBuy website did not open"

    with allure.step("Take screenshot — BestBuy website"):
        screenshot_path = take_screenshot(driver, "positive_test_01_bestbuy_website")
        allure.attach.file(screenshot_path, name="BestBuy Website", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 1 PASSED — BestBuy website opened: %s", driver.current_url)


# ==========================================================
# POSITIVE TEST 2 — OPEN BESTBUY + SELECT UNITED STATES
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Select United States")
@allure.title("Positive TC02 — Select United States")
@allure.description("Open BestBuy and select United States from country popup")
def test_02_select_united_states(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 2 — OPEN BESTBUY + SELECT UNITED STATES")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])
        logger.info("Website opened: %s", driver.current_url)

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()
        logger.info("United States selected. URL: %s", driver.current_url)
        assert "bestbuy.com" in driver.current_url.lower(), \
            "FAILED — United States homepage did not load"

    with allure.step("Take screenshot — United States selected"):
        screenshot_path = take_screenshot(driver, "positive_test_02_united_states")
        allure.attach.file(screenshot_path, name="United States Selected", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 2 PASSED — United States selected: %s", driver.current_url)


# ==========================================================
# POSITIVE TEST 3 — OPEN BESTBUY + SELECT US + CLICK TOP DEALS
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Click Top Deals")
@allure.title("Positive TC03 — Click Top Deals")
@allure.description("Open BestBuy, select US and click Top Deals")
def test_03_click_top_deals(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 3 — OPEN BESTBUY + SELECT US + CLICK TOP DEALS")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()
        logger.info("United States selected. URL: %s", driver.current_url)

    with allure.step("Click Top Deals"):
        home_page.click_top_deals()
        logger.info("Top Deals clicked. URL: %s", driver.current_url)
        assert "top-deals" in driver.current_url.lower(), \
            "FAILED — Top Deals page did not load"

    with allure.step("Take screenshot — Top Deals page"):
        screenshot_path = take_screenshot(driver, "positive_test_03_top_deals")
        allure.attach.file(screenshot_path, name="Top Deals Page", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 3 PASSED — Top Deals opened: %s", driver.current_url)


# ==========================================================
# POSITIVE TEST 4 — UP TO CLICK HEADPHONES CATEGORY
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Click Headphones Category")
@allure.title("Positive TC04 — Click Headphones Category")
@allure.description("Open BestBuy, select US, Top Deals and click Headphones category")
def test_04_click_headphones(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 4 — UP TO CLICK HEADPHONES CATEGORY")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()
        logger.info("United States selected. URL: %s", driver.current_url)

    with allure.step("Click Top Deals"):
        home_page.click_top_deals()
        logger.info("Top Deals clicked. URL: %s", driver.current_url)

    with allure.step("Click Headphones Category"):
        headphones_page = HeadphonesPage(driver)
        headphones_page.click_headphones_in_deals()
        logger.info("Headphones category clicked. URL: %s", driver.current_url)

    with allure.step("Take screenshot — Headphones page"):
        screenshot_path = take_screenshot(driver, "positive_test_04_headphones")
        allure.attach.file(screenshot_path, name="Headphones Page", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 4 PASSED — Headphones page opened: %s", driver.current_url)


# ==========================================================
# POSITIVE TEST 5 — UP TO CLICK RANDOM HEADPHONE CATEGORY
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Click Random Headphone Category")
@allure.title("Positive TC05 — Click Random Headphone Category")
@allure.description("Open BestBuy, navigate to Headphones and click a random category from Excel")
def test_05_click_random_headphone_category(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 5 — UP TO CLICK RANDOM HEADPHONE CATEGORY")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()

    with allure.step("Click Top Deals"):
        home_page.click_top_deals()

    with allure.step("Click Headphones Category"):
        headphones_page = HeadphonesPage(driver)
        headphones_page.click_headphones_in_deals()

    with allure.step("Click Random Category from Excel"):
        selected = headphones_page.click_subcategory()
        logger.info("Random category selected: %s. URL: %s", selected, driver.current_url)

    with allure.step("Take screenshot — Random category page"):
        screenshot_path = take_screenshot(driver, "positive_test_05_random_headphone_category")
        allure.attach.file(screenshot_path, name=f"Random Category — {selected}", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 5 PASSED — Random category page opened: %s", driver.current_url)


# ==========================================================
# POSITIVE TEST 6 — UP TO ADD PRODUCTS TO CART
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Add Products to Cart")
@allure.title("Positive TC06 — Add Products to Cart")
@allure.description("Full flow up to adding products to cart")
def test_06_add_products_to_cart(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 6 — UP TO ADD PRODUCTS TO CART")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()

    with allure.step("Click Top Deals"):
        home_page.click_top_deals()

    with allure.step("Click Headphones Category"):
        headphones_page = HeadphonesPage(driver)
        headphones_page.click_headphones_in_deals()

    with allure.step("Click Random Category from Excel"):
        selected = headphones_page.click_subcategory()
        logger.info("Random category selected: %s", selected)

    with allure.step("Add Products to Cart"):
        count = headphones_page.get_product_count()
        logger.info("Products found on page: %d", count)
        added = headphones_page.click_add_to_cart_on_listing()
        assert added > 0, "FAILED — No products were added to cart"
        logger.info("Products added to cart: %d", added)

    with allure.step("Take screenshot — Products added to cart"):
        screenshot_path = take_screenshot(driver, "positive_test_06_add_to_cart")
        allure.attach.file(screenshot_path, name="Add to Cart", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 6 PASSED — Products added to cart: %d", added)


# ==========================================================
# POSITIVE TEST 7 — FULL FLOW UP TO CART / ORDER SUMMARY PAGE
# ==========================================================
@allure.suite("Positive Tests")
@allure.epic("BestBuy Automation")
@allure.feature("Positive Tests")
@allure.story("Open Cart Order Summary")
@allure.title("Positive TC07 — Open Cart Order Summary")
@allure.description("Full flow up to Cart Order Summary page")
def test_07_open_cart_order_summary(setup):

    driver = setup
    config = Config.load_config()

    logger.info("=" * 60)
    logger.info("POSITIVE TEST 7 — FULL FLOW UP TO CART / ORDER SUMMARY")
    logger.info("=" * 60)

    with allure.step("Open BestBuy website"):
        driver.get(config["base_url"])

    with allure.step("Select United States"):
        home_page = HomePage(driver)
        home_page.select_country()

    with allure.step("Click Top Deals"):
        home_page.click_top_deals()

    with allure.step("Click Headphones Category"):
        headphones_page = HeadphonesPage(driver)
        headphones_page.click_headphones_in_deals()

    with allure.step("Click Random Category from Excel"):
        selected = headphones_page.click_subcategory()
        logger.info("Random category selected: %s", selected)

    with allure.step("Add Products to Cart"):
        count = headphones_page.get_product_count()
        added = headphones_page.click_add_to_cart_on_listing()
        logger.info("Products added to cart: %d", added)

    with allure.step("Open Cart / Order Summary Page"):
        headphones_page.open_cart()
        assert "cart" in driver.current_url.lower(), \
            "FAILED — Cart page did not open"
        logger.info("Cart page loaded. URL: %s", driver.current_url)

    with allure.step("Take screenshot — Cart Order Summary"):
        screenshot_path = take_screenshot(driver, "positive_test_07_cart_summary")
        allure.attach.file(screenshot_path, name="Cart Order Summary", attachment_type=allure.attachment_type.PNG)

    logger.info("POSITIVE TEST 7 PASSED — Cart page opened: %s", driver.current_url)

    print("=" * 60)
    print("ALL 7 INDIVIDUAL POSITIVE TESTS COMPLETED")
    print("Random Category Selected :", selected)
    print("Products Found           :", count)
    print("Products Added           :", added)
    print("Final Cart URL           :", driver.current_url)
    print("=" * 60)