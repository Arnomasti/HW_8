class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_visible(self, locator):
        return self.browser.find_element(*locator).is_displayed()

    def find_element(self, locator):
        return self.browser.find_element(*locator)
