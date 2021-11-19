## MODULES

# import the library example
# import urllib.request
# response = urllib.request.urlopen("http://www.codingdojo.com")
# html = response.read()
# print(html)

# Module to import arithmetic.py
import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))

## PACKAGES

# A module is a single file (or files) that is imported under one import. A package is a collection of modules in directories that give a package hierarchy.

from my_package.subdirectory import my_functions

## Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.
## In the above diagram below, the package name is my_modules.

sample_project
     |_____ python_file.py
     |_____ my_modules
               |_____ __init__.py
               |_____ test_module.py
               |_____ another_module.py
               |_____ third_module.py


