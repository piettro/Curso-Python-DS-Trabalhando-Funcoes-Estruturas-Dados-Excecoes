#Exceptions
records = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    name = input('Write the student name: ')
    result = records[name]
except KeyError:
    print('Student dont have register in class')
else:
    print(result)

#Finally
try:
    name = input('Write the student name: ')
    result = records[name]
except KeyError:
    print('Student dont have register in class')
else:
    print(result)
finally:
    print('The request has closed')

#Raise
def calculate_mean(lista: list=[0]) -> float:
    mean = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("The list cannot have more than 4 records.")
        
    return mean

try:
    records = [6, 7, 8, "9"]
    result = calculate_mean(records)
except TypeError:
    print("It was not possible to calculate the student's average. Only numerical values ​​are accepted!!")
except ValueError as e:
    print(e)
else:
    print(result)
finally:
    print("The request has closed!")