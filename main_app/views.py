from django.shortcuts import render

# Create your views here.
# Test from Dennelle


def home(request):
    return render(request, 'home.html')