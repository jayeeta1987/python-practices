'''
Created on Sep 4, 2017

@author: jayee
'''
def getSubstringsInList(iterable):
    myList = []  # an empty array to get all substring elements
    for i in range(1, len(iterable) + 1):  # loop over 1 to string_length+1
        for j in range(len(iterable) + 1 - i):  # loop over 0 to string_length+1-i
            myList.append(iterable[j:i + j])  # append the sub-string to an array with slicing the string
    return myList  # Return sub-string list
  

def getSubstringsWithNoDubs(iterable):
    subStringList = getSubstringsInList(iterable)  # calling getSubstringsInList function to get sub-string array
    uniqueStringList = []  # an empty array to get sub-strings with no duplicate
    uniqueStringList.append(subStringList[0])  # add first element to uniqueStringList
  
    for subStr in subStringList:  # loop over subStringList elements
        isContains = False
        for unqStr in uniqueStringList:  # loop over uniqueStringList
            if(subStr == unqStr):  # compare subStringList vs uniqueStringList elements
                isContains = True
                break
        if(isContains is not True):
            uniqueStringList.append(subStr)  # add element to uniqueStringList
      
    return uniqueStringList  # return uniqueStringList

s = "subsubstrings" 
print(getSubstringsInList(s))
print(getSubstringsWithNoDubs(s))
