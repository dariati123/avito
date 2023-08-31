from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
    favourite = page.locator("button").filter(has_text="Добавить в избранное")
    favourite.click()
    page.get_by_role("link", name="Избранное", exact=True).click()
    name_text = page.locator("strong").filter(has_text="Domain-Driven Design Distilled Vaughn Vernon")
    expect(name_text).to_contain_text("Domain-Driven Design Distilled Vaughn Vernon")
    expect(favourite.page).to_have_url('https://www.avito.ru/favorites')

    # -----------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
