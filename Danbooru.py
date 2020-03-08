import requests, json

### FROM https://danbooru.donmai.us/ ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    if token_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FIRST FROM: https://api.boteater.us/get_token")
        raise Exception("Wrong API Key")
    page = input("Danboru Page: ") #example page 1 or 2 or 3 or etc
    result = json.loads(requests.get("https://api.boteater.us/danbooru?page="+page+"&auth="+token_key).text)
    for img in result["result"]:
        print("Link Image: "+img)

search()
