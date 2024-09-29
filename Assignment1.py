
# Adventure Guide Project .
# Taking Name From User And Print With Welcome Message !.


def getName():
        name=input("Please Enter Your Name !\n")
        return name.title()
       
name= getName()       
message=f"Welcome {name} In Personalized Adventure Guide !"
print(message)

# '''
# take dst input from the user .
# *mountains.
# *beach
# '''

def getDestination():
    while True:
        
        destination=(input("Please Enter Your Destination  By Entering Number Or Writing Name !\n Destination ->1.Mountains 2.Beach \n")).lower().strip()   
        if destination == '1' or destination =='mountains' :
            return "Mountains"
        elif destination == '2' or destination == 'beach':
            return "Beach"
        else:
            print("You Have Entered  Wrong  Destination ! Please Enter Again !\n")
            
destination=getDestination()     
print(f'You Have Elected {destination} !!')

# Total Cost Calculation ->

def totalCost(days,budget):
    totalcost=days*budget
    return totalcost

    

# '''
# Take budget input , no of days -input from user .
# if budget :
#      >=500 -> luxury
#      200 <= budget <500 ->good
#      0< budget <200 ->budget - friendly
# '''

def getValidNum(prompt):
    while True :
        try :
            value=int(input(prompt))
            return value
        except ValueError :
            print('Invalid inpur ! enter again')
          
budget=getValidNum("Please Enter Your Daily  Budget -> Rs")
if budget>=500:
    print('Luxury Budget !')
elif budget >=200:
    print('Good Budget ! ')
elif budget >0:
    print('Friendly Budget !')
else :
    print("Invalid budget")
    
# Days Input Taken ->

days=(getValidNum('Please Enter No of Days You Want To Stay! -> '))

print(f'Total Cost For Living {days} days With {budget} is ->Rs {totalCost(budget,days)}')
  









