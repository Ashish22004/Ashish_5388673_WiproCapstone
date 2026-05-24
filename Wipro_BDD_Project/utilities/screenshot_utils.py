import os
from datetime import datetime
from utilities.logger import get_logger

logger = get_logger(__name__)


def take_screenshot(driver, name):

    # Save all screenshots directly in screenshots/ folder — no subfolders
    folder = "screenshots"

    # Create folder if it does not exist
    os.makedirs(folder, exist_ok=True)

    # Create screenshot filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    # Take and save screenshot
    driver.save_screenshot(filepath)
    logger.info("Screenshot saved: %s", filepath)

    return filepath