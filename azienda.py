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

Menu generale:
1 dipendente
2 gestore
3 esci

Menu dipendenti (1):
Chiedi nome, cognome, pw
- Visualizza ferie
- visualizza retribuzione
- visualizza report
- esci

Menu gestore (2):
Chiedi pw
- Aggiungi dipendente
- Modifica dipendente
- Rimuovi dipendente
- Genera report
- esci

Menu  modifica ...

ToDo
- aggiungere calcolo salario
- aggiungere controllo: esiste già un dipendente all'aggiunta?
- Roadmap
- risolvere bug

ROADMAP
modifica tutto
gestione permessi (ferie/ore uscita/malattia...)
aggiungere reparto
unicita utente


"""
# Importa librerie
import random
    

# Setta variabili
lista_dipendenti = []
admin_password = "12345678"


# -------------------------------------------- CLASSI --------------------------------------------------------

# Classe padre
class Persona:
    # attributi: nome, cognome, password
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def to_string(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"

# Classe figlio
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


# -------------------------------------------- FUNZIONI --------------------------------------------------------

# Funzione per verificare che l'utente sia presente e conosca la pw corretta
def controllo_password_dipendente(lista_dipendenti):
    nome = input("\nNome: ")
    cognome = input("Cognome: ")

    for dipendente in lista_dipendenti:

        if dipendente.nome == nome and dipendente.cognome == cognome:
            password = input("Password: ")

            if password == dipendente.password:
                print("\nPassword corretta.") # inserire menù dipendente
                return True 

            else:
                print("\nPassword errata.")
                return False

            
    else:
        print("\nErrore: dipendente non registrato.\n")
        return False

# Funzionalita per gestore: aggiungi dipendenti
def aggiungi_dipendente():
    print("Stai aggiungendo un nuovo dipendente")
    nome = str(input("Inserisci il nome: ")).strip()
    cognome = str(input("Inserisci il cognome: ")).strip()
    inquadramento_aziendale = str(input("Inserisci l'inquadramento aziendale: "))
    reparto = str(input("Inserisci il reparto: "))
    dipendente = Dipendente(nome,cognome,inquadramento_aziendale,reparto)
    # Fai in modo che il nuovo dipendente abbia una nuova password
    dipendente.genera_password(8)
    # aggiungi funzione controllo
    lista_dipendenti.append(dipendente)

# Funzionalita per gestore: modifica dipendenti
"""
def modifica_dipendente():
    report()
    indice_dipendente = int(input("Seleziona il dipendente da modificare: \n").strip())
    nuovo_inquadramento_aziendale = int(input("Inserisci il nuovo inquadramento aziendale\n").strip())
    lista_dipendenti[indice_dipendente].inquadramento_aziendale = nuovo_inquadramento_aziendale
    print("Modifica avvenuta con successo")
"""
def modifica_dipendente():
    report()
    flag = False
    while not flag: 
        indice_dipendente = input("Seleziona il dipendente da modificare: \n").strip()
        if controllo(0, len(lista_dipendenti), indice_dipendente):
            indice_dipendente_int = int(indice_dipendente)
            flag = True

    flag = False
    while not flag: 
        nuovo_inquadramento_aziendale = input("Inserisci il nuovo inquadramento aziendale\n").strip()
        if controllo(1, 9, nuovo_inquadramento_aziendale):
            nuovo_inquadramento_aziendale_int = int(nuovo_inquadramento_aziendale)
            flag = True

    lista_dipendenti[indice_dipendente_int].inquadramento_aziendale = nuovo_inquadramento_aziendale_int
    print("Modifica avvenuta con successo")


def controllo(a, b, elemento):
    valori_accettabili = [str(iteratore) for iteratore in range(a, b)]
    if elemento in valori_accettabili:
        return True
    else:
        return False

# Funzionalita per gestore: rimuovi dipendenti
def rimuovi_dipendente():
    report()
    indice_dipendente = int(input("Seleziona il dipendente che hai deciso di rimuovere\n").strip())
    lista_dipendenti.pop(indice_dipendente)
    print("Dipendente rimosso")

# Funzionalita per gestore: stampa il report
def report():
    if lista_dipendenti == []:
            print("Non ci sono dipendenti nella lista")
    else:
        for iteratore, elemento in enumerate(lista_dipendenti):
            print(f"{iteratore}. {elemento.to_string()}")
            
# MENU scelte dipendente: stampa retribuzione o gestisci ferie    
def menu_dipendente():
    print("Scegli l'opzione desiderata: ")
    print("1. Visualizza la propria retribuzione")
    print("2. Scegli data ferie")
    print("3. Esci")

    variabile = input().strip()         

    if variabile == "1":
        pass        # Da aggiungere
     
    elif variabile == "2":
        pass        # Da aggiungere

    elif variabile == "3":
        return "esci"
    
    else:
        print("Scegliere un comando valido")

# MENU scelta gestore: gestisci lista dipendenti (CRUD) o stampa report
def menu_gestore():
    print("Scegli l'opzione desiderata: ")
    print("1. Aggiungi dipendenti")
    print("2. Modificare un dipendente")
    print("3. Rimuovi dipendenti")
    print("4. Report")
    print("5. Esci")

    variabile = input().strip()         

    if variabile == "1":
        aggiungi_dipendente()
     
    elif variabile == "2":
        modifica_dipendente()

    elif variabile == "3":
        rimuovi_dipendente()
    
    elif variabile == "4":
        report()

    elif variabile == "5":
        return "esci"       # True
    
    else:
        print("Scegliere un comando valido")


# -------------------------------------------- BLOCCO CODICE PRINCIPALE --------------------------------------------------------


# Inizio codice
dip1 = Dipendente("Mario","Rossi",1,2)
dip2 = Dipendente("Luigi","Bianchi",3,4)
dip1.genera_password(4)
dip2.genera_password(4)
lista_dipendenti.append(dip1)
lista_dipendenti.append(dip2)
#print(dip1.password)
#print(dip2.password)



# Inizia I/O: ripeti richiesta scelta per output errati, altrimenti esci
flag = False
#flag = True
while not flag:
    print("Scegli il tipo di account: ")
    print("1. Account gestore")
    print("2. Account dipendente")
    print("3. Esci")

    variabile = input().strip()      

    if variabile == "1":
        # Chiedi e controlla la pasword
        print("Stai entranto come gestore, digita la password")
        password_digitata = input()
        if password_digitata != admin_password:
            print("Password errata! Chiusura del programma in corso...")
        else:
            # Esegui azioni fino che l'utente non ha finito  
            esci = False
            while not esci:
                esci = menu_gestore()
     
    elif variabile == "2":
        # Chiedi e controlla la pasword
        print("Digita nome")
        nome = input().strip()
        print("Digita cognome")
        cognome = input().strip()
        print("Stai entranto come dipendente, digita la password")
        password_digitata = input()
        if controllo_password_dipendente(lista_dipendenti):        # Chiamare funzione Leo
            # Esegui fino che l'utente non ha finito
            esci = False
            while not esci:
                esci = menu_dipendente()
        else: 
            print("Password errata!")
    
    elif variabile == "3":
        print("esci")
        flag = True
    
    else:
        print("Scegliere un comando valido")


