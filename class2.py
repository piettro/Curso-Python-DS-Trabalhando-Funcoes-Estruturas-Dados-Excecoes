records = {'1° Trimestre': 8.5, '2° Trimestre': 9.5, '3º trimestre': 7}
print(records)

sum_records = 0

for record in records.values():
    sum_records += record

print(sum_records)

sum_records = sum(records.values())
print(sum_records)

len_records = len(records)
print(len_records)

mean_records = sum_records / len_records
print(mean_records)
print(round(mean_records,1))

def mean(records:list):
    mean_records = sum(records) / len(records)

    return mean_records

list_records = [10,9,8,7.5,8]
list_records_mean = mean(list_records)
print(list_records_mean)

def check_record(records:list):
    mean_records = mean(records)

    if mean_records >= 6:
        result = 'Approved'
    else:
        result = 'Declined'

    return result

check_list_records = check_record(list_records)
print(check_list_records)

record_1 = float(input('Write record 1: '))
record_2 = float(input('Write record 2: '))
record_3 = float(input('Write record 3: '))

mean_input_record = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10
mean_student = mean_input_record(record_1, record_2, record_3)
print(mean_student)