# Wipro Capstone Project — BestBuy Selenium Automation

## Project Overview

This project is a Selenium-based test automation framework built for the Wipro Capstone Project.
It automates the end-to-end purchase flow on the BestBuy website using Python, Selenium WebDriver, and pytest.
The framework follows the Page Object Model (POM) design pattern for clean and maintainable code.

The main highlight of this project is the random headphone category selection — instead of always
clicking the same category, the framework reads categories from an Excel file and picks one randomly
on every run, making tests dynamic and realistic.

---

## Project Structure

Wipro_CapstoneProject/
│
├── config/                        # Configuration folder
│   ├── __init__.py                # Package init file
│   ├── config.py                  # Loads configuration from qa.yaml
│   └── qa.yaml                    # Base URL, wait times, browser settings
│
├── pages/                         # Page Object Model classes
│   ├── __init__.py                # Package init file
│   ├── base_page.py               # Base class with reusable Selenium methods
│   ├── home_page.py               # Home page — select country, top deals, deal of day
│   └── headphones_page.py         # Headphones page — subcategory, add to cart, open cart
│
├── tests/                         # All test files
│   ├── __init__.py                # Package init file
│   ├── test_1_e2e_cases.py        # 1 test — full E2E flow in one browser
│   ├── test_2_positive_cases.py   # 7 individual positive tests in 7 separate browsers
│   └── test_3_negative_cases.py   # 3 negative test cases in 3 separate browsers
│
├── test_data/                     # Test data files
│   └── headphone_categories.xlsx  # Excel file with headphone category names
│
├── utilities/                     # Utility/helper files
│   ├── __init__.py                # Package init file
│   ├── excel_utils.py             # Reads Excel and returns a random category
│   ├── logger.py                  # Logger setup — single log file for all tests
│   └── screenshot_utils.py        # Screenshot utility with timestamp
│
├── reports/                       # Test reports folder
│   ├── allure_reports/            # Raw Allure data saved here by pytest
│   ├── allure_reports_html/
│   │   └── index.html             # Allure single-file report — open directly in browser
│   └── html_reports/
│       └── report.html            # pytest-html report — open directly in browser
│
├── screenshots/                   # All 11 screenshots saved after every run
│   ├── positive_e2e_test_complete_cart.png
│   ├── positive_test_01_bestbuy_website.png
│   ├── positive_test_02_united_states.png
│   ├── positive_test_03_top_deals.png
│   ├── positive_test_04_headphones.png
│   ├── positive_test_05_random_headphone_category.png
│   ├── positive_test_06_add_to_cart.png
│   ├── positive_test_07_cart_summary.png
│   ├── negative_test_1_wrong_website_url.png
│   ├── negative_test_2_wrong_country.png
│   └── negative_test_3_wrong_section.png
│
├── logs/                          # Log files folder
│   └── test_run_YYYYMMDD_HHMMSS.log   # One log file generated per test run
│
├── conftest.py                    # pytest fixture — browser setup, teardown, allure generate
├── pytest.ini                     # pytest configuration and test paths
├── requirements.txt               # All required Python packages
├── run_tests.bat                  # Batch file to run all tests on Windows
├── .gitignore                     # Git ignore file
└── README.md                      # Project documentation

---

## How the Framework Works

### Browser Behaviour
Every single test gets its own fresh browser.
Browser opens at the start of each test and closes when that test finishes.
This is controlled by scope="function" in conftest.py.
Total browsers opened per full run = 11 (1 E2E + 7 Positive + 3 Negative).

### Random Category Selection
excel_utils.py reads test_data/headphone_categories.xlsx and picks a random category
using random.choice(). This means every run can test a different category:

    Run 1  ->  Wireless
    Run 2  ->  Wired
    Run 3  ->  Noise-Cancelling
    Run 4  ->  Open-Ear
    Run 5  ->  Sports

If the selected category is not found on the page, the code automatically falls back to Wireless.

---

## Test Files

### test_1_e2e_cases.py — End to End Flow
One browser opens, runs all 7 steps in sequence, then closes.
1 screenshot taken at the last page (Cart page).

### test_2_positive_cases.py — Individual Positive Tests
7 separate browsers open and close one by one.
Each test builds one step more than the previous.
1 screenshot taken per browser at its last page.
Total 7 screenshots generated.

### test_3_negative_cases.py — Negative Tests
3 separate browsers open and close one by one.
Each test intentionally does the wrong action to verify negative behavior.
1 screenshot taken per browser at its last page.
Total 3 screenshots generated.

---

## Test Cases

### test_1_e2e_cases.py — End to End (1 browser, 7 steps)

| Step | Action                          | Expected Result                       |
|------|---------------------------------|---------------------------------------|
| TC01 | Open BestBuy website            | bestbuy.com opens successfully        |
| TC02 | Select United States            | US homepage loads                     |
| TC03 | Click Top Deals                 | Top Deals page opens                  |
| TC04 | Click Headphones                | Headphones On Sale page opens         |
| TC05 | Click random category (Excel)   | Selected category page opens          |
| TC06 | Add 2 products to Cart          | 2 products added successfully         |
| TC07 | Open Cart / Order Summary       | Cart page opens with screenshot saved |

---

### test_2_positive_cases.py — Individual Positive Tests (7 browsers)

| Test    | Browser   | Steps Done                                                                      | Last Page Screenshot       |
|---------|-----------|---------------------------------------------------------------------------------|----------------------------|
| test_01 | Browser 1 | Open BestBuy                                                                    | BestBuy homepage           |
| test_02 | Browser 2 | Open BestBuy -> Select US                                                       | US homepage                |
| test_03 | Browser 3 | Open BestBuy -> Select US -> Top Deals                                          | Top Deals page             |
| test_04 | Browser 4 | Open BestBuy -> Select US -> Top Deals -> Headphones                            | Headphones page            |
| test_05 | Browser 5 | Open BestBuy -> Select US -> Top Deals -> Headphones -> Random Category (Excel) | Random category page       |
| test_06 | Browser 6 | Full flow -> Add to Cart                                                        | Listing page after add     |
| test_07 | Browser 7 | Full flow -> Add to Cart -> Open Cart                                           | Cart page                  |

