from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Orders

# Create your views here.


def createView(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # print(f"Form data : {form}")
        if form.is_valid():
            form.save()
            print("saved!!!")
            return redirect('/show')
        else:
            print("error!!!")
            return render(request, 'index.html', {'form': form})
    else:
        form = OrderForm
    return render(request, 'index.html', {"form":form})


def show(request):
    data = Orders.objects.all()
    return render(request, 'show.html', {'orders':data})
            

def edit(request,eid):
    order = Orders.objects.get(oid=eid)
    return render(request, 'edit.html', {"order":order})



def destroy(request, eid):
    employee = Orders.objects.get(oid=eid)
    employee.delete()
    return redirect("/show")

def update(request, eid):
    order = Orders.objects.get(oid=eid)
    form = OrderForm(request.POST, instance=order)
    print(form)
    if form.is_valid():
        form.save()
        print("---------updated-------------")
        return redirect("/show")
    return render(request, 'edit.html', {'order': order})
