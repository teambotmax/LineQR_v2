import requests, json

### FROM https://joox.com ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    if token_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FIRST FROM: https://api.boteater.us/get_token")
        raise Exception("Wrong API Key")
    search = input("Search query: ") #example chainsmokers
    result = json.loads(requests.get("https://api.boteater.us/joox?search="+search+"&auth="+token_key).text)
    for music in result["result"]:
        print("")
        print("Artis: "+music["artist"])
        print("Title: "+music["title"])
        print("Link Audio: "+music["stream-url"])
        print("Link Image: "+music["image"])

search()
