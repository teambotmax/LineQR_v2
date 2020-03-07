import requests, json

### FROM https://youtube.com ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    search = input("Search query: ") #example chainsmokers
    result = json.loads(requests.get("https://api.boteater.us/joox?search="+search+"&auth="+token_key).text)
    for music in result["result"]:
        print("")
        print("Artis: "+music["artist"])
        print("Title: "+music["title"])
        print("Link Audio: "+music["stream-url"])
        print("Link Image: "+music["image"])

search()
