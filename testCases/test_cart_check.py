import time
from pageObjects.cart_amount_path import Cart_amount_path
from utilities.Excelfile import Excel_file

class Test_cart_check():
    def test_cart_check(self,driver_setup):
        self.driver=driver_setup
        self.driver.get("https://automation.credence.in/shop")
        self.ca=Cart_amount_path(self.driver)
        self.ex=Excel_file
        self.ca.applemacbook_click()
        self.ca.addcart_mac()
        self.ca.continiue_shop()
        self.ca.xboc_path()
        self.ca.add_cart_xbox()

        self.path= r"/TestData\Excel_checkout.xlsx"
        max_row=self.ex.max_row_count(self,self.path,"Data")
        print(max_row)

        max_row_tr=self.ca.total_row()
        print(f"{max_row_tr}")

        page_cred=[]
        for i in range(max_row_tr-4):
            page_mac_name=self.ca.macname_page(i+1)
            page_cred.append(page_mac_name)
        for i in range(max_row_tr - 1):
            mac_price=self.ca.mac_price(i+1)
            page_cred.append(mac_price)
        print(page_cred)

        newlist=[]
        for i in range(len(page_cred)):
            cleaned_item=page_cred[i].replace('$','').replace(',','')
            try:
                newlist.append(cleaned_item)
            except:
                newlist.append(cleaned_item)
        print(newlist)

        macname_Check=self.ex.read_excel_data(self,self.path,"Data",2,1)
        xbox_name_check = self.ex.read_excel_data(self, self.path, "Data", 3, 1)
        mac_price = self.ex.read_excel_data(self, self.path, "Data", 2, 2)
        xbox_price = self.ex.read_excel_data(self, self.path, "Data", 3, 2)
        subtotal = self.ex.read_excel_data(self, self.path, "Data", 2, 3)
        tax = self.ex.read_excel_data(self, self.path, "Data", 3, 4)
        print(f"49 tax is {tax}")
        anual = self.ex.read_excel_data(self, self.path, "Data", 2, 5)

        print(newlist[3])

        total_amount=round(float(float(newlist[2])+float(newlist[3])),2)
        print(f"total is{total_amount}")
        taax=float(newlist[5])
        print(f"tax is {taax}")
        annual=round(float(float(total_amount)+float(taax)),2)
        print(f"anual {annual}")

        self.data="fail"
        try:
            if newlist[0]==macname_Check:
                if newlist[1] == xbox_name_check:
                    if float(newlist[2]) == float(mac_price):
                        if float(newlist[3]) == float(xbox_price):
                            if total_amount == subtotal:
                                if taax == tax:
                                    if annual == anual:
                                        self.data="pass"
                                        self.ex.write_excel_data(self,self.path,"Data",2,6, self.data)
                                        self.ex.write_excel_data(self, self.path, "Data", 3, 6,  self.data)
                                    else:
                                        self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
                                        self.ex.write_excel_data(self, self.path, "Data", 3, 6,self.data)
                                        assert False, "annual amount dosent match"
                                else:
                                    self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
                                    self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
                                    assert False ,"tax dosent match"
                            else:
                                self.ex.write_excel_data(self, self.path, "Data",2 , 6, self.data)
                                self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
                                assert False , "subtotal dosent match"
                        else:
                            self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
                            self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
                            assert False , "xbox price dosent match"
                    else:
                        self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
                        self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
                        assert False ,"mac price dosent match"
                else:
                    self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
                    self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
                    assert False,"Xbox name dosent match"
            else:
                self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
                self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
                assert  False, "Mac book name dosent match"
        except:
            self.ex.write_excel_data(self, self.path, "Data", 2, 6, self.data)
            self.ex.write_excel_data(self, self.path, "Data", 3, 6, self.data)
            assert False ,"Something mismatched"









