
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from OrangeHRM.File_To_Read_And_Write.File_Handling import write_in_file

driver = webdriver.Chrome()
driver.maximize_window()

