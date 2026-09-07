# 4-10. Slices: Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:

# •	 Print the message The first three items in the list are:. Then 
# use a slice to print the first three items from that program’s list.
# •	 Print the message Three items from the middle of the list are:. 
# Use a slice to print three items from the middle of the list.
# •	 Print the message The last three items in the list are:. Use a 
# slice to print the last three items in the list.

project = ['dark matter', 'stars luminescence', 'n-body problem', 'galaxy rotation', 'galaxy collision', 'stars system', 'cosmic cloud']

print(f"the first three items in the list are {project[0:3]}")
print(f"three items from the middle of the list are: {project[2:6]}")
print(f"the last three items in the list are: {project[-3:]}")