---

### test_3_negative_cases.py — Negative Tests (3 browsers)

| Test | Wrong Action                                    | What is Verified              | Result |
|------|-------------------------------------------------|-------------------------------|--------|
| NC01 | Opens misspelled BestBuy URL (bastbiy.com)      | bestbuy.com NOT in URL        | PASSED |
| NC02 | Selects Canada instead of United States         | united-states NOT in URL      | PASSED |
| NC03 | Clicks Deal of the Day instead of Top Deals     | top-deals NOT in URL          | PASSED |

Note — Negative tests are designed to do the wrong action intentionally.
The test PASSES when the wrong behavior is confirmed.
This proves the validation logic is working correctly.

---

## Screenshots

11 screenshots are automatically saved in the screenshots/ folder after every run.
One screenshot per browser — taken at the last page before browser closes.

| Screenshot                                 | Test           | Last Page Captured              |
|--------------------------------------------|----------------|---------------------------------|
| positive_e2e_test_complete_cart            | test_1         | Cart / Order Summary page       |
| positive_test_01_bestbuy_website           | test_2 -> TC01 | BestBuy homepage                |
| positive_test_02_united_states             | test_2 -> TC02 | US homepage                     |
| positive_test_03_top_deals                 | test_2 -> TC03 | Top Deals page                  |
| positive_test_04_headphones                | test_2 -> TC04 | Headphones On Sale page         |
| positive_test_05_random_headphone_category | test_2 -> TC05 | Random category page            |
| positive_test_06_add_to_cart               | test_2 -> TC06 | Listing page after add to cart  |
| positive_test_07_cart_summary              | test_2 -> TC07 | Cart / Order Summary page       |
| negative_test_1_wrong_website_url          | test_3 -> NC01 | Misspelled BestBuy URL page     |
| negative_test_2_wrong_country              | test_3 -> NC02 | BestBuy Canada page             |
| negative_test_3_wrong_section              | test_3 -> NC03 | Deal of the Day page            |

---

## Logs

Logs are automatically saved in the logs/ folder after every test run.
All 11 test logs are written into one single log file per run.

| What is Logged                   | Example                                                            |
|----------------------------------|--------------------------------------------------------------------|
| Browser started and closing      | Browser started. / Browser closing.                                |
| Each test step with result       | PASSED — BestBuy website opened successfully                       |
| URL confirmation at each step    | Top Deals page URL: https://www.bestbuy.com/top-deals              |
| Categories loaded from Excel     | Categories loaded from Excel: ['Wireless', 'Wired', ...]           |
| Randomly selected category       | Randomly selected category: Noise-Cancelling                       |
| Products found on page           | Found 18 products.                                                 |
| Products added to cart           | Product 1 added to cart successfully.                              |
| Cart items visible               | Cart items visible: 2                                              |
| Negative test verification       | Negative verification — bestbuy.com absent from URL: True          |
| Screenshot saved confirmation    | Screenshot saved: screenshots/positive_test_01_..._143012.png      |
| Allure report generated          | Allure report ready — open reports/allure_reports_html/index.html  |

Log file location:

    logs/test_run_YYYYMMDD_HHMMSS.log

---

## Technologies Used

| Technology         | Purpose                        |
|--------------------|--------------------------------|
| Python 3.x         | Programming language           |
| Selenium WebDriver | Browser automation             |
| pytest             | Test framework                 |
| pytest-html        | HTML report generation         |
| webdriver-manager  | Auto ChromeDriver management   |
| openpyxl           | Reading Excel test data        |
| PyYAML             | Configuration file reading     |
| allure-pytest      | Allure report integration      |

---

## How to Install

Step 1 — Extract the project folder

Step 2 — Install all required packages:

    pip install -r requirements.txt

---

## How to Run

Run all tests:

    python -m pytest

This single command automatically:

- Runs all 11 test cases
- Generates pytest-html report at reports/html_reports/report.html
- Saves raw Allure data to reports/allure_reports/
- Generates Allure single-file report at reports/allure_reports_html/index.html
- Saves 11 screenshots in screenshots/
- Saves log file in logs/

---

## How to View Reports

Both reports open with a simple double-click — no command needed:

Allure Report:

    reports/allure_reports_html/index.html

HTML Report:

    reports/html_reports/report.html

---

## Expected Test Results

    tests/test_1_e2e_cases.py::test_complete_positive_flow                    PASSED
    tests/test_2_positive_cases.py::test_01_open_bestbuy_website              PASSED
    tests/test_2_positive_cases.py::test_02_select_united_states              PASSED
    tests/test_2_positive_cases.py::test_03_click_top_deals                   PASSED
    tests/test_2_positive_cases.py::test_04_click_headphones                  PASSED
    tests/test_2_positive_cases.py::test_05_click_random_headphone_category   PASSED
    tests/test_2_positive_cases.py::test_06_add_products_to_cart              PASSED
    tests/test_2_positive_cases.py::test_07_open_cart_order_summary           PASSED
    tests/test_3_negative_cases.py::test_wrong_website_url                    PASSED
    tests/test_3_negative_cases.py::test_wrong_country_selected               PASSED
    tests/test_3_negative_cases.py::test_wrong_section_clicked                PASSED

    11 passed

---

## Author

Ashish Kumar
Wipro Capstone Project
Automation Testing using Selenium WebDriver and pytest