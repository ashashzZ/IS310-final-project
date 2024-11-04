import requests

# URL of the website
url = "https://theonion.com/"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve the HTML content
    html_content = response.text

    # Save the HTML content to a file
    with open("theonion.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("HTML content successfully saved to 'theonion.html'")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")

