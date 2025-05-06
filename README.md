# LinkedIn-WebScraper



Things I learned:

- The line ``` options.add_argument("user-data-dir=C:/Users/kushi/AppData/Local/Temp/TempChromeProfile") ``` lets you create a temporary profile in google so that your cookies/cache are saved in that temporary profile 
- The line ```options.add_argument("user-data-dir=C:/Users/kushi/AppData/Local/Google/Chrome/User Data")``` must not be specified with a profile name at the end such as: ```options.add_argument("user-data-dir=C:/Users/kushi/AppData/Local/Google/Chrome/User Data/Profile 1")``` as ```user-data-dir``` is just the directory for the **user data**
-```options.add_argument("--disable-blink-features=AutomationControlled")``` is used to make the browser controlled by Selenium appear less like an automated bot 
 - This disables a specific feature in Chromium-based browsers (like Google Chrome) called AutomationControlled.
 - By default, when a browser is controlled by automation tools like Selenium, it sets a flag (navigator.webdriver) that websites can detect to identify that the browser is being automated.
 - Disabling this feature makes it harder for websites to detect that the browser is being controlled by Selenium, which can help bypass bot detection mechanisms.
- Lines like ```job_elements = WebDriverWait(driver, 2)...```, tell selenium to wait until the element is found. If you tell it wait 20 seconds to find an element but it finds it in 5 seconds, this part of the script will execute in 5 seconds. 
