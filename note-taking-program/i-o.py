"""
#8 Input and Output (I/O)
"""

#existing filenames
filedata = ["Mayas notes", "notes"]
# outputfile = open("notes.txt", "w")

# prompt them for a filename
filename = input("Enter The File You would like to Edit?")


# if  file doesn't exist, it should prompt them to enter the text they want to write to the file
if filename not in filedata:
    new_file_name_data = []

    new_filename = input("The file your enter is not in the Data Base \n What would you like to name your new file? ")
    new_file_name_data.append(new_filename)

    data_to_file = input("enter the text you want to write to the file\n : ")
    new_file_name_data.append(data_to_file)

    filedata.append(new_file_name_data) # saves new filename to filedata

    outputfile = open(new_filename, "w")

    for data in new_file_name_data:
        outputfile.write(data)

    outputfile.close()

# if they enter a file name that already exists, it should ask the user if they want to choose a multple choice option A, B, C
elif filename in filedata:
    A = open(filename, "r")
    B = open(filename, "w")
    C = open(filename, "a+")
    options = input("Choose one of the options you would like to execute\n"
                    "A: Read the file\n"
                    "B: Open file and write only if file doesnt not exist creates file\n"
                    "C: Opens the file for both appending and reading\n\n" 
                    "Enter Your Option: ")
    if options == "A":
        print(A.name)
        print(A.mode)
        for line in A:
            print(line)
    elif options == "B":
        print(B.name)
        print("You are about to:", B.mode, "The File")
        answer = input("What would you like to write to the file?\n:")
        B.append(answer)
        for line in B:
            print(line)
    elif options == "C":
        editFile = []
        print(C.name)
        print(C.mode)
        answer = input("What would you like to write to the file?\n:")
        editFile.append(answer)
        for line in A:
            print(line)

    filedata.append(answer)

    for filename in filedata:
        for data in answer:
            answer.write(data)

    answer.close()


