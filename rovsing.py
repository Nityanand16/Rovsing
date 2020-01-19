from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains




driver = webdriver.Chrome("/Users/Nityanand/PycharmProjects/Selenium/Drivers/chromedriver")
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

#Test2.1.2 click on Board of director Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
board_of_dir = driver.find_element_by_xpath("//li[@id='menu-item-3005']")
action.move_to_element(company_menu).move_to_element(board_of_dir).click().perform()
sleep(2)

#Test2.1.2 End

#Test2.1.3 click on Management Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
management = driver.find_element_by_xpath("//li[@id= 'menu-item-3008']")
action.move_to_element(company_menu).move_to_element(management).click().perform()
sleep(2)

#Test2.1.3 End

#Test2.1.4 click on Customers Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
customers = driver.find_element_by_xpath("//li[@id= 'menu-item-3007']")
action.move_to_element(company_menu).move_to_element(customers).click().perform()
sleep(2)

#Test2.1.4 End

#Test2.1.5 Contact us Start

driver.back()
sleep(1)
action = ActionChains(driver)
company_menu = driver.find_element_by_xpath("//li[@id='menu-item-3361']")
contact_us = driver.find_element_by_xpath("//li[@id='menu-item-3132']")
action.move_to_element(company_menu).move_to_element(contact_us).click().perform()
sleep(2)

#Test2.1.5 Contact us End

#Test2.2.1 Mouse hoover Solutions menu and click on EGSE Systems Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
egse_system = driver.find_element_by_xpath("//li[@id='menu-item-2931']")
action.move_to_element(solutions_menu).move_to_element(egse_system).click().perform()
sleep(2)

#Test2.2.1 End

