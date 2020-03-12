import requests, json

### FROM https://danbooru.donmai.us/ ###

api_key= "INSERT API KEY HERE"

## GET API KEY FROM LINE ID: hertot ###

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
    search = input("Search query: ") #example chainsmokers
    result = json.loads(requests.get(failOverAPI()+"/joox?search="+search+"&auth="+api_key).text)
    for music in result["result"]:
        print("")
        print("Artis: "+music["artist"])
        print("Title: "+music["title"])
        print("Link Audio: "+music["stream-url"])
        print("Link Image: "+music["image"])

search()
