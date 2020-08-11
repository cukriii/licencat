from django.shortcuts import render
from django.http import HttpResponse
from uploading_app import views

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html", {})

def plots_page_view(request, *args, **kwargs):
    return render(request, "plots_page.html", {})

