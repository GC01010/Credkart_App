from pageObjects.login_path import Login_Page_Class
from utilities.Readdata import Read_data

class Test_Credkart_login002:

    def test_login_page(self,driver_setup):
        self.driver=driver_setup
        self.url=Read_data.login_url()

        self.lp = Login_Page_Class(self.driver)
        self.driver.get(self.url)

        email=Read_data.login_username()
        password=Read_data.login_Password()

        self.lp.login_email(email)
        self.lp.login_password(password)
        self.lp.login_button()

        if self.lp.menu_button()=="pass":
            assert True
            print("user logged in")
        else:
            print("user not logged in ")
            assert False





