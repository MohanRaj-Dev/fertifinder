from django.shortcuts import render
from App.models import Fertilizer, District_L, Rates, Product
import random
import datetime
# Create your views here.


def home(request):
    fertilizer = list(Fertilizer.objects.all())
    random.shuffle(fertilizer)
    context = {'fertilizers': fertilizer}
    return render(request, 'App/index.html', context)


def details(request, pk):
    fertilizer = Fertilizer.objects.get(pk=pk)
    
    context = {'fertilizer': fertilizer}
    return render(request, 'App/details.html', context)

def search(request):
    query = request.GET.get('q')
    crops = list(Fertilizer.objects.all())
    random.shuffle(crops)
    if query:
        results = Fertilizer.objects.filter(name__icontains=query)
        rates = Rates.objects.filter(crop__name__icontains=query)
        
        

    else:
        results = []
        rates = []
    context = {'results': results, 'crops': crops, 'query':query, 'rates':rates}

    return render(request, 'App/search.html',context )

def district(request):
    month = datetime.datetime.now().month
    season = ''
    if (month>=3 and month<=5):
        season = 'summer'
    elif (month>=6 and month<=9):
        season = 'monsoon'
    elif (month>=10 and month<=11):
        season = 'post monsoon'
    elif (month>=12 and month<=2):
        season = 'Winter'
    else:
        print('Error...')
    query = request.GET.get('d')

    if query :
        results = District_L.objects.filter(name__icontains=query)

    else: 
        results =[]

    return render(request, 'App/district.html', {'results':results})

def rates(request):
    rates = list(Rates.objects.all())
    random.shuffle(rates)
    context = {'rates':rates}
    return render(request, 'App/rates.html', context)

def products(request):
    product = Product.objects.all()
    context = {'products':product}
    return render(request, 'App/products.html', context)