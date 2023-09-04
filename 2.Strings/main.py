#concepts of the string
first_name = 'soham'
last_name = 'potharkar'
full_name = first_name + ' ' + last_name
print(full_name)

#type conversion
print(type(int((str(100)))))

#escape sequences
print("soham is a \"good\" boy")
#the backslash indicates that the whatever comes after it is the string
#it's helpful when we want to give the double slash.

#formatted strings
age = 23
print('hi'+ first_name + 'what are you ' + str(age) + ' yrats old')
#age is not a string so it is a unformatted str
print(f'hi {first_name} what are you {age} years old') # new method to format the string  




#string indexes

name = 'My name is Soham'
print(name[0])
#[start:stop:stepover]
#if the fields are left empty then in that case we consider that it will start stop or either
print(name[-3:-7:1])
#when we use the incorrect method then in that case it does not print anything
#if you want to print like this we can also use it according to the last 
print(name[-3:])

#if you would like to reverse the string then 
print(name[::-1])

#Strings are immumtable
#name[0] = '2'  this is not correct either we can reassign the value.

print(name.find('Soham')) 
print(name.replace('Soham' , 'Rohan'))


####BOOLEANS

namee = 'Soham'
is_awesome = True
print(bool(is_awesome))
