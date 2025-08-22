import statistics
import csv 

#Leer los datos de ventas mensuales desde un csv
monthly_sales = {}
with open('monthly_sales.csv', 'r') as file:
    print(file)
    reader = csv.DictReader(file)
    print(reader)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales
    
sales = list(monthly_sales.values())
print(sales)

#Hallar la media de las ventas
mean_sales = statistics.mean(sales)
print('La media es:', mean_sales)

#Hallar la mediana
median_sales = statistics.median(sales)
print('La mediana es:', median_sales)

#Hallar la moda
mode_sales = statistics.mode(sales)
print('La moda es:', mode_sales)

#Hallar la desviacion estandar
stdev_sales = statistics.stdev(sales)
print('La desviación estándar es:', stdev_sales)

#Hallar la varianza
variance_sales = statistics.variance(sales)
print('La varianza es:', variance_sales)

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print('El rango de ventas es:', range_sales)