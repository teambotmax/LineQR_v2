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
    

def tiktokdownload():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Link Tiktok Video: ") 
    result = json.loads(requests.get(failOverAPI()+"/tiktok?url="+search+"&auth="+api_key).text)
    print("Description: "+result["result"]["desc"])
    print("Video Link: "+result["result"]["video"]["bit_rate"][0]["play_addr"]["url_list"][1])
    ## MORE ARG PLEASE CHECK API MANUAL ##
        

tiktokdownload()
