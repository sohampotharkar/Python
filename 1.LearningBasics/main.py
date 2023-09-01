#Datatypes
int 
float 
complex


print(type(2/3))
print(2-3)

print(2**3) #also known as 2 to the power of 3.
print(2//3) #returns int

#maths library
print(round(2.9))
print(abs(-3-4+6))

#operatoer precedence i.e the preference given to the operator
#  while performing the maths function
#()
#**
# * /
#+ -

#There is also a datatype known as the bin() which return the binary 
# representation of the number
print(bin(5))

#If you want to return the number to integer from the binary then 
print(int('0b101',2)) #it represents that the given number entered has the base 2

#python Variables
#they can be anything starting with lowercases and the underscores.

#round off operation is performed on the data only at the time of the 
# printing and it doesnot get changed in the variale
soham = 123
roham = 124
roham = soham/roham
print(roham)
print(round(roham))
print(soham)

#normally one underscore before the variable name is declared as the private variable
_soham=1

a,b,c = 1,2,3

#constants:- Generally named using the capital letter
PI = 3.14 # but this does not mean that we can't change the value of the PI.
           #it's just that the code is more readable to the programmer

#The action we are performing is known as the expression and the line of code is the statement
user_age =100
soham_age = user_age/4
