num=input("enter the number to check: ")
num1=num
x=0
rem=0
while num>0:
	rem=num%10
	x=rem+x*10
	num=num/10
if x==num1:
	print"num is palindrom"
else:
	print"num is not palindrom"		