# Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
# person’s name.

names = ['bila', 'irda', 'indah', 'lia', 'dila']

# greetings = f"Hello, {names[i].title()}" # #idk if this will work, but let's just try
# print(greetings)

# update: well, it didn't work, let's try to do it manually

greetings = "Hello," # i add a whitesapce after the come so it'll be neat
print(f"{greetings} {names[0].title()}")
#update, the whitespace after the coma added unnecessary whitespace
# so i deleted it.

print(f"{greetings} {names[1].title()}")
print(f"{greetings} {names[2].title()}")
print(f"{greetings} {names[3].title()}")
print(f"{greetings} {names[4].title()}")
# update: the reason why the previous line (names[0]) got
# extra white space is because i add a space between the greetings
# and names variable! so on the four line of code above when i didn't
# add a space, the result actually showed Hello,names (no space between them)
# so, i added some space

# 3-2 done!