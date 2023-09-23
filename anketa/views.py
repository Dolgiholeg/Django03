from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return render(req, 'index.html')

from .forms123 import Nashaforma
def forma1(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        num = req.POST.get('num')
        output = '''<h1>Спасибо</h1>
        <h2>Ваше имя -- {0}</h2>
        <h2>Ваше число -- {1}</h2>'''.format(name, num)
        return HttpResponse(output)
    else:
        anketa1 = Nashaforma()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)

from .forms123 import Nashaforma1
def forma2(req):
    if req.method == 'POST':
        name1 = req.POST.get('name1')
        breed = req.POST.get('breed')
        age = req.POST.get('age')
        color = req.POST.get('color')
        food = req.POST.get('food')
        foto = req.FILES.get('foto').read()
        file = open('anketa/static/img/animal/{0}.jpg'.format(name1), 'wb')
        file.write(foto)
        fpath = 'img/animal/{0}.jpg'.format(name1)
        data = {'name1': name1, 'breed': breed, 'age': age, 'color': color, 'food': food, 'foto': fpath}
        return render(req, 'final.html', context=data)
    else:
        anketa1 = Nashaforma1()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)

from .forms123 import Forma3
def forma3(req):
    if req.method == 'POST':
        k1 = req.POST.get('k1')
        k2 = req.POST.get('k2')
        k3 = req.POST.get('k3')
        k4 = req.POST.get('k4')
        k5 = req.POST.get('k5')
        k6 = req.POST.get('k6')
        k7 = req.POST.get('k7')
        k10 = req.POST.get('k10')
        print(k1, k2)
        output = '''<h1>Спасибо</h1>
        <h2>первое -- {0}</h2>
        <h2>второе -- {1}</h2>
        <h2>третье -- {2}</h2>
        <h2>четвёртое -- {3}</h2> 
        <h2>пятое -- {4}</h2> 
        <h2>шестое -- {5} </h2 >
        <h2>седьмое -- {6} </h2>
        <h2>язык -- {7} </h2> '''.format(k1, k2, k3, k4, k5, k6, k7, k10)
        return HttpResponse(output)
    anketa = Forma3()
    data = {'form': anketa}
    return render(req,'forma.html',context=data)

from .forms123 import Forma4

def forma4(req):
    if req.method == 'POST':
        name = req.POST.get('k1')
        age = req.POST.get('k2')
        pol = req.POST.get('k3')
        adres = req.POST.get('k4')
        email = req.POST.get('k5')
        education = req.POST.get('k6')
        smoke = req.POST.get('k7')
        animal = req.POST.get('k8')
        status = req.POST.get('k9')
        foto = req.FILES.get('k10').read()
        file = open('anketa/static/img/{0}.jpg'.format(name), 'wb')
        file.write(foto)
        fpath = 'img/{0}.jpg'.format(name)
        data = {'k1': name, 'k2': age, 'k3': pol, 'k4': adres, 'k5': email, 'k6': education, 'k7': smoke, 'k8': animal, 'k9': status,
                'k10': fpath }
        return render(req, 'forma4.html', context=data)
    else:
        anketa1 = Forma4()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)
