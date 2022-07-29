import time
from datetime import date
from time import mktime
'''
present = date.today()

date1 = "07/07/2022"
date2 = "14/07/2022"

converted_date1 = time.strptime(date1, "%d/%m/%Y")
converted_date2 = time.strptime(date2, "%d/%m/%Y")

newdate1 = date.fromtimestamp(mktime(converted_date1))
newdate2 = date.fromtimestamp(mktime(converted_date2))

print (present < newdate1)

sdate1 = "09/08/2022"

print (type(converted_date1))
i = 1
'''

present = date.today()

date0 = "09/08/2022"
date1 = "15/08/2022"
date2 = "22/08/2022"
date3 = "29/08/2022"
date4 = "05/09/2022"
date5 = "12/09/2022"
date6 = "19/09/2022"
date7 = "26/09/2022"
date8 = "03/10/2022"
date9 = "10/10/2022"
date10 = "17/10/2022"
date11 = "24/10/2022"
date12 = "31/10/2022"

'''for i in range(13):
    x = "converted_date" + str(i)
    x = time.strptime("date"+str(i), "%d/%m/%Y")
    print (x)'''
'''for i in range(10):
    x = "name" + str(i)
    print(x)
    print(type(x))'''

present = date(2022, 7, 10)
print(type(present))