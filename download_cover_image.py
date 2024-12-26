import os
import requests

def download_image(image_url, idx, folder='opinion_images'):
    """Download an image from a URL and save it to the local machine."""
    try:
        img_data = requests.get(image_url).content
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(f'{folder}/article_{idx}.jpg', 'wb') as f:
            f.write(img_data)
        print(f"Image {idx} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading image {idx}: {e}")
