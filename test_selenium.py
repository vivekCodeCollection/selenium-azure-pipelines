import os
import time
import ssl
import urllib.request
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Disable SSL verification (temporary workaround for SSL certificate issues)
ssl._create_default_https_context = ssl._create_unverified_context

# Set your username and authkey from environment variables
username = os.getenv("CBT_USERNAME")
authkey = os.getenv("CBT_AUTHKEY")

# Chrome version (replace it with the version your container uses, or keep as "latest")
chrome_version = "latest"  # Change if you need a specific version

# Set up desired capabilities for the browser
caps = DesiredCapabilities.CHROME.copy()
caps['platform'] = 'Windows'

# Setup Chrome options (headless is optional, use if you want to run without UI)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: comment out if you don't need headless mode

# Function to download ChromeDriver dynamically
def download_chromedriver(version="latest"):
    if version == "latest":
        version_url = "https://chromedriver.storage.googleapis.com/2.41/chromedriver_win32.zip"  # Update the URL as needed
    else:
        # You can specify a different ChromeDriver version if needed
        version_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"
    
    # Directory where ChromeDriver will be downloaded and extracted
    download_dir = "/tmp/chromedriver"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Paths for downloading and extracting ChromeDriver
    driver_zip = os.path.join(download_dir, "chromedriver.zip")
    driver_path = os.path.join(download_dir, "chromedriver.exe")

    # Download ChromeDriver
    urllib.request.urlretrieve(version_url, driver_zip)

    # Extract the downloaded zip file
    with zipfile.ZipFile(driver_zip, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    return driver_path

# Download the appropriate ChromeDriver (latest version by default)
chromedriver_path = download_chromedriver(version=chrome_version)

# Create a Service object using the downloaded ChromeDriver
service = Service(executable_path=chromedriver_path)

# Now pass the service object while creating the WebDriver object
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional, if you want to run Chrome headless

# Pass the service to the WebDriver (not to Remote())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Perform the test steps
driver.get("http://www.google.com")
if "Google" not in driver.title:
    raise Exception("Unable to load Google page!")

# Locate the search bar, perform a search, and submit
elem = driver.find_element("name", "q")
elem.send_keys("CrossBrowserTesting")
elem.submit()

# Output the page title to confirm it's working
print(driver.title)

# Close the driver and end the session
driver.quit()
