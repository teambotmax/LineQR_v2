def genSendMessage():
    text = input("Input Text: ")
    print("line://app/1586794970-VKzbNLP7?act=sendMessage&text="+text.replace(" ","+"))

def genSendImage():
    url = input("Input Link Image: ")
    print("line://app/1586794970-VKzbNLP7?act=SendImage&url="+url)

def genSendAudio():
    url = input("Input Link Audio: ")
    print("line://app/1586794970-VKzbNLP7?act=sendAudio&url="+url)

def genSendVideo():
    url = input("Input Link Video: ")
    thumb = input("Input Link Thumbnail: ")
    print("line://app/1586794970-VKzbNLP7?act=sendVideo&url="+url+"&thumb="+thumb)

def genSendSticker():
    url = input("Input Link Sticker Image: ")
    print("line://app/1586794970-VKzbNLP7?act=sendSticker&url="+url)

def genViewSticker():
    ID = input("Input Sticker ID: ")
    print("line://app/1586794970-VKzbNLP7?act=viewSticker&id="+ID)

def genYoutubeDLSearch():
    search = input("Input Search Query: ")
    print("line://app/1586794970-VKzbNLP7?act=ytdl&search="+search)

def genYoutubeDLLink():
    url = input("Input Link Youtube: ")
    print("line://app/1586794970-VKzbNLP7?act=ytdl&url="+url) 

def genPhotoFunia1():
    print("line://app/1586794970-VKzbNLP7?act=photofunia1")


genPhotoFunia1()
