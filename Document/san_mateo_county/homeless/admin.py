from django.contrib import admin
from .models import HomelessPeople, Donators
# Register your models here.


class HomelessPeopleAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'higher_studies']
    list_filter = ['first_name', 'last_name', 'address']
    search_fields = ['first_name', 'last_name', 'address']

admin.site.register(HomelessPeople, HomelessPeopleAdmin)


class DonatorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'date', 'category']
    ordering = ['date']
    list_filter = ['name', 'address', 'date', 'category']
    search_fields = ['name', 'address', 'date', 'category']

admin.site.register(Donators, DonatorsAdmin)
