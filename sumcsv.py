
def sum_csv(file_name):
    somma = 0
    my_file = open(file_name, 'r')
    for line in my_file:
        elementi = line.split(', ')
        somma = somma + float(elementi[2])
    return somma
    
print(sum_csv('shampoo_sales.csv'))
