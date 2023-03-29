#es Date
#Pelusi Matteo 3M

#1 stampare la dara corrente
import datetime
date = datetime.datetime.now()
print("Data e ora :", date)

#2 creare data conpleanno
compleanno = datetime.datetime(2006,11,6)
print("Compleanno:",compleanno)

#3 stampare data compleanno testuale
compleanno = datetime.datetime(2006,11,6)
print(compleanno.strftime("%A %B %Y"))

# Differenza tra data di oggi e quella del compleanno

Differenza = date - compleanno
print(Differenza)
