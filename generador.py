import requests
import random
import os
from time import sleep
from dotenv import load_dotenv
from ia import solicitar_texto

load_dotenv()
TOKEN = os.getenv("TOKEN")

lista_subs = ["animebutts","rule34","anihentair34", "jerkbudsHentai","animefeet"]

def solicitar_url():
    subreddit = random.choice(lista_subs)
    
    url = f"https://meme-api.com/gimme/{subreddit}"
    try:
        respuesta = requests.get(url)
        return respuesta.json().get("url")
    except Exception as e:
        print(f"Excepcion: {e}")
        return None

def registrar_url(url):
    with open("urls.txt", 'a') as f:
        f.write(f"{url} \n")

def verificar_url(url):
    with open("urls.txt", 'r') as f:
        urls = f.read()
        if url in urls:
            print("Ya existe la url")
            return False    
    return True

def subir_contenido(url, caption):
    
    if (not url or not caption):
        print('Los valores url o caption son invalidos ... ')
        return
    
    response = requests.get(url) # Obtener la imagen
    url_api = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    
    data = {
        "chat_id" : "@NsfwAnimeY",
        "caption": caption
    }
    files = {
        "photo": ("imagen.jpg", response.content)
    }
    
    try:
        r = requests.post(url_api, data=data, files=files)
        
        if r.status_code == 200:
            print('Correcto, El contenido fue subido con exito')
        
    except Excepcion as e:
        print(f'Error. Excepcion: {e}')


while True:
    url = solicitar_url()
    print(f"URL: {url}")
    if verificar_url(url): # True si la url es nueva.
        
        texto = solicitar_texto()
        print(f"TEXTO: {texto}")
        
        subir_contenido(url,texto)
        
        registrar_url(url)
        print("Url registrada, fin del programa")
        break
    
    sleep(10)