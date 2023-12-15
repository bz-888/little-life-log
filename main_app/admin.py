from django.contrib import admin

from .models import Baby, Playdate, Feeding

# Register your models here.

admin.site.register(Baby)
admin.site.register(Playdate)
admin.site.register(Feeding)