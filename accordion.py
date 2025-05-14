from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Accordion(BasePage):


    SECTION_1_TEXT = (By.CSS_SELECTOR, "#section1Content > p")
    SECTION_1_HEADING = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_2_P1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    SECTION_2_P2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
    SECTION_3_P = (By.CSS_SELECTOR, "#section3Content > p")

    def __init__(self, browser, url):
        super().__init__(browser, url)
