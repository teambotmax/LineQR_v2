import requests, json

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

header_list= ["android_lite", "chrome", "ios_ipad", "desktopmac", "desktopwin"]


def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"
    

def login():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get(failOverAPI()+"/line_qr_v2?header="+header+"&auth="+api_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+api_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+api_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])


def loginWithCert():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    cert = input("Insert cert: ")
    result = json.loads(requests.get(failOverAPI()+"/line_qr_v2?header="+header+"&cert="+cert+"&auth="+api_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+api_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])
    
    
### EXAMPLE ON SCRIPT BOT ###
def getToken(to, header="ios_ipad"):
    api_key = "INSERT API KEY HERE"
    result = json.loads(requests.get(failOverAPI()+"/line_qr_v2?header="+header+"&auth="+api_key).text)
    client.sendMessage(to, "QR Link: "+result["result"]["qr_link"])
    client.sendMessage(to, "Login IP: "+result["result"]["login_ip"])
    client.sendMessage(to, "QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+api_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    client.sendMessage(to, "Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+api_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    return result["result"]["token"]
    

login()
