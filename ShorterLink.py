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
    

def shorter():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    url = input("Link Website: ") #example https://www.instagram.com/accounts/login/?hl=en
    data = {"url": url}
    result = json.loads(requests.post(failOverAPI()+"/short_link"+"?auth="+api_key, data=data).text)
    print("Short Link: "+result["result"])

shorter()

