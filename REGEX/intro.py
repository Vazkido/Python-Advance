import re

# We have re search()



pattern = "cat"
string = "what is a cat in the hat. the cat is fat. A catastrophe"

        # re.search()
re.search(pattern, string, flags=0)
print(re.search(pattern, string))

       # re.match()
re.match(pattern, string, flags=0)
print(re.match(pattern, string))

        # re.fullmatch()
print(re.fullmatch(pattern, string))

        # re.findall()
print(re.findall(pattern, string))

        # re.finditer()
print(re.finditer(pattern, string))


        # re.sub()
replace = "dog"
re.sub(pattern, replace, string, count=0, flags=0)
print(re.sub(pattern, string))

re.compile()