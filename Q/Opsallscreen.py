from behave import *
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
import allure
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://platform-dev.quantuvos.com/login")

driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("opsqdev2021@outlook.com")
driver.find_element_by_name("password").send_keys("Quantuvos@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(5)
#############################Session Screen ##################################
driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[2]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[3]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[4]').click()
time.sleep(5)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[1]').click()
time.sleep(5)
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Scheduled")
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='View']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Close']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='Edit']").click()
time.sleep(2)
driver.find_element_by_xpath(("//select[@name='status']")).click()
time.sleep(2)
driver.find_element_by_xpath("//option[@value='Rescheduling']").click()
time.sleep(2)
driver.find_element_by_xpath(("//select[@name='reason']")).click()
time.sleep(2)
driver.find_element_by_xpath("//option[text()='Qerror']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="uBody"]/modal-container/div/div/form/div[2]/textarea').send_keys("Automate change")
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Submit']").click()
time.sleep(5)

#######################################End of Session Screen ##################################

#################################Customer Screen start############################
time.sleep(5)
driver.find_element_by_xpath("//a[@title='Customers']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[text()='Add']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@name='customerName']").send_keys("Automatecustomer")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='PointOfContact']").send_keys("Seleniumcustomer")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='ContactNo']").send_keys("9876543210")
time.sleep(5)
driver.find_element_by_xpath("Email").send_keys("automate@customer.com")
time.sleep(5)
driver.find_element_by_xpath("//select[@value='Active']").click()
time.sleep(3)
driver.find_element_by_xpath("//option[text()=' Active']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='Submit']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys("AutomateCustomer")
time.sleep(5)
