
total = 0

for num in range(1, 101):
    if num % 2 == 0:
        total += num
        
print(total)

# or

total2 = 0

for num in range(2, 101, 2):
    total2 += num   
print(total2)

    