#### Modulous ####
# x = 15
# if x % 5 == 0:
#     print(x)

#### Dictionary ####
# person_two = {
#     "name" : "Maciek",
#     "age" : 32,
#     "fav_color" : "Green",
#     "food truck" : True,
#     "items" : ["pierogi", "kielbasa", "potatoes", ["pickles", "sour cream", "dill"]], #List
#     "address" : {"Boston", "Mass"} #Dictionary
# }

# print(person_two['items'][1])
# print(person_two['items'][3][0])

# person_two['fav_color'] = "Blue"
# print(person_two)

# person_three = {}
# person_three['name'] = "Ramsey"
# print(person_three)

# val_removed = person_two.pop("age")
# print(val_removed)

# del person_two["fav_color"]
# print(person_two)

# # To get the Keys of Keys
# print(person_two.keys())

# # To just get values
# print(person_two.values())

# # To get Keys and Values
# print(person_two.items())

#### CONDITIONALS ####

# x = 33
# if x > 50:
#     print("Bigger than 50")
#     print("Bigger than 50")
# elif x > 30:
#     print("Larger than 30")
# elif x > 20:
#     print("Larger than 20")
# else:
#     print("Is less than 10")

#### PASS ####
# x = 42
# if x > 32:
#     pass


# for i in range(0,51,2):
#     print(i)

# for i in range(0,50):
#     print(i)

# for i in range(51):
#     print(i)

# for i in range(51,0,-1):
#     print(i)


#### LISTS ####

## Prints the Values of the List
# person_one = ["Maciek", 32, "Green", True, 3, 5]
# for i in range(len(person_one)):
#     print(person_one[i])

## Prints the Index
# person_one = ["Maciek", 32, "Green", True, 3, 5]
# for i in range(len(person_one)):
#     print(i)

#### FUNCTIONS ####

# def sum(num):
#     print(num)
# sum(6)

def birthday(age):
    age += 1
    return age
    print(age)

print(birthday(28))