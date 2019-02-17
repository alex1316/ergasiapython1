# ergasia 2

import math

# mia sunartish h opoia tipwnei olous tous
# prwtous paragontes enos arithmou  n
def prwtoiParagontes(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2

    # n prepei na einai perittos ws edw
    # etsi wste to prosperasma 2 ( i = i + 2) na mporei na xrisimopoihthei
    for i in range(3,int(math.sqrt(n))+1,2):

        #enw i diairei n , enfanise i ad diairese  n
        while n % i== 0:
            print i,
            n = n / i

    #Synthiki an o n einai prwtos
    # arithmos megaliteros tou 2
    if n > 2:
        print n

# kwdikas o opoios mas xrhshmeuei
#sto na ektelesoume thn sunartish
n = 315
prwtoiParagontes(n)
