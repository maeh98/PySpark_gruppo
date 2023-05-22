"""
Rappresentare con le classi e l'ereditarietà una lista di operai di una fabbrica., e il loro ruolo in fabbrica.
creare un menù per l'aggiunta e la rimozione degli operai dalla lista
"""

# Creiamo la prima classe: Persona
class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


# Crea istanza
persona = Persona("Leo", "Pagani")
print(persona)
# print(f"...")
# Creiamo la seconda classe

