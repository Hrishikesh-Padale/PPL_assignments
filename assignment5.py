
file = open('123.txt','w')
file.write('\nWrites this line into the file')

file = open('123.txt','a')
file.write('\nAppends this line to the current contents')

file = open('123.txt','r')
print(file.read())


