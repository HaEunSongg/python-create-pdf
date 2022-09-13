# -*- coding: utf-8 -*-
"""
Color Table img 

"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import rcParams
import img2pdf 
from PIL import Image 
import os 

rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False


estaciones = [
    {
        "codigo": "H0011",
        "nombre": "Mira en Lita",
        "rio": "Mira - Ibarra",
        "amarilla": 3,
        "roja": 4.5
    },
    {
        "codigo": "H0015",
        "nombre": "Mira en Lita",
        "rio": "Mira - Ibarra",
        "amarilla": 3.5,
        "roja": 4.5
    },
    {
        "codigo": "H0017",
        "nombre": "Mira en Lita",
        "rio": "Mira - Ibarra",
        "amarilla": 1.3,
        "roja": 2
    },
    {
        "codigo": "H0064",
        "nombre": "Mira en Lita",
        "rio": "Mira - Ibarra",
        "amarilla": 1.3,
        "roja": 2
    },
]


def generateNivelRandom():
    import random
    nivel = round(random.uniform(0, 3), 3)
    return nivel


def setAlertNivel(nivel, amarilla, roja):

    if nivel < amarilla:
        return "Normal"
    elif nivel >= amarilla and nivel < roja:
        return "Amarilla"
    elif nivel >= roja:
        return "Roja"
    

def colorCell(val):
  if val =='Roja':
    color='#FF2828'
    return 'background-color: %s' % color
  elif val =='Amarilla':
    color='#FFF700'
    return 'background-color: %s' % color
  else:
    color='#74E200'
    return 'background-color: %s' % color

# df = pd.DataFrame(np.random.random((10,3)), columns = ("Date", "estacion", "temperatura"))

data = []
for estacion in estaciones:
    nivelRandom = generateNivelRandom()
    levelAlerta = setAlertNivel(
        nivelRandom,
        estacion['amarilla'],
        estacion['roja'])
    data.append(
        [
            estacion["codigo"],  # Code
            estacion["nombre"],
            estacion["rio"],
            nivelRandom,  # level
            levelAlerta


        ])


df = pd.DataFrame(
    data, columns=[
        'Codigo', 'Nombre estación', 'Río - Cantón', 'nivel (m)', 'Nivel de Alerta'
    ])
         
df

df=df.style.applymap(colorCell, subset=['Nivel de Alerta'])


img_path = r"C:\Users\Haeun\Documents\Python Scripts\df_styled.png"
  
pdf_path = r"C:\Users\Haeun\Documents\Python Scripts\df_styled.pdf"
  
image = Image.open(img_path) 
  
pdf_bytes = img2pdf.convert(image.filename) 
  
file = open(pdf_path, "wb") 
  
file.write(pdf_bytes) 
  
image.close() 
  
file.close() 
  
print("Successfully made pdf file") 
    
