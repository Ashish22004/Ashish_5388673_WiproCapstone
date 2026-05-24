# Wipro BDD Project — BestBuy Behave Automation

## Project Overview

This project is a BDD (Behavior-Driven Development) test automation framework built for the Wipro BDD Project.
It automates the end-to-end shopping flow on the BestBuy website using Python, Selenium WebDriver, and Behave.
The framework follows the Page Object Model (POM) design pattern for clean and maintainable code.
Test scenarios are written in plain English (Gherkin), making them readable by both technical and non-technical stakeholders.

The main highlight of this project is the random headphone category selection — instead of always
clicking the same category, the framework reads categories from an Excel file and picks one randomly
on every run, making tests dynamic and realistic.

---

## Project Structure

Wipro_BDD_Project/
│
├── config/                        # Configuration folder
│   ├── __init__.py                # Package init file
│   ├── config.py                  # Loads configuration from qa.yaml
│   └── qa.yaml                    # Base URL, wait times, browser settings
│
├── features/                      # BDD feature files and step definitions
│   ├── positive_cases.feature     # 7 positive test scenarios (TC01–TC07)
│   ├── negative_cases.feature     # 3 negative test scenarios (NC01–NC03)
│   ├── e2e.feature                # 1 full end-to-end scenario
│   ├── environment.py             # before_scenario / after_scenario / after_all hooks
│   └── steps/                     # Step definition files
│       ├── __init__.py            # Package init file
│       ├── common_steps.py        # All shared Given/When steps — used by all suites
│       ├── positive_steps.py      # Then steps for TC01–TC06
│       ├── negative_steps.py      # Then steps for NC01–NC03
│       └── e2e_steps.py           # Then step for cart page — used by TC07 and E2E
│
├── pages/                         # Page Object Model classes
│   ├── __init__.py                # Package init file
│   ├── base_page.py               # Base class with reusable Selenium methods
│   ├── home_page.py               # Home page — select country, top deals, deal of day
│   └── headphones_page.py         # Headphones page — subcategory, add to cart, open cart
│
├── test_data/                     # Test data files
│   └── headphone_categories.xlsx  # Excel file with headphone category names
│
├── utilities/                     # Utility/helper files
│   ├── __init__.py                # Package init file
│   ├── excel_utils.py             # Reads Excel and returns a random category
│   ├── logger.py                  # Logger setup — single log file for all scenarios
│   └── screenshot_utils.py        # Screenshot utility with timestamp
│
├── reports/                       # Test reports folder
│   ├── allure_reports/            # Raw Allure data saved here by Behave
│   └── allure_reports_html/
│       └── index.html             # Allure single-file report — open directly in browser
│
├── screenshots/                   # All 11 screenshots saved after every run
│   ├── e2e__cart_order_summary_page.png
│   ├── tc01__bestbuy_homepage_loaded.png
│   ├── tc02__united_states_homepage.png
│   ├── tc03__top_deals_page_opened.png
│   ├── tc04__headphones_category_page.png
│   ├── tc05__open-ear_category_page.png
│   ├── tc06__products_added_to_cart.png
│   ├── tc07__cart_order_summary_page.png
│   ├── nc01__wrong_url_page.png
│   ├── nc02__wrong_country_canada.png
│   └── nc03__wrong_section_deal_of_the_day.png
│
├── logs/                          # Log files folder
│   └── test_run_YYYYMMDD_HHMMSS.log   # One log file generated per test run
│
├── behave.ini                     # Behave configuration — paths, verbose, capture settings
├── requirements.txt               # All required Python packages
├── run_tests.py                   # Main runner — cleans old data, runs Behave, generates report
├── run_tests.bat                  # Windows one-click launcher — activates venv and runs
└── README.md                      # Project documentation

---

## How the Framework Works

### Browser Behaviour
Every single scenario gets its own fresh browser.
Browser opens at the start of each scenario and closes when that scenario finishes.
This is controlled by before_scenario and after_scenario hooks in features/environment.py.
Total browsers opened per full run = 11 (7 Positive + 3 Negative + 1 E2E).

### Random Category Selection
excel_utils.py reads test_data/headphone_categories.xlsx and picks a random category
using random.choice(). This means every run can test a different category:

    Run 1  ->  Wireless
    Run 2  ->  Wired
    Run 3  ->  Noise-Cancelling
    Run 4  ->  Open-Ear
    Run 5  ->  Sports

If the selected category is not found on the page, the code automatically falls back to Wireless.

