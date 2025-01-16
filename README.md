# BrowserStack-scraper
## Web Scraping and testing on elpais.com

This project automates web scraping on https://elpais.com to fetch article titles and contents from the "Opinión" section, translate the titles to English, and analyze repeated words. The script also supports local and BrowserStack-based parallel testing.

#### Features
Web scraping using Selenium.
Automatic translation of article titles using Rapid Translate Multi Traduction API.
Word frequency analysis in translated titles.
Image downloading for articles.
Parallel testing on BrowserStack with support for multiple browser configurations.

#### Prerequisites
* Python:
  Ensure Python 3.10+ is installed on your system.
* Google Chrome and ChromeDriver:
  * Install Google Chrome.
  * Steps to Download and Install ChromeDriver

    Check Chrome Version:

    Open Chrome, go to Help > About Google Chrome, and note the version (e.g., 117.x).
  * Download ChromeDriver:
    Visit ChromeDriver Downloads and download the version matching your Chrome's major version.

    Windows: chromedriver_win32.zip or chromedriver_win64.zip

    Mac: chromedriver_mac64.zip or chromedriver_mac64_arm64.zip

    Linux: chromedriver_linux64.zip
  * Extract ChromeDriver:
    Unzip the file and note the path to chromedriver.exe application (e.g., C:/path/to/chromedriver.exe).

* BrowserStack Account: Register at BrowserStack for automated testing.
  Note the BrowserStack username and BrowserStack Access Key for future purposes which you can find in https://www.browserstack.com/accounts/profile/details after logging in to your account.

* Setting Up RapidAPI for Translation
  * Create an Account: Sign up at RapidAPI.
  * Subscribe to the API: Visit Rapid Translate API and subscribe.
  * Get API Key: Note your X-RapidAPI-Key from the API's Endpoints tab.


#### Installation

* Clone the repository:
  * Create a new Folder and open the folder in VS code or any other IDE.
  * Go to the terminal.   
  * Run the command "git clone https://github.com/RoyLR995/Scraper-BrowserStack.git"
  * Run the command "cd Scraper-BrowserStack"

* Install the dependencies:
  * pip install selenium
  * pip install requests
  * pip install python-dotenv
  * pip install futures
    
* Create a .env file for sensitive credentials:
  * Add the following content to .env:
    * CHROME_DRIVER_PATH=</path/to/chromedriver.exe> (Replace with previously noted path to the chromedriver.exe file)
    * BROWSERSTACK_USERNAME= Mention the previously noted BrowserStack Username (Ex: "likhitharoy")
    * BROWSERSTACK_ACCESS_KEY= Mention the previously noted BrowserStack Access_key (Ex: "1224345")
    * RAPIDAPI_KEY= Mention the previously noted RapidAPI-key (Ex: "bf16181f0cmsh856525dd0f2cb44p126e93jsnd5d0d1ddf08a")
      If you haven't created an account in rapidapi.com, you can use "bf16181f0cmsh856525dd0f2cb44p126e93jsnd5d0d1ddf08a" key for now.

    Note: Do not forget to wrap all the values of the above variables inside "".

### Usage Instructions
* Run the main script to scrape articles, process titles, download cover images, and translate them in one go by running ```python scraper.py``` in the terminal

  That's it! The script handles all functionalities in a single run, including:

  * Web scraping from Elpais.com.
  * Translating titles to English.
  * Analyzing word frequencies.
  * Downloading cover images.
  * Local Testing
  * Executes the solution on BrowserStack across 5 parallel threads, testing across a combination of desktop and mobile browsers.
