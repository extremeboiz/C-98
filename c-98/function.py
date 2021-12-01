def wordsinfile():
    fileName=input("Enter the file name: ")
    file=open(fileName,'r')
    nowords=0
    for line in file:
        words=line.split()
        nowords=nowords+len(words)
    print("Number of Words are: ", nowords)

wordsinfile()