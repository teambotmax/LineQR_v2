import requests, json

### FROM https://youtube.com ###

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

if api_key == "INSERT API KEY HERE":
    print("GET API KEY FROM LINE ID: hertot")
    raise Exception("Wrong API Key")
def ytSearch():
    search= input("Search query: ") #example joji cant get over you
    result = json.loads(requests.get(failOverAPI()+"/ytdl?search="+search+"&auth="+api_key).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])

def ytLink():
    url= input("Link Youtube: ") #example https://www.youtube.com/watch?v=zbxAB7rTpDc
    result = json.loads(requests.get(failOverAPI()+"/ytdl?url="+url+"&auth="+api_key).text)
    print("Title: "+result["result"]["title"])
    print("Artist: "+result["result"]["artist"])
    print("Thumbnail: "+result["result"]["thumbnail"])
    print("Video Download: "+result["result"]["video_url"])
    print("Audio Download: "+result["result"]["audio_url"])


ytLink()
