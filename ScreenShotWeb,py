import requests, json

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    search = input("Link Website: ") #example google.com
    result = json.loads(requests.get("https://api.boteater.us/ssweb?url="+search+"&auth="+token_key).text)
    print("Link SS: "+result["result"])

search()
