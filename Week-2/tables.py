#import module
from tabulate import tabulate

#assign data
mydata = [
    ["Wachira"   ,   "Nyeri"] ,
    ["Fatuma"   ,   "Mombasa"] ,
    ["Odinga"   ,   "Kisumu"] ,
    ["Kipkoech"   ,   "Uasin Gishu"] ,
    ["Wafula"   ,    "Bungoma"] ,
    ["Muthuri"   ,   "Meru"] ,
]
#create header
head = [ "Name"   ,   "County" ]

#display table
print(tabulate(mydata , headers = head, tablefmt = "grid"))