from sys import argv


script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("??")


#opening the file
print("opening the file")
target = open(filename,'w')

#truncating the file contents
print("Truncating the file. Goodbye!!")
target.truncate()

print("Now, please add three lines")

#adding three lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#writing three lines to the file
target.write(line1)
target.write(line2)
target.write(line3)


# closing the file
print("closing the file")
target.close()