import requests, json

### FROM https://9gag.com/ ###

api_key= "INSERT API KEY HERE"

## GET API KEY FROM LINE ID: hertot ###
categoryList = ["hot", "trending", "fresh", "indonesia", "indonesia-fresh", "funny", "funny-fresh", "animals", "animals-fresh", "anime-manga", "anime-manga-fresh", "animewaifu", "animewaifu-fresh", "awesome", "awesome-fresh", "comic-webtoon", "comic-webtoon-fresh", "cosplay", "cosplay-fresh", "gaming", "gaming-fresh", "gif", "gif-fresh", "meme", "meme-fresh", "video", "video-fresh", "savage", "savage-fresh", "wtf", "wtf-fresh"]
def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"
    
def search():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(categoryList)
    category = input("Insert Category: ")
    if category not in categoryList:
        raise Exception("Wrong Category")
    result = json.loads(requests.get(failOverAPI()+"/9gag?category="+category+"&auth="+api_key).text)
    for data in result["result"]:
        print("Title: "+data["title"])
        print("Type Post: "+data["type"])
        print("Link Image: "+data["images"]["image700"]["url"])
        if data["type"] == "Animated":
            print("Link Video: "+data["images"]["image460sv"]["url"])
        print("Original Link: "+data["url"])
        print("")
        

search()
