def quotient_and_remainder(x,y):
  q = x//y
  r = x%y
  return(q,r)

quotient = 0
remainder = 0
(qoutient, remainder) = quotient_and_remainder(6, 4)
#print((qoutient, remainder))
print(qoutient)
print(remainder)
print((qoutient, remainder))

x = (1, 2, (3, 'John', 4), 'Hi')
print(x[-1][-1])