from selenium import webdriver

driver=webdriver.Chrome()

driver.get('https://oylmoney.xyz')


user=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
btn=driver.find_element_by_name("button")
user.send_keys("hisourav4u")
password.send_keys("Weareweare23@")
btn.click()
driver.implicitly_wait(5)
btn=driver.find_element_by_xpath("/html/body/div/div[2]/h2[2]/div/input")
btn.click()
driver.implicitly_wait(5)
t=158
count=0
tt=10
while(tt>0):
    while(t>0):
        text=""
        print(count)
        print("inside loop")
        text+=(driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/table/tbody/tr/td[1]/div/img").get_attribute("src"))[-5]
        print(1)
        text+=(driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/table/tbody/tr/td[2]/div/img").get_attribute("src"))[-5]
        print(2)
        text+=(driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/table/tbody/tr/td[3]/div/img").get_attribute("src"))[-5]
        print(text)
        box=driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input")
        box.send_keys(text)
        btn=driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/input")
        btn.click()
        driver.implicitly_wait(.5)
        t-=1
        count+=1

    btn=driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/form/div[1]/table/tbody/tr[14]/td[1]/a/b/font/u")
    btn.click()
    driver.implicitly_wait(4)


    user=driver.find_element_by_id("username")
    password=driver.find_element_by_id("password")
    btn=driver.find_element_by_name("button")
    user.send_keys("hisourav4u")
    password.send_keys("Weareweare23@")
    btn.click()
    driver.implicitly_wait(5)
    btn=driver.find_element_by_xpath("/html/body/div/div[2]/h2[2]/div/input")
    btn.click()
    driver.implicitly_wait(5)
    t=158
    count=0

    tt-=1



