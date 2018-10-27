from django.shortcuts import render, redirect
from time import gmtime, strftime
from . import models
import random

def index(request):
    if 'gold' not in request.session:
        request.session['sum'] = 0
        print(request.session['sum'])
        request.session['gold'] = 0
        request.session['activity'] = []
        # request.session['building'] = ''
    return render(request, 'ninja_gold_app/index.html')

def process(request, placeName):
    pGold = random.randint(10,20)
    # pBldg = placeName
    pColor = 'green'
    pTime = strftime("%I:%M:%S%p, %B %d, %Y", gmtime())

    temp = request.session['activity']
    temp.insert(0, {'color': pColor, 'gold': pGold, 'bldg': pBldg, 'time': pTime})
    request.session['activity'] = temp
    request.session['sum'] += pGold
    
    return redirect('/')

def cave(request):
    pGold = random.randint(5,10)
    pBldg = 'cave'
    pColor = 'green'
    pTime = strftime("%I:%M:%S%p, %B %d, %Y", gmtime())

    temp = request.session['activity']
    temp.insert(0, {'color': pColor, 'gold': pGold, 'bldg': pBldg, 'time': pTime})
    request.session['activity'] = temp
    request.session['sum'] += pGold
    
    return redirect('/')

def house(request):
    pGold = random.randint(2,5)
    pBldg = 'house'
    pColor = 'green'
    pTime = strftime("%I:%M:%S%p, %B %d, %Y", gmtime())

    temp = request.session['activity']
    temp.insert(0, {'color': pColor, 'gold': pGold, 'bldg': pBldg, 'time': pTime})
    request.session['activity'] = temp
    request.session['sum'] += pGold
    
    return redirect('/')

def casino(request):
    pGold = random.randint(-50,50)
    pBldg = 'casino'
    pTime = strftime("%I:%M:%S%p, %B %d, %Y", gmtime())
    if pGold <0:
        temp = request.session['activity']
        temp.insert(0, {'color': 'red', 'gold': pGold, 'bldg': pBldg, 'time': pTime})
        request.session['activity'] = temp
        request.session['sum'] += pGold
    else:
        temp = request.session['activity']
        temp.insert(0, {'color': 'green', 'gold': pGold, 'bldg': pBldg, 'time': pTime})
        request.session['activity'] = temp
        request.session['sum'] += pGold

    return redirect('/')

def reset(request):
    if 'activity'in request.session:
        request.session.clear()
    return redirect('/')


# request.session['activity'] = "<p class='gainMoney' " + "You have earned " + str(farmNum) + "!</p>" + request.session['activity']