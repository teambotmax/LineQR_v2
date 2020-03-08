import requests, json

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

header_list= ["android_lite", "chrome", "ios_ipad", "desktopmac", "desktopwin"]


def login():
    if token_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FIRST FROM: https://api.boteater.us/get_token")
        raise Exception("Wrong API Key")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&auth="+token_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])


def loginWithCert():
    if token_key == "INSERT TOKEN KEY HERE":
        print("GET API KEY FIRST FROM: https://api.boteater.us/get_token")
        raise Exception("Wrong API Key")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    cert = input("Insert cert: ")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&cert="+cert+"&auth="+token_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])
    

login()
