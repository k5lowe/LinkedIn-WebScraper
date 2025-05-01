from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=options)


role = "software engineer"
role = role.replace(" ", "+")
location = "toronto"

url = f"https://www.linkedin.com/jobs/search/?keywords={role}&location={location}"

driver.get(url)

time.sleep(5)

jobs = driver.find_elements(By.XPATH, '/html/body/div[1]/div/main/section[2]/ul')


count = 0
for job in jobs:
    # print(job.text)
    count += 1
    if count == 5:
        break
    try:
        job.click()
        time.sleep(2)
        description = driver.find_elements(By.CLASS_NAME, "show-more-less-html__markup show-more-less-html__markup--clamp-after-5\
            relative overflow-hidden")
        
        print(description)

    except Exception:
        pass