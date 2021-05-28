import ast

...

with open("/path/to/file", "r") as data:
    dictionary = ast.literal_eval(data.read())