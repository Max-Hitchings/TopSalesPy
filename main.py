def countCommars(string: str):
    count = 0
    for x in string:
        if x == ",":
            count += 1
    if count == 2:
        return True
    else:
        return False


def checkForNumbers(inp):
    ### TODO ###
    return True


def testInput(inp: str):
    try:
        if countCommars(inp):
            if checkForNumbers(inp):
                return True
            else:
                return False
        else:
            return False
    except:
        return False





def takeInput(f):

    print("enter your data in the format 'product, first month sales, second month sales'\nwhen you are finished enter a blank entry")
    while True:
        newInput = input()
        if newInput == "": break
        else:
            if countCommars(newInput) != 2:
                print("error with input please enter again")
            else:
                f.write(newInput+"\n")


def readFile(fileName):
    f = open(fileName, "r").read().strip().replace(' ', '')
    unsplitProducts = f.split('\n')
    products = []
    for product in unsplitProducts:
         products.append(product.split(','))
    return products


def orderByName(data):
    data = sorted(data, key=lambda y: y[0])
    for i, x in enumerate(data):
        if int(x[1]) > int(x[2]):
            data[i].append(x[1])
        else:
            data[i].append(x[2])

    for x in data:
        print(f"Max sale for {x[0]} is {x[3]}")

def orderByMax(data):
    for i, x in enumerate(data):
        if int(x[1]) > int(x[2]):
            data[i].append(int(x[1]))
        else:
            data[i].append(int(x[2]))
    data = sorted(data, key=lambda y: y[3], reverse=True)

    for x in data:
        print(f"Max sale for {x[0]} is {x[3]}")

def orderByAverage(data):
    for i, x in enumerate(data):
        data[i].append((int(x[1])+int(x[2]))/2)

    data = sorted(data, key=lambda y: y[3], reverse=True)

    for x in data:
        print(f"Average sale for {x[0]} is {x[3]}")


def menu(fileName):
    menuOptionsText = "1. Order by product name\n2. Order by max sales\n3. Order by average sales\n"
    menuOptions = {
        "1": orderByName,
        "2": orderByMax,
        "3": orderByAverage
    }

    while True:
        userPick = input(menuOptionsText)
        if userPick == '':break
        data = readFile(fileName)
        menuOptions[userPick](data)




fileName = input("pick a file name to store your data in")
fileName = fileName+".csv"
csvFile = open(fileName, "w")
takeInput(csvFile)
csvFile.close()
menu(fileName)




