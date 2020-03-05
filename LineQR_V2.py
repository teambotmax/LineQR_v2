import requests, json

### QR ROTATE LOGIN EXAMPLE ###

header_list= ["android_lite", "chrome", "ios_ipad", "desktopmac", "desktopwin"]

print(header_list)

def login():
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])


def loginWithCert():
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    cert = input("Insert cert: ")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&cert="+cert).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])

login()
