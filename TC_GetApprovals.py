from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import by
# This example requires Selenium WebDriver 3.13 or newer


driver = webdriver.Chrome("E:\\SeleniumQuickStart\\drivers\\chromedriver.exe")
wait = WebDriverWait(driver, 10)
driver.get("http://fulton.vsoftconsulting.com")
driver.find_element_by_id("password_protected_pass").clear()
driver.find_element_by_id("password_protected_pass").send_keys("Vsc@321")
driver.find_element_by_id("wp-submit").click()
driver.maximize_window()
# Entering username in sso
driver.find_element_by_id("i0116").click()
driver.find_element_by_id("i0116").clear()
driver.find_element_by_id("i0116").send_keys("upateel@vsoftconsulting.com")
driver.find_element_by_id("idSIButton9").click()
wait = WebDriverWait(driver, 10)
# Entering Password
driver.find_element_by_id("i0118").clear()
driver.find_element_by_id("i0118").send_keys("ukr_1244")
time.sleep(10)
driver.find_element_by_id("idSIButton9").click()
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("idBtn_Back").click()
wait = WebDriverWait(driver, 10)
# Opening chatwindow
driver.find_element_by_xpath("//*[@id='chat-circle']").click()
time.sleep(10)
# Reading from excel
location_TestData = ("C:/Users/VSCBS/Downloads/FultonCounty/FultonTestData.xlsx")
# To open Workbook
wb = xlrd.open_workbook(location_TestData)
sheet = wb.sheet_by_name("GetApprovals")
# Starting Chat get PTO
elementiterator = 2*sheet.nrows
print(elementiterator)
index = 0
for x in range(0, elementiterator, 2):
    y = 4+x
    z = 3+x
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_id("chat-input").send_keys(sheet.cell_value(index, 0) + Keys.ENTER)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-"+str(y))))
    GetApprovalsResp = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div["+str(z)+"]/div") \
            .get_attribute('textContent')
    index = index + 1
    # print("Response :" + GetApprovalsResp)
    # print("Test Case Get Approvals for row " + str(index))
    if GetApprovalsResp.find("approvals") != -1:
        print("Test Case in row " + str(index) + " Passed")
    else:
        print("Test Case in row " + str(index) + " Failed")

