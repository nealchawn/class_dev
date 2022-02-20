def apply_to_each(list, func):
  for i in range(len(list)):
    list[i] = func(list[i])
  print(list)

some_list = [-2,5.63, 8]
print(some_list)
apply_to_each(some_list,int)
apply_to_each(some_list,abs)

# map must be converted to a list
# lambda needs prefix
print(list(map(abs, [-1,-2,-3,4])))
print("Map with lambda")
print(list(map(lambda a : a + 5, [-1,-2,-3,4])))

t1 = (1,2,3,4)
t2 = (5,6,7,8)
# 6, 8, 10, 12

print(list(map(lambda x, y : x+ y, t1, t2)))


