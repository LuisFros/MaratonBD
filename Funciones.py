import math
import requests
import json


# Obtiene ubicaciones de tweets de bomberos, sólo si tienen el link.
def bomberos_tweet_filter(tweet):
    if len(tweet["entities"]["urls"]) > 0:
        b = tweet["entities"]["urls"][0]["expanded_url"]
        x = b.split("=")[1].split(",")[0]
        y = b.split("=")[1].split(",")[1].strip("&t")
        return x, y
    else:
        print("tweet sin link")


# calcula la distancia entre dos coordenadas del tipo lat1 lon1 lat2 lon2
# calcula la distancia entre dos coordenadas del tipo lat1 lon1 lat2 lon2
def distance_calculator(lat1, lon1, lat2, lon2):
    lat1 = float(lat1) * math.pi / 180
    lon1 = float(lon1) * math.pi / 180
    lat2 = float(lat2) * math.pi / 180
    lon2 = float(lon2) * math.pi / 180
    return (math.acos(
        math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(
            lat2) * math.cos(lon1 - lon2))) * 6371


def where_am_i():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    # print("you are at:")
    # print(lat, lon)
    return (lat, lon)
