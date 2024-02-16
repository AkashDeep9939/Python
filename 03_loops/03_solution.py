print("Enter the table you want to print")

number = int(input())

for it in range(1, 11):
    if it == 5:
        continue
    print(number, "X", it, "=", number * it)

