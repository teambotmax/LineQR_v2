import requests, json

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    if token_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FIRST FROM: https://api.boteater.us/get_token")
        raise Exception("Wrong API Key")
    search = input("Link Website: ") #example google.com
    result = json.loads(requests.get("https://api.boteater.us/ssweb?url="+search+"&auth="+token_key).text)
    print("Link SS: "+result["result"])

search()
