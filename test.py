import math

print(math.cos(3.14))
print(3**2)


print("For loop below")
num=10
for num in range(5):
    print(num)
print(num)

print("Snowy things below")
count = 0
for letter in 'Snow!':
    print("Letter # " + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

print("divisor")

divisor = 2
for num in range(0,5,2):
    print(num/divisor)

print("mod 4 or mod 16")
for var in range(20):
    if var % 4 == 0:
        print(var)
    if var % 16 == 0:
        print("Foo!")

print("MIT incoming")

school = "Massachusetts Institute of Technology"
num_vow = 0
num_con = 0

for letter in school:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter ==  'o' or letter == 'u':
        num_vow += 1
    else:
        num_con -= 1

print("Vowels: "+ str(num_vow))
print("Consinents: "+ str(num_con))
