from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize the Chrome browser
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.example.com")

# Perform any actions you need here

# Close the browser
driver.quit()
