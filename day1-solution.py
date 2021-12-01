my_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

increased_count = 0
decreased_count = 0

# for i in range(len(my_list)):
#     if i+1 > len(my_list):
#         break
#     elif my_list[i] < my_list[i+1]:
#         increased_count += 1
#     else:
#         decreased_count += 1


for i, j in enumerate(my_list[:-1]):
    if j < my_list[i+1]:
        increased_count += 1
    else:
        decreased_count += 1

print(f"Increased measurements: {increased_count}")
print(f"Decreased measurements: {decreased_count}")
