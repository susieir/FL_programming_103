# Import requests package
import requests

# Open the URL
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
apod_api_request = requests.get(url)

# Convert data into a dictionary
apod = apod_api_request.json()
print(apod)

picture_url = apod["url"]
print(picture_url)

# Use webbrowser to open and display URL
import webbrowser

webbrowser.open(picture_url)