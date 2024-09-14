
limit = input("limit: ")
for i in range(int(limit) + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz: " + str(i))
        continue
    if i % 3 == 0 and i % 5 != 0:
        print("fizz: " + str(i))
        continue
    if i % 3 != 0 and i % 5 == 0:
        print("buzz: " + str(i))
        continue
    print(i)