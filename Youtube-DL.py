import requests, json

### FROM https://youtube.com ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def ytSearch():
    search= input("Search query: ") #example joji cant get over you
    result = json.loads(requests.get("https://api.boteater.us/ytdl?search="+search+"&auth="+token_key).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])

def ytLink():
    url= input("Link Youtube: ") #example https://www.youtube.com/watch?v=zbxAB7rTpDc
    result = json.loads(requests.get("https://api.boteater.us/ytdl?url="+url+"&auth="+token_key).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])


ytLink()
