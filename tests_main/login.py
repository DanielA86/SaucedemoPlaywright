from playwright.sync_api import Playwright, sync_playwright, expect

class LoginTest:
    def __init__(self, page):
        self.page = page

    def login(self, username: str, password: str):
        self.page.goto("https://www.saucedemo.com/")
        expect(self.page.locator("#user-name")).to_be_visible()
        self.page.locator("#user-name").fill(username)
        self.page.locator("[data-test=\"password\"]").fill(password)
        self.page.locator("[data-test=\"login-button\"]").click()
        expect(self.page.locator("#logout_sidebar_link")).to_be_enabled()

