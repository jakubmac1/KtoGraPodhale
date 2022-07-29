from django.shortcuts import render, redirect
from ktograapp.models import League, Match
import datetime
import time
from datetime import date
from time import mktime


# Create your views here.



def home(request):

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
    date13 = "07/11/2022"
    date14 = "14/11/2022"
    date15 = "21/11/2022"

    converted_date0 = time.strptime(date0, "%d/%m/%Y")
    converted_date1 = time.strptime(date1, "%d/%m/%Y")
    converted_date2 = time.strptime(date2, "%d/%m/%Y")
    converted_date3 = time.strptime(date3, "%d/%m/%Y")
    converted_date4 = time.strptime(date4, "%d/%m/%Y")
    converted_date5 = time.strptime(date5, "%d/%m/%Y")
    converted_date6 = time.strptime(date6, "%d/%m/%Y")
    converted_date7 = time.strptime(date7, "%d/%m/%Y")
    converted_date8 = time.strptime(date8, "%d/%m/%Y")
    converted_date9 = time.strptime(date9, "%d/%m/%Y")
    converted_date10 = time.strptime(date10, "%d/%m/%Y")
    converted_date11 = time.strptime(date11, "%d/%m/%Y")
    converted_date12 = time.strptime(date12, "%d/%m/%Y")
    converted_date13 = time.strptime(date13, "%d/%m/%Y")
    converted_date14 = time.strptime(date14, "%d/%m/%Y")
    converted_date15 = time.strptime(date15, "%d/%m/%Y")

    newdate0 = date.fromtimestamp(mktime(converted_date0))
    newdate1 = date.fromtimestamp(mktime(converted_date1))
    newdate2 = date.fromtimestamp(mktime(converted_date2))
    newdate3 = date.fromtimestamp(mktime(converted_date3))
    newdate4 = date.fromtimestamp(mktime(converted_date4))
    newdate5 = date.fromtimestamp(mktime(converted_date5))
    newdate6 = date.fromtimestamp(mktime(converted_date6))
    newdate7 = date.fromtimestamp(mktime(converted_date7))
    newdate8 = date.fromtimestamp(mktime(converted_date8))
    newdate9 = date.fromtimestamp(mktime(converted_date9))
    newdate10 = date.fromtimestamp(mktime(converted_date10))
    newdate11 = date.fromtimestamp(mktime(converted_date11))
    newdate12 = date.fromtimestamp(mktime(converted_date12))
    newdate13 = date.fromtimestamp(mktime(converted_date13))
    newdate14 = date.fromtimestamp(mktime(converted_date14))
    newdate15 = date.fromtimestamp(mktime(converted_date15))

    if present < newdate0:
        klasaa = Match.objects.filter(matchday=1, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=2, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=3, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=4, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=5, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=6, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=7, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=8, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=9, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=10, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=11, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=12, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=13, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=14, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=15, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=16, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=17, league_id=0)
    elif newdate0 < present < newdate1:
        klasaa = Match.objects.filter(matchday=18, league_id=0)

    if present < newdate0:
        liga3 = Match.objects.filter(matchday=1, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=2, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=3, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=4, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=5, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=6, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=7, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=8, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=9, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=10, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=11, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=12, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=13, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=14, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=15, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=16, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=17, league_id=3)
    elif newdate0 < present < newdate1:
        liga3 = Match.objects.filter(matchday=18, league_id=3)


    if present < newdate0:
        liga4 = Match.objects.filter(matchday=1, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=2, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=3, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=4, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=5, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=6, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=7, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=8, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=9, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=10, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=11, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=12, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=13, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=14, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=15, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=16, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=17, league_id=4)
    elif newdate0 < present < newdate1:
        liga4 = Match.objects.filter(matchday=18, league_id=4)


    if present < newdate0:
        liga5 = Match.objects.filter(matchday=1, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=2, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=3, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=4, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=5, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=6, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=7, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=8, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=9, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=10, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=11, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=12, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=13, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=14, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=15, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=16, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=17, league_id=5)
    elif newdate0 < present < newdate1:
        liga5 = Match.objects.filter(matchday=18, league_id=5)


    if present < newdate0:
        klasa0 = Match.objects.filter(matchday=1, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=2, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=3, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=4, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=5, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=6, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=7, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=8, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=9, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=10, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=11, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=12, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=13, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=14, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=15, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=16, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=17, league_id=6)
    elif newdate0 < present < newdate1:
        klasa0 = Match.objects.filter(matchday=18, league_id=6)

    return render(request, 'ktograapp/index.html', {'liga3': liga3,'klasaa':klasaa, 'liga4':liga4, 'liga5':liga5, 'klasa0':klasa0})

