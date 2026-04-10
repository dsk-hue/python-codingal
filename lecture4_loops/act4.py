num = int(input("What number would you like to test?"))
counter = 0
for i in range(2, num):
    if num % i == 0:
        print("This number is composite.")
        break
else:
    print("This number is prime.")