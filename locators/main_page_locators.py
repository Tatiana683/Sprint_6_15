from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, ".//div[@id = 'accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, ".//div[@aria-labelledby = 'accordion__heading-{}']"
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, ".//div[@id = 'accordion__heading-7']"
    LOGO_SCOOTER = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    LOGO_YANDEX = By.XPATH, './/a[@rel = "noopener noreferrer"]'
    BUTTON_ORDER_IN_THE_HEADER = By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]'
    BUTTON_ORDER_IN_THE_MIDDLE = By.XPATH, './/div[@class = "Home_FinishButton__1_cWm"] / button[text() = "Заказать"]'
    DESCRIPTION_ON_MAIN_PAGE = By.XPATH, './/div[contains(text(), "Самокат")]'
