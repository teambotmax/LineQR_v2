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
    
def convert():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    authkey = input("Your Authkey: ")
    result = json.loads(requests.get(failOverAPI()+"/authkey2primary?authkey="+authkey+"&auth="+api_key).text)
    print("Android / IOS Token: "+ result["result"]["android_token"])
    print("Android Lite Token: "+ result["result"]["android_lite_token"])
        

convert()
