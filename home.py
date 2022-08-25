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
    "AAAAAAAAAAAAAAAAAAAAAHLbgAEAAAAAH1Pejzy3rS6ZyVmEBQ2iTQTtew4%3DydwSDzWK2sFatOdHgGPsl2FOG2V43604xUEHLcvXEW7gYWAK0w",
    consumer_key="DfIabDgzwrNm2i0JNThaPOG2b",
    consumer_key_secret="aaoHxeACfCkGeuTMuiuR2wwiKhANamk518qCxJVDUI2ypPRldU",
    access_token="1561011215752564736-oJmHJrT9arByqfgxiJjd39u0LRsxDN",
    access_token_secret="Cb9uatzNFBhrxzb3DV8xFsjzX2O27SJ0UIncSn7P2BjJc",
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