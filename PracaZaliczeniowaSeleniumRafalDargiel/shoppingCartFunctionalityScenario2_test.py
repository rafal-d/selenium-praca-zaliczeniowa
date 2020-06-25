import unittest
from selenium import webdriver

class BasektFunctionalityScenario_2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://lawif.pl")
        self.driver.set_window_size(1920,1080)

    def tearDown(self):
        self.driver.quit()

    # Test Case no.1 Add product to cart
    def testAddProductToCart_TC1(self):
        driver = self.driver
        itemMenuGadzetyReklamowe = driver.find_element_by_xpath('//a[contains(@class,"no-click")]//span[text()="Gadżety reklamowe"]')
        webdriver.ActionChains(driver).move_to_element(itemMenuGadzetyReklamowe).perform()
        itemMenuRozwin = driver.find_element_by_xpath('//li[contains(@class,"nav-1-1-1")]//span[text()="rozwiń"]')
        webdriver.ActionChains(driver).move_to_element(itemMenuRozwin).perform()
        itemMenuApteczki = driver.find_element_by_xpath('//li[contains(@class,"nav-1-1-1-2")]//span[text()="Apteczki"]')
        itemMenuApteczki.click()
        #************** SELECT PRODUCT **************
        categoryProducts = driver.find_elements_by_xpath('//div[@class="category-products"]//li[@class="item"]')
        print(len(categoryProducts))
        for product in range(len(categoryProducts)):
            if product == 0:
                categoryProducts[product].click()
        #************** SELECT PRODUCT OPTIONS **************
        # Please select product colors
        checkboxProductColor = driver.find_element_by_xpath('//div[@class="input-box"]//span[@class="label"]//label[text()="niebieski "]')
        checkboxProductColor.click()
        # Price with one color print, 1 page
        radioOneColorOnePage = driver.find_element_by_id('options_10566_2')
        radioOneColorOnePage.click()
        # Courier cost
        radioCostOfDelivery = driver.find_element_by_id('options_10565_2')
        radioCostOfDelivery.click()
        # Add to quote button
        btnAddToQuote = driver.find_element_by_id('product-addtocart-button')
        btnAddToQuote.click()
        msgAddedProductToCart = driver.find_element_by_xpath('//div[@class="cart"]//li[@class="success-msg"]//li')
        #************** ASSERT **************
        assert msgAddedProductToCart.text == 'Apteczka turystyczna Basic was added to your shopping cart.', 'Wrong message - Added product to cart'
        print('The expected result has been correctly implemented, the user received information that')
        print(msgAddedProductToCart.text)
        print('Test Case no.1 is correct')
    # Test Case no.2 Remove product from basket
    def testRemoveProductFromBasket_TC2(self):
        driver = self.driver
        itemMenuGadzetyReklamowe = driver.find_element_by_xpath('//a[contains(@class,"no-click")]//span[text()="Gadżety reklamowe"]')
        webdriver.ActionChains(driver).move_to_element(itemMenuGadzetyReklamowe).perform()
        itemMenuRozwin = driver.find_element_by_xpath('//li[contains(@class,"nav-1-1-1")]//span[text()="rozwiń"]')
        webdriver.ActionChains(driver).move_to_element(itemMenuRozwin).perform()
        itemMenuApteczki = driver.find_element_by_xpath('//li[contains(@class,"nav-1-1-1-2")]//span[text()="Apteczki"]')
        itemMenuApteczki.click()
        #************** SELECT PRODUCT **************
        categoryProducts = driver.find_elements_by_xpath('//div[@class="category-products"]//li[@class="item"]')
        print(len(categoryProducts))
        for product in range(len(categoryProducts)):
            if product == 0:
                categoryProducts[product].click()
        #************** SELECT PRODUCT OPTIONS **************
        # Please select product colors
        checkboxProductColor = driver.find_element_by_xpath('//div[@class="input-box"]//span[@class="label"]//label[text()="niebieski "]')
        checkboxProductColor.click()
        # Price with one color print, 1 page
        radioOneColorOnePage = driver.find_element_by_id('options_10566_2')
        radioOneColorOnePage.click()
        # Courier cost
        radioCostOfDelivery = driver.find_element_by_id('options_10565_2')
        radioCostOfDelivery.click()
        # Add to quote button
        btnAddToQuote = driver.find_element_by_id('product-addtocart-button')
        btnAddToQuote.click()
        # Remove product
        btnRemove = driver.find_element_by_xpath('//td[@class="col-delete a-center last"]/a[@class="btn-remove btn-remove2"]')
        btnRemove.click()
        msgProductRemovedFromCart = driver.find_element_by_class_name('page-title')
        #************** ASSERT **************
        assert msgProductRemovedFromCart.text == 'Koszyk jest pusty', 'Wrong message - Basket is empty'
        print('The expected result has been correctly implemented, the user received information that')
        print(msgProductRemovedFromCart.text)
        print('Test Case no.2 is correct')


if __name__ == '__main__':
    unittest.main(verbosity=2)
