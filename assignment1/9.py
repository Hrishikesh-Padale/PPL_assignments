N = 2
z = type(N)
sum1 = 0
count = 0
n = 0
while n < 10:
 for x in range(1,N+1):
    if(N%x==0):
      sum1 += 1/x
      count += 1
 mean = count/sum1
 l = int(mean)
 mean = mean * 10
 l = l*10
 if l == mean :
     print(x)
     n += 1
 N += 1
 sum1 = 0
 count = 0
 
    



