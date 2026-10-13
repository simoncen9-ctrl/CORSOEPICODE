# 1. Richiesta di Input all'utente
citta = input("Qual è la città in cui sei nato/a o in cui vivi? ")
animale = input("Qual è il nome del tuo animale domestico? ")

# 2. Generazione del Nome della Band (combinando le stringhe)
# Usiamo la f-string per unire le parole e aggiungere uno spazio in mezzo
nome_band = f"{citta} {animale}"

# 3. nome band = città + animale
print(f"Il nome perfetto per la tua band è: {nome_band}")