# Compilation and Running: python lab03.py int_password_size String_containing_password
#
#   int_password_size :             password size <= (length of String_containing_password)
#   String_containing_password :    string containing the password of specified size
# Purpose:
#  Determine the password of size N by:
#  1) Isolating the substrings with N characters in the input string
#  2) Then hashing the substrings
#  3) Then counting the amount that hash to the same number
#  4) Then getting the max count and undoing the hash so that you get the substring again
#  and return the substring to be the password you are looking for
#
# Parameters as input:
#  size of the password - int n - found on args[0]
#  encoded message - String str - found on args[1]
# Returns: None,
#
# Examples:
#  n = 3
#  str = bbbacbbbbacb
#
#  bbb = 3
#  bba = 2
#  bac = 2
#  acb = 2
#  cbb = 1
#
#  the password is bbb because it is the greatest

#Global variables
hashTable = []
tableSz = 100

# Purpose: Make hashtable of size tableSz that's initiated with -1 at every index
def makeHashTable():
    i = 0
    while (i < tableSz):
        hashTable.append(-1)
        i+=1

# Main method
def main():
    l = input('Input password length:\n')
    s = input('Input string containing password:\n')

    print("\nYou entered:\npassword length:\t",l,"\nstring:\t\t",s)

    # pass in substring length
    pl = int(l)

    # string length
    sl = len(s)

    #Dictionary with:
    #   Key : hash as an int
    #   Value : count of how many instances
    ssInstanceDict = {}

    i = 0
    while (i < sl-pl+1):
        ss = getSubstring(i,pl,s)
        hash = getHash(ss,tableSz)
        #  Put your substring in the hashTable
        hashTable[hash] = ss
        enterKey(ssInstanceDict,ss)
        i+=1
    #  Set max instance = 0
    max = 0
    maxK = 0
    for key, value in ssInstanceDict.items():
        if (value >= max):
            max = value
            maxK = key
    print("The password is:\t",maxK)

#Purpose:   Gets the substring of a specified length (passLength)
#Returns:   String str - the substring
#Params:    int iteration - the iteration of the Larger string you are at
#           int passLength - the specified length of the sub array
#           String string - the larger string containing the pass as a substring
def getSubstring(iteration, passLength, string):
    i = 0
    str = ""
    while (i < passLength):
        str += string[iteration+i]
        i+=1
    return str

#Purpose:   Gives hash of the input substring according to the table size
#Returns:   int hashIndex - the index that you want to put your value into in the hash table
#Params:    String subString - a sub string of the original input string that is the length of the password
#           int tableSz - the size of the hash table
def getHash(subString,tableSz):
    i = 0
    sum = 0
    while (i < len(subString)):
        sum += ord(subString[i])
        i+=1
    return sum%tableSz

#Purpose:   Enter the key (hash # as an int) into the dictionary (2 cases):
#           CASE 1: key is in dict then increment value by one
#           CASE 2: key is not in dict so add it and initialize the value to 0
#Returns:   None
#Params:    Dict dict - a dictionary that you want to insert into
#           K key - the key that you want to insert into the dict and keep track of instance amount
def enterKey(dict,key):
    if (key in dict):
        dict[key]+=1
    else:
        dict[key]=1

makeHashTable()
#   Call to main method
main()
