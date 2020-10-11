from sys import argv

script, from_file, to_file = argv

print("This is a program to copy file contents to a new file")
print(f"You have entered {from_file} and want to copy to {to_file}")


open_file = open(from_file,'r')
file_data = open_file.read()

print(f"Your content: {file_data} is \n {len(file_data)} bytes long")

open_next_file = open(to_file,'w')
open_next_file.write(file_data)

print("your file contents have been written")
open_next_file.close()
open_file.close()