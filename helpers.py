import random
from locators.order_page_locators import OrderLocators

class GenerateData:
    def choice_of_metro_station():
        metro_station = random.choice([0, 1, 2, 3, 4, 5, 6])
        return metro_station
    def choice_of_rental_period():
        rental_period = random.choice(['сутки', 'двое суток', 'трое суток', 'четверо суток'])
        return rental_period

    def choice_color_of_scooter():
        color_scooter = random.choice([OrderLocators.BLACK_COLOR_SCOOTER, OrderLocators.GREY_COLOR_SCOOTER])
        return color_scooter
