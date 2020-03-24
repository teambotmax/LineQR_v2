
import requests, json

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
    

def instapost():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Link IG Post: ") 
    result = json.loads(requests.get(failOverAPI()+"/instapost?url="+search+"&auth="+api_key).text)
    print("Title: "+result["result"]["caption"])
    print("By: "+result["result"]["owner"]["username"])
    print("Total Like: "+str(result["result"]["like_count"]))
    for item in result["result"]["media"]:
        print("")
        if item["is_video"]:
            print("Video Link: "+item["video"])
        print("Image Link: "+item["img"])
        

instapost()
