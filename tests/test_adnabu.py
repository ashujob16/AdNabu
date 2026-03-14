from pages.adnabu_page import AdnabuPage
from utils.driver_setup import get_driver


def test_adnabu_execute():

    driver = get_driver()

    driver.get("https://adnabu-store-assignment1.myshopify.com/password")

    page = AdnabuPage(driver)

    page.enter_password("AdNabuQA")
    page.click_enter_button()
    page.click_search_icon()
    page.enter_text("Snowboard")
    page.click_search_button()
    page.select_product()
    page.add_to_cart()

    driver.quit()
