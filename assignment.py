from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()
import time


driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

actual_text=driver.find_element(By.XPATH,'//*[@id="example_filter"]/label/input').send_keys('New York')

actual_text == expected_text#, f"Text mismatch! Expected: {expected_text}, Got: {actual_text}"

time.sleep(3)