from selenium.webdriver.common.by import By


class Cart_amount_path:
        Applemacbook_xpath="//img[@src='https://automation.credence.in/img/macbook-pro.jpg']"
        Addto_cart_macbook="//input[@value='Add to Cart']"
        continue_shoping="//a[@class='btn btn-primary btn-lg']"
        Xbox_path="//h3[normalize-space()='Xbox One']"
        Addcart_xbox="//input[@value='Add to Cart']"

        appleprice="//td[normalize-space()='$2299.99']"
        xbox_price="//td[normalize-space()='$449.99']"

        subtotal="//td[normalize-space()='$2,749.98']"
        tax="//td[normalize-space()='$357.50']"
        anual_total="//td[@class='table-bg']"

        checkout_form="//h1[normalize-space()='Checkout form']"


        row_on_page="//table/tbody/tr"

        def __init__(self,driver):
            self.driver=driver

        def applemacbook_click(self):
            self.driver.find_element(By.XPATH,self.Applemacbook_xpath).click()

        def addcart_mac(self):
            self.driver.find_element(By.XPATH,self.Addto_cart_macbook).click()

        def continiue_shop(self):
            self.driver.find_element(By.XPATH,self.continue_shoping).click()

        def xboc_path(self):
            self.driver.find_element(By.XPATH,self.Xbox_path).click()

        def add_cart_xbox(self):
            self.driver.find_element(By.XPATH,self.Addcart_xbox).click()

        def macname_page(self,count):
            mac_namee=self.driver.find_element(By.XPATH,f"//table/tbody/tr[{count}]/td[2]").text
            return mac_namee

        def xboxname_page(self,count):
            xbox_name_page = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{count}]/td[2]").text
            return xbox_name_page

        def mac_price(self,count):
            return self.driver.find_element(By.XPATH, f"//table/tbody/tr[{count}]/td[4]").text

        def xbox_price(self,count):
            return self.driver.find_element(By.XPATH, f"//table/tbody/tr[{count}]/td[4]").text
        def sub_total(self):
            return self.driver.find_element(By.XPATH, self.subtotal).text

        def tax(self):
            return self.driver.find_element(By.XPATH, self.tax).text

        def anual_total(self):
            return self.driver.find_element(By.XPATH, self.anual_total).text

        def total_row(self):
            self.driver.get("https://automation.credence.in/cart")
            length_row=self.driver.find_elements(By.TAG_NAME,"tr")
            return len(length_row)

