from selenium import webdriver
import pytest
import allure


@allure.title("Print the page source of the page")

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("http://thetestingacademy.com")
    print(driver.page_source)
