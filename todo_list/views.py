from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Added to the list'))
            return render(request, 'home.html', {'all_items':all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    return render(request, 'about.html', {})


def delete_checked(request):
    List.objects.filter(completed__exact=True).delete()

    return redirect('home')


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been Deleted'))
    return redirect('home')


def delete_all(request):
    List.objects.all().delete()
    return redirect('home')


def check(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()

    return redirect('home')


def uncheck(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()

    return redirect('home')


def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':


        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Edited'))
            return redirect('home')
    else:

        return render(request, 'edit.html', {'item': item})


def count_all(request):
    items_count = List.objects.count()
    count = {'items_count': items_count}

    return render(request, 'home', count)



