from playwright.sync_api import Playwright, sync_playwright, expect
from pytest_playwright.pytest_playwright import browser

from tests_main.login import LoginTest
import pytest

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),])
   # ("locked_out_user", "secret_sauce"),
  #  ("problem_user", "secret_sauce"),])


def test_login(playwright: Playwright, username, password) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        # Create an instance of LoginTest
        login_test = LoginTest(page)

        # Run login with user
        login_test.login(username, password)
        # return valdiate xy

        # Cleanup
        context.close()
        browser.close()

#will change and remove later
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),])

def test_buy_product(playwright: Playwright, username, password) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        login_test = LoginTest(page)
        login_test.login(username, password)
        page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        expect(page.locator(".shopping_cart_badge")).to_be_visible()
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")
        page.locator("[data-test=\"shopping-cart-link\"]").click()
        page.locator("[data-test=\"checkout\"]").click()
        page.locator("[data-test=\"firstName\"]").fill("dan")
        page.locator("[data-test=\"lastName\"]").fill("and")
        page.locator("[data-test=\"postalCode\"]").fill("2223")
        page.locator("[data-test=\"continue\"]").click()
        page.locator("[data-test=\"finish\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        expect(page.locator(".shopping_cart_badge")).not_to_be_visible()
        page.locator("#react-burger-menu-btn").click()
        page.locator("#logout_sidebar_link").click()