### Step Reuse
All Given and When steps are written once in common_steps.py and shared across all three
feature files. No step is duplicated. The Then steps are split by suite — positive_steps.py,
negative_steps.py, and e2e_steps.py — keeping assertions cleanly separated.

---

## Feature Files

### positive_cases.feature — Individual Positive Tests
7 scenarios run in 7 separate browsers, one by one.
Each scenario builds one step more than the previous.
1 screenshot taken per scenario at its last page.
Total 7 screenshots generated.

### negative_cases.feature — Negative Tests
3 scenarios run in 3 separate browsers, one by one.
Each scenario intentionally does the wrong action to verify negative behavior.
1 screenshot taken per scenario at its last page.
Total 3 screenshots generated.

### e2e.feature — End to End Flow
One browser opens, runs all 7 steps in sequence, then closes.
1 screenshot taken at the last page (Cart page).

---

## Test Scenarios

### positive_cases.feature — Individual Positive Tests (7 browsers)

| Scenario | Browser   | Steps Done                                                                      | Last Page Screenshot |
|----------|-----------|---------------------------------------------------------------------------------|----------------------|
| TC01     | Browser 1 | Open BestBuy                                                                    | BestBuy homepage     |
| TC02     | Browser 2 | Open BestBuy -> Select US                                                       | US homepage          |
| TC03     | Browser 3 | Open BestBuy -> Select US -> Top Deals                                          | Top Deals page       |
| TC04     | Browser 4 | Open BestBuy -> Select US -> Top Deals -> Headphones                            | Headphones page      |
| TC05     | Browser 5 | Open BestBuy -> Select US -> Top Deals -> Headphones -> Random Category (Excel) | Random category page |
| TC06     | Browser 6 | Full flow -> Add to Cart                                                        | Listing page         |
| TC07     | Browser 7 | Full flow -> Add to Cart -> Open Cart                                           | Cart page            |

---

### negative_cases.feature — Negative Tests (3 browsers)

| Scenario | Wrong Action                                 | What is Verified         | Result |
|----------|----------------------------------------------|--------------------------|--------|
| NC01     | Opens misspelled BestBuy URL (bastbiy.com)   | bestbuy.com NOT in URL   | PASSED |
| NC02     | Selects Canada instead of United States      | united-states NOT in URL | PASSED |
| NC03     | Clicks Deal of the Day instead of Top Deals  | top-deals NOT in URL     | PASSED |

Note — Negative scenarios are designed to do the wrong action intentionally.
The scenario PASSES when the wrong behavior is confirmed.
This proves the validation logic is working correctly.

---

### e2e.feature — End to End (1 browser, 7 steps)

| Step | Action                        | Expected Result                       |
|------|-------------------------------|---------------------------------------|
| TC01 | Open BestBuy website          | bestbuy.com opens successfully        |
| TC02 | Select United States          | US homepage loads                     |
| TC03 | Click Top Deals               | Top Deals page opens                  |
| TC04 | Click Headphones              | Headphones On Sale page opens         |
| TC05 | Click random category (Excel) | Selected category page opens          |
| TC06 | Add 2 products to Cart        | 2 products added successfully         |
| TC07 | Open Cart / Order Summary     | Cart page opens with screenshot saved |

---

## Screenshots

11 screenshots are automatically saved in the screenshots/ folder after every run.
One screenshot per scenario — taken at the last step before the browser closes.

| Screenshot                          | Scenario    | Last Page Captured             |
|-------------------------------------|-------------|--------------------------------|
| tc01__bestbuy_homepage_loaded       | TC01        | BestBuy homepage               |
| tc02__united_states_homepage        | TC02        | US homepage                    |
| tc03__top_deals_page_opened         | TC03        | Top Deals page                 |
| tc04__headphones_category_page      | TC04        | Headphones On Sale page        |
| tc05__open-ear_category_page        | TC05        | Random category page           |
| tc06__products_added_to_cart        | TC06        | Listing page after add to cart |
| tc07__cart_order_summary_page       | TC07        | Cart / Order Summary page      |
| nc01__wrong_url_page                | NC01        | Misspelled URL page            |
| nc02__wrong_country_canada          | NC02        | BestBuy Canada page            |
| nc03__wrong_section_deal_of_the_day | NC03        | Deal of the Day page           |
| e2e__cart_order_summary_page        | E2E         | Cart / Order Summary page      |

---

## Logs

