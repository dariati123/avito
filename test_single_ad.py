from playwright.sync_api import Page, expect


def test_add_ad_to_favourites(page: Page):
    ad_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    page.goto(ad_url)
    ad_title = page.locator(".title-info-title-text").inner_text()
    page.locator("button").filter(has_text="Добавить в избранное").click()
    page.get_by_role("link", name="Избранное", exact=True).click()
    ad_locator = page.locator("strong").filter(has_text=ad_title)
    expect(ad_locator).to_contain_text(ad_title)
    ad_locator.click()
    expect(page).to_have_url(ad_url)
