

# sequences
test = 'a string'
print(len(test))
print(test[5])
print(test[-1])
print(test[2:5])

#from end
print(test[:-2])
print(test[:])

#concat
print(test + "abc")

#convert to list
print(list(test))


#find/replace
print(test.find('str'))
print(test.replace('str', 'f'))

#split
print(test.split(' '))

#all fincts
print(dir(test))

#help
#print(help(test.split))


#multiline
test = """
multi
line t
est
"""
print(test)


#patterns
import re
match = re.match('\n(.*)ul', test)
match.groups()
print(match.group(1))
