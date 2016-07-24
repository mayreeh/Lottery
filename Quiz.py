def getLotteryPrizings():
    numbers = input("Enter Values separated by commas ");
    people = input("Enter participants names ");
#convert to list
    numbersList = list(numbers)
    peopleList = list(people)

    peopleNumber = len(peopleList)
    numberListTotal = 0
    for i in numbersList:
        numberListTotal = numberListTotal + i

#highest person shuld get , first identify if the total is even
    if   numberListTotal % peopleNumber == 0:
        averageNumber = numberListTotal / peopleNumber


        people_assigned = []
        numbers_assigned = []
        dic = {}
#check in the list if the averagenumber is in the list, if so assign to one person
        if averageNumber in numbersList:
                numbers_assigned.append(averageNumber)
                l = len(numbers_assigned)
                for p in peopleList[0:l]:
                    people_assigned.append(p)
                    #create a dictionary that stores persons and average prize number
                    dic[p] = averageNumber
                    numbersList.remove(averageNumber)
                    peopleList.remove(p)
                    #distribute the rest
                    for pple in peopleList:
                        dic[pple] = ""
                return dic




print getLotteryPrizings()
