import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

directory = '/Users/ashash/Desktop/IS310 webs/data'
data = []

def scrape_article(url):
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



for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        article_type = filename.split('_')[2].replace('.csv', '')
        for index, row in df.iterrows():
            link = row['Article Link']
            title, text = scrape_article(link)
            data.append({
                'type': article_type,
                'link': link,
                'title': title,
                'text': text
            })

output_df = pd.DataFrame(data)
output_df.to_csv('data/scraped_articles.csv', index=False, encoding='utf-8')

