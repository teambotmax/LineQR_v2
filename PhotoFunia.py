import requests, json

### FROM https://photofunia.com/ ###

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

### EFECT LIST ONE ###
def photofunia1(filename):
    category_list = ['at-the-gallery', 'halloween-pumpkins', 'rijskmuseum', 'broadway-at-night', 'the-frame', 'morning-newspaper', 'new-york-at-night', 'easter-greetings', 'brussels-museum', 'vintage-scooter', 'card-with-flowers', 'giant-artwork', 'christmas-present', 'christmas-diary', 'posters-on-the-wall', 'explorer-drawing', 'at-the-beach', 'in-the-woods', 'banksy-shredder', 'golden-coin', 'autumn-leaf', 'interior-picture', 'shopping-arcade', 'poster-wall', 'magic-card', 'sketch-practicing', 'passage', 'cloudy-filter', 'postage-stamp', 'activists', 'travellers-sketch', 'mirror', 'ink-portrait', 'old-tram', 'truck-advert', 'gallery-visitors', 'girl-with-bicycle', 'easter-flowers', 'painting-snap', 'coffee-and-tulips', 'night-street', 'red-wall', 'rose-vine', 'city-billboard', 'travellers-diary', 'frosted-filter', 'underground-poster', 'portrait-gallery', 'festive-greetings', 'xmas-time', 'famous-gallery', 'missing-person', 'the-book', 'business-newspaper', 'tablet', 'vinyl-store', 'black-and-white-mural', 'vintage-photos', 'art-experts', 'billboards-at-night', 'scroll', 'worker-by-the-billboard', 'analogue-tv', 'old-camera', 'square-billboard', 'tokyo-crossing', 'in-the-cinema', 'spring-flowers', 'easter-nest', 'open-book', 'shop-posters', 'love-letter', 'two-valentines', 'champagne', 'snow-globe', 'roller-shutters', 'harry-potter-style-poster', 'watercolour-painting', 'black-white-gallery', 'lightning', 'summoning-spirits', 'stadium', 'coloured-pencils', 'four-billboards', 'travelers-suitcase', 'piccadilly-arcade', 'morning-mug', 'art-on-the-brick-wall', 'big-screen', 'spy-dossier', 'drawing-photo', 'artistic-filter', 'very-old-book', 'hanging-billboard', 'rainy-night', 'easter-card', 'top-secret', 'roses-and-marshmallows', 'artist-in-a-hat', 'playful-cat', 'wall-mural', 'gallery-visitor', 'night-motion', 'campaign', 'santas-parcel-picture', 'graffiti-circle-on-the-wall', 'you-are-my-universe', 'new-year-frames', 'museum-banners', 'brass-frame', 'red-and-blue', 'painting-and-sketches', 'toasts', 'wedding-day', 'vhs', 'double-decker', 'breaking-news', 'passing-by-the-painting', 'cookbook', 'lemon-tree', 'evening-billboard', 'kitty-and-frame', 'double-exposure', 'playing_cards', 'press_conference', 'picture_at_the_gallery', 'five_paintings', 'heart_locket', 'antique_shop', 'marine', 'gallery_of_art', 'art_book', 'london_gallery', 'deep_forest', 'ornament', 'new_year_tree', 'winter_spirit', 'apples', 'indian_summer', 'queens_theatre', 'quill', 'painter_on_the_bridge', 'evening_storm', 'brugge', 'medieval_art', 'cappuccino', 'streets_of_new_york', 'cool_wind', 'modern_art_exhibition', 'classic_book', 'watercolours', 'pavement_artist', 'easter_postcard', 'daffodils', 'memories_of_paris', 'reading_on_the_balcony', 'asteroid', 'frame_and_roses', 'copying_masterpiece', 'oxford', 'taxis_on_times_square', 'card_with_laces', 'christmas_tree', 'snowy_day', 'midnight_billboard', 'on_the_bike', 'autumn', 'bottle_of_wine', 'together_forever', 'pisa_street', 'space_romance', 'morning_news', 'pictures_sale', 'sixties', 'citylight', 'film_scan', 'picadilly_circus', 'interview', 'graffiti_billboard', 'romantic_etude', 'broadway', 'girls_dream', 'summer_love', 'vintage_shot', 'jade', 'mint_frame', 'last_warm_day', 'dark_night', 'romantic', 'vue', 'easter', 'lomography', 'warm_spring', 'snow_in_london', 'aqua', 'vintage_frame', 'sepia', 'pink_heart', 'be_my_valentine', 'family_in_museum', 'contrast_bw', 'oil_painting', 'new_year_presents', 'xmas_tree', 'graffiti_wall', 'graffiti_artist', 'lavander', 'truck', 'roses', 'genova', 'graffiti', 'photobooth', 'riverside_billboard', 'stacco', 'theatre', 'reading', 'fancywork', 'embroidery', 'national_gallery', 'sidewalk', 'mysterious_painting', 'prince_of_wales_theatre', 'hand_lens', 'photo_exhibition', 'nyc_billboards', 'swedish_billboard', 'cyclist', 'nyc', 'art_gallery', 'city', 'at_the_mirror', 'tulips', 'flower_frame', 'lego_portrait', 'cafe', 'ax', 'artist_in_the_dark', 'hammock', 'photowall', 'huge_billboard', 'pencil_drawing', 'decorated_billboard', 'leftfield', 'pavement_art', 'night_square', 'vintage_photo', 'underground', 'street_artist', 'watercolor', 'drawing', 'valentine', 'times_square', '3_shop_posters', 'girls_with_poster', 'watchinng', '100_dollars', 'smart_kitty', 'puzzle', 'pastel', 'urban_billboard', 'glass', 'broken_glass', 'brick_wall', 'stamps', 'icecream', 'modern_art', 'rainy_day', 'urban', 'local_shop', 'grieder', 'jigsaw_puzzle', 'lego', 'under_the_heel', 'esquire', 'galatea', 'coin', 'macho', 'reproduction', 'death_proof', 'chris_pirillo', 'shop_poster', 'retail_park', 'purple_sky', 'warhol', 'special_billboard', 'mini_cooper', 'reconstruction', 'frame', 'night_city', 'paris_hilton', 'two_female_fans', 'vogue', 'behind_the_fence', 'perfume_shop', 'billboard', 'music_shop', 'shopping_center']
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(category_list)
    category = input("Insert Category: ")
    if category not in category_list:
        raise Exception("Wrong Category")
    files = {"file": open(filename, "rb")}
    result = json.loads(requests.post("https://api.boteater.us/photofunia1?category="+category+"&auth="+api_key,files=files).text)
    print("Link Image: "+result["result"]["image"])
    print("Animated: "+str(result["result"]["animated"]))
        

photofunia1("path_to_file")
