from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_MOBILE_NUMBER = os.getenv("MY_MOBILE_NUMBER")

def abort_application():
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()
    time.sleep(2)
    discard_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4240185366&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
time.sleep(5)
sign_in_button = driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

time.sleep(2)

email_input = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
email_input.send_keys(MY_EMAIL)
password_input = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password_input.send_keys(MY_PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(5)
all_listings = driver.find_elements(By.CLASS_NAME, value="job-card-container--clickable")
print(len(all_listings))
for listing in all_listings:
    print("Opening listing")
    listing.click()
    time.sleep(2)
    try:
        jobs_apply = driver.find_element(By.ID, value="jobs-apply-button-id")
        jobs_apply.click()

        time.sleep(3)

        mobile_input = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if mobile_input.get_attribute("value") == "":
            mobile_input.send_keys(MY_MOBILE_NUMBER)
        else:
            mobile_input.clear()
            mobile_input.send_keys(MY_MOBILE_NUMBER)

        submit_button = driver.find_element(By.CSS_SELECTOR ,"button.artdeco-button--primary")
        if submit_button.get_attribute("aria-label")=="Continue to next step":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)

        Close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        Close_button.click()

        time.sleep(2)

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()