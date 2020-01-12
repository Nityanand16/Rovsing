from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains



driver = webdriver.Chrome(executable_path="/Users/Nityanand/PycharmProjects/Selenium/Drivers/chromedriver")
#driver = webdriver.firefox(executable_path="/Users/Nityanand/PycharmProjects/Selenium/Drivers/selenium-firefox-driver-2.4.0.jar")
#driver.implicitly_wait(10)
#sleep(2)

#Test1 Cookies Policy Start

driver.get("http://rovsing.dk/")
sleep(2)
driver.find_element_by_class_name('easy-cookies-policy-accept').click()
driver.maximize_window()
sleep(2)

#Test1 End

#Test2.1 Mouse hoover Company menu and click on About us Start

action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
about_us =driver.find_element_by_xpath("//li[@id='menu-item-3004']")
sleep(2)
action.move_to_element(company_menu).move_to_element(about_us).click().perform()
sleep(1)

#Test2.1 End

#Test2.2 click on Board of director Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
board_of_dir = driver.find_element_by_xpath("//li[@id='menu-item-3005']")
action.move_to_element(company_menu).move_to_element(board_of_dir).click().perform()
sleep(2)

#Test2.2 End

#Test2.3 click on Management Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
management = driver.find_element_by_xpath("//li[@id= 'menu-item-3008']")
action.move_to_element(company_menu).move_to_element(management).click().perform()
sleep(2)

#Test2.3 End

#Test2.4 click on Customers Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
customers = driver.find_element_by_xpath("//li[@id= 'menu-item-3007']")
action.move_to_element(company_menu).move_to_element(customers).click().perform()
sleep(2)

#Test2.4 End

#Test2.5 Contact us Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
contact_us = driver.find_element_by_xpath("//li[@id='menu-item-3132']")
action.move_to_element(company_menu).move_to_element(contact_us).click().perform()
sleep(2)

#Test2.5 Contact us End

#Test3.1 Mouse hoover Solutions menu and click on EGSE Systems Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
egse_system = driver.find_element_by_xpath("//li[@id='menu-item-2931']")
action.move_to_element(solutions_menu).move_to_element(egse_system).click().perform()
sleep(2)

#Test3.1 End

#Test3.2.1 Mouse hoover Solutions menu, Products and click on ro5000 Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
ro5000 = driver.find_element_by_xpath("//li[@id='menu-item-3333']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(ro5000).click().perform()
sleep(2)

#Test3.2.1 End

#Test3.2.2 Mouse hoover Solutions menu, Products and click on ro2000 Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
ro2000 = driver.find_element_by_xpath("//li[@id='menu-item-3335']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(ro2000).click().perform()
sleep(2)

#Test3.2.2 End

#Test3.2.3 Mouse hoover Sloutions menu, Products and click on ro1000 Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
ro1000 = driver.find_element_by_xpath("//li[@id='menu-item-3336']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(ro1000).click().perform()
sleep(2)

#Test3.2.3 End

#Test3.2.4 Mouse hoover Solutions menu, Products and click on dste Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
dste = driver.find_element_by_xpath("//li[@id='menu-item-3334']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(dste).click().perform()
sleep(2)

#Test3.2.4

#Test3.3 Mouse hoover on Solution menu and click on Software Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
software = driver.find_element_by_xpath("//li[@id='menu-item-2933']")
action.move_to_element(solutions_menu).move_to_element(software).click().perform()
sleep(2)

#Test3.3

#Test3.4 Mouse hoover on Solutions menu and click on on Board and ground Support Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
obgs = driver.find_element_by_xpath("//li[@id='menu-item-2934']")
action.move_to_element(solutions_menu).move_to_element(obgs).click().perform()
sleep(2)

#Test3.4 End

#Test3.5 Mouse hoover on Solutions menu and click on on Site Engineering Support Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
oses = driver.find_element_by_xpath("//li[@id='menu-item-2935']")
action.move_to_element(solutions_menu).move_to_element(oses).click().perform()
sleep(2)

#Test3.5 End

#Test3.6 Mouse hoover on Solutions menu and click on Software Verification And Validation Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
vavs = driver.find_element_by_xpath("//li[@id='menu-item-2936']")
action.move_to_element(solutions_menu).move_to_element(vavs).click().perform()
sleep(2)

#Test3.6 End

driver.save_screenshot("screenshort.png")

print ()
sleep(2)

#from firstbarnch

driver.close()
driver.quit()