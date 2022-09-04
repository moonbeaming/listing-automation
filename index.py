from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time 

# email = input('Enter your email: ')
# password = input('Enter your password: ')
# image_path = input('Enter your image path: ')
# image_path = input('Enter your image path: ')

driver = webdriver.Chrome(ChromeDriverManager().install())  # Optional argument, if not specified will search path.
wait = WebDriverWait(driver, 10)
driver.get('https://www.carousell.sg/sell')

select_photos = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/label/div[1]')
select_photos.click()
driver.implicitly_wait(5)
login_select = driver.find_element(By.XPATH, ('/html/body/div[4]/div/div/div/div/div[3]/button | /html/body/div[5]/div/div/div/div/div[3]/button'))
login_select.click()
driver.implicitly_wait(5)
email_input = driver.find_element(By.XPATH, '//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/div[1]/div/div/input')
email_input.send_keys("e0421353@u.nus.edu")
password_input = driver.find_element(By.XPATH, '//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/div[2]/div/div/input')
password_input.send_keys("Password123")
login_btn = driver.find_element(By.XPATH, '//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/button')
login_btn.click()
time.sleep(15)
# select_photos = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/label/div[1]')
select_photos = driver.find_element(By.XPATH, '//input[@type="file"]')
select_photos.send_keys('C:/Users/Luna/Documents/CarousellBot/MinecraftLogo.png')
time.sleep(3)
open_category = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div')
open_category.click()
time.sleep(3)
select_category = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[32]')
select_category.click()
select_subcategory = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[37]')
select_subcategory.click()
select_finalcategory = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[38]')
select_finalcategory.click()
title_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[1]/div/div/div/div/input')
title_input.send_keys("temporary title")
select_brandnew = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[2]/div/div/div[1]')
select_brandnew.click()
price_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[4]/div[1]/div/div/input')
price_input.send_keys(10)
description_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[5]/div/div/div[1]/textarea')
description_input.send_keys("temporary description that is really long")
# brand_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[6]/div/div[1]/div/div/input')
# brand_input.send_keys("")
size_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[7]/div/div[1]/div/div')
size_input.click()

size = 1
size_select1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[7]/div/div[2]/div')
size_select2 = size_select1.find_element(By.XPATH, '/div[{size}]')
size_select2.click()
# /html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[7]/div/div[2]/div/div[1]
# /html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[7]/div/div[2]/div/div[2]
time.sleep(5)

# sell_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/a | /html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a')
# sell_btn.click()
# wait.until(EC.url_changes('https://www.carousell.sg/sell/'))


# post_btn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/div/div/button')
# post_btn.click()
# wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your post is now published.')]")))
print('code ran successfully!')
driver.quit()