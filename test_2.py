iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("iteration"+str(iteration)+" count: "+str(count))
    iteration +=1

print("Cube root")
cube = 29
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while(abs((guess**3)-cube) >= epsilon):
    guess += increment
    num_guesses += 1

print('num_guesses = '+str(num_guesses))
if(abs((guess**3)-cube) >= epsilon):
    print("Failed on cube root of", cube)
else:
    print(guess, 'is close to the cube root of', cube)
