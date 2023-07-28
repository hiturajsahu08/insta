import json
import requests
import time
from datetime import datetime

# Get the current date and day of the week (Monday is 0, Sunday is 6).
dt = datetime.now()
# o for monday or 6 for sunday
dayoftheday = dt.weekday()
#formate of date 2023-07-24
#dateoftheday=(str(dt)[:10])
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
    fields_txt = 'business_discovery.username('+ username +'){media{media_url,media_type,timestamp}}'

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
        'caption': "Follow for more....................DM for credit or removal................ #trending #viral #explorepage #funny #memes",
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
        'caption': "Follow for more.. #reelvideo #reelsinstagram #Reels #trendingreels #viralreels #explorepage #trending #viral #funny #memes ............DM for credit or removal..............",
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
    #print("\n\n\nproblem is: ",c)
    #print("before removal  \n\n: ",a)
    '''if c != 'media_url':
        print('we are here \n\n')
        del a[0]
    '''
    #rint("after removal : \n\n",a[1])
    for each in a:
        #print(each,"\n\n\n\n")
        try:
            image_url = each["media_url"]
            pos_type = each["media_type"]
        except:
            continue
        #timestamp_str=each["timestamp"]
        #count = count + 1
        #if count == 1:
        if (pos_type=="VIDEO" or pos_type=="REELS"):
            print("found a video")
            #if dateoftheday[:10]==timestamp_str[:10]:
            #    print("we are at right place")
            #print(image_url)
            break
    return image_url, pos_type

# Function to handle publishing content based on the day of the week.
def lets_publish_content(username):
    # Call the function to download the link of the post for the given username.
    #print(username)
    d = download_link_of_post(username)

    # Get the image URL and media type from the result.
    post_url, post_type = parse_link_from_result(d)

    # Check the media type and call the appropriate function for publishing.
    if post_type == "IMAGE" or post_type == "CAROUSEL_ALBUM":
    #    publish_image(post_url)
        print(0)
    if post_type == "VIDEO" or post_type == "REELS":
        publish_video(post_url)
        print(1)

# List of Instagram accounts to publish content for.
#not buiz account alex__mustakil09
#only with carasol profile : 'letss.bark'
list_of_ig_account = ['theindianmemes' ,'meme.wali01','shortmemer05','memesandook','funny_hindi_jokes_', 'bcbilliofficial', 'hindi_.memes', 'desii.crap', 'bhopali_epic_memes', 'superchutya', 'thesarcasticpage', 'sarcasm.villa', 'memes_ka_hutiapa','these_funny_videos','Gratefuldoggos','thehilarious.ted','_crankykitty_','Thefelinefunnies','Heyyhumor','Kehkire','Dogculture.xd','Your_innoncent_memer','Memesviral.in','_bestiies.4ever._','The.best.reels','Memekingzyx','Idiotic.dunia','_naughtysociety','Messywomenn','Desi.empire','69casm','Beviral.in','_gyanibaba']
print(len(list_of_ig_account))
print(dayoftheday)

#get indexes bases on weekday
#monday 0, tuesday 4
index=dayoftheday*4

#reset instance, 2pm 430pm 730pm 11pm four instances 0,1,2,3
file1 = open("/home/hitu/Documents/Instaproject/log.txt","r")
instance=int(file1.read())
file1.close()

'''
# Iterate through the list of Instagram accounts.
for idx, username in enumerate(list_of_ig_account):
    # Wait for 1 second before processing the next account.
    time.sleep(1)

    # Check if the index is within the range of today's day of the week (dayoftheday).
    if idx >= dayoftheday and idx < dayoftheday + 1:
        # Print the username to indicate which account's content is being processed.
        print(username)
        # Call the function to publish content for the current account.
        lets_publish_content(username)

test code
#print(len(list_of_ig_account))
d={}
lets_publish_content('letss.bark')
'''
lets_publish_content(list_of_ig_account[index+instance])

instance=instance+1
if instance>=4:
    instance=0
file1 = open("/home/hitu/Documents/Instaproject/log.txt","w")
file1.write(str(instance))
file1.close()
