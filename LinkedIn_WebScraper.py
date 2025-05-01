from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

role = "software engineer"
role_url = role.replace(" ", "+")
location = "toronto"

url = f"https://www.linkedin.com/jobs/search/?keywords={role_url}&location={location}"

headers = {
    "User-Agent": "Mozilla/5.0"
    }

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

service = Service(r"C:\Users\kushi\OneDrive\Documents\Python Projects\LinkedIn-WebScraper\drivers\chromedriver.exe")  # Replace with the path to your ChromeDriver
browser = webdriver.Chrome(service=service, options=chrome_options)

# Load the LinkedIn jobs page
browser.get(url)

# Wait for the page to load completely
time.sleep(5)  # Adjust the sleep time as needed

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(browser.page_source, "html.parser")

# Close the browser
browser.quit()

print(soup.prettify())