import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up desired capabilities for the browser (if needed)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: comment out if you don't need headless mode

# Download and set up ChromeDriver using WebDriverManager
driver_path = ChromeDriverManager().install()

# Create a Service object using the downloaded ChromeDriver
service = Service(executable_path=driver_path)

# Initialize WebDriver with the Service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google
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
