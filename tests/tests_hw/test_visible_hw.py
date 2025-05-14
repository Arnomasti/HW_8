import time
from pages.accordion import Accordion

def test_visible_accordion(browser):
    page = Accordion(browser, "https://demoqa.com/accordian")
    page.open()

    assert page.is_visible(page.SECTION_1_TEXT)
    page.find_element(page.SECTION_1_HEADING).click()
    time.sleep(2)
    assert not page.is_visible(page.SECTION_1_TEXT)

def test_visible_accordion_default(browser):
    page = Accordion(browser, "https://demoqa.com/accordian")
    page.open()

    assert not page.is_visible(page.SECTION_2_P1)
    assert not page.is_visible(page.SECTION_2_P2)
    assert not page.is_visible(page.SECTION_3_P)

