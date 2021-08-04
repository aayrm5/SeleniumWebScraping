from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

#path to the element in the HTML file
input1=browser.find_element_by_xpath("//input[@id='r1Input']")
butn1=browser.find_element_by_xpath("//button[@id='r1Btn']")

input2=browser.find_element_by_xpath("//input[@id='r2Input']")
butn2=browser.find_element_by_xpath("//button[@id='r2Butn']")

input1.send_keys("Rock")
input2.send_keys("bamboo")
butn1.click()
butn2.click()

# Jessica=browser.find_element_by_xpath("//*[text()[contains(.,'Jessica')]]/../../p")[0]
# Bernard=browser.find_element_by_xpath("//*[text()[contains(.,'Bernard')]]/../../p")[0]
#
# print(Jessica, Bernard)

input3=browser.find_element_by_xpath("//input[@id='r3Input']")
butn3=browser.find_element_by_xpath("//button[@id='r3Butn']")

input3.send_keys("Jessica")
butn3.click()

butn4=browser.find_element_by_id("checkButn")
butn4.click()