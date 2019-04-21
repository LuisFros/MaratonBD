import requests

class Telegram:
    def __init__(self, token, heroku, id):
        self.url = "https://api.telegram.org/bot{}".format(token)
        self.token = token
        self.heroku = heroku
        self.id = id
        if heroku is not None:
            self.set_webhook()

    def set_webhook(self):
        ulr = "https://api.telegram.org/bot{}/setWebhook".format(self.token)
        print(requests.get(ulr, json={"url": self.heroku}))

    def send_message(self, message):
        a = requests.get(self.url + "/sendMessage",
                         params={'chat_id': self.id, 'text': message})
        print(a.json())


def tel_main(ngrok):
    chat_id = int("chat_id")
    token_tel = "token_here"
    aux = Telegram(token_tel, ngrok, chat_id)
    return aux


def encontrar_id(token):
    link = "https://api.telegram.org/bot{}/getUpdates".format(token)
    a = requests.get(link).json()
    return a["message"]["chat"]["id"]
