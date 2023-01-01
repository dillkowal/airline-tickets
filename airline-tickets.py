name=input()
member=input()
miles=int(input())
print("What is the customer's first and last name?")
print('Is the customer a member (y/n)?')
print('How many miles does the customer have?')
print("What was the cost of their ticket?")
ticket_cost=float(input())
ticket_cost1=int(ticket_cost)
if (miles<0) or (ticket_cost1<0):
    print('ERROR: Number of miles or ticket cost is less than zero.')

else:
    print(f"Dear {name},")
    print()
    if member=='y':
       if 0<=miles<25000:
           print('You are a member of SpartanAir loyalty rewards and are currently at Base tier.')
           print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {ticket_cost1*5} miles.')
           print(f'Your total number of miles has increased from {miles} miles to {miles+(ticket_cost1*5)} miles.')
           miles = miles+(ticket_cost1*5)
           if 25000<=miles<50000:
               print('You are eligible for a status upgrade from Base to Silver.')
           elif 50000<=miles<75000:
               print('You are eligible for a status upgrade from Base to Gold.')
           elif 75000<=miles<125000:
               print('You are eligible for a status upgrade from Base to Platinum.')
           elif miles>=125000:
               print('You are eligible for a status upgrade from Base to Diamond.')
       elif 25000<=miles<50000:
           print('You are a member of SpartanAir loyalty rewards and are currently at Silver tier.')
           print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {ticket_cost1*7} miles.')
           print(f'Your total number of miles has increased from {miles} miles to {miles+(ticket_cost1*7)} miles.')
           miles = miles+(ticket_cost1*7)
           if 50000<=miles<75000:
               print('You are eligible for a status upgrade from Silver to Gold.')
           elif 75000<=miles<125000:
               print('You are eligible for a status upgrade from Silver to Platinum.')
           elif miles>=125000:
               print('You are eligible for a status upgrade from Silver to Diamond.')
       elif 50000<=miles<75000:
           print('You are a member of SpartanAir loyalty rewards and are currently at Gold tier.')
           print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {ticket_cost1*8} miles.')
           print(f'Your total number of miles has increased from {miles} miles to {miles+(ticket_cost1*8)} miles.')
           miles = miles+(ticket_cost1*8)
           if 75000<=miles<125000:
               print('You are eligible for a status upgrade from Gold to Platinum.')
           elif miles>=125000:
               print('You are eligible for a status upgrade from Silver to Diamond.')
       elif 75000<=miles<125000:
           print('You are a member of SpartanAir loyalty rewards and are currently at Platinum tier.')
           print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {ticket_cost1*9} miles.')
           print(f'Your total number of miles has increased from {miles} miles to {miles+(ticket_cost1*9)} miles.')
           miles = miles+(ticket_cost1*9)
           if miles>=125000:
               print('You are eligible for a status upgrade from Platinum to Diamond.')
        
       elif miles>=125000:
           print('You are a member of SpartanAir loyalty rewards and are currently at Diamond tier.')
           print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {ticket_cost1*11} miles.')
           print(f'Your total number of miles has increased from {miles} miles to {miles+(ticket_cost1*11)} miles.')
    elif member=='n':
       print('SpartanAir would like to invite you to become a loyalty rewards member.')
       if ticket_cost<=0:
          print(f'As a Base tier member, your recent ticket purchase of ${ticket_cost:.2f} would earn you 0 miles.')
       elif ticket_cost>0:
          print(f'As a Base tier member, your recent ticket purchase of ${ticket_cost:.2f} would earn you {ticket_cost1*5} miles.')
