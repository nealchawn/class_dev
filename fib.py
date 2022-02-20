# base cases: fib(0) = 1 fib(1) = 1
def fib(x):
  if x < 2:
    return x
  else:
    return fib(x-1) + fib(x-2)

# base if in arr return
# else append
arr = [0,1]
def fib_2(x):
  if x < len(arr):
    return arr[x]
  arr.append(fib_2(x-1) + fib_2(x-2))
  return arr[x]

print(fib_2(2));print(fib_2(3));print(fib_2(4));print(fib_2(5));print(fib_2(6));
print(fib(2));print(fib(3));print(fib(4));print(fib(5));print(fib(6));