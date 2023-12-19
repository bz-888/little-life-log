from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Baby, Playdate, Photo
from .forms import FeedingForm, DiaperForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import boto3
import uuid
import os
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

#===ADD PHOTO FUNCTION===
def add_photo(request, baby_id):
	photo_file = request.FILES.get('photo-file', None)
	if photo_file:
		s3 = boto3.client('s3')
		key = f"littlelifelog/{uuid.uuid4().hex[:6]}{photo_file.name[photo_file.name.rfind('.'):]}"
		try:
			bucket = os.environ['BUCKET_NAME']
			s3.upload_fileobj(photo_file, bucket, key)
			photo_url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
			Photo.objects.create(url=photo_url, baby_id=baby_id)

		except Exception as e:
			print('AN error uploading to aws')
			print(e)
	return redirect('detail', baby_id=baby_id)

#=====BABY MODEL CREATE,UPDATE,DELETE FUNCTIONS HERE=====
#===CREATE FUNCTION===
class BabyCreate(CreateView):
    model = Baby
    fields = ['name', 'date_of_birth', 'height', 'weight']
    success_url='/babies'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#===UPDATE FUNCTION===
class BabyUpdate(UpdateView):
    model = Baby
    fields = ['name', 'height', 'weight']

#===DELETE FUNCTION===
class BabyDelete(DeleteView):
    model = Baby
    success_url = '/babies'

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

#===UPDATE FUNCTION===
class PlayDateUpdate(UpdateView):
    model = Playdate
    fields = '__all__'


#===DELETE FUNCTION===
class PlayDateDelete(DeleteView):
    model = Playdate
    success_url = '/playdates'
#===ASSOC PLAYDATE TO BABY FUNCTION===
def assoc_playdate(request, baby_id, playdate_id):
    Baby.objects.get(id=baby_id).playdate.add(playdate_id)
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
    id_list= baby.playdate.all().values_list('id')
    playdates_baby_doesnt_have = Playdate.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    diaper_form = DiaperForm()
    return render(request, 'babies/detail.html', {
        'baby': baby, 
        'feeding_form': feeding_form, 
        'diaper_form': diaper_form, 
        'playdates': playdates_baby_doesnt_have})

#===ADD FEEDING FUNCTION===
def add_feeding(request, baby_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.baby_id = baby_id
        new_feeding.save()
    return redirect('detail', baby_id=baby_id)

#===ADD DIAPER CHANGE FUNCTION===
def add_change(request, baby_id):
    form = DiaperForm(request.POST)
    if form.is_valid():
        new_change = form.save(commit=False)
        new_change.baby_id = baby_id
        new_change.save()
    return redirect('detail', baby_id=baby_id)
