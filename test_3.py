a_f = 10
def f_1(x):
    return (x+a_f)
a_f = 3
print(f_1(1))

print("global")

def f(x,y):
    return x+y-2

print(f)

x =23
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
    else:
        break

if abs(guess**2 -x) >= epsilon:
    print("failed")
else:
    print("Succeeded: " +str(guess))