Logs are automatically saved in the logs/ folder after every test run.
All 11 scenario logs are written into one single log file per run.

| What is Logged                  | Example                                                         |
|---------------------------------|-----------------------------------------------------------------|
| Scenario start and finish       | SCENARIO STARTING: TC01 / SCENARIO FINISHED: TC01 PASSED       |
| Browser launched and closed     | Chrome browser launched successfully / Browser closed           |
| Each step action with result    | PASSED — BestBuy website opened successfully                    |
| URL confirmation at each step   | Top Deals page URL: https://www.bestbuy.com/top-deals           |
| Categories loaded from Excel    | Categories loaded from Excel: ['Wireless', 'Wired', ...]        |
| Randomly selected category      | Randomly selected category: Open-Ear                            |
| Products found on page          | Found 18 products.                                              |
| Products added to cart          | Product 1 added to cart successfully.                           |
| Cart items visible              | Cart items visible: 2                                           |
| Negative test verification      | NC01 PASSED — WRONG URL VALIDATION SUCCESSFUL                   |
| Screenshot saved confirmation   | Screenshot saved: screenshots/tc01__bestbuy_homepage_..._png    |
| Log attached to Allure          | Logs attached to Allure                                         |

Log file location:

    logs/test_run_YYYYMMDD_HHMMSS.log

---

## Technologies Used

| Technology            | Purpose                        |
|-----------------------|--------------------------------|
| Python 3.9+           | Programming language           |
| Selenium WebDriver    | Browser automation             |
| Behave                | BDD framework                  |
| Allure Behave         | Allure report integration      |
| behave-html-formatter | HTML report generation         |
| webdriver-manager     | Auto ChromeDriver management   |
| openpyxl              | Reading Excel test data        |
| PyYAML                | Configuration file reading     |

---

## How to Install

Step 1 — Extract the project folder

Step 2 — Install all required packages:

    pip install -r requirements.txt

---

## How to Run

### Option 1 — run_tests.bat (Recommended — Windows One-Click)

Double-click run_tests.bat from Windows Explorer, OR run from Command Prompt:

    run_tests.bat

What run_tests.bat does internally:

    @echo off
    call .venv\Scripts\activate
    python run_tests.py
    pause

It automatically activates the virtual environment, runs all tests, and keeps the terminal open.

---

### Option 2 — Python Runner

    python run_tests.py

This single command automatically:

- Cleans old screenshots, logs, and reports before the run
- Runs all 11 scenarios
- Saves raw Allure data to reports/allure_reports/
- Generates Allure single-file report at reports/allure_reports_html/index.html
- Saves 11 screenshots in screenshots/
- Saves log file in logs/

---

### Option 3 — Run by Tag

    python -m behave --tags=positive
    python -m behave --tags=negative
    python -m behave --tags=e2e

---

### Option 4 — Run Behave Directly with Allure Output

    python -m behave -f allure_behave.formatter:AllureFormatter -o reports/allure_reports

Generate HTML report after the above command:

    allure generate reports/allure_reports --single-file -o reports/allure_reports_html --clean

---

## How to View Reports

Allure Report — open directly in browser (double-click):

    reports/allure_reports_html/index.html

Note — The Allure CLI must be installed separately and available on PATH.
If allure command is not found, the HTML report step will silently skip.

---

## Expected Test Results

    features/positive_cases.feature  Scenario: TC01 — Open BestBuy website                   PASSED
    features/positive_cases.feature  Scenario: TC02 — Select United States                   PASSED
    features/positive_cases.feature  Scenario: TC03 — Click Top Deals                        PASSED
    features/positive_cases.feature  Scenario: TC04 — Click Headphones category              PASSED
    features/positive_cases.feature  Scenario: TC05 — Select random headphone category       PASSED
    features/positive_cases.feature  Scenario: TC06 — Add products to cart                   PASSED
    features/positive_cases.feature  Scenario: TC07 — Open cart page                         PASSED
    features/negative_cases.feature  Scenario: NC01 — Wrong website URL                      PASSED
    features/negative_cases.feature  Scenario: NC02 — Wrong country selected                 PASSED
    features/negative_cases.feature  Scenario: NC03 — Wrong section clicked                  PASSED
    features/e2e.feature             Scenario: Complete positive flow — open BestBuy to cart  PASSED

    11 scenarios passed

---

## Author

Ashish Kumar
Wipro BDD Project
Behavior-Driven Development using Behave and Selenium WebDriver