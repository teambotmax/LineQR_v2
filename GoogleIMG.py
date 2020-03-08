import requests, json

### FROM https://google.com ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    if token_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FIRST FROM: https://api.boteater.us/get_token")
        raise Exception("Wrong API Key")
    search = input("Search query: ") # example anime
    result = json.loads(requests.get("https://api.boteater.us/googleimg?search="+search+"&auth="+token_key).text)
    for img in result["result"]:
        print("Link Image: "+img)

search()
