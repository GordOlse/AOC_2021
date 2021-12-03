from collections import Counter

with open('Day3\\sample-data.txt', 'r') as file:
    data = file.read().splitlines()

# print(data)

first_digits = [str(x)[0] for x in data]
second_digits = [str(x)[1] for x in data]
third_digits = [str(x)[2] for x in data]
fourth_digits = [str(x)[3] for x in data]
fifth_digits = [str(x)[4] for x in data]

first_count = Counter(first_digits)
second_count = Counter(second_digits)
third_count = Counter(third_digits)
fourth_count = Counter(fourth_digits)
fifth_count = Counter(fifth_digits)

gamma_rate = ""
epsilon = ""


if first_count['1'] > first_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if second_count['1'] > second_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if third_count['1'] > third_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if fourth_count['1'] > fourth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if fifth_count['1'] > fifth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'


p_consumption = int(gamma_rate, 2)*int(epsilon, 2)

print(first_count)
print(second_count)

print(f"Power Consumption: {p_consumption}")
