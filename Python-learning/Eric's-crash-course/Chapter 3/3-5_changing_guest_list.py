# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite

# - Start with your program from Exercise 3-4. Add a print() call 
# at the end of your program stating the name of the guest who 
# can’t make it.

# - Modify your list, replacing the name of the guest who can’t 
# make it with the name of the new person you are inviting.

# - Print a second set of invitation messages, one for each person 
# who is still in your list.

guest_list = ['Aglaea','Tifa', 'Aerith']
invitation = "would you like to have dinner with me?"

print("oh no! Tifa can't attend the dinner :(")

guest_list[1]= "Madam M" 

# here i'm updating the list, from now in index 1 will be Madam M instead of Tifa
print(f"\n{guest_list[0]}, {invitation}")
print(f"{guest_list[1]}, {invitation}")
print(f"{guest_list[2]}, {invitation}")

#3-5 done!
