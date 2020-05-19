num1 = 1
count = 0
sum1 = 0
sum2 = 0
x = 220
while count < 10:
  for i in range (1,x) :
      if x % i == 0:
          sum1  += i
  for j in range (1,sum1) :
      if sum1 % j == 0:
          sum2 += j            
  if x == sum2 :
      print(x,sum1)
      count += 1
  sum1 = 0
  sum2 = 0
  x += 1
    
