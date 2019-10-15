import re

exclusionList = [("é|è|ê",'e'),(",|!|:|'",""),("ç","c"),("à|â","a")]


def clean_Word(value,exclusionList):
        for reg in exclusionList:
                return re.sub(reg[0],reg[1],value)




def is_palindrome(theString):
        stringToEvaluate=clean_Word(theString, exlusionList).lower()

        if stringToEvaluate == stringToEvaluate[::-1] and len(theString) !=0:
                print("{0} is a palindrome".format(theString))
        else: 
                print("{0} is not a palindrome".format(theString))

def main():

        names_list = ['anna','cyril','Boob!', 'sebastien','','11','112','121','@!@!@']
    
        for name in names_list:
                is_palindrome(name)

main()


