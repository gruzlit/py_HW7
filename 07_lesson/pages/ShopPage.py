from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ShopPage:

    def __init__(self, driver):
        self._driver = driver


    def open_pages(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def authorization(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = user-name]").send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, "[id = password]").send_keys("secret_sauce")

    def click_submit(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type = submit]'))
        )

        self._driver.find_element(By.CSS_SELECTOR, "[type = submit]").click()

    def add_product(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-backpack]").click()
        self._driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-bolt-t-shirt]").click()
        self._driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-onesie]").click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = shopping_cart_container]").click()

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = checkout]").click()

    def data_entry(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = first-name]").send_keys("Владимир")
        self._driver.find_element(By.CSS_SELECTOR, "[id = last-name]").send_keys("Ахалкаци")
        self._driver.find_element(By.CSS_SELECTOR, "[id = postal-code]").send_keys("647000")

    def continue_click(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = continue]").click()

    def get_total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        assert total == 'Total: $58.29'

    def click_finish(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = finish]").click()

    def close_driver(self):
        self._driver.quit()