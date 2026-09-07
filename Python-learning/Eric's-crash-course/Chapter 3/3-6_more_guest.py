# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# •	 Start with your program from Exercise 3-4 or Exercise 3-5. 
# Add a print() call to the end of your program informing people 
# that you found a bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in 
# your list.

print("Update everyone! I just found a bigger dinner table, now we can invite more people!")

guest_list = ['Aglaea','Tifa', 'Aerith']
invitation = "would you like to have dinner with me?"

print("oh no! Tifa can't attend the dinner :(")

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

#3-6 done!