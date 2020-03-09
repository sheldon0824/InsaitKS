import os.path
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path_mac = os.path.dirname(os.path.abspath('../testCases')) + '/tools/chromedriver'
print(chrome_driver_path_mac)

driver = webdriver.Chrome(chrome_driver_path_mac)
driver.get("https://ks.gengee.com/cn/#/login")
time.sleep(3)

# # driver.fullscreen_window()
# driver.find_element_by_id("username").send_keys("testqa1")
# driver.find_element_by_id("password").send_keys("admin123")
driver.find_element_by_id("username").send_keys("proqa2")
driver.find_element_by_id("password").send_keys("admin123")
driver.find_element_by_xpath("//*/input[@class='dropdown-value']").click()
driver.find_element_by_xpath("//*[@class='dropdown-menu']/li[2]").click()
driver.find_element_by_xpath("//*[@type='submit']").click()
# driver.implicitly_wait(3)
time.sleep(5)
# driver.find_element_by_xpath("//*[@ng-reflect-router-link='/football/player']").click(
driver.find_element_by_xpath("//*[@ng-reflect-router-link='/football/team']").click()
# driver.find_element_by_xpath("//*/ul[@class='li']/li[2]").click()
# time.sleep(5)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='team-content']/div/button[2]").click()
driver.find_element_by_xpath("//*[@class='team pull-left isDelete'][1]").click()
driver.find_element_by_xpath("//*[@id='team-content']/app-alert/div/div/footer/button[1]").click()
# driver.find_element_by_xpath("//*[@class='header team-adder clearfix']/button[1]").click()
# time.sleep(3)
# //*[@id="team-content"]/app-alert/div/div/footer/button[1]
# driver.find_element_by_id("teamName").send_keys(time.strftime("Team%Y%m%d%H%M%S", time.localtime()))
# driver.find_element_by_xpath("//*[@id='colorHome']/div").click()
# driver.find_element_by_xpath("//*[@class='dropdown-menu color-ul clear-fix']/li[9]").click()
# driver.find_element_by_xpath("//*[@id='colorGuest']/div").click()
# driver.find_element_by_xpath("//*[@id='colorGuest']/div/ul/li[1]").click()
# driver.find_element_by_xpath("//*[@class='speed-wrapper clearfix']/div/label[2]").click()
# driver.find_element_by_xpath("//*[@class='btn btn-primary btn-md']").click()
# # time.sleep(3)
# driver.find_element_by_xpath("//*/div[@class='team pull-left']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@class='nav']/ul/li[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@class='btn btn-default btn-add']").click()
# driver.find_element_by_xpath("//*[@class='text-center'][3]").click()
# import excel
# file_excel = os.path.dirname(os.path.abspath('.')) + '/tools/导入模板.xlsx'  # base_page.py
# print(file_excel)
# driver.find_element_by_id("drop-zone").send_keys(file_excel)
# time.sleep(3)
# driver.quit()