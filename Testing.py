from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# consumer key, consumer secret, access token, access secret.
ckey = ""
csecret = ""
atoken = ""
asecret = ""
# trusho
cuenta_bombero = str(908094329918554112)


# real
# cuenta_bombero = str(305559699)


class Listener(StreamListener):
    def on_data(self, data):
        a = json.loads(data)
        ### Omitir Retweets ##
        if not (a["retweeted"]):
            for i in a:
                # Pretty print"#
                print(i + "---->" + "".join(map(str, str(a[i]))) + "\n")
            return True
        else:
            return False

    def on_error(self, status):
        print(status)


# Obtiene ubicaciones de tweets de bomberos, sólo si tienen el link.


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

h_keys = ["choque", "incendio", "accidente", "heridos", "balazos", "disparos",
          "volcamiento", "volcado", "fuga de gas"]


twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["PYTONESUC"])

# AreaStream = Stream(auth, Listener())
# AreaStream.filter(locations=[-33.501661, -70.616093, -33.49598, -70.606724])


# "TwitTwittest"
