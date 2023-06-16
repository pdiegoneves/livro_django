from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    # list_display = ('user', 'role', 'birthday', 'specialtiesList','addressesList',)
    list_display = ('user', 'role', 'birthday',)
    empty_value_display = 'Vazio'
    list_display_links = ('user', 'role')
    list_filter = ('user__is_active', )
    fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'addresses',)
    exclude = ('favorites', 'created_at', 'updated_at')
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    list_filter  = ('user__is_active', 'role')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)