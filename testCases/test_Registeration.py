from pageObjects.Registeation_path import Registeration_path_class
from faker import Faker
from pageObjects.Login_path import Login_Page_Class

class Test_Registeration_class:
    def test_registeration(self,driver_setup):
        faker=Faker()
        self.name=faker.name()
        print(self.name)
        self.email=faker.email()
        print(self.email)
        self.driver=driver_setup
        self.driver.get("https://automation.credence.in/register")
        self.rp=Registeration_path_class(self.driver)
        self.lp=Login_Page_Class(self.driver)
        self.rp.Enter_Name(self.name)
        self.rp.enter_email(self.email)
        self.rp.enter_password("ola123")
        self.rp.enter_confirm_password("ola123")
        self.rp.click_Register()
        if self.lp.menu_button()=="pass":
            print("user registered successfully")
        else:
            print("user not registered")
            assert False






