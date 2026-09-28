#Write a function that removes the dollar sign (“$”) in a string, named
#remove_dollar_sign, takes 1 parameter: s, where s is the input string,
#returns the new string with no dollar sign in it.
def remove_dollar_sign(s):
    result = ""
    for char in s:
        if char != "$":
            result += char
    return result

text = input("Enter a string: ")
print(remove_dollar_sign(text))