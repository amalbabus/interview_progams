from datetime import date
def server_cost(start_date,ending_date):

    f_date = date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
    l_date = date(int(ending_date[2]), int(ending_date[1]), int(ending_date[0]))
    delta = l_date - f_date
    totaldays= delta.days
    if(totaldays==0):
        return 20
    elif(totaldays<=30):
        return 30* totaldays
    elif (totaldays>30 and totaldays<=365):
        return totaldays//30 * 1000
    elif(totaldays>365):
        return 20000 

start_date = input().split()
ending_date = input().split()

print(server_cost(start_date,ending_date))