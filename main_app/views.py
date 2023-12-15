from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Baby



# Create your views here.
# Test from Dennelle


class BabyCreate(CreateView):
    model = Baby
    fields = '__all__'
    success_url='/babys'

class BabyUpdate(UpdateView):
    model = Baby
    fields = '__all__'

class BabyDelete(DeleteView):
    model = Baby
    success_url = '/babys'

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