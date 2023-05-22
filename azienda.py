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
print(dipendente1.to_string())
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

while False:
    # condizione
    switch_menu()


 





