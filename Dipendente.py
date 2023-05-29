from Persona import Persona
import random
from Controllo import controllo

# Classe figlio
# attributi ereditati: nome, cognome
# attributi proprietari: password, primo_ingresso, ore_ferie, inquadramento_aziendale, reparto
class Dipendente(Persona):
    password = ""
    primo_ingresso = True
    ore_Ferie = 0
    char_array = "0123456789QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm"
    ore_lavorate = 40


    def __init__(self, nome, cognome, inquadramento_aziendale, reparto):
        super().__init__(nome, cognome)
        self.inquadramento_aziendale = inquadramento_aziendale
        self.reparto = reparto

    # metodo che genera una password d'accesso in maniera randomica
    def genera_password(self, n):
        self.password = ""
        for i in range(0, n):
            self.password += self.char_array[random.randint(0, 61)]
        return self.password

    def to_string(self):
        return (
            super().to_string()
            + f" lavora nel reparto {self.reparto} con un inquadramento_aziendale {self.inquadramento_aziendale}"
        )

    # metodo che calcolo lo stipendio del Dipendente in base ad un parametro
    def calcola_stipendio(self):
        stipendio_base = {1: 1200, 2: 1500, 3: 2000, 4: 3000}
        coefficiente = {1: 1, 2: 1.1, 3: 1.2, 4: 1.3, 5: 1.4, 6: 1.5, 7: 2, 8: 2.5}
        stipendio = (
            stipendio_base[self.reparto] * coefficiente[self.inquadramento_aziendale]
        )
        return stipendio

    def premio(self):
        if 20 <= self.ore_lavorate <= 40:
            bonus = 0.1
            print(f"Lo stipendio incluso il bonus è: {self.calcola_stipendio() * (1 + bonus) * self.ore_lavorate / 40: ,.2f}€")
        elif self.ore_lavorate < 20:
            bonus = 0
            print(f"Il tuo stipendio è: {self.calcola_stipendio() * self.ore_lavorate / 40: ,.2f}€")
        elif self.ore_lavorate > 40:
            bonus = 0.2
            print(f"Lo stipendio incluso il superbonus è: {self.calcola_stipendio() * (1 + bonus) * self.ore_lavorate / 40: ,.2f}€")

    def inserisciOre(self):
        flag = False
        while not flag:
            print("Inserisci un numero di ore lavorate da 0 a 60")
            numero_ore = input()
            if controllo(0, 60, numero_ore):
                self.ore_lavorate = int(numero_ore)
                flag = True
            else:
                print("Valore non accettabile")

    # metodo per inserire le ferie
    def settaFerie(self):
        flag = True
        while flag:
            print("Aggiungi orario ferie")
            print("Premi 1 per aggiornare le tue ferie 2 per uscire")
            scelta = input("Inserisci la tua risposta\n")
            if scelta == "1":
                print("Puoi richiedere fino a un massimo di 5 ore di ferie")
                nuove_ore = input("Inserisci le ore che vuoi richiedere\n")
                if controllo(1, 6, nuove_ore):
                    self.ore_Ferie = int(nuove_ore)
                    print("Ferie accettate")
                    flag = False
                else:
                    print("Inserire un comando valido")

            elif scelta == "2":
                print("Stai uscendo dal sistema...")
                flag = False

            else:
                print("Inserisci numero valido\n")

    def modificaPassword(self):
        flag = False
        while not flag:
            print("Imposta la tua nuova password")
            print("1. Generare una password randomizzata")
            print("2. Digita la nuova password")
            print("3. Esci")
            scelta = input("Inserisci la tua risposta\n")
            if scelta == "1":
                self.genera_password(8)
                print(f"La password randomizzata è: {self.password}")
                flag = True
            
            elif scelta == "2":
                flag2 = False
                while not flag2:
                    print("Digita la nuova password, deve contenere almeno 8 caratteri alfanumerici")
                    nuova_password = input()
                    pw_ok = True

                    if len(nuova_password) < 8:
                        print("Errore, password troppo corta")
                        pw_ok = False
                        continue

                    else:
                        for i in range(0, len(nuova_password)):
                            if nuova_password[i] not in self.char_array:
                                print("Carattere non ammesso, utilizza 0-9, a-z, A-Z")
                                pw_ok = False
                                break
                    
                    if pw_ok == True:
                        self.password = nuova_password
                        print("Password modificata correttamente")
                        flag2 = True

            elif scelta == "3":
                print("Stai uscendo dal sistema...")
                flag = True

            else:
                print("Inserisci numero valido\n")

dip1 = Dipendente("topo", "lino", 2, 2)
print(dip1.to_string())
#dip1.modificaPassword()
#print(dip1.password)
dip1.inserisciOre()
print(f"Hai lavorato {dip1.ore_lavorate} ore")
print(dip1.premio())
