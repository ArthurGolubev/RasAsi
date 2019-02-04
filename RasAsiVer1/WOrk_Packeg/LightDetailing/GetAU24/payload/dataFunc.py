def dataFunc(dictValues):
    listOfData = []
    for i in dictValues:
        listOfData.append({
            'range': f'{i}!A2',
            'values': dictValues.get(i)
        })
    print(listOfData)
    # input('pause')
    return listOfData
