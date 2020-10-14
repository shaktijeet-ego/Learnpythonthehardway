people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.") #This will be printed

elif cars < people:
    print("We should not take the cars ") #skipped

else:
    print("We can't decide") #skipped


if trucks > cars : 
    print("that's too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks") #This will be printed
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks") #This will be printed
else:
    print("fine let's just stay home then")


    #Note if the first block is TRUE it will only run the first block
    