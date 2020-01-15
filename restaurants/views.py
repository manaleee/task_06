from django.shortcuts import render
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form = Restaurant()
    if request.method == "POST":
        form = ModelNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
            
    context = {
       "form":form
    } 
    return render(request, 'create.html', context)
