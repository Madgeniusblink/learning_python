"""
#8 Input and Output (I/O) homework #8
"""
# Input file name
fileName = input("Enter the file you would like to edit: ")

fileData = ["Mayas notes"]


#if file name already eist ask the following 

if fileName in fileData:
    selectOptions = input("Choose one of the options you would like to execute\n"
                    "A: Read the file\n"
                    "B: Open file, delete all content, and write new content to file\n"
                    "C: Opens the file for both appending and reading\n\n" 
                    "Enter Your Option: ")
    # A read the file
    if selectOptions == "A":
        fileInput = open(fileName, "r")
        print(fileInput.read())
        fileInput.close()
    # B delete the file and start over
    if selectOptions == "B":
        fileInput = open(fileName, "w")
        newInput = input("What would you like to write the file? \n :")
        fileInput.write(newInput)
        fileInput.close()
    # C Append the file
    if selectOptions == "C":
        fileInput = open(fileName, "a")
        newInput = input("What would you like to add to your file?: \n")
        fileInput.write(newInput)
        fileInput = open(fileName, "r")
        print(fileInput.read())
        fileInput.close()

# if file name doest not exist - create file, enter text to write a file,  save file
else:
    newFileName = open(fileName, "w")
    fileInput = input("What would you like to write to your new file?\n :")
    newFileName.write(fileInput)
    newFileName = open(fileName, "r")
    print(newFileName.read())
    newFileName.close()

    

