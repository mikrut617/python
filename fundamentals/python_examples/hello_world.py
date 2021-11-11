# # 1. TASK: print "Hello World"
# print('Hello World')
# # 2. print "Hello Noelle!" with the name in a variable
# name = "Maciek"
# print("Hello ",  name)	# with a comma
# print("Hello " + name  )	# with a +
# # 3. print "Hello 24!" with the number in a variable
# name = 24
# print("Hello ",name,"!" )	# with a comma
# print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error!
# # # 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print("I love {fave_food1} and {fave_food2}.".format(fave_food1 = "sushi", fave_food2 = "pizza")) # with .format()
# print(f"I love {fave_food1} and {fave_food2}!") # with an f string

def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)


def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# # output:
# >>>[2,4,10,16] 5
# >>>[2,4,10,16]





