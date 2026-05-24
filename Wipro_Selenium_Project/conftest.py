import pytest
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import get_logger

logger = get_logger(__name__)


# ============================================================
# FUNCTION FIXTURE — new browser opens and closes for every test
# ============================================================
@pytest.fixture(scope="function")
def setup():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    logger.info("Browser started.")

    yield driver

    logger.info("Browser closing.")
    driver.quit()


# ============================================================
# SESSION HOOK — runs automatically after ALL tests finish
# Generates Allure single-file index.html automatically
# No need to pass any command manually
# ============================================================
def pytest_sessionfinish(session, exitstatus):
    logger.info("Generating Allure single-file HTML report...")
    subprocess.run(
        [
            "allure", "generate",
            "reports/allure_reports",
            "--single-file",
            "-o", "reports/allure_reports_html"
        ],
        shell=True
    )
    logger.info("Allure report ready — open reports/allure_reports_html/index.html")