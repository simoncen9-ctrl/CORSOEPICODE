# Importa il modulo 'os' per gestire le interazioni con il sistema operativo
import os

# Importa la libreria ufficiale di Google GenAI per comunicare con i modelli Gemini
from google import genai

# Inizializza il client dell'API. 
# Legge automaticamente la chiave segreta configurata nella variabile d'ambiente GEMINI_API_KEY.
client = genai.Client()

def main():
    print("Invio del prompt a Gemini...")
    
    # Invia una richiesta di generazione di contenuto sincrona (senza chat continua)
    response = client.models.generate_content(
        model="gemini-3.8-flash", # Il modello linguistico leggero e veloce di Google
        contents="Spiega in una frase perché la crittografia end-to-end è fondamentale nella Cyber Security.", # Il prompt inviato al modello
    )
    
    print("\nRisposta da Gemini:")
    # Stampa il testo estratto dalla risposta ricevuta dall'API
    print(response.text)

# Punto di ingresso standard di Python: esegue la funzione main() se il file viene avviato direttamente
if __name__ == "__main__":
    main()


# MINI GLOSSARIO DEGLI ELEMENTI UTILIZZATI IN QUESTO SCRIPT:
 
# 1. import os:
#    Libreria standard di Python per interfacciarsi con il sistema operativo 
#    e leggere le variabili d'ambiente (come la chiave API).
#
# 2. client = genai.Client():
#    Crea l'oggetto client autenticato che permette allo script di comunicare 
#    con i servizi cloud di Google GenAI.
#
# 3. client.models.generate_content(...):
#    Funzione dell'SDK utilizzata per inviare un prompt "singolo" (una tantum) 
#    al modello senza mantenere lo storico di una chat continua.
#
# 4. contents:
#    Il parametro in cui viene inserita la stringa (il prompt) con la richiesta 
#    o la domanda da rivolgere all'intelligenza artificiale.
#
# 5. response.text:
#    L'attributo dell'oggetto di risposta che estrae e restituisce il testo 
#    generato e pulito restituito dal modello Gemini.
