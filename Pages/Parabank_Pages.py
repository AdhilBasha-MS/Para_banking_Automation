from selenium import webdriver

from Locators.Locators import Locators

class Parabank_Pages():
    def __init__(self, driver):
        # driver = webdriver.Chrome(executable_path="C:/Software/chromedriver_win32/chromedriver.exe")
        self.driver = driver
        self.register = Locators.Register_xp
        self.firstname = Locators.Firstname_id
        self.Lastname = Locators.Lastname_id
        self.address = Locators.address_id
        self.city = Locators.city_id
        self.state = Locators.state_id
        self.zip = Locators.zip_code_id
        self.phone = Locators.phone_id
        self.snnn = Locators.Snn_id
        self.usernamee = Locators.username_id
        self.pwwd = Locators.pwd_id
        self.conforrm = Locators.conform_id
        self.regisster = Locators.register_xpath
        self.logout = Locators.Logout
        self.usr = Locators.UserName
        self.Pass = Locators.Password
        self.login = Locators.Login_btn
        self.billpaaye = Locators.billpay_xp
        self.Paeename = Locators.Payeename_name
        self.addressee = Locators.addressss_name
        self.cityname = Locators.city_name
        self.statename = Locators.state_name
        self.zipname = Locators.zipcode_name
        self.phonename = Locators.phone_name
        self.accountname = Locators.accountname_name
        self.verifyacc = Locators.verifyaccount_name
        self.amount = Locators.amount_name
        self.sendpay = Locators.sendpayment_xp
        self.opennewaccount = Locators.Opennewaccount_xpath
        self.accounttype = Locators.Accounttype_id
        self.existingaccount = Locators.Existingaccount_id
        self.newaccount = Locators.Newaccount_xpath
        self.message_icon = Locators.messageicon_lt
        self.name = Locators.name_id
        self.email = Locators.email_id
        self.phonenumber = Locators.Phone_id
        self.message = Locators.message_id
        self.send = Locators.sendtocc_xpath
        self.text = Locators.text_xapth
        self.updater = Locators.updater
        self.mobilen = Locators.mobilen



    def click_register(self):
        self.driver.find_element_by_xpath(self.register).click()

    def firstnaame(self, uname):
        self.driver.find_element_by_id(self.firstname)
        self.driver.find_element_by_id(self.firstname).send_keys(uname)

    def lazstname(self, aaa):
        self.driver.find_element_by_id(self.Lastname)
        self.driver.find_element_by_id(self.Lastname).send_keys(aaa)

    def addressw(self, www):
        self.driver.find_element_by_id(self.address)
        self.driver.find_element_by_id(self.address).send_keys(www)

    def cityy(self, uuu):
        self.driver.find_element_by_id(self.city)
        self.driver.find_element_by_id(self.city).send_keys(uuu)

    def states(self, iii):
        self.driver.find_element_by_id(self.state)
        self.driver.find_element_by_id(self.state).send_keys(iii)

    def zipcode(self, oo):
        self.driver.find_element_by_id(self.zip)
        self.driver.find_element_by_id(self.zip).send_keys(oo)

    def phonen(self, pp):
        self.driver.find_element_by_id(self.phone)
        self.driver.find_element_by_id(self.phone).send_keys(pp)

    def snnno(self, u):
        self.driver.find_element_by_id(self.snnn)
        self.driver.find_element_by_id(self.snnn).send_keys(u)

    def usname(self, ty):
        self.driver.find_element_by_id(self.usernamee)
        self.driver.find_element_by_id(self.usernamee).send_keys(ty)

    def pwd(self, ll):
        self.driver.find_element_by_id(self.pwwd)
        self.driver.find_element_by_id(self.pwwd).send_keys(ll)

    def confo(self, k):
        self.driver.find_element_by_id(self.conforrm)
        self.driver.find_element_by_id(self.conforrm).send_keys(k)

    def clickregi(self):
        self.driver.find_element_by_xpath(self.regisster).click()

    def Logo(self):
        self.driver.find_element_by_xpath(self.logout).click()

    def Usr(self,l):
        self.driver.find_element_by_xpath(self.usr)
        self.driver.find_element_by_xpath(self.usr).send_keys(l)

    def Pas(self,j):
        self.driver.find_element_by_xpath(self.Pass)
        self.driver.find_element_by_xpath(self.Pass).send_keys(j)

    def Logi(self):
        self.driver.find_element_by_xpath(self.login).click()

    def bill(self):
        self.driver.find_element_by_xpath(self.billpaaye).click()

    def paee(self, eee):
        self.driver.find_element_by_name(self.Paeename)
        self.driver.find_element_by_name(self.Paeename).send_keys(eee)

    def add(self, mm):
        self.driver.find_element_by_name(self.addressee)
        self.driver.find_element_by_name(self.addressee).send_keys(mm)

    def cityn(self, qqq):
        self.driver.find_element_by_name(self.cityname)
        self.driver.find_element_by_name(self.cityname).send_keys(qqq)

    def statees(self, lp):
        self.driver.find_element_by_name(self.statename)
        self.driver.find_element_by_name(self.statename).send_keys(lp)

    def zipnee(self, uy):
        self.driver.find_element_by_name(self.zipname)
        self.driver.find_element_by_name(self.zipname).send_keys(uy)

    def phonees(self, kk):
        self.driver.find_element_by_name(self.phonename)
        self.driver.find_element_by_name(self.phonename).send_keys(kk)

    def accountee(self, ijn):
        self.driver.find_element_by_name(self.accountname)
        self.driver.find_element_by_name(self.accountname).send_keys(ijn)

    def verifyv(self, lb):
        self.driver.find_element_by_name(self.verifyacc)
        self.driver.find_element_by_name(self.verifyacc).send_keys(lb)

    def amo(self, nm):
        self.driver.find_element_by_name(self.amount)
        self.driver.find_element_by_name(self.amount).send_keys(nm)

    def sendp(self):
        self.driver.find_element_by_xpath(self.sendpay).click()

    def clickopennew(self):
        self.driver.find_element_by_xpath(self.opennewaccount).click()

    def accountty(self, ppp):
        self.driver.find_element_by_id(self.accounttype)
        self.driver.find_element_by_id(self.accounttype).send_keys(ppp)

    def existingacc(self, sln):
        self.driver.find_element_by_id(self.existingaccount)
        self.driver.find_element_by_id(self.existingaccount).send_keys(sln)

    def clickopen(self):
        self.driver.find_element_by_xpath(self.newaccount).click()

    def clickicon(self):
        self.driver.find_element_by_link_text(self.message_icon).click()

    def entername(self, namee):
        self.driver.find_element_by_id(self.name).clear()
        self.driver.find_element_by_id(self.name).send_keys(namee)

    def enteremail(self, mail):
        self.driver.find_element_by_id(self.email).clear()
        self.driver.find_element_by_id(self.email).send_keys(mail)

    def enterphonenumber(self, num):
        self.driver.find_element_by_id(self.phonenumber).clear()
        self.driver.find_element_by_id(self.phonenumber).send_keys(num)

    def entermessage(self, msg):
        self.driver.find_element_by_id(self.message).clear()
        self.driver.find_element_by_id(self.message).send_keys(msg)

    def clicksend(self):
        self.driver.find_element_by_xpath(self.send).click()

    def printtext(self):
        I=self.driver.find_element_by_xpath(self.text).text
        return I





