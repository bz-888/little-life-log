from django.contrib import admin

from .models import Baby, Playdate, Feeding, Photo, Diaper, Sleep

# Register your models here.
admin.site.register(Baby)
admin.site.register(Playdate)
admin.site.register(Feeding)
admin.site.register(Photo)
admin.site.register(Diaper)
admin.site.register(Sleep)
