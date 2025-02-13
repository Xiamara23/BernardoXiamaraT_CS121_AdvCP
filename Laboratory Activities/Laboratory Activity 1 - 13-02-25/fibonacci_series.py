n = int(input("Enter the number of terms: "))

first, second = 0,1
for _ in range (n):
    print(first, end=" ")
    first, second = second, first + second