from django.shortcuts import redirect, render


def landing_page(request):
    return render(request, "landing_in.html")

def about(request):
    return render(request, "about.html")

def people(request):
    return render(request, "people.html")

def contact(request):
    return render(request, "contactus.html")

def gallery(request):
    return render(request, "gallery.html")

def fund(request):
    return render(request, "fundus.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def in_land(request):
    return render(request, "in_landing.html")


def prac(request):
    return render(request, "practicevideos.html")

