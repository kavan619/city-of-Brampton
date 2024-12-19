import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('https://cityofbrampton.perfectmind.com/Menu/MemberRegistration/MemberSignIn')
driver.set_window_size(1920, 1080)
username = driver.find_element(By.ID,'textBoxUsername')
username.send_keys('Kavan.Gudhka@brampton.ca')
box = driver.find_element(By.CLASS_NAME, 'forgot-pass')
box.click()

driver.get('https://cityofbrampton.perfectmind.com/OtherApps/Program')
search_bar = driver.find_element(By.CLASS_NAME,'search-text-input')
search_bar.click()
search_bar.send_keys('Aquatic Instructor')
search_bar.send_keys(Keys.ENTER)

service_name = driver.find_element(By.XPATH,"//td[@class='aoda_filter__Name' and text()='Aquatic Instructor']")
service_name.click()

edit_button = driver.find_element(By.ID,'editObject')
edit_button.click()
time.sleep(3)

facility_add = driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[2]/div/table/tbody/tr/td/form/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[7]/td[2]/div/div/div[1]/input')
facility_add.click()
time.sleep(2)
facility_add.send_keys('Full pool')
time.sleep(2)
full_pool_option = driver.find_element(By.XPATH, "//div[contains(text(), 'McMurchy Youth Centre for Sports Excellence')]") #This is to differentiate between location names for the same facility name
full_pool_option.click()

save_button = driver.find_element(By.ID, "submitLinkVisible")
actions = ActionChains(driver)
actions.move_to_element(save_button)
time.sleep(1)
actions.click().perform()
input()