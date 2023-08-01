from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    # list_display = ('user', 'role', 'birthday', 'specialtiesList','addressesList',)
    list_display = ('user', 'role', 'birthday',)
    list_display = ('user', 'birth',)

    class Media:
        css = {
            "all": ("css/custom.css",)
        }
        js = ("js/custom.js",)

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
    
    birth.empty_value_display = '__/__/____'

    empty_value_display = 'Vazio'
    # list_display_links = ('user', 'role')
    list_filter = ('user__is_active', )
    # fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'addresses',)
    exclude = ('favorites', 'created_at', 'updated_at')
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    list_filter  = ('user__is_active', 'role')

    fieldsets = (
        ('Usuário', 
            {'fields': ('user', 'birthday', 'image')
        }),
        ('Função', 
            {'fields': ('role',)
        }),
        ('Extras', 
            {'fields': ('specialties', 'addresses')
        }),
    )
    list_display = ('user', 'specialtiesList', 'addressesList',)

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)