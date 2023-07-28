import json
import requests
import time
from datetime import datetime


# Get the current date and day of the week (Monday is 0, Sunday is 6).
dt = datetime.now()
dayoftheday = dt.weekday()

# Create an empty dictionary and results1 dictionary.
d = {}
results1 = dict()

# Initialize the image_url variable.
image_url = ''

# Function to download the link of a post from Instagram based on the username.
def download_link_of_post(username):
    # Access token for the Instagram Graph API (should be provided here or input interactively).
    access_token = "EAAVTPAKh6s8BAImmMej5HznZCJDYBAu9ZCvvjN3jNInOAG5okyHL3qWfMA5NYTz7u1BS1SSYmJIpZBHr3utQFzgQY6fG1LAuqaX7JAsyfEpclApYMFo2qvL8ZCHwEqxWIJxcvBq3Rh9CYPZAPwgn9N5ZCjewgRxU1cSTtlOucAhhCrq3zFx1qH"

    # Instagram User ID for business account (bcbilliofficial).
    ig_user_id = "17841449696506825"

    # URL for fetching data from the Instagram Graph API.
    down_url = 'https://graph.facebook.com/v17.0/{}'.format(ig_user_id)

    # Define fields to retrieve from the API for the specified username.
    fields_txt = 'business_discovery.username('+ username +'){media{media_url,media_type}}'

    # Payload with access token and fields information.
    payload = {
        'fields': fields_txt,
        'access_token': access_token
    }

    # Make a GET request to the Instagram Graph API to get the data.
    r = requests.get(down_url, params=payload)

    # Convert the response to JSON format.
    results = json.loads(r.text)

    # Copy the results to another dictionary.
    results1 = results.copy()

    # Return the results.
    return results

# Function to publish an image post to Instagram using the Instagram Graph API.
def publish_image(image_url):
    # Access token for the Instagram Graph API (should be provided here or input interactively).
    access_token = "EAAVTPAKh6s8BAImmMej5HznZCJDYBAu9ZCvvjN3jNInOAG5okyHL3qWfMA5NYTz7u1BS1SSYmJIpZBHr3utQFzgQY6fG1LAuqaX7JAsyfEpclApYMFo2qvL8ZCHwEqxWIJxcvBq3Rh9CYPZAPwgn9N5ZCjewgRxU1cSTtlOucAhhCrq3zFx1qH"

    # Instagram User ID for business account (bcbilliofficial).
    ig_user_id = "17841449696506825"

    # URL for posting media to Instagram.
    post_url = 'https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id)

    # Payload with the image URL, caption, and access token.
    payload = {
        'image_url': image_url,
        'caption': "insta post using graph api",
        'access_token': access_token
    }

    # Make a POST request to upload the image to Instagram.
    r = requests.post(post_url, data=payload)

    # Convert the response to JSON format.
    results12 = json.loads(r.text)

    # Get the creation ID of the uploaded media.
    creation_id = results12['id']

    # URL for the second POST request to publish the image to Instagram.
    second_url = 'https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)

    # Payload with the creation ID and access token.
    second_payload = {
        'creation_id': creation_id,
        'access_token': access_token
    }

    # Make a second POST request to publish the image on Instagram.
    r = requests.post(second_url, data=second_payload)

    # Print the response and success message.
    print(r.text)
    print("Image published to Instagram")

# Function to publish a video post to Instagram using the Instagram Graph API.
def publish_video(video_url):
    # Access token for the Instagram Graph API (should be provided here or input interactively).
    access_token = "EAAVTPAKh6s8BAImmMej5HznZCJDYBAu9ZCvvjN3jNInOAG5okyHL3qWfMA5NYTz7u1BS1SSYmJIpZBHr3utQFzgQY6fG1LAuqaX7JAsyfEpclApYMFo2qvL8ZCHwEqxWIJxcvBq3Rh9CYPZAPwgn9N5ZCjewgRxU1cSTtlOucAhhCrq3zFx1qH"

    # Instagram User ID for business account (bcbilliofficial).
    ig_user_id = "17841449696506825"

    # URL for posting media to Instagram.
    post_url = 'https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id)

    # Payload with the video URL, media type, caption, and access token.
    payload = {
        'video_url': video_url,
        'media_type': "VIDEO",
        'caption': "insta post using graph api",
        'access_token': access_token
    }

    # Make a POST request to upload the video to Instagram.
    r = requests.post(post_url, data=payload)

    # Convert the response to JSON format.
    results12 = json.loads(r.text)

    # Get the creation ID of the uploaded media.
    creation_id = results12['id']

    # Wait for 25 seconds to allow the video processing on Instagram's side.
    time.sleep(25)

    # URL for fetching the status of the media container.
    down_url = 'https://graph.facebook.com/v17.0/{}'.format(creation_id)

    # Payload with fields to retrieve the status code and access token.
    third_payload = {
        'fields': 'status_code',
        'access_token': access_token
    }

    # Make a GET request to check the status of the media container.
    r = requests.get(down_url, params=third_payload, timeout=10)

    # Print the status of the container.
    print("Status of the container: ", r.text)

    # URL for the second POST request to publish the video to Instagram.
    second_url = 'https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)

    # Payload with the creation ID and access token.
    second_payload = {
        'creation_id': creation_id,
        'access_token': access_token
    }

    # Make a second POST request to publish the video on Instagram.
    r = requests.post(second_url, data=second_payload)

    # Print the response and success message.
    #print(r.text)
    print("Video published to Instagram")

# Function to parse the link and media type from the result of the API call.
def parse_link_from_result(result):
    #print(result)
    y = result["business_discovery"]
    z = y["media"]
    a = z["data"]
    b = list(a[0])
    c = (b[0])
    count = 0
    final = dict(a[0])
    #print("we are here ", final)
    #print(type(final))
    if c != 'media_url':
        #print('we are here')
        del a[0]
    for each in a:
        image_url = each["media_url"]
        pos_type = each["media_type"]
        count = count + 1
        if count == 1:
            break
    return image_url, pos_type

# Function to handle publishing content based on the day of the week.
def lets_publish_content(username):
    # Call the function to download the link of the post for the given username.
    d = download_link_of_post(username)

    # Get the image URL and media type from the result.
    post_url, post_type = parse_link_from_result(d)

    # Check the media type and call the appropriate function for publishing.
    if post_type == "IMAGE" or post_type == "CAROUSEL_ALBUM":
        publish_image(post_url)
        #print(0)
    if post_type == "VIDEO" or post_type == "REELS":
        publish_video(post_url)
        #print(1)

# List of Instagram accounts to publish content for.
list_of_ig_account = ['funny_hindi_jokes_', 'bcbilliofficial', 'hindi_.memes', 'desii.crap', 'bhopali_epic_memes', 'superchutya', 'thesarcasticpage', 'sarcasm.villa', 'theindianmemes', 'memes_ka_hutiapa']

# Iterate through the list of Instagram accounts.
for idx, username in enumerate(list_of_ig_account):
    # Wait for 1 second before processing the next account.
    time.sleep(1)

    # Check if the index is within the range of today's day of the week (dayoftheday).
    if idx >= dayoftheday + 1 and idx < dayoftheday + 3:
        # Print the username to indicate which account's content is being processed.
        print(username)
        # Call the function to publish content for the current account.
        lets_publish_content(username)














