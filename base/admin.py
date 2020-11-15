from django.contrib import admin
from .models import Items, tables

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    model = Items
    list_filter = ('category', 'table')
    list_display = ['table', 'Items','Bill_no','category','quantity','U_PRS_USD','TOTAL_PRS_USD','U_PRS_DHS','S_PRS_dhs','LO_AND_PR']
    search_fields = ('table__table_name__startswith',)

class tablesAdmin(admin.ModelAdmin):
    model = tables


admin.site.register(Items, ItemsAdmin)
admin.site.register(tables, tablesAdmin)