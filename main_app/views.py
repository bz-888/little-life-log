from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Baby, Playdate

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# Test from Dennelle

#===SIGN UP FUNCTION===
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign Up - try again!'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



#=====BABY MODEL CREATE,UPDATE,DELETE FUNCTIONS HERE=====
#===CREATE FUNCTION===
class BabyCreate(CreateView):
    model = Baby
    fields = ['name', 'date_of_birth', 'height', 'weight']
    success_url='/babys'

#===UPDATE FUNCTION===
class BabyUpdate(UpdateView):
    model = Baby
    fields = ['name', 'height', 'weight']
    success_url = '/babys'

#===DELETE FUNCTION===
class BabyDelete(DeleteView):
    model = Baby
    success_url = '/babys'

#=====PLAYDATE MODEL CREATE,UPDATE,DELETE FUNCTIONS HERE=====

#===LIST FUNCTION===
class PlayDateList(ListView):
    model = Playdate

#===DETAIL FUNCTION===
class PlayDateDetail(DetailView):
    model = Playdate

#===CREATE FUNCTION===
class PlayDateCreate(CreateView):
    model = Playdate
    fields = '__all__'
    success_url = '/babys'

#===UPDATE FUNCTION===
class PlayDateUpdate(UpdateView):
    model = Playdate
    fields = '__all__'
    success_url = '/babys'

#===DELETE FUNCTION===
class PlayDateDelete(DeleteView):
    model = Playdate
    success_url = '/babys'

#===ASSOC PLAYDATE TO BABY FUNCTION===
def assoc_playdate(request, baby_id, playdate_id):
    Baby.objects.get(id=baby_id).playdates.add(playdate_id)
    return redirect('detail', baby_id=baby_id)


#===HOME PAGE FUNCTION===
def home(request):
    return render(request, 'home.html')

#===ABOUT PAGE FUNCTION===
def about(request):
    return render(request, 'about.html')

#===BABY INDEX PAGE FUNCTION===
def babies_index(request):
    babies = Baby.objects.all()
    return render(request, 'babies/index.html', {'babies': babies})

#===BABY DETAIL PAGE FUNCTION===
def babies_detail(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    return render(request, 'cats/detail.html', {'baby': baby})