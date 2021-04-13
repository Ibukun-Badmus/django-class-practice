from django.shortcuts import HttpResponse, render


def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def index(request):
    return render(request, "index.html")


def landing_page(request):
    return render(request, "landing_page.html")
