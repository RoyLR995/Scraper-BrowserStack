import os
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CHROME_DRIVER_PATH, BASE_URL, OPINION_SECTION_TEXT, BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, BROWSER_CONFIGS

from scrape_articles import scrape_articles
from process_titles import process_titles

def handle_cookie_consent(driver):
    """Function to handle the cookie consent on the page."""
    # Wait for the cookies pop up
    driver.implicitly_wait(10)

    try:
        # Handle cookie consent
        cookie_button = driver.find_element(By.ID, "didomi-notice-agree-button")
        print("Found button to accept cookies.")

        # Check visibility and click via JavaScript
        is_visible = driver.execute_script(
            "return arguments[0] !== null && arguments[0].offsetParent !== null;", 
            cookie_button
        )
        if is_visible:
            print("Clicking button.")
            driver.execute_script("document.getElementById('didomi-notice-agree-button').click();")
            print("Cookie consent accepted.")
        else:
            print("Button not found. Skipping click.")

    except Exception as e:
        print(f"Error: {e}")
        
def run_scraper(remote=False, capabilities=None):
    """Function to run the scraper, locally or remotely via BrowserStack."""
    if remote:
        # Remote testing via BrowserStack
        options = Options()
        
        # Set capabilities
        for key, value in capabilities.items():
            options.set_capability(key, value)
        
        driver = webdriver.Remote(
            command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
            options=options  # Pass options here
        )
    else:
        # Local testing
        service = Service(CHROME_DRIVER_PATH)
        chrome_options = Options()
        chrome_options.add_argument("--lang=es")
        driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the website
    driver.get(BASE_URL)

    handle_cookie_consent(driver)

    # Wait for the <html> element to be present before retrieving the lang attribute
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "html"))
    )

    # Retrieve the lang attribute of the <html> element
    lang_attribute = driver.execute_script(
        "return document.documentElement.getAttribute('lang');"
    )

    if lang_attribute.startswith("es"):
        print("The website's text is displayed in Spanish.")
    else:
        print(f"The website's language is {lang_attribute}, not Spanish.")

    # Navigate to the Opinion section
    try:
        opinion_section = driver.find_element(By.PARTIAL_LINK_TEXT, OPINION_SECTION_TEXT)
        opinion_section.click()
        print("Navigating to the Opinion section...")
    except Exception as e:
        driver.quit()
        print(f"Error finding the Opinion section: {e}")
    
    # Wait for the Opinion section to load
    driver.implicitly_wait(5)

    # Scrape articles and translate titles
    translated_titles, articles = scrape_articles(driver)

    # Process titles to count repeated words
    process_titles(translated_titles)

    # Close the browser
    driver.quit()

# Add the following lines to ensure that the script runs when called directly
if __name__ == "__main__":
    # Local Testing
    print("Testing Locally")
    run_scraper()
    print("Successfully completed testing on Local")

    print("Testing on BrowserStack")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Running 5 tests in parallel
        futures = [executor.submit(run_scraper, remote=True, capabilities=config) for config in BROWSER_CONFIGS]
        
        # Wait for all tests to complete
        for future in concurrent.futures.as_completed(futures):
            print("Successfully tested on a configuration.")

    print("Successfully completed testing on BrowserStack")