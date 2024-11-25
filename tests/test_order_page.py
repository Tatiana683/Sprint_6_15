import pytest
from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import GenerateData
from data import Constants
import allure

@allure.title('Проверка создания заказа с разных точек входа на страницу оформления заказа')
class TestOrderPage:
    @allure.description('В кейсе проверяется позитивный сценарий создания заказа с проверкой текста в модальном окне')
    @pytest.mark.parametrize(
        'locator, num, text',
        [
            (MainPageLocators.BUTTON_ORDER_IN_THE_HEADER, GenerateData.choice_of_metro_station(),
             GenerateData.choice_of_rental_period()),
            (MainPageLocators.BUTTON_ORDER_IN_THE_MIDDLE, GenerateData.choice_of_metro_station(),
             GenerateData.choice_of_rental_period())
        ]
    )
    def test_create_order(self, driver, locator, num, text):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        order_page.create_order(num, text)
        assert 'Заказ оформлен' in order_page.check_created_order()
