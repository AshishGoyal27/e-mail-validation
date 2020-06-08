from collections import Counter
import re
from termcolor import colored
email = input("Enter email")
a = list(email)# to break the string word into character
#print(a)
counts = Counter(a)#to see the occurence of all character in list
#print(counts)
regex = re.compile('[`;_!#$%^&*()<>?/\|}{~:]')
if counts['@'] == 1 and counts['.']>0 and email[-1]!='.' and email[0]!='@' and abs(a.index('@')-a.index('.'))!=1 and regex.search(email) == None:
    print(email, "is a valid email")
else:
    print(email, "is not a valid email")
