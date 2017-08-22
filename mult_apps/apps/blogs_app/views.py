from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    print number
    response = "placeholder to display blog"
    return HttpResponse(response + " " + number)

def edit(request, number):
    print number
    response = "place holder to edit blog"
    return HttpResponse(response + " " + number)

def destroy(request, number):
    print number
    return redirect('/blogs')