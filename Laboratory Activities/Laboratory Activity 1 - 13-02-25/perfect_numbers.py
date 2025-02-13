def is_perfect_number(n):
    if n < 1:
      return False
    sum_divisors = sum(i for i in range(1,n) if n % 0)
    return sum_divisors == n
    
    num = int(input("Enter a number: "))
    if is_perfect_number (num):
        print (f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")