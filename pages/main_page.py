from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    @allure.step('Получение текста вопроса в дроп.меню "Вопросы о важном"')
    def click_to_question(self, num):
        locator_q_formated = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formated)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formated = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formated)

    @allure.step('Проверка ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)
