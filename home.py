import urllib.request
import os
import pytweet
import requests
import json
import time

# Create a developer account and make an app in https://apps.twitter.com first

# Connecting to Twitter API
# Pytweet link - https://github.com/PyTweet/PyTweet/tree/master/
client = pytweet.Client(
    "Add your bearer token here",
    consumer_key="Add your consumer key here",
    consumer_key_secret="Add your secret key here",
    access_token="Add your access token here",
    access_token_secret="Add your secret access token here",
) 

while(True):

    # fetch a random meme object from reddit
    # Meme API - https://github.com/D3vd/Meme_Api
    response = requests.get("https://meme-api.herokuapp.com/gimme/")
    imgData = response.json()

    # avoiding GIF files
    imgURL = imgData["url"]
    while(imgURL.endswith("gif")):
        print("GIF spotted")
        response = requests.get("https://meme-api.herokuapp.com/gimme/")
        imgData = response.json()
        imgURL = imgData["url"]

    # choosing the correct file type
    location = "Memes/meme."
    file_types = ["jpg", "png"]
    for file_type in file_types:
        if imgURL.endswith(file_type):
            location += file_type
        else:
            continue

    # Meme
    urllib.request.urlretrieve(imgURL, location)
    file = pytweet.File(location) 

    # Caption
    title = imgData["title"]
    author = imgData["author"]
    caption = f"{title}\n\nMeme by: {author}"

    # Tweeting
    client.tweet(text=caption, file=file)

    # Deleting the meme from the folder
    os.remove(location)

    # Pause for 15mins
    time.sleep(900)
