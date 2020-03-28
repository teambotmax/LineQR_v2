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
    

def tiktoksearch():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Tiktok User ID: ") 
    result = json.loads(requests.get(failOverAPI()+"/tiktok?userid="+search+"&auth="+api_key).text)
    for data in result["result"]:
        print("")
        print("Nickname: "+data["nickname"])
        print("Follower : "+str(data["follower_count"]))
        print("Following : "+str(data["following_count"]))
        print("Avatar URL : "+data["avatar_larger"]["url_list"][0])
        print("Cover URL : "+data["cover_url"][0]["url_list"][0])
        print("Signature : "+data["signature"])
        print("Birthday : "+data["birthday"])
    ## MORE ARG PLEASE CHECK API MANUAL ##
        

tiktoksearch()
