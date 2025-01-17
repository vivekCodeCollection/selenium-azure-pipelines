from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os, time

# Set your username and authkey from environment variables
username = os.getenv("CBT_USERNAME")
authkey = os.getenv("CBT_AUTHKEY")

# Set up desired capabilities for the remote browser
caps = DesiredCapabilities.CHROME.copy()
caps['platform'] = 'Windows'

# Set Chrome options if you need specific options
chrome_options = Options()
chrome_options.add_argument("--headless")  # If you want to run headless

# Create a service object (optional for newer versions)
service = Service()

# Connect to the remote browser
driver = webdriver.Remote(
    command_executor=f"http://{username}:{authkey}@hub.crossbrowsertesting.com/wd/hub",
    desired_capabilities=caps,
    options=chrome_options  # Add options if required
)

# Perform the test steps
driver.get("http://www.google.com")
if "Google" not in driver.title:
    raise Exception("Unable to load Google page!")

elem = driver.find_element("name", "q")
elem.send_keys("CrossBrowserTesting")
elem.submit()

# Output the page title to confirm it's working
print(driver.title)

# Close the driver and end the session
driver.quit()
