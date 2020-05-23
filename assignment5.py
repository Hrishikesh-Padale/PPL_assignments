fh = open("testfile.txt","w+")
try:
   fh = open("testfile.txt", "r")
   fh.write("This is my test file for exception handling!!")
   fh.close()
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")

try:
   fh = open("testfile.txt", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()

def temp_convert(var):
   try:
      return int(var)
   except (ValueError, Argument):
      print("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")
