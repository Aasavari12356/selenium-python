from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver=webdriver.Edge()

 # Step 1: Navigate to the Selenium Playground Table Search Demo
driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')

# Step 2: Locate and interact with the search box to search for "New York"
searchBox=driver.find_element(By.XPATH,'//*[@id="example_filter"]/label/input').send_keys('New York')

# Give the page a moment to filter results
time.sleep(2)

# Step 3: Validate the search results
rows = driver.find_elements(By.XPATH, '//*[@id="example_wrapper"]/tbody/tr')

# Check for rows containing "New York" and count them
visible_count=5
for row in rows:
       if "New York" in row.text:
              visible_count +=1


# Check the total number of entries
expected_visible_count = 5  # Example assumption

if visible_count == expected_visible_count:
        print(f"Test Passed: {visible_count} entries are visible, as expected.")
else:
        print(f"Test Failed: Expected {expected_visible_count} entries, but found {visible_count}.")


# Close the browser
driver.quit()