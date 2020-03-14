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
    

def smule():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Link Smule: ") 
    result = json.loads(requests.get(failOverAPI()+"/smule?url="+search+"&auth="+api_key).text)
    print("Title: "+result["result"]["title"])
    print("By: "+result["result"]["performed_by_url"])
    print("Message: "+result["result"]["message"])
    print("Image Link: "+result["result"]["image_link"])
    print("Download Link: "+result["result"]["download_link"])

smule()
