from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#To use By
from selenium.webdriver.common.by import By
#For pause
import time

#Keep open the window
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#Eliminate 'Bluetooth: bluetooth_adapter' error messeage
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#Install driver and open page with it
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.lg.com/global')
#Maximize window
driver.maximize_window()
#-------------------------------------------------------------------------

#Get total height of the page
last_height = driver.execute_script("return document.body.scrollHeight")
#Initial height value
new_height = 300
#Incremental value
increase_value = 700
#Scroll down by incremental value and click go to top button
for i in range (new_height, last_height-1000, increase_value):
    #scroll to new_height value
    driver.execute_script("window.scrollTo(0, '"+str(new_height)+"')")
    time.sleep(1)
    #The current window's y-value before click the top button 
    height_before_topBtn = driver.execute_script("return window.pageYOffset")
    print("Height before top BTN click:" + str(height_before_topBtn))
    #Click Top BTN
    driver.find_element(By.CLASS_NAME, "back-to-top").click()
    new_height = new_height + increase_value
    time.sleep(1)
    #The current window's y-value after click the top button  
    height_after_topBtn = driver.execute_script("return window.pageYOffset")
    print("Height after top BTN click:" + str(height_after_topBtn))
    #Print "pass" when the top button work properly, if not print "fail"
    result = ""
    if height_after_topBtn == 0:
        result = "pass"
    else:
        result = "fail"
driver.close()