#To change this template use Tools | Templates.


age = 16
print('age')  # prints the word
print(age)    # prints the value of variable
name='Simone'

print('I am %d years old' % age)
print('%s is my name' % name)

message ='You are %d years old'   # %d does a number substitution
print (message % age)

# you can do a substitution in print statement as well as a math operator
print ('On your next birthday you will be %d' % (age+1))

# you can also use a , to print a variable value next to a line
print ('Your age is', age)
print ('On your next birthday you will be', (age+1))

# you can also do mulitple subsitutions
print ('%s your age is %d' % (name,age))
