import requests, json

### FROM https://danbooru.donmai.us/ ###

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

def search():
    if api_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    page = input("Danboru Page: ") #example page 1 or 2 or 3 or etc
    result = json.loads(requests.get("https://api.boteater.us/danbooru?page="+page+"&auth="+api_key).text)
    for img in result["result"]:
        print("Link Image: "+img)

search()
