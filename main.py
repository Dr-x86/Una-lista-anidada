import requests
import random
import os
from time import sleep
from dotenv import load_dotenv
# from ia import solicitar_texto

load_dotenv()
TOKEN = os.getenv("TOKEN")


"""
"animebutts","rule34","anihentair34","jerkbudsHentai","rule_34_for_all",
"animefeet","ElizabethLiones","Rule_34","CartoonPorn","SFW_Rule34","hentai",
"""


lista_subs = ["hentai","masteruwuoficial","spicyteto","HatsuneMiku_Hentai","hatsunemikuhentaiv3","vocaloidhentai"]

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


def solicitar_url():
    subreddit = random.choice(lista_subs)
    print(f"Subreddit elegido: {subreddit}")
    url = f"https://meme-api.com/gimme/{subreddit}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        
        data = {
            "url": respuesta.json().get("url"),
            "title": respuesta.json().get("title")
        }
        
        return data
    
    except requests.exceptions.HTTPError as err:
        print(f"\nExcepcion err: {err}\nContenido: { respuesta.json()['message'] }\n")
        return None
    
    except ReferenceError as r:
        print(f"\nExcepcion err: {r}\nContenido: { respuesta.json()['message'] }\n")
        return None
    
    except Exception as e:
        print(f"\nExcepcion err: {e}\nContenido: { respuesta.json()['message'] }\n")
        return None


def subir_contenido(url, caption=''):    
    if (not url):
        print(f'Los valores url son invalidos ...  {url}')
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
            return True

        else:
            print(f'Error codigo {r.status_code}, Detalles: {r.text}')
        
    except Excepcion as e:
        print(f'Error. Excepcion: {e}')
        
    return False
    
    
def limpiar_urls(limite):
    with open("urls.txt", 'r') as f:
        urls = f.readlines()
      
    if len(urls) >= limite:
        open('urls.txt', 'w').close()
        print("Limpieza ... ")
        return

def obtener_data(max = 100):    
    intentos = 0
    while intentos < max: 
        data = solicitar_url()
        
        if data == None:
            print("Error - La data no puede ser un valor nulo")
            intentos += 1
            continue
            
        if verificar_url(data.get('url')):
            return data
        
        intentos+=1


def iterable(maximo = 10):    
    limpiar_urls(256)
    
    i = 0
    while i <= maximo: 
        data = obtener_data()
        
        url = data.get("url")
        title = data.get("title")
        
        if subir_contenido(url, title):
            registrar_url(url)
            break
        
        i=+1
    

if __name__ == "__main__":
    
    iterable()
    