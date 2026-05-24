# environment.py
import os
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.logger import get_logger

logger = get_logger(__name__)


def before_scenario(context, scenario):
    logger.info("=" * 70)
    logger.info("SCENARIO STARTING: %s", scenario.name)
    logger.info("=" * 70)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    logger.info("Chrome browser launched successfully")


def after_scenario(context, scenario):
    logger.info("=" * 70)
    logger.info(
        "SCENARIO FINISHED: %s | STATUS: %s",
        scenario.name,
        scenario.status
    )
    logger.info("=" * 70)

    try:
        # ATTACH LOG FILE TO ALLURE
        logs_folder = "logs"
        if os.path.exists(logs_folder):
            log_files = sorted(
                [
                    os.path.join(logs_folder, f)
                    for f in os.listdir(logs_folder)
                    if f.endswith(".log")
                ],
                key=os.path.getmtime
            )
            if log_files:
                latest_log = log_files[-1]
                try:
                    allure.attach.file(
                        latest_log,
                        name="Execution Logs",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    logger.info("Logs attached to Allure")
                except Exception as e:
                    logger.warning("Could not attach logs: %s", str(e))

    except Exception as e:
        logger.error("Error in after_scenario: %s", str(e))

    finally:
        if hasattr(context, "driver") and context.driver:
            context.driver.quit()
            logger.info("Browser closed successfully")


def after_all(context):
    logger.info("=" * 70)
    logger.info("ALL SCENARIOS COMPLETE")
    logger.info("=" * 70)