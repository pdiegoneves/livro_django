from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(DayWeek)
admin.site.register(Neighborhood)
admin.site.register(Speciality)
admin.site.register(State)