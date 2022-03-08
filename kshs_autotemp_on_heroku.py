from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import random
from datetime import datetime

if datetime.today().weekday() > 4:
    sys.exit()
# set up
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

# build driver
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
driver.get("https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx")

# send ID and submit
waitforbrowser = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtId"))
)
ID = driver.find_element_by_id("ContentPlaceHolder1_txtId")
ID.send_keys("[ID here]")
submit_1 = driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnId")
submit_1.click()

# send info
waitforbrowser = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_rbType_1"))
)

ways = driver.find_element_by_id("ContentPlaceHolder1_rbType_1")
ways.click()

temp_1 = driver.find_element_by_id("ContentPlaceHolder1_ddl1")
Select(temp_1).select_by_value("36")

temp_2 = driver.find_element_by_id("ContentPlaceHolder1_ddl2")
Select(temp_2).select_by_value(str(random.randint(5, 8)))

attendance = driver.find_element_by_id("ContentPlaceHolder1_ddl3")
Select(attendance).select_by_value("1")

submit_2 = driver.find_element_by_id("ContentPlaceHolder1_btnId0")
submit_2.click()

# Close window
waitforbrowser = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)
driver.switch_to.alert.accept()
driver.close()
sys.exit()

# DONE!