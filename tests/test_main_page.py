import pytest
from pages.main_page import MainPage
from conftest import driver
from data import Constants
import allure

@allure.title('Проверка соответствия текста ответов на вопросы в аккордеон-меню блока "Вопрос о важном"')

class TestMainPage:

    @allure.description('В кейсе проверяется аккордеон меню при клике на элементы и соответствие текста')
    @pytest.mark.parametrize(
        'num, result',
        Constants.accordion_on_main_page
    )
    def test_question_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.url_main_page)
        main_page.check_question_and_answer(num)
        assert main_page.get_answer_text(num) == result
