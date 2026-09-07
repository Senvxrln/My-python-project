# You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("Update everyone! I just found a bigger dinner table, now we can invite more people!")

guest_list = ['Aglaea','Tifa', 'Aerith']
invitation = "would you like to have dinner with me?"

print("\noh no! Tifa can't attend the dinner :(")

guest_list[1]= "Madam M"

# recall, to use insert you do this: list.insert(index, value)

guest_list.insert(0, "Dan Heng")
guest_list.insert(2, "Sunday")
guest_list.append("Madam Jade")

print(guest_list)

print(f"\n{guest_list[0]}, {invitation}")
print(f"{guest_list[1]}, {invitation}")
print(f"{guest_list[2]}, {invitation}")
print(f"{guest_list[3]}, {invitation}")
print(f"{guest_list[4]}, {invitation}")
print(f"{guest_list[5]}, {invitation}")


print("\nbad news: the dinner table will arrive late! I can only provide for two guests!")

print(guest_list)

# guest_list.pop(0)
# guest_list.pop(1)
# guest_list.pop(2)
# guest_list.pop(2) # because there's only 3 value left in the list, i'm not repeating this because of error, it is correct

# the pop method is kinda weird,  when i popped a value, then the whole
# index and arrangement got changed. Danheng is 0 and Sunday is 2, but
# after i popped danheng, sunday got different index (it should be though)
# but it makes me need to put more work into counting them
# or maybe i just referred to the initial index - 1? of course it applies
# only if i popped a value before, if not, then it wouldn't affect the index

# update: still not working, i look at the book, they assigned the value
# to a variable, i think i should try it

first = guest_list.pop(0)
second = guest_list.pop(1)
third = guest_list.pop(1) # i want to remove madam M, which has the index 3 in original list, but because i already removed two value before, then the index become 3-2 = 1
fourth = guest_list.pop(2)

print(f"i'm so sorry, {first}")
print(f"i'm so sorry, {second}")
print(f"i'm so sorry, {third}")
print(f"i'm so sorry, {fourth}")

print(f"\nremaining guest: {guest_list}")

# alright, this one work! because the repeition (bcs the index change after i popped values)
# but by assigning them to variable, i can use them without confusion! (maybe there is, just a little).

# now the invitation for the final guests

print(f"\nHey, {guest_list[0]}, don't forget for our dinner tonight!")
print(f"Hey, {guest_list[1]}, don't forget for our dinner tonight!")

del guest_list[0]
del guest_list[0] # for the same reason i delete Madam M

print("\nNow i have no guests left to give updates to.")
print(f"\n{guest_list}")

# 3-7 done! 