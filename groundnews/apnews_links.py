import requests
from bs4 import BeautifulSoup
import csv

url = 'https://apnews.com/politics'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all links to articles (assuming they are within <a> tags with a specific class or attribute)
    article_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Filter for article links (this may vary depending on the website's structure)
        if '/article/' in href or '/news/' in href:
            full_url = 'https://ground.news' + href if href.startswith('/') else href
            article_links.append(full_url)

    # Save the collected article links to a CSV file

    # Remove duplicates from the collected links
    article_links = list(set(article_links))

    with open('data/apnews_article_links.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Article Link'])  # Write header
        for article in article_links[0:17]:
            writer.writerow([article])

    print("Article links saved to data/groundnews_article_links.csv")
else:
    print("Failed to retrieve the webpage.")
