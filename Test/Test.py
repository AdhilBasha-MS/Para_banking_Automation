import time
import unittest

from selenium import webdriver

from Pages.Parabank_Pages import Parabank_Pages
from Utilities.Excel_operation import ExcelUtil


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path="C:/Software 1/edgedriver_win64 (1)/msedgedriver.exe")
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.driver.maximize_window()

    def test_Para_Register(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(2,1))
        SOS.lazstname(exl.readData(2,2))
        SOS.addressw(exl.readData(2,3))
        SOS.cityy(exl.readData(2,4))
        SOS.states(exl.readData(2,5))
        SOS.zipcode(exl.readData(2,6))
        SOS.phonen(exl.readData(2,7))
        SOS.snnno(exl.readData(2,8))
        SOS.usname(exl.readData(2,9))
        SOS.pwd(exl.readData(2,10))
        SOS.confo(exl.readData(2,11))
        SOS.clickregi()
        time.sleep(2)
        A=self.driver.find_element_by_xpath("//p[text()='Your account was created successfully. You are now logged in.']").text
        print(A)
        exp1 = "Your account was created successfully. You are now logged in."
        act1 = A
        self.assertEqual(exp1, act1)


    def test_para_Register1(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(5,1))
        SOS.lazstname(exl.readData(5,2))
        SOS.addressw(exl.readData(5,3))
        SOS.cityy(exl.readData(5,4))
        SOS.states(exl.readData(5,5))
        SOS.zipcode(exl.readData(5,6))
        SOS.phonen(exl.readData(5,7))
        SOS.snnno(exl.readData(5,8))
        SOS.usname(exl.readData(5,9))
        SOS.pwd(exl.readData(5,10))
        SOS.confo(exl.readData(5,11))
        SOS.clickregi()
        time.sleep(2)
        B = self.driver.find_element_by_xpath("//p[text()='Your account was created successfully. You are now logged in.']").text
        print(B)
        exp2 = "Your account was created successfully. You are now logged in."
        act2 = B
        self.assertEqual(exp2, act2)

    def test_Para_Login(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(8,1))
        SOS.lazstname(exl.readData(8,2))
        SOS.addressw(exl.readData(8,3))
        SOS.cityy(exl.readData(8,4))
        SOS.states(exl.readData(8,5))
        SOS.zipcode(exl.readData(8,6))
        SOS.phonen(exl.readData(8,7))
        SOS.snnno(exl.readData(8,8))
        SOS.usname(exl.readData(8,9))
        SOS.pwd(exl.readData(8,10))
        SOS.confo(exl.readData(8,11))
        SOS.clickregi()
        SOS.Logo()
        SOS.Usr(exl.readData(8,12))
        SOS.Pas(exl.readData(8,13))
        SOS.Logi()
        C = self.driver.find_element_by_xpath("//h1[@class='title']").text
        print(C)
        exp3 = "Accounts Overview"
        act3 = C
        self.assertEqual(exp3, act3)

    def test_Para_Login1(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(11,1))
        SOS.lazstname(exl.readData(11,2))
        SOS.addressw(exl.readData(11,3))
        SOS.cityy(exl.readData(11,4))
        SOS.states(exl.readData(11,5))
        SOS.zipcode(exl.readData(11,6))
        SOS.phonen(exl.readData(11,7))
        SOS.snnno(exl.readData(11,8))
        SOS.usname(exl.readData(11,9))
        SOS.pwd(exl.readData(11,10))
        SOS.confo(exl.readData(11,11))
        SOS.clickregi()
        SOS.Logo()
        SOS.Usr(exl.readData(11,12))
        SOS.Pas(exl.readData(11,13))
        SOS.Logi()
        D = self.driver.find_element_by_xpath("//h1[@class='title']").text
        print(D)
        exp4 = "Accounts Overview"
        act4 = D
        self.assertEqual(exp4, act4)

    def test_Para_Billpay(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(14,1))
        SOS.lazstname(exl.readData(14,2))
        SOS.addressw(exl.readData(14,3))
        SOS.cityy(exl.readData(14,4))
        SOS.states(exl.readData(14,5))
        SOS.zipcode(exl.readData(14,6))
        SOS.phonen(exl.readData(14,7))
        SOS.snnno(exl.readData(14,8))
        SOS.usname(exl.readData(14,9))
        SOS.pwd(exl.readData(14,10))
        SOS.confo(exl.readData(14,11))
        SOS.clickregi()
        SOS.bill()
        SOS.paee(exl.readData(14,12))
        SOS.add(exl.readData(14,13))
        SOS.cityn(exl.readData(14,14))
        SOS.statees(exl.readData(14,15))
        SOS.zipnee(exl.readData(14,16))
        SOS.phonees(exl.readData(14,17))
        SOS.accountee(exl.readData(14,18))
        SOS.verifyv(exl.readData(14,19))
        SOS.amo(exl.readData(14,20))
        SOS.sendp()
        E=self.driver.find_element_by_xpath("//h1[text()='Bill Payment Service']").text
        print(E)
        exp5 = "Bill Payment Service"
        act5 = E
        self.assertEqual(exp5,act5)

    def test_para_Billpay1(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(17,1))
        SOS.lazstname(exl.readData(17,2))
        SOS.addressw(exl.readData(17,3))
        SOS.cityy(exl.readData(17,4))
        SOS.states(exl.readData(17,5))
        SOS.zipcode(exl.readData(17,6))
        SOS.phonen(exl.readData(17,7))
        SOS.snnno(exl.readData(17,8))
        SOS.usname(exl.readData(17,9))
        SOS.pwd(exl.readData(17,10))
        SOS.confo(exl.readData(17,11))
        SOS.clickregi()
        SOS.bill()
        SOS.paee(exl.readData(17,12))
        SOS.add(exl.readData(17,13))
        SOS.cityn(exl.readData(17,14))
        SOS.statees(exl.readData(17,15))
        SOS.zipnee(exl.readData(17,16))
        SOS.phonees(exl.readData(17,17))
        SOS.accountee(exl.readData(17,18))
        SOS.verifyv(exl.readData(17,19))
        SOS.amo(exl.readData(17,20))
        SOS.sendp()
        F = self.driver.find_element_by_xpath("//h1[text()='Bill Payment Service']").text
        print(F)
        exp6 = "Bill Payment Service"
        act6 = F
        self.assertEqual(exp6, act6)

    def test_Para_Opennewacc(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(20,1))
        SOS.lazstname(exl.readData(20,2))
        SOS.addressw(exl.readData(20,3))
        SOS.cityy(exl.readData(20,4))
        SOS.states(exl.readData(20,5))
        SOS.zipcode(exl.readData(20,6))
        SOS.phonen(exl.readData(20,7))
        SOS.snnno(exl.readData(20,8))
        SOS.usname(exl.readData(20,9))
        SOS.pwd(exl.readData(20,10))
        SOS.confo(exl.readData(20,11))
        SOS.clickregi()
        SOS.clickopennew()
        SOS.accountty(exl.readData(20,11))
        SOS.existingacc(exl.readData(20,12))
        SOS.clickopen()
        G = self.driver.find_element_by_xpath("//p[text()='Congratulations, your account is now open.']").text
        print(G)
        Exp7 = "Congratulations, your account is now open."
        Act7 = G
        self.assertEqual(Exp7, Act7)

    def test_Para_opennewacc1(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame(exl.readData(23,1))
        SOS.lazstname(exl.readData(23,2))
        SOS.addressw(exl.readData(23,3))
        SOS.cityy(exl.readData(23,4))
        SOS.states(exl.readData(23,5))
        SOS.zipcode(exl.readData(23,6))
        SOS.phonen(exl.readData(23,7))
        SOS.snnno(exl.readData(23,8))
        SOS.usname(exl.readData(23,9))
        SOS.pwd(exl.readData(23,10))
        SOS.confo(exl.readData(23,11))
        SOS.clickregi()
        SOS.clickopennew()
        SOS.accountty(exl.readData(23,12))
        SOS.existingacc(exl.readData(23,13))
        SOS.clickopen()
        H = self.driver.find_element_by_xpath("//p[text()='Congratulations, your account is now open.']").text
        print(H)
        Exp8 = "Congratulations, your account is now open."
        Act8 = H
        self.assertEqual(Exp8, Act8)

    def test_para_contact_us(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        lp = Parabank_Pages(self.driver)
        lp.clickicon()
        lp.entername(exl.readData(26,1))
        lp.enteremail(exl.readData(26,2))
        lp.enterphonenumber(exl.readData(26,3))
        time.sleep(2)
        lp.entermessage(exl.readData(26,4))
        lp.clicksend()
        time.sleep(2)
        exp9 = "A Customer Care Representative will be contacting you."
        act9 = lp.printtext()
        self.assertEqual(exp9, act9)
        time.sleep(2)

    def test_para_contact_us1(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/n.muthumanickam/OneDrive - HCL Technologies Ltd/Desktop/New folder/Testdata.xlsx")
        lp = Parabank_Pages(self.driver)
        lp.clickicon()
        lp.entername(exl.readData(29,1))
        lp.enteremail(exl.readData(29,2))
        lp.enterphonenumber(exl.readData(29,3))
        time.sleep(2)
        lp.entermessage(exl.readData(29,4))
        lp.clicksend()
        time.sleep(2)
        exp10 = "A Customer Care Representative will be contacting you."
        act10 = lp.printtext()
        self.assertEqual(exp10, act10)
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()

