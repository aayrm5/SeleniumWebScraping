from selenium import webdriver
bro=webdriver.Chrome()
bro.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Y6BmYLiaISFXyUsSI1dnni-_GyBhqhtjsX8QudxD15s__g/viewform?vc=0&c=0&w=1&flr=0&gxids=7628")

inp_name=bro.find_element_by_tag_name("input[type='email']")

inp_name.send_keys("aayrm5@gmail.com")

