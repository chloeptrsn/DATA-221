from random import random

values = [random() for x in range(20)]
x = random()

counter_for_each_value = 0
sorted_list = []
match = []

while counter_for_each_value <= 20:
    for i in values:
        if i >= x:
            sorted_list.append(i)
            sorted_list.append(values)
            counter_for_each_value += 1

    else:
        continue

for value in sorted_list:
    if value == x:
        match.append(value)
        break

print(sorted_list)
if match:
    print(f"The matching value for x is in the index: {sorted_list.index()}")
else:
    print("There are no matching values for x.")
