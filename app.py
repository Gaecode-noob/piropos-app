from flask import Flask, render_template, request
import random
import json
import os
from datetime import date

app = Flask(__name__)

ARCHIVO_DATOS = "datos_piropos.json"

PIROPOS = [
    "Si la belleza fuera delito, tú tendrías cadena perpetua",
    "¿Eres Google? Porque tienes todo lo que busco",
    "Si fueras un emoji, serías el de fueguitos 🔥",
    "Contigo hasta el WiFi tiene mejor conexión",
    "Si fueras un error 404, es porque no te encuentro defectos",
    "¿Eres el sol? Porque iluminas todos mis días",
    "No eres wifi, pero siento una conexión contigo",
    "Si besarte fuera pecado, caminaría feliz por el infierno",
    "¿Crees en amor a primera vista o paso otra vez?",
    "Perdí mi número... ¿me das el tuyo?",
    "Ojalá fueras lunes para verte toda la semana",
    "Si fueras tarea, te haría con gusto",
    "acaso te llamas canaan? o por que quiero conquistarte?",
    "me dijieron piensa en algo bonito, no pude pensar en algo mas que fueran tus ojitos",
    "Eres como la oracion. Buena, agradable y perfecta",
    "Tu pueblo sera mi pueblo, tu Dios sera mi Dios y tus padres seran mis suegros",
    "en cada mañana no puedo pensar en algo mas que no seas tu",
    "eres tan hermosa que hasta el cielo se quiere lucir de colores solo para ganarte en belleza",
    "Ni los israelitas le dieron tantas vueltas a jerico como lo haces tu en mi mente"
]

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {"ultima_fecha": "", "piropo": ""}

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f)

def obtener_piropo():
    datos = cargar_datos()
    hoy = str(date.today())

    if datos["ultima_fecha"] == hoy:
        return datos["piropo"]

    nuevo = random.choice(PIROPOS)
    datos["ultima_fecha"] = hoy
    datos["piropo"] = nuevo
    guardar_datos(datos)

    return nuevo

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        piropo = random.choice(PIROPOS)
    else:
        piropo = obtener_piropo()

    return render_template("index.html", piropo=piropo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
