#Write a program that asks user for their favorite color. Look for this color in
#the given list. If the color is found, print out the index of this color in the
#list. If not, print out “Sorry, I could not find your color”.
color = ["black", "red", "blue", "green", "pink", "gray", "yellow"]
fav_color = input("What is your favorite color? ")
if fav_color in color:
    print(f"Your color is at index {color.index(fav_color)} in my list")
else:
    print("Sorry, I could not find your color")          