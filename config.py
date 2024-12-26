from dotenv import load_dotenv
import os
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", "default/path/to/chromedriver")
BASE_URL = "https://elpais.com/"
OPINION_SECTION_TEXT = "Opinión"
IMAGE_FOLDER = "opinion_images"

# RapidAPI Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "rapid-translate-multi-traduction.p.rapidapi.com"

# BrowserStack Configuration
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

BROWSER_CONFIGS = [
    {
        "os": "OS X",
        "os_version": "Sonoma",
        "browser": "safari",
        "browser_version": "latest",
        "build": "Build_Parallel",
    },
    {
        "deviceName": "OnePlus 11R",
        "osVersion": "13.0",
        "browserName": "chrome",
        "real_mobile": "true",
        "build": "Build_Parallel",
    },
    {
        "os": "Windows",
        "os_version": "11",
        "browser": "Firefox",
        "browser_version": "latest",
        "build": "Build_Parallel",
    },
    {
        "device": "Google Pixel 8",
        "os_version": "14.0",
        "browser": "chrome",
        "real_mobile": "true",
        "build": "Build_Parallel",
    },
    {
        "os": "Windows",
        "os_version": "10",
        "browser": "Chrome",
        "browser_version": "latest",
        "build": "Build_Parallel",
    },
    ]