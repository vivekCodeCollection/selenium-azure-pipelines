pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a website
driver.get("https://www.example.com")

# Perform any actions you need here

# Close the browser
driver.quit()
