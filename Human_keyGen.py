import json


def agregar_palabra(palabra):
    with open("Human_keys.json") as data:
        current = json.load(data)
    current.append(palabra)
    with open("Human_keys.json", "w") as file:
        json.dump(current, file)


palabras = ["choque", "incendio", "accidente", "heridos", "balazos", "disparos",
            "volcamiento", "volcado", "fuga de gas"]
for word in palabras:
    agregar_palabra(word)
