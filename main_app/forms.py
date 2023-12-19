from django.forms import ModelForm
from .models import Feeding, Diaper

class FeedingForm(ModelForm):
	class Meta:
		model = Feeding
		fields = ['date', 'time', 'meal', 'amount']
  
class DiaperForm(ModelForm):
    class Meta:
        model = Diaper
        fields = ['date', 'time', 'type']