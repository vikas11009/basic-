class cal:
	counter=0
	def __init__(x,num1,num2):
		x.num1=num1
		x.num2=num2
		cal.counter+=1

	def display_count(x):
		print"no of calculation: ",cal.counter 

	def sum(x):
		ans=x.num1+x.num2
		print "sum of the numbers is: ", ans

	def sub(x):
		ans=x.num1-x.num2
		print "differance in number is: ", ans

	def multi(x):
		ans=x.num1*x.num2
		print "multiplication of numbers is: ", ans

	def divide(x):
		ans=x.num1/x.num2
		print 'division of the number is: ',ans
r=1
while (r==1):
	a=cal(input("emter 1st number: "),input("2nd number: "))
	print"enter 1 for addition, 2 for subtractio, 3 for multiplication, 4 for division and 0 to exit"
	mode=input("enter the operation")
	a.display_count()
	if mode==1:
		a.sum()
	elif mode==2:
		a.sub()
	elif mode==3:
		a.multi()
	elif mode==4:
		a.divide
	r=input("enter you choice: ")
	print"press 1 to use it again and press 0 to exist.",r
	


