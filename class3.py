from random import randint

##List of lists
class_records = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

names =[]
records_agg = []

for i in class_records:
    if type(i) is str:
        names.append(i)
    else:
        records_agg.append(i)

records = []

for i in range(0,len(records_agg),3):
    records.append([records_agg[i],records_agg[i+1],records_agg[i+2]])

##List of Tuples
def generate_code():
    return str(randint(0,999))

code_students = []

for i in range(len(names)):
    code_students.append((names[i],names[i][0] + generate_code()))

print(code_students)

##List comprehension 
def mean(lista: list=[0]) -> float:
  calculo = sum(lista) / len(lista)

  return calculo

means = [round(mean(record), 1) for record in records]
print(means)

##List comprehension with IF and ELSE
situation = ["Approved" if mean >= 6 else "Declined" for mean in means]
print(situation)

register = [x for x in [names, records, means]]
print(register)

complete_list = [code_students, records, means,situation]
print(complete_list)

##Dict comprehension
coluns = ['Records','Final Mean','Situation']

register = {coluns[i]: complete_list[i+1] for i in range(len(coluns))}
register['Student'] = [complete_list[0][i][0] for i in range(len(complete_list[0]))]
print(register)