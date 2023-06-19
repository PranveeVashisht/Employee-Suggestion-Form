from django.shortcuts import render,redirect
from .models import Suggestion

# Create your views here.

def home(request): #view for home page
    return render(request, 'suggestions/home.html')

def suggestion_form(request): #view for suggestion form
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        suggestion_content = request.POST['suggestion']
        Suggestion.objects.create(content=suggestion_content, name=name, email=email)
        
        return redirect('home')
    return render(request, 'suggestions/suggestion_form.html')
