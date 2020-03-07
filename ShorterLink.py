import requests, json

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def shorter():
    url = input("Link Website: ") #example https://www.instagram.com/accounts/login/?hl=en
    data = {"url": url}
    result = json.loads(requests.post("https://api.boteater.us/short_link"+"?auth="+token_key, data=data).text)
    print("Short Link: "+result["result"])

shorter()
