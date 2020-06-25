from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest

# test data
firstName = "Kamila"
lastName = "Kowalska"
email = "kamilaK@o2.pl"
nip = "123456789"
password = "kkamila"
# bad test data
badEmail = "kamilaK.pl"
badPassword = "kk"
rePassword = "kk1"


class RegistrationNewUserScenario_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://lawif.pl")
        self.driver.set_window_size(1920,1080)

    def tearDown(self):
        self.driver.quit()
    
    # Test case no.1: Registration new user with bad e-mail
    def testRegistrationNewUserWithBadEmail_TC1(self):
        driver = self.driver
        myAccount = driver.find_element_by_xpath('//div[@id="header-account"]//a[text()="Moje konto"]')
        myAccount.click()
        btnCreateAccount = driver.find_element_by_xpath('//div[@class="buttons-set"]//button[@title="Utwórz konto"]')
        btnCreateAccount.click()
        inputName = driver.find_element_by_id('firstname')
        inputName.send_keys(firstName)
        inputLastName = driver.find_element_by_id('lastname')
        inputLastName.send_keys(lastName)
        inputBadEmail = driver.find_element_by_id('email_address')
        inputBadEmail.send_keys(badEmail)
        inputNIP = driver.find_element_by_id('taxvat')
        inputNIP.send_keys(nip)
        inputPassword = driver.find_element_by_id('password')
        inputPassword.send_keys(password)
        inputRePassword = driver.find_element_by_id('confirmation')
        inputRePassword.send_keys(password)
        btnSend = driver.find_element_by_xpath('//div[@class="buttons-set"]//button[@title="Wyślij"]')
        btnSend.click()
        alertValidEmail = driver.find_element_by_id('advice-validate-email-email_address')
        # ************************ ASSERT ************************ 
        assert alertValidEmail.text == 'Prosimy o wprowadzenie poprawnego adresu e-mail. Dla przykładu: jankowalski@domena.pl.'
        print('The expected result was implemented correctly, the user received feedback:')
        print(alertValidEmail.text)
        print('Test Case no.1 is correct')
    # Test case no.2: Registration new user with bad password
    def testRegistrationNewUserWithBadPassword_TC2(self):    
        driver = self.driver
        myAccount = driver.find_element_by_xpath('//div[@id="header-account"]//a[text()="Moje konto"]')
        myAccount.click()
        btnCreateAccount = driver.find_element_by_xpath('//div[@class="buttons-set"]//button[@title="Utwórz konto"]')
        btnCreateAccount.click()
        inputName = driver.find_element_by_id('firstname')
        inputName.send_keys(firstName)
        inputLastName = driver.find_element_by_id('lastname')
        inputLastName.send_keys(lastName)
        inputEmail = driver.find_element_by_id('email_address')
        inputEmail.send_keys(email)
        inputNIP = driver.find_element_by_id('taxvat')
        inputNIP.send_keys(nip)
        inputBadPassword = driver.find_element_by_id('password')
        inputBadPassword.send_keys(badPassword)
        inputRePassword = driver.find_element_by_id('confirmation')
        inputRePassword.send_keys(password)
        btnSend = driver.find_element_by_xpath('//div[@class="buttons-set"]//button[@title="Wyślij"]')
        btnSend.click()
        alertValidatePassword = driver.find_element_by_id('advice-validate-password-password')
        # ************************ ASSERT ************************ 
        assert alertValidatePassword.text == 'Please enter 6 or more characters without leading or trailing spaces.'
        print('The expected result was implemented correctly, the user received feedback:')
        print(alertValidatePassword.text)
        print('Test Case no.2 is correct')
     # Test case no.3: Registration new user with bad repeat password
    def testRegistrationNewUserWithBadRepeatPassword_TC3(self):    
        driver = self.driver
        myAccount = driver.find_element_by_xpath('//div[@id="header-account"]//a[text()="Moje konto"]')
        myAccount.click()
        btnCreateAccount = driver.find_element_by_xpath('//div[@class="buttons-set"]//button[@title="Utwórz konto"]')
        btnCreateAccount.click()
        inputName = driver.find_element_by_id('firstname')
        inputName.send_keys(firstName)
        inputLastName = driver.find_element_by_id('lastname')
        inputLastName.send_keys(lastName)
        inputEmail = driver.find_element_by_id('email_address')
        inputEmail.send_keys(email)
        inputNIP = driver.find_element_by_id('taxvat')
        inputNIP.send_keys(nip)
        inputPassword = driver.find_element_by_id('password')
        inputPassword.send_keys(password)
        inputBadRePassword = driver.find_element_by_id('confirmation')
        inputBadRePassword.send_keys(rePassword)
        btnSend = driver.find_element_by_xpath('//div[@class="buttons-set"]//button[@title="Wyślij"]')
        btnSend.click()
        alertValidateRepeatPassword = driver.find_element_by_id('advice-validate-cpassword-confirmation')
        # ************************ ASSERT ************************ 
        assert alertValidateRepeatPassword.text == 'Prosimy upewnić się, że hasła psują do siebie.'
        print('The expected result was implemented correctly, the user received feedback:')
        print(alertValidateRepeatPassword.text)
        print('Test Case no.3 is correct')    


if __name__ == '__main__':
    unittest.main(verbosity=2)
