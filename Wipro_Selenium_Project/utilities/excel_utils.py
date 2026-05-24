import openpyxl
import random
import os
from utilities.logger import get_logger

logger = get_logger(__name__)


def get_random_category():

    # Build path to Excel file
    file_path = os.path.join("test_data", "headphone_categories.xlsx")

    # Open Excel file
    workbook = openpyxl.load_workbook(file_path)

    # Get active sheet
    sheet = workbook.active

    # Read all categories from column A — skip first row (heading)
    categories = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0]:
            categories.append(row[0])

    logger.info("Categories loaded from Excel: %s", categories)

    # Randomly select one category
    selected = random.choice(categories)

    logger.info("Randomly selected category: %s", selected)

    return selected