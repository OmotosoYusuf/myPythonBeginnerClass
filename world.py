# this code prints the world hello python
print ('hello python!')

#the below codes are based on operators

x = 10
y = 15
z = 5 

""" 
Assigning variables is quiet easy with python 
"""
a = x + y #arithmetic operation by addition 
print (a)

b = x - y #arithmetic operation by subtraction
print(b)

c = 10 ** 5 #this line of code performs exponentiation (i.e raise to power)
print(c)

x += 2 #this code takes the value of x and adds 2 
print(x)

y += 5 # this code takes the value of y and adds 5 to it
print(y)

z = y % x #this code divides the value of y by x and displays the remainder
print(z)

#below is a function that takes three numbers and adds them together

def area(l,b,h):
	"""
	takes the values of l, b & h and adds them up
	@type l is either int | float
	@type b is either int|float
	@type h is either int|float
	@retype is either int|float

	"""
	return l + b + h

#below is a function that takes two values and checks there divisibility 

def is_divisible (v,w):
	"""
	checks whether v is divisible by w

	@type v is either an integer | float
	@type w is either an integer | float
	@rtype is either an integer | float


	"""
	if v % w == 0:
		return True
	else:
		return False
def hyp_side(a,b):
	cSquared = ((a**2) + (b**2))
	return cSquared**(1/2)

#below codes calls the defined functions to print out values	

print(area(3,4,5))
print(is_divisible(12,5))
print(hyp_side(3,4))


