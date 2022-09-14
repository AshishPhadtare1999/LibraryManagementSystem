from ast import Add
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            passw=form.cleaned_data['password']
            user=authenticate(username=uname,password=passw)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/book/")
    else:
        form=AuthenticationForm()
    return render(request,"bookApp/login.html",{'form':form})

def register(request):
    if request.method=='POST':
        form=CustomUser(request.POST)
        if form.is_valid():
            messages.success(request,"Account created successfully..")
            form.save()
    else:
        form=CustomUser()
    return render(request,'bookApp/register.html',{'form':form})
        

def book_view(request):
    if request.method=="POST":
        fm=AddBookForm(request.POST)
        if fm.is_valid():
            fm.save()
        fm=AddBookForm()
    else:
        fm=AddBookForm()
    book_data=Book.objects.all()
    print(book_data)
    return render(request,"bookApp/Book.html",{"form":fm,"book":book_data})


def update_book(request,id):
    if request.method=='POST':
        obj=Book.objects.get(pk=id)
        form=AddBookForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/book/')
    else:
        obj=Book.objects.get(pk=id)
        form=AddBookForm(instance=obj)
    return render(request,"bookApp/update.html",{"form":form})

def delete_book(request,id):
    obj=Book.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/book/')
