

def makeAnagram(a,b):
    """This function determines the minimum number of character deletion required to make two strings anagram"""
    #we assign a and b two different variables i.e a1 and a2 so that modifications won't affect values of a and b
    a1=a
    b1=b
    #if string are equal they are anagram
    if a==b:
        print(a+" and "+b+" are Anagram")
        exit(0)
    #comparing the characters of first string with second string if they are equal remove the characters from string
    #This is basically done to get only unequal charcters in a1 and b1
    for c1 in a1:
        for c2 in b1:
            if c1==c2:
                a1=a1.replace(c1,"",1)
                b1=b1.replace(c2,"",1)
                break;
    #now a1 and b1 has characters which are not similar
    #thus finding the length of a1 and b1 will give the total number of characters that must be deleted to make a and b anagram
    if len(a1)==len(a) and len(b1)==len(b): #if strings are disjoint or totally not similar we cannot convert its anagram
        print("Cannot convert into anagram either of string must be deleted and reassigned")
        exit(0)
    c=len(a1)+len(b1)
    if c==0:
        print(a+" and "+b+" are Anagram")
    else:
        print("Minimum character deletion required to make "+a+ " and "+ b+"  anagram is:"+str(c));

a=raw_input("Enter String1")
b=raw_input("Enter String2")
if len(a)<=10000 and len(b)<=10000:#checking string lengths<=10000
    makeAnagram(a,b)
else:
    print("Strings are too long")

"""testing sample input
Enter String1cde
Enter String2Abc
Minimum character deletion required to make cde and Abc  anagram is:4"""

    

            
            
    
