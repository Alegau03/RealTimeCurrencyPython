from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import matplotlib.dates as mdates



def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup= BeautifulSoup(content,"html.parser")
    rate =soup.find("span",class_="ccOutputRslt").get_text()
    # FINO A QUESTO PUNTO PRENDE IL TASSO DI CAMBIO TRA LE DUE VALUTE E LO PRINTA
    rate= float(rate[:-4])
    return rate
    #Prendo il valore e torno solo i numeri



valori_stringa = []
valori_float = []

i=0
while i<5:
    time.sleep(60)
    currency_rate=(get_currency("EUR","USD"))
    ora = datetime.datetime.now().strftime("%H:%M:%S")
    valori_stringa.append(ora)
    valori_float.append((currency_rate))
    i+=1



# Creazione del grafico
plt.figure(figsize=(10, 6))  # Imposta le dimensioni del grafico

# Definisci l'asse x come valori stringa
plt.plot(valori_stringa, valori_float, marker='o', linestyle='-')

# Aggiungi titoli ed etichette agli assi
plt.xlabel("Tempo (Valori Stringa)")
plt.ylabel("Valori Float")
plt.title("Oscillazione dei Dati Float nel Tempo")

# Mostra i valori float sopra i punti lungo l'asse y
for i, val in enumerate(valori_float):
    plt.text(valori_stringa[i], val, f'{val:.6f}', ha='center', va='bottom')

plt.grid(True)  # Aggiungi una griglia
plt.xticks(rotation=45)  # Ruota le etichette sull'asse x per una migliore leggibilità
plt.tight_layout()  # Imposta il layout del grafico
plt.show()