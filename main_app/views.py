from django.shortcuts import render

from .models import Baby

# Create your views here.
# Test from Dennelle


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def babies_index(request):
    babies = Baby.objects.all()
    return render(request, 'babies/index.html', {'babies': babies})

def babies_detail(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    return render(request, 'cats/detail.html', {'baby': baby})