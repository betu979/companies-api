from django.contrib import admin
from api.models import Company,Employee

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type',)
    #search_fields = ('name',)
    list_editable = ('location',)
    list_filter = ('type',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee)
