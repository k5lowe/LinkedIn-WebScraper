from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("user-data-dir=C:/Users/kushi/AppData/Local/Temp/TempChromeProfile")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")

print("working 1")
driver = webdriver.Chrome(options=options)
print("working 2")


driver.get("https://www.linkedin.com/jobs/search/?keywords=software+engineer&location=toronto&f_TPR=r86400")



time.sleep(1000)