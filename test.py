from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("user-data-dir=C:/Users/kushi/AppData/Local/Google/Chrome/User Data/Profile 4")
# options.add_argument("profile-directory=Profile 4")  # or "Default"


driver = webdriver.Chrome(options=options)

time.sleep(2)


role = "software engineer"
role = role.replace(" ", "+")
location = "toronto"
date_range = 86400

# Update the URL to include the full LinkedIn job search path and query parameters
# url = f"https://www.linkedin.com/jobs/search/?keywords={role}&location={location}&f_TPR=r{date_range}"

url = "https://www.linkedin.com/jobs/search/?keywords=software+engineer&location=toronto&f_TPR=r86400"
print(url)


driver.get(url)

print("Current URL:", driver.current_url)

# Add debugging steps to verify the URL and browser navigation
print("Navigating to URL:", url)

# Check if the browser successfully navigates to the URL
def verify_navigation():
    current_url = driver.current_url
    print("Current URL after navigation:", current_url)
    if current_url.startswith("https://www.linkedin.com/jobs/search"):
        print("Navigation successful!")
    else:
        print("Navigation failed. Please check the URL or browser settings.")

verify_navigation()


# try:
#     sign_in_class = "sign-in-modal__outlet-btn cursor-pointer btn-md btn-primary btn-secondary"
#     sign_in_button = driver.find_element(By.CLASS_NAME, sign_in_class)
#     sign_in_button.click()

# except ImportError:
#     print("somrthing happened")
#     pass


time.sleep(1000)


# wait = WebDriverWait(driver, 15)

# job_list_container = wait.until(EC.presence_of_element_located(
#     (By.XPATH, '//ul[contains(@class, "jobs-search__results-list")]')
# ))




# job_cards = job_list_container.find_elements(By.XPATH, './li[contains(@class, "scaffold-layout__list-item")]')


# print(job_cards)
# for job in job_cards:
#     job.click()
#     time.sleep(5)

#     break




# time.sleep(5)


# first_job.click()
# time.sleep(2)

# jobs = driver.find_element(By.XPATH, '//*[@id="job-details"]/div/p')

# print(jobs)






# count = 0
# for job in jobs:
#     # print(job.text)
#     count += 1
#     if count == 5:
#         break
#     try:
#         job.click()
#         time.sleep(2)
#         description = driver.find_elements(By.CLASS_NAME, "show-more-less-html__markup show-more-less-html__markup--clamp-after-5\
#             relative overflow-hidden")
        
#         print(description)

#     except Exception:
#         pass


