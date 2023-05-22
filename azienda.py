"""
Un'azienda ha bisogno di un app per gestione le proprie risorse umane-
Release 1.0: 
Bisogna integrare un sistema di registrazione dipendenti con funzionalità CRUD (aggiungere dipendenti, eliminarli, modificare le loro informazioni) e che generi automaticamente un report quando richiesto. 
Release 2.0:
Bisogna implementare una funzionalità di calcolo delle retribuzioni e della gestione ferie.

"""

"""
classe dipendenti
classe con lista dipendenti (oggetti), accesso con password per il ceo

switch menu, login, pw per dipendenti

Menu:
- dipendente
- gestore
- esci

Menu dipendenti:
Chiedi pw
- Visualizza ferie
- visualizza retribuzione
- visualizza report
- esci

Menu gestore:
Chiedi pw
- Aggiungi dipendente
- Modifica dipendente
- Rimuovi dipendente
- Genera report
- esci

Menu  modifica ...

"""
import random
class Persona:
    # attributi: nome, cognome, password
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def to_string(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"

class Dipendente(Persona):
    password = ""
    def __init__(self, nome, cognome, inquadramento_aziendale, reparto):
        super().__init__(nome, cognome)   
        self.inquadramento_aziendale = inquadramento_aziendale
        self.reparto = reparto 
    
    def genera_password(self, n):
        self.password = ""
        char_list = ["0","1","2","3","4","5","6","7","8","9","A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        for i in range(0,n):
            self.password += char_list[random.randint(0,61)]
        return self.password
    
    def to_string(self):
        return super().to_string() + f" lavora nel reparto {self.reparto} con un inquadramento_aziendale {self.inquadramento_aziendale}"


    # attributi: inquadramento_aziendale, reparto
    # metodo: calcolo_retribuzione, to_string (ereditato), scelta ferie
    
dipendente1 = Dipendente("nome", "cognome", 1, 2)
print("------------------------------")
print(dipendente1.to_string())
print("------------------------------")

# lista_dipendenti (contiene oggetti)
# funzioni aggiungi dipendenti, rimuovi dipendenti, modifica dipendenti, report

def switch_menu():
    # esci
    # gestore
    # dipendente
    pass

def switch_menu_gestore():
    # aggiungi_dipendenti()
    # modifica_dipendenti()
    # rimuovi_dipendenti()
    # report()
    pass

"""
esci = False
while not esci:
    esci = switch_menu()
"""

 

"""

class ORDINE:
    lista_ordinazioni = []
    nome = ""
    conto_totale = 0
    MENU = [("antipasto", 5), ("primo piatto", 10), ("secondo piatto", 15), ("dolce", 3)]

    # Settare nome
    def chiedi_nome(self):
        self.nome = input("Come ti chiami?\n")
    
    def esci(self):
        print("Hai scelto di uscire, arriverci!")
        return None

    def aggiungi_piatto(self):
        print("I piatti disponibili sono: ")
        for contatore in range(4):
            print(f"{contatore}. {self.MENU[contatore][0]} costa {self.MENU[contatore][1]}€")
        
        piatto_scelto = int(input().strip())

        self.lista_ordinazioni += [ordinazione.MENU[piatto_scelto]]

    def modifica_piatto(self):
        print("I piatti nell'ordinazione sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{contatore}. {self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")

        print ("Quale desideri rimuovere?\n")
        piatto_da_rimuovere = int(input().strip())
        print("Con quale piatto lo vuoi rimpiazzare? \nI piatti disponibili sono: ")
        for contatore in range(4):
            print(f"{contatore}. {self.MENU[contatore][0]} costa {self.MENU[contatore][1]}€")
        
        piatto_da_aggiungere = int(input().strip())
        self.lista_ordinazioni[piatto_da_rimuovere] = self.MENU[piatto_da_aggiungere]


    def ordinare_conto(self):
        # Resetta conto
        self.conto_totale = 0
        print("I piatti ordinati sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{contatore}. {self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")
            self.conto_totale += self.lista_ordinazioni[contatore][1]
        
        print(f"Il conto totale di {self.nome} è {self.conto_totale}")


    def switch_primo(self):
        print("Scegli l'opzione desiderata: ")
        print("1. Ordina un piatto")
        print("2. Modificare un piatto")
        print("3. Ordinare il conto")
        print("4. Esci")

        variabile = input().strip()         

        if variabile == "1":
            self.aggiungi_piatto()

        elif variabile == "2":
            self.modifica_piatto()

        elif variabile == "3":
            self.ordinare_conto()
        
        elif variabile == "4":
            self.esci()
            return "esci"
        
        else:
            print("L'ordine non è stato eseguito correttamente")


ordinazione = ORDINE()
ordinazione.chiedi_nome()

esci = False
while not esci:
    esci = ordinazione.switch_primo()

"""



