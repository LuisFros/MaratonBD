from flask import Flask, request
import json
from Telegram import tel_main
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def api_post():
    token = "token_here"
    telegra = tel_main("https://df2b808b.ngrok.io")
    if request.content_type == 'application/json':
        with open('post.txt', 'w') as fid:
            json.dump(request.json, fid)

        dic = request.json
        # Mensaje comando de Telegram

        telegra.send_message(dic["mensaje"])
        # if "message" in dic and "entities" in dic["message"]:
        #     id = dic['message']['chat']['id']
        #     # response = git.manejar_comando(dic["message"]["text"])
        #
        #     a = requests.get('https://api.telegram.org/bot{}'
        #                      '/sendMessage'.format(token),
        #                      params={'chat_id': id, 'text': "funciona flask"})

    return "strig"


if __name__ == "__main__":
    app.run(port=8080)
