#Write a function that extracts the even items in a given integer list, named
#extract_even, takes 1 parameter: l, where l is the given integer list ([1, 4, 5,
#-1, 10] for example), returns a new list contains only even numbers ([4, 10]
#if the given list is [1,4,5,-1,10]).
def extract_even(l):
    result = []

    for number in l:
        if number % 2 == 0:
            result.append(number)
    return result

print(extract_even([1, 4, 5, -1, 10])) #4 10
