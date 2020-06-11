def	printPicnic(itemsDict,	leftWidth,	rightWidth):
    print('PICNIC	ITEMS'.center(leftWidth	+	rightWidth,	'-'))
    for	k,	v	in	itemsDict.items():
        print(k.ljust(leftWidth,	'.')	+	str(v).rjust(rightWidth))

picnicItems	=	{'sandwiches':	4,	'apples':	12,	'cups':	4,	'cookies':	8000}
# printPicnic(picnicItems,	12,	5)
# printPicnic(picnicItems,	20,	6) 



tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable():
    itemcount = len(tableData[0])
    colWidths = [0] * len(tableData)


    for item_index in range(itemcount):
        for col_index in range(len(tableData)):
            item = tableData[col_index][item_index]
            if (len(item) >= colWidths[col_index]):
               colWidths[col_index] = len(item)

    print(colWidths)
    
    text = ""
    for item_index in range(itemcount):
        text = ''
        for col_index in range(len(tableData)):
            item = tableData[col_index][item_index]
            just = colWidths[col_index] - len(item)
            #print('item: ' + item + ' len: ' + str(len(item)) + ' col: ' + str(colWidths[col_index]) +  ' just: ' + str(just))
            
            text+=item.rjust(len(item) + just) + ' '

        print(text)
            
        

    
            
        

printTable()
print('hello'.ljust(20, '-'))


    
