speedingTicket =[]
totalTicket = 2
name = ""


def printSummary ():

    print("""---------------------------------
    Printing summary of speedingTickt for the day
    ------------------------------------------""")

for i in range (totalTicket):

    name = input("Enter name : ")
    speedinglimit = int(input("Enter speedlint : "))
    speed = int(input("Enter speed: "))
    fine = speed - speedinglimit
    speedingTicket.append([name,fine])

print ("""
------------------------------------------------
Displaying indexed data stored (appended to) list
------------------------------------------------
""")
print(speedingTicket)
printSummary()