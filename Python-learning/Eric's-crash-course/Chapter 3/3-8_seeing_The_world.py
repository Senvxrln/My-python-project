# Seeing the World: Think of at least five places in the world you’d like to
# visit.
# •    Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.


places = ["switzerland", "germany", "italia", "iceland", "japan"]

print("Here's the original list:")
print(places)

print("\nHere the sorted list:")
print(sorted(places))

print("\nHere's the original list(again):")
print(places)

print("\nHere the list in reverse alphabetical order:")
r_list = sorted(places)
r_list.reverse()
print(r_list)

# another way is to add another value inside the sorted() built-in 
# function! like this:
# r_list = sorted(places, reverse=True)
# print(r_list) 
# it work the same! so information to remember: you can assign an argument to a function and method!

print("\nHere's the original list(again):")
print(places)

print("\nHere's a permanently reversed list:")
places.reverse()
print(places)

print("\nI reversed it again:")
places.reverse()
print(places)

print("\nHere's a permanently sorted list:")
places.sort()
print(places)

print("\nHere's a permanently sorted in reverse alphabetical order:")
places.reverse()
print(places)

# 3-8 done!







