import requests
from bs4 import BeautifulSoup
import csv

url = 'https://theonion.com/politics/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

article_links = []

for article in articles:
    # find the <a> tag inside the article
    link_tag = article.find('a', href=True)
    if link_tag:
        link = link_tag['href']
        article_links.append(link)

# Step 5: Save the article links to a CSV file
with open('data/theonion_links_politics.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Article Link'])  # Write the header

    # Write each article link to the file
    for link in article_links:
        writer.writerow([link])
