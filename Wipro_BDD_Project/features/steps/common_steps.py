# common_steps.py
import time
import allure
from behave import given, when
from config.config import Config
from pages.home_page import HomePage
from pages.headphones_page import HeadphonesPage
from utilities.logger import get_logger

logger = get_logger(__name__)


# ============================================================
# GIVEN STEPS
# ============================================================

@given("I open the BestBuy website")
def step_open_bestbuy(context):
    with allure.step("POSITIVE TEST 1 — Open BestBuy Website"):
        config = Config.load_config()
        base_url = config["base_url"]
        logger.info("Opening BestBuy website: %s", base_url)
        context.driver.get(base_url)
        allure.attach(
            context.driver.current_url,
            name="Website URL",
            attachment_type=allure.attachment_type.TEXT
        )
        logger.info("BestBuy website opened. URL: %s", context.driver.current_url)


@given("I open a wrong misspelled website URL")
def step_open_wrong_url(context):
    with allure.step("NEGATIVE TEST 1 — Open Wrong Misspelled URL"):
        wrong_url = "https://www.bastbiy.com"
        logger.info("NEGATIVE TEST — Opening wrong URL: %s", wrong_url)
        try:
            context.driver.get(wrong_url)
            time.sleep(3)
        except Exception:
            pass
        logger.info("Wrong URL — Title: %s | URL: %s",
                    context.driver.title, context.driver.current_url)


# ============================================================
# WHEN STEPS
# ============================================================

@when("I select United States")
def step_select_united_states(context):
    with allure.step("POSITIVE TEST 2 — Select United States"):
        logger.info("Selecting United States...")
        context.home_page = HomePage(context.driver)
        context.home_page.select_country()
        logger.info("United States selected. URL: %s", context.driver.current_url)


@when("I click Top Deals")
def step_click_top_deals(context):
    with allure.step("POSITIVE TEST 3 — Click Top Deals"):
        logger.info("Clicking Top Deals...")
        context.home_page.click_top_deals()
        logger.info("Top Deals opened. URL: %s", context.driver.current_url)


@when("I click the Headphones category")
def step_click_headphones(context):
    with allure.step("POSITIVE TEST 4 — Click Headphones Category"):
        logger.info("Clicking Headphones category...")
        context.headphones_page = HeadphonesPage(context.driver)
        context.headphones_page.click_headphones_in_deals()
        logger.info("Headphones page opened. URL: %s", context.driver.current_url)


@when("I select a random headphone category from Excel")
def step_select_random_category(context):
    with allure.step("POSITIVE TEST 5 — Click Random Headphone Category"):
        logger.info("Selecting random category from Excel...")
        context.selected_category = context.headphones_page.click_subcategory()
        logger.info("Category selected: %s | URL: %s",
                    context.selected_category, context.driver.current_url)


@when("I add products to the cart")
def step_add_products(context):
    with allure.step("POSITIVE TEST 6 — Add Products to Cart"):
        logger.info("Adding products to cart...")
        context.product_count = context.headphones_page.get_product_count()
        context.added_count = context.headphones_page.click_add_to_cart_on_listing()
        logger.info("Products added to cart: %d", context.added_count)


@when("I open the cart page")
def step_open_cart(context):
    with allure.step("POSITIVE TEST 7 — Open Cart / Order Summary Page"):
        logger.info("Navigating to cart page...")
        context.headphones_page.open_cart()
        logger.info("Cart page loaded. URL: %s", context.driver.current_url)


# ============================================================
# NEGATIVE TEST WHEN STEPS
# ============================================================

@when("I select Canada instead of United States")
def step_select_canada(context):
    with allure.step("NEGATIVE TEST 2 — Select Canada (Wrong Country)"):
        logger.info("NEGATIVE TEST — Selecting Canada...")
        context.home_page = HomePage(context.driver)
        context.home_page.select_canada()
        logger.info("Canada selected. URL: %s", context.driver.current_url)


@when("I click Deal of the Day instead of Top Deals")
def step_click_deal_of_day(context):
    with allure.step("NEGATIVE TEST 3 — Click Deal of the Day (Wrong Section)"):
        logger.info("NEGATIVE TEST — Clicking Deal of the Day...")
        context.home_page.click_deal_of_the_day()
        logger.info("Deal of the Day clicked. URL: %s", context.driver.current_url)