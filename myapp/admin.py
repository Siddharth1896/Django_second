from django.contrib import admin
#from django import import_export
from import_export.admin import ImportExportActionModelAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter
#from advanced_filters.admin import AdminAdvancedFiltersMixin

# Register your models here.

from .models import Data

@admin.register(Data)
class ViewAdmin(ImportExportActionModelAdmin):
    list_display = ('License_name','Part_number','Date_of_entry','Country','Vendor','Metric','Currency','Process_number','GLobal_price_listprice_USD','Discount_from_pricelist','Final_price_USD','Finalprice_of_Localcurrency','Awarded','Quantity','Volume_of_Deal')
    list_per_page = 50
    list_filter = (
        ('Currency', DropdownFilter),
        ('Country', DropdownFilter),
        ('Metric', DropdownFilter),
    )
