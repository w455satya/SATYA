name=input("Hello user ! Please Enter Your Name ! :\n ").title()
message=f"Welcome {name} In Personalized Adventure Guide !"
print(message)

'''
take dst input from the user .
*mountains.
*beach
'''
destination=input("Please Enter Your Destinatio ! ").lower().strip()
if destination == "mountains":
    print('you have elected mountains')
elif destination == "beach":
    print()
else:
    print("you have not selecyed any destination")

'''
Take budget input , no of days -input from user .
if budget :
     >=500 -> luxury
     200 <= budget <500 ->good
     0< budget <200 ->budget - friendly
'''
budget=int(input())
if budget>=500:
    print()
elif budget >=200:
    print()
elif budget >0:
    print()
else :
    print("Invalid budget")

def totalCost(budget , days):
    return budget * days
#days

days=int(input())
totalCost=totalCost(budget,days)

print(r'''days -{days} \n.
      budget-{budget}\n
      totalCost-{totalCost}\n''')



def getValidNum(prompt):
    while True :
        try :
            value=int(input(prompt))
            return value
        except ValueError :
            print('Invalid inpur ! enter again')
            
print(getValidNum('test'))