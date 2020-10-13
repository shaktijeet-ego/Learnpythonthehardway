#--------------------------------------#
#A script to solve different proble,   #
#Created By Shaktijeet Mani Tripathi   #
#Date: 13th October, 2020              #
#--------------------------------------#

#(a+b)^2
def formula1(a,b):
    print("Your formula for (a+b)^2 is a^2+2ab+b^2")
    print(f"Your entered value is {a}{b}")
    return (a**2+2*a*b+b**2)


first_value_a= int(input("Enter the value of a: "))
Second_value_b = int(input("Enter the value of b: "))

query = formula1(first_value_a,Second_value_b)

print (query + 1)
