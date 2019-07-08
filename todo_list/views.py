from django.shortcuts import render, redirect 
from . models import List
from .forms import HomeForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def login(request):
        return render(request,'registration/login.html',{})
# Create your views here.
# def home(request):
#     show_all=List.objects.all()
#     # messages.success(request, ('Item Has been added to List'))
#     show_all_item= {
#         'all_items': show_all
#     }
#     return render(request, 'home.html', show_all_item)

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            redirect('home')
    else:
        form=UserCreationForm()

    context = {'form':form}
    return render(request, 'registration/register.html',context)
        

def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items=List.objects.all
            messages.success(request, ('Item Has been added to List'))
            return render(request, 'home.html', {'all_items':all_items})
    else:
        all_items= List.objects.all()
        return render(request, 'home.html', {'all_items':all_items})

# def postitem(self, request):
#     form=HomeForm(request.POST)
#     if form.is_valid():
#         form.save()
#         text=form.cleaned_data['post']
#         form=HomeForm()
#         return redirect('todo_list.base')
    
#     args={'form': form, 'text': text}
#     return render(request, 'home.html', args)


def deleteItem(request, list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted Successfully'))
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item=List.objects.get(pk=list_id)

        form=HomeForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been edit successfully!')
            return redirect('home')
    else:
        item=List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item':item})

def details(request, list_id):
        item=List.objects.get(pk=list_id)
        context = {
                'item':item
        }
        return render(request, 'detail.html', context)