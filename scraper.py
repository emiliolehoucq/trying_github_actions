# Script to test scraping with GitHub Actions
# Emilio Lehoucq

# Importing libraries
import requests
import datetime

# URL to scrape
url = 'https://en.wikipedia.org/wiki/Mindfulness'

# Requesting the URL
response = requests.get(url)

# Get title
title = response.text.split('<title>')[1].split('</title>')[0]
print(title)

# Get current date and time
dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# Path of the file
path = f'data/{dt}.txt'

# Save the title to a file
with open(path, 'w') as file:
    file.write(title)
