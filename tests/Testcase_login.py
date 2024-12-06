from playwright.sync_api import Playwright, sync_playwright, expect
from login_test import LoginTest

def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Create an instance of LoginTest
        login_test = LoginTest(page)

        # Run login test with valid credentials
        login_test.login("standard_user", "secret_sauce")

        # Cleanup
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
