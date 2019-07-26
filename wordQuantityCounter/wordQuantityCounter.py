# the code is tested on small amount of data where quantity of words is predefined -  the perfect match was reached
import string
from tkinter import filedialog

wordDictionary = dict()

# after user chooses file(the limitation is set to choose *.txt files ONLY) its path is assigned to file_path variable
file_path = filedialog.askopenfilename(initialdir = "/",
                                       title = "Open File",
                                       filetypes = (("Text Files", "*.txt"), ("Text Files", "*.txt")))

# in case if user doesn't choose any file the program is stopped gracefully with appropriate message
try:
    sourceFile = open(file_path)
except:
    print('Sorry, the file is not found')
    exit()

# function that accepts value of file handle as the argument and fills dictionary with distinct keys and their appropriate values (count of the words)
def wordQuantityCount(sourceFile):
    for line in sourceFile:
        line = line.rstrip()   # all spaces, 'new line' characters are cut out from line beginning and end
        line = line.translate(line.maketrans(string.punctuation, '                                ',))   # each sign that is in string.punctuation string is replaced with space for each line
        line = line.lower()   # all words become lowercase for each line
        listOfWords = line.split()   # each line of the dictionary is transformed into list of strings
        for word in listOfWords:
            wordDictionary[word] = wordDictionary.get(word, 0) + 1   # each word is checked for its presence in the list and in case of True get() returns 0. otherwise (False, in other words if it is already there) it returns the value for the key(word)

# function that accepts dictionary as argument and prints content of the dictionary
def printDictionary(dictionary):
    listOfKeysInWordDictionary = list(dictionary.keys())
    listOfKeysInWordDictionary.sort()
    for key in listOfKeysInWordDictionary:
        print(key, dictionary[key])

wordQuantityCount(sourceFile)
printDictionary(wordDictionary)
sourceFile.close()
