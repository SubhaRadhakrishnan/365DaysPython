__Date__ = '9/21/2015'
def reverse(line):
    word=''
    returnline=''
    for char in line:
        if (char!=' ') and (char != '\n'):
            word = word+char
        else:
            returnline = word+' '+returnline
            word=''
    return returnline+'\n'

from sys import argv
script, inFilename = argv
print( "File Name is",inFilename)
outFileName = inFilename.rstrip('in')+'out'
writeFile = open(outFileName,'w')
count=0
for line in open(inFilename):
    #print(line.rstrip('\n'))
    if(count !=0):
        writeFile.write ("Case #"+ str(count) + ': ' + reverse(line))
    count+=1