import requests, json

### FROM https://wall.alphacoders.com/ ###

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

def search():
    if api_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Search query: ") #example naruto
    result = json.loads(requests.get("https://api.boteater.us/alphacoders?search="+search+"&auth="+api_key).text)
    for img in result["result"]:
        print("")
        print("Image Name: "+img["name"])
        print("Link Image: "+img["url"])

search()
