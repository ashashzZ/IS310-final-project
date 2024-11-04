import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Set the directory containing the CSV files
directory = '/Users/ashash/Desktop/IS310 webs/theonion/links'  # Update this if your links directory is in a different path

# Initialize a list to store data
data = []


# Function to scrape the title and text from a given link
def scrape_article(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the title
        title_tag = soup.find('h1', class_='has-link-color')
        title = title_tag.get_text(strip=True) if title_tag else "Title not found"

        # Get the article content
        article_content_tag = soup.find('div',
                                        class_='entry-content single-post-content single-post-content--has-watermark wp-block-post-content has-echo-font-size is-layout-flow wp-block-post-content-is-layout-flow')
        content_text = article_content_tag.get_text(strip=True) if article_content_tag else "Content not found"

        return title, content_text

    except Exception as e:
        print(f"Failed to retrieve {url}: {e}")
        return "Title not found", "Content not found"


# Iterate through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Determine the type (e.g., news, local, etc.) from the filename
        article_type = filename.split('_')[2].replace('.csv', '')

        # Go through each link in the CSV file
        for index, row in df.iterrows():
            link = row['Article Link']

            # Scrape the title and text from the article
            title, text = scrape_article(link)

            # Append the data to the list
            data.append({
                'type': article_type,
                'link': link,
                'title': title,
                'text': text
            })

# Convert the list into a pandas DataFrame
output_df = pd.DataFrame(data)

# Save the DataFrame to a new CSV file
output_df.to_csv('scraped_articles.csv', index=False, encoding='utf-8')

print("Scraping completed and saved to scraped_articles.csv.")
