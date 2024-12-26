from selenium.webdriver.common.by import By
from translate import translate_text
from download_cover_image import download_image
from config import IMAGE_FOLDER

def scrape_articles(driver):
    # Find the first five articles
    articles = driver.find_elements(By.CSS_SELECTOR, "article")[:5]
    
    translated_titles = []

    # Scrape title, content, and image for each article
    for idx, article in enumerate(articles, start=1):
        title = article.find_element(By.CSS_SELECTOR, "h2").text
        content = article.find_element(By.CSS_SELECTOR, "p").text
        print(f"Article {idx}:")

        # Translate the article title to English and add it to the list
        translated_title = translate_text(title)
        translated_titles.append(translated_title)

        print(f"Title: {title}")
        print(f"Content: {content}\n")

        # Download the cover image if available
        try:
            image_url = article.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
            if image_url:
                download_image(image_url, idx, IMAGE_FOLDER)
        except Exception as e:
            print(f"No image found for Article {idx}")
    
    return translated_titles, articles
