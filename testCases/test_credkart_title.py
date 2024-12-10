from utilities.Readdata import Read_data

class Test_Login_credkart:
    def test_login_credkart(self,driver_setup):
        login_url=Read_data.login_url()
        print(login_url)
        self.driver=driver_setup
        self.driver.get(login_url)
        print(f"title is {self.driver.title}")
        if self.driver.title == "CredKart":
            print("title is correct")
        else:
            assert False,"Title is Incorrect"

