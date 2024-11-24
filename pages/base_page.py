from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу по URL')
    def go_to_page(self, driver, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием по локатору')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу, найденному по локатору')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста в элемент, найденному по локатору')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Клик по кнопке Enter')
    def click_Enter(self, locator):
        self.find_element_with_wait(locator).send_keys(Keys.ENTER)

    @allure.step('Получение текста из элемента, найденного по локатору')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Перемещение по странице к элементу, найденному по локатору')
    def scroll_to_element(self, locator):
        element= self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Подстановка значения num в форматируемый текст')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step('Подстановка значения text в форматируемый текст')
    def format_locators_text(self, locator, text):
        method, locator = locator
        locator = locator.format(text)
        return (method, locator)
