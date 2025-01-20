from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # If you want it to run headlessly
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-software-rasterizer")  # to avoid crashes in a container
chrome_options.add_argument("--remote-debugging-port=9222")  # Optional debugging

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("https://www.example.com")
print(driver.title)
driver.quit()
