#previously handled script
def print_two(*args):
    arg1,arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

#takes two arguments
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#akes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#takes no arguments
def print_none():
    print("I got nothing")


print_two("Zed","Shaw")
print_two_again("Zed","Sjhaw")
print_one("First")
print_none()