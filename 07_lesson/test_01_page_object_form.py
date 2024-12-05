from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage


def test_data_form():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    main_page = MainPage(driver)
    main_page.data_entry()
    main_page.search_button()
    main_page.get_color()
    main_page.get_color2()
    main_page.close_driver()



