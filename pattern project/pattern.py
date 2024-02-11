
def design(rows,columns):
  for k in range(1,rows+2):
    if k==1:
      for j in range(1,columns-1):
        if j<=rows:
         print(" ___  ",end="  ")
      print()
    else:  
      for j in range(1,columns-1):
        if j<=rows: 
          print("/   ",end="")
          print('\\',end="")
          if j!=rows:
           print("___",end="")
      print()
      for j in range(1,columns-1):
        if j<=rows:  
          print("\___/  ", end=" ")
      print()
design(int(input("number of rows")),
        int(input("number of columns")))  