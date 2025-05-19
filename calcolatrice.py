# calcolatrice.py

def somma(a, b):
    return a + b

def sottrai(a, b):
    return a - b

def moltiplica(a, b):
    return a * b

def dividi(a, b):
    if b == 0:
        return "Errore: divisione per zero!"
    return a / b

def main():
    print("=== Calcolatrice Semplice ===")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    
    print("\nOperazioni disponibili:")
    print("1. Somma")
    print("2. Sottrai")
    print("3. Moltiplica")
    print("4. Dividi")

    scelta = input("Scegli un'operazione (1/2/3/4): ")

    if scelta == "1":
        print("Risultato:", somma(a, b))
    elif scelta == "2":
        print("Risultato:", sottrai(a, b))
    elif scelta == "3":
        print("Risultato:", moltiplica(a, b))
    elif scelta == "4":
        print("Risultato:", dividi(a, b))
    else:
        print("Operazione non valida!")

if __name__ == "__main__":
    main()
