from flask import Flask, render_template, request
import random

app = Flask(__name__)

piropos = [
    "¿Eres Google? Porque tienes todo lo que busco 😍",
    "Si la belleza fuera pecado, tú no tendrías perdón 🙀",
    "¿Tienes un mapa? Porque me perdí en tu mirada ❤️",
    "Eres como el sol... iluminas todo 🌞",
    "Si fueras canción, serías mi favorita 🎶",
    "¿Crees en el amor a primera vista o paso otra vez? 😉",
    "acaso te llamas canaan? o por que quiero conquistarte?",
    "me dijieron piensa en algo bonito, no pude pensar en algo mas no que fueran tus ojitos",
    "Eres como la oracion. Buena, agradable y perfecta",
    "Tu pueblo sera mi pueblo, tu Dios sera mi Dios y tus padres seran mis suegros",
    "en cada mañana no puedo pensar en algo mas que no seas tu",
    "eres tan hermosa que hasta el cielo se quiere lucir de colores solo para ganarte en belleza",
    "Ni los israelitas le dieron tantas vueltas a jerico como lo haces tu en mi mente",
    "el color de tus ojos, desperto mi interes"
]

@app.route("/", methods=["GET", "POST"])
def index():
    piropo = random.choice(piropos)
    return render_template("index.html", piropo=piropo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
