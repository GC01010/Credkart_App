import time
from pageObjects.checkout_path import Test_Checkout_path

class Test_checkout:

    def test_checkout01(self,login_ficture,driver_setup):
        self.driver=driver_setup

        cp=Test_Checkout_path(self.driver)
        time.sleep(2)
        cp.Click_macbookpro()
        time.sleep(2)
        cp.Enter_Firstname("Jethalal")
        cp.Enter_Lastname("Gada")
        cp.Enter_Phone("1234567890")
        cp.Enter_Address("Pune, Maharashtra, India, Earth")
        cp.Enter_Zipcode("411413")
        cp.Select_State("Delhi")
        cp.Enter_Owner("Credence")
        cp.Enter_CVV("043")
        cp.Enter_CardNumber("5281")
        cp.Enter_CardNumber("0370")
        cp.Enter_CardNumber("4891")
        cp.Enter_CardNumber("6168")
        cp.Select_Year("2025")
        cp.Select_Month("May")
        cp.Click_Checkout()
        if cp.Verify_Success_Message()== "Your order has been placed successfully.":
            assert True
        else:
            assert False




