print"claculater"
num1=input("enter 1st number for operation: ")
num2=input("enter 2nd number for operation:")
print"press a for addition, b for subtraction, c for multiplication, d for division"
x=raw_input("type of operation: ")
if x=="a":
	c=num1+num2
elif x=="b":
	c=num1-num2
elif x=="c":
	c=num1*num2
elif x=="d":
	c=num1/num2
print c