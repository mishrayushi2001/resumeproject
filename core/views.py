from django.shortcuts import render

def home(request):
    context={'home':'active'}
    return render(request,"core/home.html",context)

def contact(request):
    return render(request,"core/contact.html")
