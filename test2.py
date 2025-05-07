from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSW = os.getenv('PASSW')
API_KEY = os.getenv('API_KEY')
client = genai.Client(api_key=API_KEY)



options = Options()
# options.add_argument("--headless")
options.add_argument("user-data-dir=C:/Users/kushi/AppData/Local/Temp/TempChromeProfile")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")


print("working 1")
driver = webdriver.Chrome(options=options)
print("working 2")


role = "software engineer"
role = role.replace(" ", "+")
location = "toronto"
date_range = 86400


url = f"https://www.linkedin.com/jobs/search/?keywords={role}&location={location}&f_TPR=r{date_range}"
driver.get(url)
time.sleep(5)

try:
    
    sign_in_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-in-modal__outlet-btn"))
    )
    
    sign_in_button.click()

    email_input = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "base-sign-in-modal_session_key"))
    )

    email_input.send_keys(EMAIL)
    
    
    

except Exception as e:
    print("sign in doesnt work")
    pass


time.sleep(30000)

try:
    close_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-dismiss"))
    )
    close_btn.click()
except TimeoutException:
    pass



try:
    job_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//li[contains(@class, "scaffold-layout__list-item")]')))

    print("Found", len(job_elements), "jobs")

except TimeoutException:
    print("No jobs have been found")




for job in job_elements:
    try:
        job.click()
        # details = WebDriverWait(driver,5).until(
        #     EC.presence_of_all_elements_located(
        #         (By.XPATH, '//*[@id="job-details"]')))

        details = WebDriverWait(driver,5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="job-details"]')))

        
        # details = WebDriverWait(driver,5).until(
        #     EC.presence_of_all_elements_located(
        #         (By.XPATH, '//*[@id="job-details"]/div/p')))

        # details = driver.find_element(By.XPATH, '//*[@id="job-details"]/div1/p')
        # print("success")
        # time.sleep(3)

        prompt = f"""
            Extract the qualifications or skills required from the following job 
            description. Only return that section in bullet points:

            \"\"\"{details.text}\"\"\"
            """

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        print(response.text)



        time.sleep(30)

        
    except Exception as e:
        print(f"Error clicking job: {e}")


