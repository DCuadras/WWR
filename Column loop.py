columns_rows = int(input("How many columns and rows do you want in your multiplication table? "))

i = 0
j = 1

for i in range(1, columns_rows + 1):
    for column in range(1,columns_rows + 1):
        print(f"{column * j:3}",end = " ")

    j+= 1

    print()