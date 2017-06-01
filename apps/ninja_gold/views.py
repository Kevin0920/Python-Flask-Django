from django.shortcuts import render, redirect
import random
from datetime import datetime  

# Create your views here.
def index(request):
    if request.session.get('gold') == None:
        request.session['gold'] = 0
    if request.session.get('log') == None:
        request.session['log'] = []
    return render(request, 'ninja_gold/index.html')
def process(request):
    building = request.POST.get('building', False)
    earn = 0
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    log = ''
    if building == 'farm':
        earn = random.randrange(10, 21)
    elif building == 'cave':
        earn = random.randrange(5, 11)
    elif building == 'house':
        earn = random.randrange(2, 6)
    elif building == 'casino':
        earn = random.randrange(-50, 51)
    request.session['gold'] += earn   
    if earn >= 0:
        log = 'Earned ' + str(earn) + ' golds from the '+ building + '! (' + time + ' )'
        color = 'red'
    else:
        log = 'Entered a casino and lost ' + str(earn * -1) + ' golds...ouch.. (' + time + ' )'
        color = 'green'
    request.session['log'].append([log, color])
    return redirect('/')  
          

          