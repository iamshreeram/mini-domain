import whois
import json 

# for permutation of 3 letter words
from itertools import product
from string import ascii_lowercase

# calculating performance
import time

tld = "org"
avail = []
unavail = []


def isdomainavailable(keywrd):
    '''
    # function will take keyword and returns the availablity
    '''
    dname =str(keywrd)+"."+tld
    w = whois.whois(dname)
    if w["domain_name"] == None:
        avail.append(dname)
        return True
    else:
        unavail.append(dname)
        return False


# search for all letters - permutation and combination
def dnamegenerator():
    '''
    Domain name generator : Creates a list of keywords for domain name 
    '''
    alphas = list(map(''.join, product(ascii_lowercase, repeat=3)))
    # alphas = [a+b+c for a,b,c in product(ascii_lowercase, repeat=3)] # Generates letters with 3 permutation
    numbers = list(range(1,1000))      # generates numbers
    keywords = alphas+numbers       # combains both the lists
    return keywords


keywrds = dnamegenerator()
results = list(map(isdomainavailable,keywrds))
print(avail)
