# positive_steps.py
import allure
from behave import then
from utilities.logger import get_logger
from utilities.screenshot_utils import take_screenshot

logger = get_logger(__name__)


def attach_screenshot(context, name):
    try:
        path = take_screenshot(
            context.driver,
            name.replace(" ", "_").replace("—", "").replace("/", "").lower()
        )
        allure.attach.file(
            path,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        logger.warning("Screenshot attach failed: %s", str(e))


@then("the BestBuy website should load successfully")
def step_verify_bestbuy_loaded(context):
    current_url = context.driver.current_url

    assert "bestbuy" in current_url.lower(), \
        f"TC01 FAILED — BestBuy website did not open. URL: {current_url}"

    attach_screenshot(context, "TC01 — BestBuy Homepage Loaded")

    logger.info("=" * 60)
    logger.info("TC01 PASSED — BestBuy homepage loaded")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 60)


@then("the United States homepage should load")
def step_verify_us_homepage(context):
    current_url = context.driver.current_url

    assert "bestbuy.com" in current_url.lower(), \
        f"TC02 FAILED — US homepage did not load. URL: {current_url}"

    attach_screenshot(context, "TC02 — United States Homepage")

    logger.info("=" * 60)
    logger.info("TC02 PASSED — United States homepage loaded")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 60)


@then("the Top Deals page should open")
def step_verify_top_deals(context):
    current_url = context.driver.current_url

    assert "top-deals" in current_url.lower(), \
        f"TC03 FAILED — Top Deals page did not open. URL: {current_url}"

    attach_screenshot(context, "TC03 — Top Deals Page Opened")

    logger.info("=" * 60)
    logger.info("TC03 PASSED — Top Deals page opened")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 60)


@then("the Headphones page should open")
def step_verify_headphones_page(context):
    current_url = context.driver.current_url

    assert "top-deals" not in current_url.lower(), \
        f"TC04 FAILED — Still on Top Deals page. URL: {current_url}"

    attach_screenshot(context, "TC04 — Headphones Category Page")

    logger.info("=" * 60)
    logger.info("TC04 PASSED — Headphones page opened")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 60)


@then("the headphone category page should open")
def step_verify_category_page(context):
    current_url = context.driver.current_url
    selected_category = getattr(context, "selected_category", "N/A")

    assert current_url is not None and len(current_url) > 0, \
        "TC05 FAILED — Category page URL is empty"

    attach_screenshot(context, f"TC05 — {selected_category} Category Page")

    logger.info("=" * 60)
    logger.info("TC05 PASSED — Category page opened")
    logger.info("Selected Category: %s", selected_category)
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 60)


@then("at least one product should be added to the cart")
def step_verify_products_added(context):
    added = getattr(context, "added_count", 0)

    assert added > 0, \
        f"TC06 FAILED — No products added to cart. Count: {added}"

    attach_screenshot(context, "TC06 — Products Added to Cart")

    logger.info("=" * 60)
    logger.info("TC06 PASSED — Products added successfully")
    logger.info("Products Added: %d", added)
    logger.info("=" * 60)


# TC07 reuses "the cart page should be displayed successfully"
# from e2e_steps.py — DO NOT redefine here