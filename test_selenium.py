import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up desired capabilities for the browser (if needed)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: comment out if you don't need headless mode

# Use WebDriverManager to install the required version of ChromeDriver
driver_path = ChromeDriverManager().install()

# Initialize WebDriver with the downloaded ChromeDriver path
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Perform the operations
driver.get("http://www.google.com")
if "Google" not in driver.title:
    raise Exception("Unable to load Google page!")

# Perform a search operation
elem = driver.find_element("name", "q")
elem.send_keys("CrossBrowserTesting")
elem.submit()

# Print the title of the page
print(driver.title)

# Close the driver and end the session
driver.quit()
