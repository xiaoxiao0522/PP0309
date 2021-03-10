arrayTest = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num1 in arrayTest:

    for num2 in arrayTest:
        if num2 >= num1:
            sum = num1 * num2
            print(num1, "x", num2, "=", sum, "\t", end='')

    print()
