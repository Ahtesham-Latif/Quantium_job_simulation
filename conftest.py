import pytest
# This file is used to configure pytest for testing the Dash app.
# It sets up the necessary options for running the tests in a headless browser environment.
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.service import Service

def pytest_setup_options():
    # Configure Chrome options for headless testing
    options = Options()
    # Add necessary arguments for headless testing
    options.add_argument("--headless")
    # Add additional options to ensure compatibility in various environments
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options