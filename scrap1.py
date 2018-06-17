from selenium import webdriver

print("1. Comenzandando ...")

driver = webdriver.Chrome('./chromedriver')

print("2......")

driver.get('http://web.whatsapp.com')

print("3......")

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

print("user ........: ", user)

user.click()

print("4 ..........")


#msg_box = driver.find_element_by_class_name('input-container')
msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg + " Ale mandando el nro: " + str(i))
    driver.find_element_by_class_name('_2lkdt').click()