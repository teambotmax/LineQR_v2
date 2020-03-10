import requests, json

### FROM https://joox.com ###

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

def search():
    if api_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Search query: ") #example chainsmokers
    result = json.loads(requests.get("https://api.boteater.us/joox?search="+search+"&auth="+api_key).text)
    for music in result["result"]:
        print("")
        print("Artis: "+music["artist"])
        print("Title: "+music["title"])
        print("Link Audio: "+music["stream-url"])
        print("Link Image: "+music["image"])

search()
