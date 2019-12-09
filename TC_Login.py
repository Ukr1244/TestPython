from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import by
# This example requires Selenium WebDriver 3.13 or newer

# driver=webdriver.firefox("E:\GeckoDriver\geckodriver.exe")
driver = webdriver.Chrome("E:\SeleniumQuickStart\drivers\chromedriver.exe")
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

# Starting Chat with Order Catalog items

driver.find_element_by_id("order_catalog").click()
driver.find_element_by_id("chat-input").clear()
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-4")))
OrderCatalogResp1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[3]/div")\
    .get_attribute('textContent')
print(OrderCatalogResp1)
assert "What would you like to order?" in OrderCatalogResp1
print("Test Case step 1 passed")

driver.find_element_by_id("chat-input").send_keys("Iphone"+Keys.ENTER)

WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-6")))
OrderCatalogResp2=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[5]/div")\
    .get_attribute('textContent')

assert "I could find the following" in OrderCatalogResp2
print("Test Case step 2 passed")
# driver.find_element_by_id("chat-input").send_keys("iphone")

# Starting Chat get incidents
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("chat-input").send_keys("get Incidents"+Keys.ENTER)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-8")))
GetIncidentsResp1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[7]/div")\
    .get_attribute('textContent')
print("Response"+GetIncidentsResp1)
assert "incidents" in GetIncidentsResp1
print("Test Case Get Incidents passed")

# Starting Chat get PTO
time.sleep(3)
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("chat-input").send_keys("get PTO"+Keys.ENTER)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-11")))
GetPTOResp1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[10]/div")\
    .get_attribute('textContent')
print("Response"+GetPTOResp1)
assert "Your PTO" in GetPTOResp1
print("Test Case Get PTO passed")

# Starting Chat get Approvals
time.sleep(3)
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("chat-input").send_keys("get Approvals"+Keys.ENTER)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-13")))
GetApprovalsResp1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[12]/div")\
    .get_attribute('textContent')
print("Response"+GetApprovalsResp1)
assert "approvals" in GetApprovalsResp1
print("Test Case Get Approvals passed")

# Starting Chat get holiday Calender
time.sleep(5)
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("chat-input").send_keys("get Holiday calender"+Keys.ENTER)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-15")))
GetHolidaysResp = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[14]/div")\
    .get_attribute('textContent')
print("Response"+GetHolidaysResp)
assert "holidays" in GetHolidaysResp
print("Test Case Get Holidays Calender passed")

#driver.find_element_by_id("chat-input").send_keys("Iphone"+Keys.ENTER)

#WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by.By.ID, "cm-msg-6")))
#OrderCatalogResp2=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[5]/div")\
 #   .get_attribute('textContent')

#assert "I could find the following" in OrderCatalogResp2
#print("Test Case step 2 passed")