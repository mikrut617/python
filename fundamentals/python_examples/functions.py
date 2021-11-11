def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

### INVOKING A FUNCTION ###

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum3)

