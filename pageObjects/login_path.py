
from selenium.webdriver.common.by import By

class Login_Page_Class:
    login_email_Xpath="//input[@id='email']"
    login_password_xpath="//input[@id='password']"
    login_button_xpath="//button[@type='submit']"
    menu_button_xpath="//a[@role='button']"
    logout_button_Xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def login_email(self,email):
        self.driver.find_element(By.XPATH,self.login_email_Xpath).send_keys(email)
    def login_password(self,password):
        self.driver.find_element(By.XPATH,self.login_password_xpath).send_keys(password)
    def login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
    def menu_button(self):
        try:
            self.driver.find_element(By.XPATH,self.menu_button_xpath).click()
            self.driver.find_element(By.XPATH, self.logout_button_Xpath).click()
            return "pass"
        except:
            return "fail"





