k = int(input("Сколько вам шариков): "))

if k % 3 == 0 and (k % 5 == 3 or k % 5 == 0):
    print("yes")
else:
    print("No")
