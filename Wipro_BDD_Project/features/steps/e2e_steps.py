# e2e_steps.py
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


@then("the cart page should be displayed successfully")
def step_verify_cart_page(context):
    logger.info("=" * 70)
    logger.info("VERIFYING CART PAGE")
    logger.info("=" * 70)

    current_url = context.driver.current_url
    selected_category = getattr(context, "selected_category", "N/A")
    product_count = getattr(context, "product_count", "N/A")
    added_count = getattr(context, "added_count", "N/A")

    assert "cart" in current_url.lower(), \
        f"FAILED — Cart page did not open. URL: {current_url}"

    # Name screenshot based on which scenario is running
    scenario_name = context.scenario.name
    if "TC07" in scenario_name:
        screenshot_name = "TC07 — Cart Order Summary Page"
    else:
        screenshot_name = "E2E — Cart Order Summary Page"

    attach_screenshot(context, screenshot_name)

    logger.info("=" * 70)
    logger.info("TEST PASSED — CART PAGE OPENED SUCCESSFULLY")
    logger.info("Selected Category : %s", selected_category)
    logger.info("Products On Page  : %s", product_count)
    logger.info("Products Added    : %s", added_count)
    logger.info("Final Cart URL    : %s", current_url)
    logger.info("=" * 70)

    print("=" * 70)
    print("FINAL TEST SUMMARY")
    print("=" * 70)
    print(f"Selected Category : {selected_category}")
    print(f"Products On Page  : {product_count}")
    print(f"Products Added    : {added_count}")
    print(f"Final Cart URL    : {current_url}")
    print("=" * 70)

    try:
        allure.attach(
            f"Selected Category : {selected_category}\n"
            f"Products On Page  : {product_count}\n"
            f"Products Added    : {added_count}\n"
            f"Final Cart URL    : {current_url}",
            name="Final Test Summary",
            attachment_type=allure.attachment_type.TEXT
        )
        logger.info("Summary attached to Allure")
    except Exception as e:
        logger.warning("Allure attach failed: %s", str(e))