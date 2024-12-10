from selenium.webdriver.common.by import By

class Registeration_path_class:
    name_Xpath = "//input[@id='name']"
    email_xpath = "//input[@id='email']"
    password_xpath = "//input[@id='password']"
    confirm_password_xpath = "//input[@id='password-confirm']"
    reg_button_Xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver


    def Enter_Name(self, name):
        self.driver.find_element(By.XPATH, self.name_Xpath).send_keys(name)
    # def enter_name(self,name):
        # self.driver.find_element(By.Xpath,self.name_Xpath).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_password)

    def click_Register(self):
        self.driver.find_element(By.XPATH,self.reg_button_Xpath).click()


