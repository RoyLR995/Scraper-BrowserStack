import re
from collections import Counter

def process_titles(translated_titles):
    # Step 1: Clean and split titles into words
    all_words = []
    for title in translated_titles:
        # Remove punctuation (except for apostrophes and hyphens) and convert to lowercase
        title = title.lower()  # Convert to lowercase
        title = re.sub(r"[^\w\s'-]", "", title)
        words = title.split()  # Split the title into words
        all_words.extend(words)

    # Step 2: Count occurrences of each word
    word_counts = Counter(all_words)

    # Step 3: Identify words repeated more than twice
    repeated_words = {word: count for word, count in word_counts.items() if count > 2}

    # Step 4: Print repeated words and their counts
    if repeated_words:
        print("Repeated words across titles (appearing more than twice):")
        for word, count in repeated_words.items():
            print(f"{word}: {count}")
    else:
        print("No words appear more than twice across the titles.")
