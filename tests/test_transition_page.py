from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from data import Constants
from locators.main_page_locators import MainPageLocators
from locators.transition_page_locators import TransitionPageLocators
from pages.main_page import MainPage
import allure

@allure.title('Проверка переходов по клику лого "Самокат" и "Яндекс"')
class TestTransitionPages:
    @allure.description('В кейсе проверяется переход на страницы при клике по элементам логотипа')
    def test_of_transition_to_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.url_main_page)
        main_page.click_to_element(MainPageLocators.LOGO_YANDEX)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TransitionPageLocators.LOGO_DZEN_NEWS))

    @allure.description('')
    def test_of_transition_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.url_create_order)
        main_page.click_to_element(MainPageLocators.LOGO_SCOOTER)
        assert "Самокат" in main_page.get_text_from_element(MainPageLocators.DESCRIPTION_ON_MAIN_PAGE)
