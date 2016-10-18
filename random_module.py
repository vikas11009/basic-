elist=[]
olist=[]
i=0
import random
while (i<=10):
	a=random.randint(1,6) #for random integer. in brackets range is given.
	c=a%2
	if c==0:
		elist.append(a)
	else:
		olist.append(a)
	i+=1
print elist
print olist