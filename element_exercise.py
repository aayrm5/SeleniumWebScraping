from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')

# Path to the element in HTML file
input2_locator = 'input[id="ipt2"]' #CSS
button4_locator = "//button[@id='b4']" #XPATH

# Assign elements
input2_elem=browser.find_element_by_css_selector(input2_locator)
butn4_elem=browser.find_element_by_xpath(button4_locator)

# Manipulate elements
input2_elem.send_keys("Test text")
butn4_elem.click()
browser.quit()