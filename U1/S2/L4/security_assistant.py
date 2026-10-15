# Importa il modulo 'os' per interagire con il sistema operativo (es. leggere le variabili d'ambiente)
import os

# Importa la libreria ufficiale di Google GenAI per comunicare con i modelli Gemini
from google import genai

# Importa i tipi di configurazione specifici per definire parametri avanzati (come il system instruction)
from google.genai import types

def main():
    # Inizializza il client dell'API. 
    # Legge in automatico la chiave segreta salvata nella variabile d'ambiente GEMINI_API_KEY.
    client = genai.Client()
    
    # 1. DEFINIZIONE DEL SYSTEM PROMPT (ISTRUZIONE DI SISTEMA)
    # Serve a dare un'identità fissa e un comportamento specifico all'intelligenza artificiale,
    # vincolandola a rispondere come un esperto di Cyber Security difensiva.
    system_instruction = (
        "Sei un assistente esperto di Cyber Security difensiva. "
        "Aiuti gli sviluppatori a scrivere codice sicuro, a identificare vulnerabilità "
        "comuni (come OWASP Top 10) e a spiegare concetti di sicurezza in modo chiaro, "
        "professionale e orientato alle best practice."
    )

    # 2. CREAZIONE DELLA SESSIONE DI CHAT PERSISTENTE
    # Utilizziamo 'client.chats.create' anziché una semplice generazione singola.
    # Questo permette al modello di ricordare la cronologia della conversazione.
    chat = client.chats.create(
        model="gemini-3.8-flash", # Il modello linguistico leggero e veloce di Google
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3, # Valore basso (0.3): rende le risposte più tecniche, precise e focalizzate
        )
    )

    print("--- Security Assistant avviato ---")
    print("Scrivi una domanda sulla sicurezza informatica (es. 'Come prevengo le SQL injection in Python?')")
    print("Digita 'exit' o 'quit' per terminare la chat.\n")

    # 3. CICLO DI CONVERSAZIONE INTERATTIVO (LOOP)
    # Permette di mantenere il programma attivo finché l'utente non decide di uscire.
    while True:
        # Cattura l'input digitato da tastiera dall'utente
        user_input = input("Tu: ")
        
        # Condizione di uscita dalla chat
        if user_input.lower() in ["exit", "quit"]:
            print("Chiusura del Security Assistant. Resta sicuro!")
            break
        
        # Ignora i messaggi vuoti
        if not user_input.strip():
            continue

        try:
            # Invia il messaggio al chatbot mantenendo lo storico dei messaggi precedenti
            response = chat.send_message(user_input)
            
            # Stampa la risposta generata da Gemini
            print(f"\nAssistant: {response.text}\n" + "-"*50)
            
        except Exception as e:
            # Gestisce eventuali errori (es. problemi di connessione o quote esaurite)
            print(f"\n[Errore]: {e}\n")

# Punto di ingresso standard in Python: avvia la funzione main() se il file viene eseguito direttamente
if __name__ == "__main__":
    main()

    # GLOSSARIO E RIEPILOGO DEI CONCETTI UTILIZZATI NELL'ESERCIZIO:


# 2. Virtual Environment (venv):
#    Una cartella isolata sul computer che contiene una copia indipendente 
#    di Python e delle librerie installate. Evita conflitti tra i pacchetti 
#    di progetti diversi.
#
# 3. comando 'pip install google-genai pandas':
#    Il comando del gestore di pacchetti di Python per scaricare e installare 
#    la libreria ufficiale Google GenAI e pandas per la gestione dei dati.
#
# 4. Variabile d'ambiente (GEMINI_API_KEY):
#    Un modo sicuro per memorizzare la chiave segreta dell'API nel terminale 
#    senza scriverla "in chiaro" all'interno del codice sorgente.
#
# 5. client = genai.Client():
#    L'istruzione che autentica lo script Python presso i server di Google 
#    sfruttando la chiave API impostata nel sistema.
#
# 6. Modello (gemini-3.8-flash):
#    Il Large Language Model (LLM) leggero, veloce ed efficiente messo 
#    a disposizione da Google per elaborare prompt testuali e chat.
#
# 7. System Prompt (system_instruction):
#    Le istruzioni di sistema iniziali passate al modello per definirne il "ruolo" 
#    (assistente di Cyber Security), orientandone tono, competenze e rigore.
#
# 8. Chat Persistente (client.chats.create):
#    Funzione avanzata dell'SDK che gestisce in autonomia lo storico dei messaggi, 
#    permettendo all'AI di ricordare le battute precedenti durante la conversazione.
#
# 9. Temperatura (temperature=0.3):
#    Parametro che regola la creatività del modello. Valori bassi (vicini a 0) 
#    rendono l'output più deterministico, tecnico e rigoroso, ideale per la programmazione.
# =====================================================================