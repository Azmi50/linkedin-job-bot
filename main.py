from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env file
load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL") or input("Enter LinkedIn email: ")
PASSWORD = os.getenv("LINKEDIN_PASSWORD") or input("Enter LinkedIn password: ")
PHONE = os.getenv("PHONE_NUMBER") or input("Enter phone number: ")
a
def abort_application():
    """Abort the application process"""
    try:
        # Click Close Button
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        
        time.sleep(1)
        # Click Discard Button
        discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
        print("Application aborted")
    except Exception as e:
        print(f"Error aborting application: {e}")

# Set up driver with webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                         options=chrome_options)
driver.maximize_window()

# Job search URL (customize as needed)
job_search_url = (
    "https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
    "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true"
)

try:
    # Open LinkedIn jobs page
    driver.get(job_search_url)
    time.sleep(3)

    # Click Reject Cookies Button if exists
    try:
        reject_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[action-type="DENY"]'))
        )
        reject_button.click()
        print("Cookies rejected")
    except Exception as e:
        print("No cookie button found or couldn't click it")

    # Click Sign in Button
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    sign_in_button.click()
    print("Sign in button clicked")

    # Sign in
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_field.send_keys(EMAIL)
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)
    print("Login credentials entered")

    # CAPTCHA handling
    print("Please solve CAPTCHA if required...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results-list"))
    )
    print("Assuming CAPTCHA solved or not required")

    # Get Listings
    all_listings = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable"))
    )
    print(f"Found {len(all_listings)} job listings")

    # Apply for Jobs
    for i, listing in enumerate(all_listings, 1):
        print(f"\nProcessing listing {i}/{len(all_listings)}")
        try:
            listing.click()
            time.sleep(2)
            
            try:
                # Click Apply Button
                apply_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-s-apply button"))
                )
                apply_button.click()
                time.sleep(3)

                # Insert Phone Number if field is empty
                try:
                    phone = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
                    if phone.get_attribute("value") == "":
                        phone.send_keys(PHONE)
                except NoSuchElementException:
                    pass

                # Check if application is multi-page
                submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
                if submit_button.get_attribute("data-control-name") == "continue_unify":
                    abort_application()
                    print("Complex application, skipped.")
                    continue
                else:
                    # Click Submit Button
                    print("Submitting job application")
                    submit_button.click()
                    time.sleep(2)

                # Close the modal if it appears
                try:
                    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close_button.click()
                except NoSuchElementException:
                    pass

            except (NoSuchElementException, ElementClickInterceptedException):
                abort_application()
                print("No application button or couldn't click, skipped.")
                continue

        except Exception as e:
            print(f"Error processing listing: {e}")
            continue

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
    print("Browser closed")
