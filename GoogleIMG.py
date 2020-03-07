import requests, json

### FROM https://google.com ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    search = input("Search query: ")
    result = json.loads(requests.get("https://api.boteater.us/googleimg?search="+search+"&auth="+token_key).text)
    for img in result["result"]:
        print("Link Image: "+img)

search()
