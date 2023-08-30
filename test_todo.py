from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Привет кто это")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("где я?")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    # ---------------------
    context.close()
    browser.close()


