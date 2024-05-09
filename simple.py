print("Enter the Principle Amount: ")
p = float(input())
print("Enter Rate of Interest (%): ")
r = float(input())
print("Enter Time Period: ")
t = float(input())
si = (p*r*t)/100

print("\nSimple Interest Amount: ")
print(si)

print("\nSimple Interest Amount in months: ")
print(si/(t*12))
