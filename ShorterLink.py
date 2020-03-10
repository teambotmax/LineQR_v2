import requests, json

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

def shorter():
    if api_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    url = input("Link Website: ") #example https://www.instagram.com/accounts/login/?hl=en
    data = {"url": url}
    result = json.loads(requests.post("https://api.boteater.us/short_link"+"?auth="+api_key, data=data).text)
    print("Short Link: "+result["result"])

shorter()
