from playwright.sync_api import Playwright, sync_playwright, expect
from tests_main.login import LoginTest
import pytest

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),])


def test_login(playwright: Playwright, username, password) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Create an instance of LoginTest
        login_test = LoginTest(page)

        # Run login with user
        login_test.login(username, password)

        # Cleanup
        context.close()
        browser.close()


#with sync_playwright() as playwright:
 #   test_login(playwright)
