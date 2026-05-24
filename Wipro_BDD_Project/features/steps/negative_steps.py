# negative_steps.py
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


@then("bestbuy.com should not be in the URL")
def step_verify_wrong_url(context):
    current_url = context.driver.current_url

    assert "bestbuy.com" not in current_url.lower(), \
        f"NC01 FAILED — bestbuy.com found in URL. URL: {current_url}"

    attach_screenshot(context, "NC01 — Wrong URL Page")

    logger.info("=" * 70)
    logger.info("NC01 PASSED — WRONG URL VALIDATION SUCCESSFUL")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 70)


@then("united-states should not be in the URL")
def step_verify_wrong_country(context):
    current_url = context.driver.current_url

    assert "united-states" not in current_url.lower(), \
        f"NC02 FAILED — united-states found in URL. URL: {current_url}"

    attach_screenshot(context, "NC02 — Wrong Country Canada")

    logger.info("=" * 70)
    logger.info("NC02 PASSED — CANADA VALIDATION SUCCESSFUL")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 70)


@then("top-deals should not be in the URL")
def step_verify_wrong_section(context):
    current_url = context.driver.current_url

    assert "top-deals" not in current_url.lower(), \
        f"NC03 FAILED — top-deals found in URL. URL: {current_url}"

    attach_screenshot(context, "NC03 — Wrong Section Deal of the Day")

    logger.info("=" * 70)
    logger.info("NC03 PASSED — DEAL OF THE DAY VALIDATION SUCCESSFUL")
    logger.info("Current URL: %s", current_url)
    logger.info("=" * 70)