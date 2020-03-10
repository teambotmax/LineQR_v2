import requests, json

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

def ssweb():
    if api_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Link Website: ") #example google.com
    result = json.loads(requests.get("https://api.boteater.us/ssweb?url="+search+"&auth="+api_key).text)
    print("Link SS: "+result["result"])

ssweb()
