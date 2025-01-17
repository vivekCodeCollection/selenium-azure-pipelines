import os
import time
import urllib.request
import zipfile
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Get your username and authkey from environment variables
username = os.getenv("CBT_USERNAME")
authkey = os.getenv("CBT_AUTHKEY")

# Chrome version (replace it with the version your container uses)
chrome_version = "latest"  # You can set a specific version here

# Set up the desired capabilities for the browser
caps = DesiredCapabilities.CHROME.copy()
caps['platform'] = 'Windows'

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional if running headless

# Download ChromeDriver based on the browser version
def download_chromedriver(version="latest"):
    # Build the URL to download the corresponding ChromeDriver
    if version == "latest":
        version_url = "https://chromedriver.storage.googleapis.com/2.41/chromedriver_win32.zip"
    else:
        # In case you need a specific version of ChromeDriver
        version_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"
    
    # Temp directory to download the driver
    download_dir = "/tmp/chromedriver"

    # Ensure the download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Full path where the driver will be extracted
    driver_zip = os.path.join(download_dir, "chromedriver.zip")
    driver_path = os.path.join(download_dir, "chromedriver.exe")

    # Download ChromeDriver
    urllib.request.urlretrieve(version_url, driver_zip)

    # Extract the downloaded driver
    with zipfile.ZipFile(driver_zip, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    return driver_path

# Download the appropriate ChromeDriver (for latest version in this case)
chromedriver_path = download_chromedriver(version=chrome_version)

# Set up the Service with the downloaded ChromeDriver
service = Service(executable_path=chromedriver_path)

# Create the WebDriver object for remote execution
driver = webdriver.Remote(
    command_executor=f"http://{username}:{authkey}@hub.crossbrowsertesting.com/wd/hub",
    desired_capabilities=caps,
    options=chrome_options,
    service=service  # Include the service with the path to ChromeDriver
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
