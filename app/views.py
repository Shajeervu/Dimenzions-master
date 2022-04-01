from unicodedata import category
from django.shortcuts import redirect, render
from .models import *

# Create your views here.


def addmodel(request):
    var=categories.objects.all()

    return render(request, "addmodel.html",{'var':var})


def createmodel(request):
    if request.method == 'POST':

        modelname = request.POST['modelname']
        description = request.POST['description']
        gib = request.FILES['gib']
        price = request.POST['price']
        types = request.POST['types']
        format = request.POST['format']
        category = request.POST['category']
        modeltype = request.POST['modeltype']
        fbx = request.FILES['fbx']

        item = items(modelname=modelname, description=description, gib=gib, price=price, types=types, format=format, modeltype=modeltype,
                     fbx=fbx,cat_id_id=category)
        item.save()
        return redirect('addmodel')
    else:
        return redirect('createmodel')

def base(request):
    return render(request,'base.html')
def admin_models(request):
    return render(request,'admin_models.html')

def admin_current_models(request):
    category=categories.objects.all()
    item=items.objects.all()
    return render(request,'admin_current_models.html', {'category':category,'item':item})


def delete(request,id):
     
        abc=items.objects.get(id=id)
        abc.delete()
        return redirect('admin_current_models')


