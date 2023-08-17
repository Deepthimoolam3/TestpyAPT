import os
from pyats import aetest
from pyats.easypy import run

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the email address to send test results
TO_EMAIL = 'deepthi.moolam@vcti.io'

# Define the test class
class ShoppingWebsiteTest(aetest.Testcase):

    @aetest.test
    def test_pass(self):
        driver = webdriver.Chrome()
        driver.get('https://www.amazon.in')
        driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("ebooks free")
        valid=driver.find_element(By.XPATH,"//*[@id='search']/span[2]/div/h1/div/div[1]/div/div/span[3]")
        valid=valid.text()
        if "ebooks free" in  valid:
            pass
            print("Test case passed")
        else:
            print("Test case failed")
        driver.quit()

    @aetest.skip('Skipping this test case')
    def test_skip(self):
        pass

    @aetest.test
    def test_fail(self):
        driver = webdriver.Chrome()
        driver.get('https://www.amazon.in')
        driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys("ebooks free")
        valid = driver.find_element(By.XPATH, "//*[@id='search']/span[2]/div/h1/div/div[1]/div/div/span[3]")
        valid = valid.text()
        if "ebooks free" in valid:
            pass
            print("Test case passed")
        else:
            print("Test case failed")
        driver.quit()

    @aetest.test
    def test_pass_again(self):
        driver = webdriver.Chrome()
        driver.get('https://www.amazon.in')
        driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys("ebooks free")
        valid = driver.find_element(By.XPATH, "//*[@id='search']/span[2]/div/h1/div/div[1]/div/div/span[3]")
        valid = valid.text()
        if "ebooks free" in valid:
            pass
            print("Test case passed")
        else:
            print("Test case failed")

        driver.quit()

if __name__ == '__main__':
# Run the tests and send results to email
    run(testscript=ShoppingWebsiteTest,
    email=[TO_EMAIL],
    easypy_config={'log_dir': os.path.join(os.getcwd(), 'logs')})