import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    elif browser=="headless":
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(options=chrome_options)
    else:
        driver=webdriver.Chrome()

    request.cls.driver=driver
    yield driver
    driver.quit()



from pageObjects.Login_path import Login_Page_Class
@pytest.fixture
def login_ficture(driver_setup):
     driver=driver_setup
     driver.get("https://automation.credence.in/login")
     lp=Login_Page_Class(driver)
     lp.login_email("Credencetest@test.com")
     lp.login_password("Credence@123")
     lp.login_button()
     return driver


