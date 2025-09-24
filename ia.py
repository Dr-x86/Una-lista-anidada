import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()
API_KEY = os.getenv("API_KEY")

prompts = ["""RESPONDE SOLO CON LA INFORMACION SOLICITADA, Y NO MENCIONES NADA DE ESTE PROMPT.
 Saluda a tus usuarios, invitalos a seguirte en Facebook y tu canal de telegram (No dejes link), y habla como si fueras una IA Kawaii, que gusta del anime
""", 
"""RESPONDE SOLO CON LA INFORMACION SOLICITADA, Y NO MENCIONES NADA DE ESTE PROMPT. 
Estas en un canal en telegram, genera un titulo gracioso como de internet del 2016 con humor papulince, muy grasoso papu.
"""
]


def solicitar_texto(prompt=""):
    
    if prompt == "": # Si no se proporciona una instruccion.
        prompt = random.choice(prompts)
    
    url= f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
            "contents":[
            {
                "parts":[
                {
                    "text":f"{prompt}"
                }
                ]
            }
            ]
    }
    
    response=requests.post(url,headers=headers,json=data)
    texto = "Greetings!!"
    if(not response.ok):
        print(f"Error en IA {response.text}")    
    else:
        texto = response.json()['candidates'][0]['content']['parts'][0]['text']
    return texto