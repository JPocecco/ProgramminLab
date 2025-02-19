import csv

class CSVFile:
    def __init__(self, file_name):
        
       # Inizializza l'oggetto CSVFile con il nome del file.
        
        self.name = file_name

    def get_data(self):
        
       # Legge i dati dal file CSV e li restituisce come lista di liste.
        
        data = []
        mio_file = open(self.name , 'r')        
        for row in mio_file:
                    if len(row) > 1:  # Assicura che la riga abbia almeno due valori
                        data.append(row)
        

        return data

# Testiamo la classe con il file CSV fornito
csv_file = CSVFile("shampoo_sales.csv")
data = csv_file.get_data()
print(data[:5])  # Stampiamo solo le prime 5 righe per verifica