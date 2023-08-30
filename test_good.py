from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
    page.locator("button").filter(has_text="Добавить в избранное").click()
    page.get_by_role("link", name="Избранное", exact=True).click()

    # ---------------+-----------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)