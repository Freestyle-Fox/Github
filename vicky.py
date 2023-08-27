# ask name of the user
name = input("whats your name : ").title().strip()

# Remove whitespace of user name  And also remove whitespace
# name = name.strip().title()

# capitalize the first letter of the word
# name = name.capitalize()

# capitalize the first letter of the every word
# name = name.title()

# Split the user name 
first,last = name.split(" ")

# say hello to the user
print(f"hello , {first}")
