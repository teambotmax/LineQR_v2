import requests, json

### FROM https://otakudesu.org/ ###

api_key= "INSERT API KEY HERE"

## GET API KEY FROM LINE ID: hertot ###

def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"
    

def search():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    result = json.loads(requests.get(failOverAPI()+"/otakudesu?&auth="+api_key).text)
    for item in result["result"]:
        print("")
        print("Title: "+item["title"])
        print("Episode: "+item["episode"])
        print("Date: "+item["date"])
        print("Link Image: "+item["img"])
        print("Link Stream: "+item["stream"]["url"])

search()
