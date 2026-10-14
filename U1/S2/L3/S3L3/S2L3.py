import math  # Importiamo la libreria matematica per usare il pi greco esatto


# Avviamo un ciclo infinito per non far chiudere il programma dopo un solo calcolo
while True:


    # Mostriamo a schermo il menu con le opzioni 
    print("\n--- MENU GEOMETRICO ---")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    print("Scrivi 'esci' per chiudere.")


    
    # Chiediamo all'utente quale figura vuole calcolare
    scelta = input("Fai una scelta: ").strip().lower()


    
    # Se l'utente scrive 'esci', blocchiamo il ciclo e chiudiamo il programma
    if scelta == 'esci':
        print("Uscita in corso...")
        break


        
    # Se sceglie 1, calcoliamo il perimetro del quadrato
    if scelta == '1':
        try:
            #il Float converte l'input in numero (intero o decimale) per i calcoli
            lato = float(input("Inserisci il lato: "))
            
            # Controlliamo che il numero non sia negativo
            if lato < 0:
                print("Errore: il lato non può essere negativo.\n")
                continue
                
            # Formula del perimetro: lato * 4
            perimetro = lato * 4
            print(f"Risultato - Perimetro del quadrato: {perimetro}\n")
            
        except ValueError:
            # Se l'utente scrive lettere invece di numeri, gestiamo l'errore
            print("Errore: devi inserire un numero!\n")


            
    # Se sceglie 2, calcoliamo la circonferenza del cerchio
    elif scelta == '2':
        try:
            # Chiediamo il raggio del cerchio
            raggio = float(input("Inserisci il raggio: "))
            
            if raggio < 0:
                print("Errore: il raggio non può essere negativo.\n")
                continue

                
            # Formula della circonferenza: 2 * pi greco * raggio
            circonferenza = 2 * math.pi * raggio
            print(f"Risultato - Circonferenza del cerchio: {circonferenza:.2f}\n")
            
        except ValueError:
            print("Errore: devi inserire un numero!\n")



            
    # Se sceglie 3, calcoliamo il perimetro del rettangolo
    elif scelta == '3':
        try:
            # Chiediamo base e altezza
            base = float(input("Inserisci la base: "))
            altezza = float(input("Inserisci l'altezza: "))
            
            if base < 0 or altezza < 0:
                print("Errore: i valori non possono essere negativi.\n")
                continue
                
            # Formula del perimetro: (base * 2) + (altezza * 2)
            perimetro = (base * 2) + (altezza * 2)
            print(f"Risultato - Perimetro del rettangolo: {perimetro}\n")
            
        except ValueError:
            print("Errore: devi inserire dei numeri!\n")
            
    else:
        # Se l'utente digita un numero o una parola non prevista nel menu
        print("Scelta non valida. Scegli 1, 2, 3 o scrivi 'esci'.\n")


        
# MINI-GLOSSARIO DEI COMANDI PYTHON

# # while True:     -> Crea un ciclo infinito che ripete il codice finché non incontra un 'break'.
# # break:          -> Interrompe e chiude immediatamente il ciclo in corso.
# # continue:       -> Salta il resto del giro attuale e riparte dall'inizio del ciclo.
# # input():        -> Mostra un messaggio a schermo e cattura ciò che digiti da tastiera.
# # float():        -> Converte l'input testuale in un numero (intero o con la virgola).
# # if:             -> "Se". Verifica se una condizione è vera; se sì, esegue il codice.
# # elif:           -> "Altrimenti se". Controlla un'altra condizione se la precedente (if) era falsa.
# # else:           -> "Altrimenti". Si attiva come ultima scelta se tutto il resto è falso.
# # try-except:     -> Blocco di sicurezza: 'try' prova a eseguire un'azione, 'except' blocca eventuali crash se l'utente sbaglia a digitare.
# # import math:    -> Importa la libreria di funzioni matematiche avanzate (es. math.pi).