from collections import Counter

with open('Day3\\solution-data.txt', 'r') as file:
    data = file.read().splitlines()

# print(data)

# Splitting out each column into their own string
first_digits = [str(x)[0] for x in data]
second_digits = [str(x)[1] for x in data]
third_digits = [str(x)[2] for x in data]
fourth_digits = [str(x)[3] for x in data]
fifth_digits = [str(x)[4] for x in data]
sixth_digits = [str(x)[5] for x in data]
seventh_digits = [str(x)[6] for x in data]
eighth_digits = [str(x)[7] for x in data]
nineth_digits = [str(x)[8] for x in data]
tenth_digits = [str(x)[9] for x in data]
eleventh_digits = [str(x)[10] for x in data]
twelveth_digits = [str(x)[11] for x in data]


# Counter dictionary
first_count = Counter(first_digits)
second_count = Counter(second_digits)
third_count = Counter(third_digits)
fourth_count = Counter(fourth_digits)
fifth_count = Counter(fifth_digits)
sixth_count = Counter(sixth_digits)
seventh_count = Counter(seventh_digits)
eighth_count = Counter(eighth_digits)
nineth_count = Counter(nineth_digits)
tenth_count = Counter(tenth_digits)
eleventh_count = Counter(eleventh_digits)
twelveth_count = Counter(twelveth_digits)


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

if sixth_count['1'] > sixth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if seventh_count['1'] > seventh_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if eighth_count['1'] > eighth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if nineth_count['1'] > nineth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if tenth_count['1'] > tenth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if eleventh_count['1'] > eleventh_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'

if twelveth_count['1'] > twelveth_count['0']:
    gamma_rate += '1'
    epsilon += '0'
else:
    gamma_rate += '0'
    epsilon += '1'


p_consumption = int(gamma_rate, 2)*int(epsilon, 2)


print(f"Power Consumption: {p_consumption}")


###Part 2###
