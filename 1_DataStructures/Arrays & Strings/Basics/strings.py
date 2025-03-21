# NOTE: Strings are immutable in python that's why the original string can't be modified

string = 'Pakistan'

# append to end - O(n)
newString = string + 'i'
print(newString)

# searching something in string - O(n)
if 'i' in string:
    print(True)

# accessing at particular position - O(1)
print(string[0])

# length - O(1)
print(len(string))
