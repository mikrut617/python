import parent


## Namespace:
# Namespace refers to which variables, functions, and classes are accessible to us at any given time during a program’s execution. Namespace is important because we have to know what variables we have access to. To see what variables are available in any given place, add the line print(locals()) and see what variables are in your current namespace. The object that prints will be a dictionary where the variable names are keys and the objects they reference are the values.

print(locals())