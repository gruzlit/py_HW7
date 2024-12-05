from selenium.webdriver.common.by import By

class MainPage:

 def __init__(self, driver):
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    self._driver.implicitly_wait(4)
    self._driver.maximize_window()

 def data_entry(self):
    self._driver.find_element(By.CSS_SELECTOR, "[name = first-name]").send_keys("Иван")
    self._driver.find_element(By.CSS_SELECTOR, "[name = last-name]").send_keys("Петров")
    self._driver.find_element(By.CSS_SELECTOR, "[name = address]").send_keys("Ленина, 55-3")
    self._driver.find_element(By.CSS_SELECTOR, "[name = e-mail]").send_keys("test@skypro.com")
    self._driver.find_element(By.CSS_SELECTOR, "[name = phone]").send_keys("+7985899998787")
    self._driver.find_element(By.CSS_SELECTOR, "[name = zip-code]").send_keys("")
    self._driver.find_element(By.CSS_SELECTOR, "[name = city]").send_keys("Москва")
    self._driver.find_element(By.CSS_SELECTOR, "[name = country]").send_keys("Россия")
    self._driver.find_element(By.CSS_SELECTOR, "[name = job-position]").send_keys("QA")
    self._driver.find_element(By.CSS_SELECTOR, "[name = company]").send_keys("SkyPro")

 def search_button(self):
    self._driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

 def get_color(self):
      color = self._driver.find_element(By.CSS_SELECTOR, "[id = zip-code]").value_of_css_property("color")
      assert color == "rgba(132, 32, 41, 1)"

 def get_color2(self):
     elements = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
     for i in elements:
         color = self._driver.find_element(By.CSS_SELECTOR, "[id=%s]" % i).value_of_css_property("color")

     assert color == "rgba(15, 81, 50, 1)"

 def close_driver(self):
     self._driver.quit()