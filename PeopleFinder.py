from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import requests
from Funciones import where_am_i, distance_calculator
import urllib.request
import json

key = ""
print("1")
longitude = where_am_i()[0]
latitude = where_am_i()[1]
print("2")
print(longitude)
print(latitude)

routeUrl = "http://dev.virtualearth.net/REST/v1/Locations/" + str(
    longitude) + "," + str(latitude) + "?o=xml&key=" + str(key)

request = urllib.request.Request(routeUrl)
response = urllib.request.urlopen(request)

# r = response.read().decode(encoding="utf-8-sig")
# result = json.loads(r)

stat = response.read().decode().split("FormattedAddress")
print(stat[1])
print(stat[1].strip(">").strip("</"))
dir = stat[1].strip(">").strip("</").split(", ")
print(dir)

# if i[4] == "Name>":
#    print(i[5:len(i)-1])
# Automatic searching
lugar = dir[0]

# Prototype only
lugar = "San Joaquin"

ckey = ""
csecret = ""
atoken = ""
asecret = ""
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


class Telegramer(StreamListener):
    def on_data(self, data):
        a = json.loads(data)
        if "place" in a.keys() and a["place"] != None:
            if a["place"]["country"] == "Chile":
                print(a)
            # if a["coordinates"]:
            #     x, y = a["coordinates"]["coordinates"]
            #     if self.according_distance(x, y):
            #         print("Entra")
            #         print(a)
                b = requests.get('https://df2b808b.ngrok.io/', json={
                    "mensaje": "Hemos detectado un evento de emergencia en tu cercania, por favor contactarse con las autoridades\n'{}'".format(a["text"])})
                return True
        return True

    def according_distance(self, x1, y1, x2=-33.497596, y2=-70.615543):
        print("Entra")
        if distance_calculator(y1, x1, x2, y2) <= 10:
            print(distance_calculator(y1, x1, x2, y2))
            return True
        return False

    def on_error(self, status):
        print(status)


twitterStream = Stream(auth, Telegramer())

h_keys = [lugar, "choque", "incendio", "accidente", "heridos", "balazos",
          "disparos",
          "volcamiento", "volcado", "fuga de gas"]
twitterStream.filter(track=h_keys)
