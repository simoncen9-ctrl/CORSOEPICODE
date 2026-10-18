import random

def assistente_caffe(scelta):
    if scelta == "caffè" or scelta == "caffe":
        risposta = random.choice(["Ecco il tuo caffè!", "Caffè pronto!", "Buon caffè!"])
    elif scelta == "nescafe" or scelta == "nescafè" or scelta == "nescafe":
        risposta = random.choice(["Pessima idea, ma non posso non fartelo!", "Questa terribile bevanda è pronta!", "Solo perchè sento astinenza di caffeina, te lo faccio!"]) 
    else:
        risposta = "Mi dispiace, non posso preparare quella bevanda."
    
    return risposta

while True:
    scelta_utente = input("Ciao, hai già preso il caffè oggi? (si/no/esci) ").strip().lower()

    if scelta_utente == "esci":
        print("Arrivederci!")
        break
    elif scelta_utente == "si":
        print("Ottimo, allora sei già carico!")
    elif scelta_utente == "no":
        scelta_bevanda = input("Vuoi il Nescafè di Paolo o un caffè normale? (caffè/nescafe) ").strip().lower()
        print(assistente_caffe(scelta_bevanda))
    else:
        print("Rispondi semplicemente con 'si' o 'no'.")
