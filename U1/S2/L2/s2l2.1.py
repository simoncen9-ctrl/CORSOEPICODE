# CALCOLA LA MEDIA DI UNA LISTA DI NUMERI CON UNA FINANZA MOBILE DI DIMENSIONE N


def calcola_media_mobile(numeri, n):
  medie = []
  for i in range(len(numeri)):
    # 1. Determina l'indice di inizio della finestra
    inizio = max(0, i - n + 1)

    # 2. Estrae la finestra degli ultimi n elementi
    finestra = numeri[inizio : i + 1]

    # 3. Calcola la media e la aggiunge alla lista dei risultati
    media = sum(finestra) / len(finestra)
    medie.append(media)

  return medie


# Dati di input richiesti dalla traccia bonus
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

# Chiamata della funzione
risultato = calcola_media_mobile(numeri, n)

# Stampa del risultato finale
print(risultato)