def cwfromfile():
    filename=input("Enter the file name: ")
    file=open(filename,'r')

    noOfWords = 0

    for line in file:
        words=line.split( )
        noOfWords = noOfWords + len(words)
    print("Number of words : ")
    print(noOfWords)

cwfromfile()