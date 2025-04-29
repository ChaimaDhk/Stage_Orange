from django.contrib import admin
from .models import Inventaire,Incident
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Inventaire)
class InventaireAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('SN',)
    list_display =('SN','Application','IP','Marque','Disk','CPU','RAM','Date','Support','Type','Site','Position')
@admin.register(Incident)
class IncidentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =('SN','Date','Description','Application','Type')
