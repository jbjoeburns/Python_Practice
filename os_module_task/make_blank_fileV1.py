import os

# asks where user wants file created
desired_directory = input("Where would you like the file to be created?: ")

# asks user what they want the filename to be
filename = input("What would you like to name the file?: ")

# changes to the location user wants the file made
os.chdir(desired_directory)

# creates file at this location
# cannot use os to make the file, as os.mknod() does not function on windows, instead using python's inbuilt open command
open(filename, "x")