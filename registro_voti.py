voti = []

def aggiungi_voto(voto):
    voti.append(voto)
    print(f"Voto {voto} aggiunto.")

def togli_voto(voto):
    if voto in voti:
        voti.remove(voto)
        print(f"Voto {voto} rimosso.")
    else:
        print(f"Voto {voto} non trovato.")


aggiungi_voto(8)
aggiungi_voto(7.5)
aggiungi_voto(6)

print("Voti attuali:", voti)

togli_voto(7.5)

print("Voti aggiornati:", voti)