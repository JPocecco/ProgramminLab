import csv

def sommalista(lista):
    return sum(lista)

def sum_csv(file_name):
    valori = []
    try:
        with open(file_name, 'r', newline='') as my_file:
            reader = csv.reader(my_file)  # Usa il modulo csv per gestire i file in modo sicuro
            next(reader)  # Salta l'intestazione

            for elementi in reader:
                if len(elementi) > 1:  # Controlla che ci siano abbastanza colonne
                    try:
                        valore = float(elementi[1])  # Converte il valore in float
                        valori.append(valore)
                    except ValueError:
                        print(f"Errore di conversione: '{elementi[1]}' non è un numero valido.")

    except FileNotFoundError:
        print(f"Errore: Il file '{file_name}' non esiste.")
        return None

    return sommalista(valori)

# Testiamo il codice con il tuo file
somma_totale = sum_csv('shampoo_sales.csv')
print(f"Somma totale delle vendite di shampoo: {somma_totale}")

