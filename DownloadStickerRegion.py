import requests, json

### FROM https://danbooru.donmai.us/ ###

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

### YOUR LINE MUST LOGIN WITH FACEBOOK ###

region_list = ['UnitedStates', 'Canada', 'Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'BosniaandHerzegovina', 'Brazil', 'BritishVirginIslands', 'Brunei', 'Bulgaria', 'Cambodia', 'Cameroon', 'Canada', 'Chile', 'China', 'Colombia', 'CostaRica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'DominicanRepublic', 'Ecuador', 'Egypt', 'ElSalvador', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guyana', 'HashemiteKingdomofJordan', 'HongKong', 'Hungary', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Latvia', 'Liechtenstein', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malaysia', 'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'NewZealand', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'PapuaNewGuinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'PuertoRico', 'Qatar', 'RepublicofLithuania', 'RepublicofMoldova', 'Romania', 'Russia', 'SaudiArabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'SouthAfrica', 'SouthKorea', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'TrinidadandTobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'UnitedArabEmirates', 'UnitedKingdom', 'UnitedStates', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia']
header_list= ["ios", "android_lite", "chrome", "ios_ipad", "desktopmac", "desktopwin"]

def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"

def getPaidSticker():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(region_list)
    region = input("Insert Region: ")
    if region not in region_list:
        raise Exception("Wrong Region!!!")
    token = input("Insert Your Token: ")
    to = input("Insert Your Receiver Mid: ")
    print(header_list)
    header = input("Insert Header: ")
    if header not in header_list:
        raise Exception("Wrong Header!!!")
    sticker_id = input("Insert Your Sticker ID: ")
    result = json.loads(requests.get(failOverAPI()+"/line_sticker?type=paid&region="+region+"&to="+to+"&product_id="+sticker_id+"&token="+token+"&header="+header+"&auth="+api_key).text)
    print(result)
    
def getFreeSticker():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(region_list)
    region = input("Insert Region: ")
    if region not in region_list:
        raise Exception("Wrong Region!!!")
    result = json.loads(requests.get(failOverAPI()+"/line_sticker?region="+region+"&auth="+api_key).text)
    sticker_list = []
    for item in result["result"]:
        print("")
        print("Name: "+item["name"])
        print("Region: "+region)
        print("Author: "+item["author"])
        print("ID: "+item["id"])
        sticker_list.append(item["id"])
    print("")
    token = input("Insert Your Token: ")
    mid = input("Insert Your Mid: ")
    print(header_list)
    header = input("Insert Header: ")
    if header not in header_list:
        raise Exception("Wrong Header!!!")
    for sticker in sticker_list:
        result = json.loads(requests.get(failOverAPI()+"/line_sticker?type=free&region="+region+"&to="+mid+"&product_id="+sticker+"&token="+token+"&header="+header+"&auth="+api_key).text)
        print(result)


getFreeSticker()
