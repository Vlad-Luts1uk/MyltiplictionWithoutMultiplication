num1 = int(input("Enter The First #: "))
num2 = int(input("Enter The Second #: "))

result = 0

if num2 < 0:   
    count = -num2
else:
    count = num2

while count > 0:  
  
    if num1 == 0: 
        count = 0      
    result += num1         
    count -= 1         

print ("Her is the answere", result)