@echo off

:: ============================================================
:: run_tests.bat — Wipro Capstone Project
:: Double click this file on Windows to run all tests
:: ============================================================

echo ========================================
echo    Wipro Capstone Project - BestBuy
echo    Selenium Automation Test Runner
echo ========================================
echo.

echo Activating virtual environment...
call .venv\Scripts\activate

echo.
echo Running all tests...
echo.
python -m pytest -v

echo.
echo Generating Allure HTML report...
allure generate reports\allure_reports --single-file -o reports\allure_reports_html
echo Done — Allure report ready.
echo.

echo.
echo ========================================
echo    Test Run Complete
echo ========================================
echo.

echo Tests Run : 11 total
echo   E2E      : 1  test  (test_1_e2e_cases.py)
echo   Positive : 7  tests (test_2_positive_cases.py)
echo   Negative : 3  tests (test_3_negative_cases.py)
echo.

echo HTML Report saved at:
echo reports\html_reports\report.html
echo.

echo Allure Report saved at:
echo reports\allure_reports_html\index.html
echo (double-click index.html to open in browser — no command needed)
echo.

echo Screenshots saved at:
echo screenshots\
echo.

echo Logs saved at:
echo logs\
echo.

pause