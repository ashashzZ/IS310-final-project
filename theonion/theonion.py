import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a request to the Onion's website
url = 'https://theonion.com/politics/'
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all articles and their links
articles = soup.find_all('article')

# Step 4: Create a list to store article links
article_links = []

for article in articles:
    # Find the <a> tag inside the article
    link_tag = article.find('a', href=True)
    if link_tag:
        link = link_tag['href']
        article_links.append(link)

# Step 5: Save the article links to a CSV file
with open('links/theonion_links_opinion.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Article Link'])  # Write the header

    # Write each article link to the file
    for link in article_links:
        writer.writerow([link])

print("Article links have been saved to 'theonion_article_links.csv'")
