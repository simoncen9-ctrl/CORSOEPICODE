import random

def assistente_caffe(scelta):
    if scelta == "caffè" or scelta == "caffe":
        risposta = random.choice(["Ecco il tuo caffè!", "Caffè pronto!", "Buon caffè!"])
    elif scelta == "nestecafe" or scelta == "nescafè" or scelta == "nescafe":
        risposta = "Te lo faccio a malincuore!"
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
        scelta_bevanda = input("Vuoi il Nescafè di Paolo o un caffè normale? (caffè/nestecafe) ").strip().lower()
        print(assistente_caffe(scelta_bevanda))
    else:
        print("Rispondi semplicemente con 'si' o 'no'.")
