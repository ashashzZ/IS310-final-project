import csv
import requests
from bs4 import BeautifulSoup

# Input and output file paths
input_csv = 'data/apnews_article_links.csv'  # Replace with your actual file path
output_csv = 'data/apnews_scraped_articles.csv'

# Define the type for the articles
article_type = 'politics'

# Function to extract the title and text from an article link
def scrape_article(link):
    try:
        response = requests.get(link)
        response.raise_for_status()  # Raise HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title (modify the selector based on the website's structure)
        title = soup.find('title').text.strip()
        
        # Extract article text (modify this to match the actual structure of articles on the website)
        paragraphs = soup.find_all('p')  # Adjust based on the site's structure
        text = ' '.join([para.text.strip() for para in paragraphs if para.text.strip()])
        
        return title, text
    except Exception as e:
        print(f"Error scraping {link}: {e}")
        return None, None

# Read input CSV, scrape articles, and write to output CSV
with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['type', 'link', 'title', 'text']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()  # Write column headers

    for row in reader:
        link = row['Article Link']  # Adjust column name based on your CSV structure
        title, text = scrape_article(link)
        if title and text:
            writer.writerow({'type': article_type, 'link': link, 'title': title, 'text': text})

print(f"Scraped articles saved to {output_csv}")