#Test2.2.1A Mouse hoover Solutions menu, Products and click on ro5000 Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
ro5000 = driver.find_element_by_xpath("//li[@id='menu-item-3333']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(ro5000).click().perform()
sleep(2)

#Test2.2.1A End

#Test2.2.1B Mouse hoover Solutions menu, Products and click on ro2000 Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
ro2000 = driver.find_element_by_xpath("//li[@id='menu-item-3335']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(ro2000).click().perform()
sleep(2)

#Test2.2.1B End

#Test2.2.1C Mouse hoover Sloutions menu, Products and click on ro1000 Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
ro1000 = driver.find_element_by_xpath("//li[@id='menu-item-3336']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(ro1000).click().perform()
sleep(2)

#Test2.2.1C End

#Test2.2.1D Mouse hoover Solutions menu, Products and click on dste Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
products = driver.find_element_by_xpath("//li[@id='menu-item-2932']")
dste = driver.find_element_by_xpath("//li[@id='menu-item-3334']")
action.move_to_element(solutions_menu).move_to_element(products).move_to_element(dste).click().perform()
sleep(2)

#Test2.2.1D End

#Test2.2.2 Mouse hoover on Solution menu and click on Software Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
software = driver.find_element_by_xpath("//li[@id='menu-item-2933']")
action.move_to_element(solutions_menu).move_to_element(software).click().perform()
sleep(2)

#Test2.2.2 End

#Test2.2.3 Mouse hoover on Solutions menu and click on on Board and ground Support Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
obgs = driver.find_element_by_xpath("//li[@id='menu-item-2934']")
action.move_to_element(solutions_menu).move_to_element(obgs).click().perform()
sleep(2)

#Test2.2.3 End

#Test2.2.4 Mouse hoover on Solutions menu and click on on Site Engineering Support Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
sess = driver.find_element_by_xpath("//li[@id='menu-item-2935']")
action.move_to_element(solutions_menu).move_to_element(sess).click().perform()
sleep(2)

#Test2.2.4 End

#Test2.2.5 Mouse hoover on Solutions menu and click on Software Verification And Validation Start

driver.back()
sleep(1)
action = ActionChains(driver)
solutions_menu = driver.find_element_by_xpath("//li[@id='menu-item-2746']")
svvs = driver.find_element_by_xpath("//li[@id='menu-item-2936']")
action.move_to_element(solutions_menu).move_to_element(svvs).click().perform()
sleep(2)

#Test2.2.5 End

#Test2.3.1 Mouse hoover on Investor Relations Menu and click on Announcements
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
Announcements = driver.find_element_by_xpath("//li[@id='menu-item-3648']")
action.move_to_element(Investor_Menu).move_to_element(Announcements).click().perform()
sleep(2)

#Test2.3.1 End

#Test2.3.2 Mouse hoover on Investor Relations Menu and click on Annual Report and Financial Information
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
ARFI_menu = driver.find_element_by_xpath("//li[@id='menu-item-2994']")
action.move_to_element(Investor_Menu).move_to_element(ARFI_menu).click().perform()
sleep(2)

#Test2.3.2 End


#Test2.3.3 Mouse hoover on Investor Relations Menu and click on Financial Calender
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
Financial_Calender = driver.find_element_by_xpath("//li[@id='menu-item-2996']")
action.move_to_element(Investor_Menu).move_to_element(Financial_Calender).click().perform()
sleep(2)

#Test2.3.3 End

#Test2.3.4 Mouse hoover on Investor Relations Menu and click on Coporate Governance
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
Corporate_Governance = driver.find_element_by_xpath("//li[@id='menu-item-2995']")
action.move_to_element(Investor_Menu).move_to_element(Corporate_Governance).click().perform()
sleep(2)

#Test2.3.4 End

#Test2.3.5 Mouse hoover on Investor Relations Menu and click on Incentive Schemes
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
Incentive_Schemes = driver.find_element_by_xpath("//li[@id='menu-item-2997']")
action.move_to_element(Investor_Menu).move_to_element(Incentive_Schemes).click().perform()
sleep(2)

#Test2.3.5 End

#Test2.3.6 Mouse hoover on Investor Relations Menu and click on General Meetings
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
General_Meetings = driver.find_element_by_xpath("//li[@id='menu-item-2998']")
action.move_to_element(Investor_Menu).move_to_element(General_Meetings).click().perform()
sleep(2)

#Test2.3.6 End

#Test2.3.7 Mouse hoover on Investor Relations Menu and click on Convertible Credit Facility
driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
CCF = driver.find_element_by_xpath("//li[@id='menu-item-4179']")
action.move_to_element(Investor_Menu).move_to_element(CCF).click().perform()
sleep(2)

#Test2.3.7 End

#Test2.3.8 Mouse hoover on Investor Relations Menu and click on NASDAQ OMX

driver.back()
sleep(1)
action = ActionChains(driver)
Investor_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3754']")
NO_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3895']")
action.move_to_element(Investor_Menu).move_to_element(NO_Menu).click().perform()
sleep(2)
#driver.find_element_by_xpath("//a[@id='cookieConsentOK']").click()

first_window = driver.window_handles[0]
driver.switch_to.window(first_window)


#Test2.3.8 End

#Test2.4.1 Mouse hoover on Careers and click on Open Positions

#driver.back()
sleep(1)
action = ActionChains(driver)
Careers_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3225']")
OpenPositions_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3001']")
action.move_to_element(Careers_Menu).move_to_element(OpenPositions_Menu).click().perform()
sleep(2)

#Test2.4.1 End

#Test2.4.2 Mouse hoover on Careers and click on Unsolicited Applications

driver.back()
sleep(1)
action = ActionChains(driver)
Careers_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3225']")
UnsolicitedApplications_Menu = driver.find_element_by_xpath("//li[@id='menu-item-3002']")
action.move_to_element(Careers_Menu).move_to_element(UnsolicitedApplications_Menu).click().perform()
sleep(2)

#Test2.4.2 End

#Test2.5 Mouse hoover on News and click

driver.back()
sleep(1)
action = ActionChains(driver)
News_Menu = driver.find_element_by_xpath("//li[@id='menu-item-2840']")
action.move_to_element(News_Menu).click().perform()
sleep(2)

#Test2.5 End

#Test Read more
driver.back()
sleep(1)
action = ActionChains(driver)
Readmore1_menu = driver.find_element_by_xpath("//div[@class='vc_column-inner vc_custom_1508311142963']//a[@class='vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-rounded vc_btn3-style-custom']")
action.move_to_element(Readmore1_menu).click().perform()
sleep(2)

driver.back()
sleep(1)
action = ActionChains(driver)
Readmore2_menu = driver.find_element_by_xpath("//div[@class='vc_column-inner vc_custom_1508577011599']//a[@class='vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-rounded vc_btn3-style-custom']")
action.move_to_element(Readmore2_menu).click().perform()
sleep(2)

driver.back()
sleep(1)
action = ActionChains(driver)
Readmore3_menu = driver.find_element_by_xpath("//div[@class='vc_column-inner vc_custom_1508311929041']//a[@class='vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-rounded vc_btn3-style-custom']")
action.move_to_element(Readmore3_menu).click().perform()
sleep(2)

driver.back()
sleep(1)
action = ActionChains(driver)
Readmare4_menu = driver.find_element_by_xpath("//div[@class='vc_column-inner vc_custom_1508576628748']//a[@class='vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-rounded vc_btn3-style-custom']")
action.move_to_element(Readmare4_menu).click().perform()
sleep(2)

#Test Read more end

#Test Bottom Links

#Test Bottom menu 1 EGSE System
driver.back()
sleep(1)
action = ActionChains(driver)
EGSESystem_menu = driver.find_element_by_xpath("//li[@id='menu-item-2918']")
action.move_to_element(EGSESystem_menu).click().perform()
sleep(2)

#Test Bottom menu 2 Products
driver.back()
sleep(1)
action = ActionChains(driver)
Products_menu = driver.find_element_by_xpath("//li[@id='menu-item-2917']")
action.move_to_element(Products_menu).click().perform()
sleep(2)

#Test Bottom menu 3
driver.back()
sleep(1)
action = ActionChains(driver)
Software_menu = driver.find_element_by_xpath("//li[@id='menu-item-2916']")
action.move_to_element(Software_menu).click().perform()
sleep(2)

#Test Bottom menu 4 On Board and Ground Support
driver.back()
sleep(1)
action = ActionChains(driver)
obgs_menu = driver.find_element_by_xpath("//li[@id='menu-item-2915']")
action.move_to_element(obgs_menu).click().perform()
sleep(2)

#Test Bottom menu 5 On Site Engineering Support
driver.back()
sleep(1)
action = ActionChains(driver)
oses_menu = driver.find_element_by_xpath("//li[@id='menu-item-2921']")
action.move_to_element(oses_menu).click().perform()
sleep(2)

#Test Bottom menu 6 Software Verification and Validation
driver.back()
sleep(1)
action = ActionChains(driver)
svv_menu = driver.find_element_by_xpath("//li[@id='menu-item-2922']")
action.move_to_element(svv_menu).click().perform()
sleep(2)


#Test Bottom menu 7 About us
driver.back()
sleep(1)
action = ActionChains(driver)
Aboutus_menu = driver.find_element_by_xpath("//li[@id='menu-item-2973']")
action.move_to_element(Aboutus_menu).click().perform()
sleep(2)

#Test Bottom menu 8 Board of Directors
driver.back()
sleep(1)
action = ActionChains(driver)
bod_menu = driver.find_element_by_xpath("//li[@id='menu-item-2974']")
action.move_to_element(bod_menu).click().perform()
sleep(2)

#Test Bottom menu 9 Management
driver.back()
sleep(1)
action = ActionChains(driver)
management_menu = driver.find_element_by_xpath("//li[@id='menu-item-2977']")
action.move_to_element(management_menu).click().perform()
sleep(2)

#Test Bottom menu 10 Customers
driver.back()
sleep(1)
action = ActionChains(driver)
customers_menu = driver.find_element_by_xpath("//li[@id='menu-item-2976']")
action.move_to_element(customers_menu).click().perform()
sleep(2)

#Test Bottom menu 11 Contact us
driver.back()
sleep(1)
action = ActionChains(driver)
contactus_menu = driver.find_element_by_xpath("//li[@id='menu-item-3138']")
action.move_to_element(contactus_menu).click().perform()
sleep(2)

#Test Bottom menu 12 Announcements
driver.back()
sleep(1)
action = ActionChains(driver)
announcements_menu = driver.find_element_by_xpath("//li[@id='menu-item-3661']")
action.move_to_element(announcements_menu).click().perform()
sleep(2)

#Test Bottom menu 13 Annual Report and Financial Information
driver.back()
sleep(1)
action = ActionChains(driver)
arfi_menu = driver.find_element_by_xpath("//li[@id='menu-item-2978']")
action.move_to_element(arfi_menu).click().perform()
sleep(2)

#Test Bottom menu 14 Financial Calendar
driver.back()
sleep(1)
action = ActionChains(driver)
fc_menu = driver.find_element_by_xpath("//li[@id='menu-item-2980']")
action.move_to_element(fc_menu).click().perform()
sleep(2)


#Test Bottom menu 15 Corporate Governance
driver.back()
sleep(1)
action = ActionChains(driver)
cg_menu = driver.find_element_by_xpath("//li[@id='menu-item-2979']")
action.move_to_element(cg_menu).click().perform()
sleep(2)

#Test Bottom menu 16 Incentive Schemes
driver.back()
sleep(1)
action = ActionChains(driver)
is_menu = driver.find_element_by_xpath("//li[@id='menu-item-2981']")
action.move_to_element(is_menu).click().perform()
sleep(2)

#Test Bottom menu 17 General Meetings
driver.back()
sleep(1)
action = ActionChains(driver)
gm_menu = driver.find_element_by_xpath("//li[@id='menu-item-2982']")
action.move_to_element(gm_menu).click().perform()
sleep(2)

#Test Bottom menu 18 Convertible Credit Facility
driver.back()
sleep(1)
action = ActionChains(driver)
ccf_menu = driver.find_element_by_xpath("//li[@id='menu-item-4180']")
action.move_to_element(ccf_menu).click().perform()
sleep(2)


#Test Bottom menu 19 News
driver.back()
sleep(1)
action = ActionChains(driver)
news_menu = driver.find_element_by_xpath("//li[@id='menu-item-3462']")
action.move_to_element(news_menu).click().perform()
sleep(2)


#Test Bottom menu 20 Careers
driver.back()
sleep(1)
action = ActionChains(driver)
careers_menu = driver.find_element_by_xpath("//li[@id='menu-item-3463']")
action.move_to_element(careers_menu).click().perform()
sleep(2)

#Test Bottom menu 21 Sitemap
driver.back()
sleep(1)
action = ActionChains(driver)
sitemap_menu = driver.find_element_by_xpath("//li[@id='menu-item-3744']")
action.move_to_element(sitemap_menu).click().perform()
sleep(2)


#Test Bottom Links End


driver.save_screenshot("screenshort.png")

print ()
sleep(2)


driver.close()
driver.quit()
#