import requests, json
token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def ytSearch(search):
    result = json.loads(requests.get("https://api.boteater.us/ytdl?search="+search+"&auth="+token_key).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])

def ytLink(link):
    result = json.loads(requests.get("https://api.boteater.us/ytdl?url="+link+"&auth="+token_key).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])
