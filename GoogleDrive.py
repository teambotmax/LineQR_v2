import requests, json

### FROM https://danbooru.donmai.us/ ###

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

def upload(path):
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    files = {'file': open(path,"rb")}
    result = json.loads(requests.post(failOverAPI()+"/gdrive?auth="+api_key,files=files).text)
    print(result["result"])


upload("path_to_file")
