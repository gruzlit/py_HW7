from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CalcPage:

    def __init__(self, driver):
        self._driver = driver


    def open_pages(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id = delay]").clear()
        self._driver.find_element(By.CSS_SELECTOR, "[id = delay]").send_keys("45")

    def data_entry(self):
        self._driver.find_element(By.XPATH, ('//span[text()="7"]')).click()
        self._driver.find_element(By.XPATH, ('//span[text()="+"]')).click()
        self._driver.find_element(By.XPATH, ('//span[text()="8"]')).click()
        self._driver.find_element(By.XPATH, ('//span[text()="="]')).click()

    def get_result(self):
        WebDriverWait(self._driver, 60).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
                                        )
        res = self._driver.find_element(By.CLASS_NAME, "screen").text
        assert res == "15"

    def close_driver(self):
        self._driver.quit()