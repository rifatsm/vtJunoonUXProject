from django.shortcuts import redirect, render


def landing_page(request):
    return render(request, "landing_in.html")