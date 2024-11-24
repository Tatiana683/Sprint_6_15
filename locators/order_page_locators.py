from selenium.webdriver.common.by import By

class OrderLocators:
    NAME_FIELD = By.XPATH, './/input[@placeholder = "* Имя"]'
    SURNAME_FIELD = By.XPATH, './/input[@placeholder = "* Фамилия"]'
    ADDRESS_FIELD = By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]'
    METRO_STATION_FIELD = By.XPATH, './/input[@placeholder = "* Станция метро"]'
    METRO_STATION_CHOICE = By.XPATH, './/li[@data-index = "{}"]'
    TELEPHONE_NUMBER_FIELD = By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]'
    BUTTON_NEXT = By.XPATH, './/button[text() = "Далее"]'
    TIME_OF_DELIVERY_FIELD = By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]'
    RENTAL_TERM_FIELD = By.XPATH, './/div[@aria-haspopup = "listbox"]'
    RENTAL_TERM_CHOICE = By.XPATH, './/div[text() = "{}"]'
    BLACK_COLOR_SCOOTER = By.ID, 'black'
    GREY_COLOR_SCOOTER = By.ID, 'grey'
    BUTTON_CREATE_ORDER = By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]'
    BUTTON_CONFIRMATION_ORDER = By.XPATH, './/button[text() = "Да"]'
    SUCCESSFUL_ORDER_HEADLINE = By.XPATH, './/div[text()= "Заказ оформлен"]'
