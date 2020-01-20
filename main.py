# -*- coding: utf-8 -*-

with open("./usuarios.txt", "r") as file:
    data = file.readlines()

def GetDataUsed(data):
    dataUsedList = []

    for line in data:
        dataUsed = []
        counter = 0
        while(counter < len(line)):
            if(line[counter].isnumeric()):
                dataUsed.append(line[counter])
            counter += 1
        dataUsedJoined = "".join(dataUsed)
        dataUsedList.append(int(dataUsedJoined))
    return dataUsedList

def GetUserNames(data):
    namesList = []

    for line in data:
        name = []
        counter = 0
        while(counter < len(line)):
            if(line[counter].isalpha()):
                name.append(line[counter])
            counter += 1
        nameJoined = "".join(name)
        namesList.append(nameJoined)
    return namesList

def GenerateReport(data):
    header = "FOML Inc.           Uso do espaco em disco pelos usuarios\n------------------------------------------------------------------------"
    tableHeader = "\nNr.  Usuario        Espaco utilizado     % do uso\n"
    dataUsedLineDisplay = "Espaco total ocupado: {0:.2f} MB\n"
    dataUsedMeanLineDisplay = "Espaco medio ocupado: {0:.2f} MB"
    dataUsed = GetDataUsed(data)
    names = GetUserNames(data)
    message = header+tableHeader
    totalData = sum(dataUsed) * 0.000001
    dataUsedMean = totalData/len(dataUsed)
    
    for i in range(len(names)):
        line = str(i + 1) + "    " + names[i] + "       " + str(round(dataUsed[i] * 0.000001, 2)) + " MB"
        line += "            " + str(round(dataUsed[i]/totalData * 0.0001, 2)) + "%\n"
        message += line
    message += dataUsedLineDisplay.format(totalData) + dataUsedMeanLineDisplay.format(dataUsedMean)
    
    with open("./relatorio.txt", "w") as file:
        file.write(message)

GenerateReport(data)

