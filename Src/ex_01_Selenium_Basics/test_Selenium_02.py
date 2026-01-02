from selenium import webdriver
import pytest
import allure


@allure.title("Verify that we are open a page by using selenium")
@allure.description("We will open a page and Verify that we are open a page by using selenium")
def test_first_tc():
    #Selenium 3 Not much used Now
    #driver_path = "Users/prashant.kavinkar/Downloads/chrome/chromedriver
    #driver= webdriver.chromeService(executable_ptah=driver_path)
    driver = webdriver.Chrome()
    driver.get("http://thetestingacademy.com")
    print(driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

