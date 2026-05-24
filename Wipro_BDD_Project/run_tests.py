# run_tests.py
import os
import sys
import shutil
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


def clean_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    logger.info("Cleaned: %s", path)


def run():

    logger.info("=" * 60)
    logger.info("Wipro BDD Project - BestBuy — Behave BDD Test Runner")
    logger.info("=" * 60)

    # ============================================================
    # CLEAN OLD DATA
    # ============================================================
    logger.info("Cleaning old data...")
    clean_folder("reports/allure_reports")
    clean_folder("reports/allure_reports_html")
    clean_folder("screenshots")
    clean_folder("logs")
    logger.info("Cleaned successfully.")

    # ============================================================
    # RUN BEHAVE TESTS
    # ============================================================
    logger.info("=" * 60)
    logger.info("RUNNING BDD TESTS")
    logger.info("=" * 60)

    subprocess.run([
        sys.executable, "-m", "behave",
        "--no-capture",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", "reports/allure_reports"
    ])

    logger.info("Tests completed.")

    # ============================================================
    # GENERATE ALLURE SINGLE FILE REPORT
    # ============================================================
    logger.info("=" * 60)
    logger.info("GENERATING ALLURE REPORT")
    logger.info("=" * 60)

    subprocess.run(
        "allure generate reports/allure_reports --single-file -o reports/allure_reports_html --clean",
        shell=True
    )

    logger.info("Allure report generated.")

    # ============================================================
    # EXECUTION SUMMARY
    # ============================================================
    logger.info("=" * 60)
    logger.info("TEST EXECUTION SUMMARY")
    logger.info("=" * 60)
    logger.info("TOTAL TESTS : 11")
    logger.info("E2E         : 1 Scenario")
    logger.info("POSITIVE    : 7 Scenarios")
    logger.info("NEGATIVE    : 3 Scenarios")
    logger.info("=" * 60)
    logger.info("REPORT PATHS")
    logger.info("=" * 60)
    logger.info("Allure Report : reports/allure_reports_html/index.html")
    logger.info("Screenshots   : screenshots/")
    logger.info("Logs          : logs/")
    logger.info("=" * 60)
    logger.info("BDD TEST EXECUTION COMPLETED")
    logger.info("=" * 60)


if __name__ == "__main__":
    run()