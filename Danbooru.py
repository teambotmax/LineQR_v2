import requests, json

### QR ROTATE LOGIN EXAMPLE ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    page = input("Danboru Page: ") #example page 1 or 2 or 3 or etc
    result = json.loads(requests.get("https://api.boteater.us/danbooru?page="+page+"&auth="+token_key).text)
    for img in result["result"]:
        print("Link Image: "+img)

search()
