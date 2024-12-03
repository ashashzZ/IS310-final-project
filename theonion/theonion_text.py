import pandas as pd
import requests
from bs4 import BeautifulSoup

# Input CSV file containing article links
input_csv = '/Users/ashash/Desktop/IS310 webs/data/theonion_links_politics.csv'
output_csv = '/Users/ashash/Desktop/IS310 webs/data/theonion_scraped_articles.csv'

# Function to scrape title and text from an article link
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the article title
        title_tag = soup.find('h1')  # Adjust tag/class if needed for The Onion
        title = title_tag.get_text(strip=True) if title_tag else "Title not found"
        
        # Extract the article content
        content_tags = soup.find_all('p')  # Collect all paragraph tags for the article
        text = ' '.join([tag.get_text(strip=True) for tag in content_tags])
        
        return title, text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "Error", "Error"

# Read input CSV and prepare for scraping
df = pd.read_csv(input_csv)

# Ensure the column name matches exactly as in your CSV file
if 'Article Link' not in df.columns:
    print("The CSV does not have an 'Article Link' column.")
    exit()

# Create an empty list to store article data
scraped_data = []

# Loop through each article link and scrape content
for index, row in df.iterrows():
    link = row['Article Link']  # Replace with actual column name
    title, text = scrape_article(link)
    scraped_data.append({
        'type': 'politics',  # Set the type as 'politics'
        'link': link,
        'title': title,
        'text': text,
    })

# Convert scraped data into a DataFrame
output_df = pd.DataFrame(scraped_data)

# Save the DataFrame to a CSV file
output_df.to_csv(output_csv, index=False, encoding='utf-8')

print(f"Scraped articles saved to {output_csv}")
