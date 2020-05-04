# #Different Selenium library automation tools will be required
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Firefox(executable_path='/home/yash/Downloads/geckodriver')#After opening browser open web.whatsapp.com through next command
# driver.get("https://web.whatsapp.com/")
# wait = WebDriverWait(driver, 600)
# target = '"Lund"'
# string = "Lund it's party time!!!"
# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = driver.find_element_by_xpath(x_arg)
# group_title.click()
# inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
# input_box = driver.find_element_by_xpath(inp_xpath)
# for i in range(100):
#   input_box.send_keys(string + Keys.ENTER)
#   time.sleep(1)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/home/yash/Downloads/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Jyotsna"'

# Replace the below string with your own message
string = "Call Utha!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(50):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)