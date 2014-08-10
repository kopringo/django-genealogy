from django.contrib import admin

# Register your models here.

from models import *

admin.site.register(Person)
admin.site.register(Family)
admin.site.register(Event)
admin.site.register(Place)
admin.site.register(Media)
admin.site.register(Note)