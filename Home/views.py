from django.shortcuts import render,get_object_or_404
from . models import Car,BodyType,Brand

# Create your views here.

def home(request):
    car_obj = Car.objects.order_by('priority')[:4]

    latest_cars = Car.objects.order_by('-id')[:5]

    brand_detail = Brand.objects.all().order_by('name')

    context = {'cars':car_obj,'latest_cars':latest_cars,'brand_detail':brand_detail}
    return render(request,'home.html',context)



def car_details(request,pk):
    car_obj = Car.objects.get(id=pk)

    similar_cars = Car.objects.filter(body=car_obj.body).exclude(id=pk)[:5] 

    recent_clicks = request.session.get('recent_views',[])
    if pk in recent_clicks:# to remove duplicate values from the list.
        recent_clicks.remove(pk)
    recent_clicks.insert(0,pk)
    recent_clicks = recent_clicks[:10]
    request.session['recent_views'] = recent_clicks

    recent_visited = Car.objects.filter(id__in = recent_clicks).exclude(id=pk)# to get multiple objects in recent clicks
    sorted_products = sorted(recent_visited, key=lambda p: recent_clicks.index(p.id))[:5] # to sort in an order to view in front end.
    print(sorted_products)

    context = {'car':car_obj,'similar_cars':similar_cars,'recent_visited':sorted_products}
    return render(request,'product_detail.html',context)



def brand_list(request,pk):
    brand_obj = Brand.objects.get(id=pk)
    brand = Car.objects.filter(brand=pk)

    context={'brand':brand,'brand_obj':brand_obj}
    return render(request,'brand_list.html',context)


def search_car(request):
    searched = request.GET.get('search')
    if len(searched) > 30:
        car_obj = []
    else:
        car_obj = Car.objects.filter(title__icontains=searched)
    
    context = {'searched':car_obj,'search':searched}
        # cannot render with empty context
    return render(request,'search_output.html',context)


def car_comparison(request):
    return render(request,'car_comparison.html')