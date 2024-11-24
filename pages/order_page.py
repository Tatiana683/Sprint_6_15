from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage
from helpers import GenerateData
from data import Constants
import allure


class OrderPage(BasePage):
    @allure.step('Заполнение поля "Имя"')
    def filling_field_of_name(self):
        self.add_text_to_element(OrderLocators.NAME_FIELD, Constants.name)

    @allure.step('Заполнение поля "Фамилия')
    def filling_field_of_surname(self):
        self.add_text_to_element(OrderLocators.SURNAME_FIELD, Constants.surname)

    @allure.step('Заполнение поля адреса доставки')
    def filling_field_of_address(self):
        self.add_text_to_element(OrderLocators.ADDRESS_FIELD, Constants.address)

    @allure.step('Выбор станции метро')
    def choice_of_metro_station(self, num):
        self.click_to_element(OrderLocators.METRO_STATION_FIELD)
        locator_m_formated = self.format_locators(OrderLocators.METRO_STATION_CHOICE, num)
        self.click_to_element(locator_m_formated)

    @allure.step('Ввод номера телефона')
    def filling_field_of_phone(self):
        self.add_text_to_element(OrderLocators.TELEPHONE_NUMBER_FIELD, Constants.phone)

    @allure.step('Нажатие на кнопку перехода на следующий этап')
    def transition_on_next_step(self):
        self.click_to_element(OrderLocators.BUTTON_NEXT)

    @allure.step('Заполнение даты доставки')
    def filling_field_of_date_delivery(self):
        self.add_text_to_element(OrderLocators.TIME_OF_DELIVERY_FIELD, Constants.date_delivery)
        self.click_Enter(OrderLocators.TIME_OF_DELIVERY_FIELD)

    @allure.step('Выбор срока аренды')
    def choice_of_rental_term(self, text):
        self.click_to_element(OrderLocators.RENTAL_TERM_FIELD)
        locator_r_formated = self.format_locators_text(OrderLocators.RENTAL_TERM_CHOICE, text)
        self.click_to_element(locator_r_formated)

    @allure.step('Выбор цвета самоката')
    def choice_of_scooter_color(self):
        self.click_to_element(GenerateData.choice_color_of_scooter())

    @allure.step('Нажатие на кнопку завершения оформления заказа')
    def clik_button_completion_of_order(self):
        self.click_to_element(OrderLocators.BUTTON_CREATE_ORDER)

    @allure.step('Клик на кнопку подтверждения заказа')
    def clik_button_confirmation_order(self):
        self.click_to_element(OrderLocators.BUTTON_CONFIRMATION_ORDER)

    @allure.step('Получение текста модального окна')
    def check_created_order(self):
        return self.get_text_from_element(OrderLocators.SUCCESSFUL_ORDER_HEADLINE)


    @allure.step('Создание заказа аренды самоката')
    def create_order(self, num, text):
        self.filling_field_of_name()
        self.filling_field_of_surname()
        self.filling_field_of_address()
        self.choice_of_metro_station(num)
        self.filling_field_of_phone()
        self.transition_on_next_step()
        self.filling_field_of_date_delivery()
        self.choice_of_rental_term(text)
        self.choice_of_scooter_color()
        self.clik_button_completion_of_order()
        self.clik_button_confirmation_order()
        self.check_created_order()
