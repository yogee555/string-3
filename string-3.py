# String functions
ch = "my_string"
print(len(ch))                                       # check length

g = "my_name"
print(g.upper())                                     # convert upper case

k = "MY_CHARACTER"
print(k.lower())                                    # convert lower case

# Replacing a substring
l = "my_name"
print(l.replace("n","k"))              # replace another value

new_string = "hello, hello, hello, world"
print(new_string.count("hello"))                   # count value

s1 = "This is yogeesh"
print(s1.find("yogeesh"))                          # find string

t1 = "I like mqango, apple, orange"                # split separate value
print(t1.split(","))