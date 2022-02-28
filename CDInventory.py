
#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TDavis, modified to satisfy assignment 05
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dictRow = {}  # list of data row as dictionary
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile=open(strFileName, 'r') #ooens to read
        for row in objFile:
            lstRow=row.strip().split(',') #turns each row in file into a string
            dictRow={'IDNumber': lstRow[0], 'CD Title': lstRow[1], 'Artist Name': lstRow[2]}
            print(dictRow) #prints all entries as dictionaries
        objFile.close()
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow={'IDNumber: ': intID, 'CDTitle: ': strTitle, 'ArtistName: ': strArtist} #converts to dict
        lstTbl.append(dictRow) #Appending the 2d list with the new dictionary input
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
       objFile=open(strFileName, 'r') #ooens to read existing entries in 
       for row in objFile:
           lstRow=row.strip().split(',') #turns each row in file into a string
           dictRow={'IDNumber': lstRow[0], 'CD Title': lstRow[1], 'Artist Name': lstRow[2]}
           print(dictRow)
           lstTbl.append(dictRow) #turns entries into table for get method
       objFile.close()
       delEntry=input('Please enter the ID Number of the entry you'
              ' would like to delete: ')
       #Checkseach row in table for delEntry value
       for row in lstTbl:
           if delEntry==row.get('IDNumber'):
               lstTbl.remove(row) #removes the selected entry
     #this block prepares updated list to be overwritten to .txt file
       strdict=''
       for row in lstTbl:
           for item in row.values():
             strdict+=str(item) + ', ' #turns each row into a string
           strdict=strdict[:-2] + '\n' #Prints a new line after each entry and removes the trailing comma 
       objFile=open(strFileName, 'w') #opens and allows appending file
       objFile.write(strdict) #writes the row(s) to file
       objFile.close() #closes file
       pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        strdict=''
        for row in lstTbl:
            for item in row.values():
              strdict+=str(item) + ', ' #turns each row into a string
            strdict=strdict[:-2] + '\n' #Prints a new line after each entry and removes the trailing comma 
        objFile=open(strFileName, 'a') #opens and allows appending file
        objFile.write(strdict) #writes the row(s) to file
        objFile.close() #closes file
    else:
        print('Please choose either l, a, i, d, s or x!')