import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(3)
    wd.set_window_position(0,-1000)
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.google.com/")
    driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver,10).until(EC.title_is("webdriver - Google Search"))
