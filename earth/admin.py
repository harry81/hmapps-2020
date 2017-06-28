from django.contrib import admin
from .models import Address, AddressCode, Deal, Location


class AddressAdmin(admin.ModelAdmin):
    list_display = ("sido_code", "gugun_code", "dong_code")


admin.site.register(Address, AddressAdmin)


class AddressCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "gubun")
    list_filter = ("gubun", )


admin.site.register(AddressCode, AddressCodeAdmin)


class DealAdmin(admin.ModelAdmin):
    list_display = ("bldg_nm", "bldg_area", "sum_amount", "dong", "bobn", "deal_dd")
    list_filter = ("deal_yy", "deal_mm", "deal_dd")


admin.site.register(Deal, DealAdmin)


class DealInline(admin.TabularInline):
    model = Deal


class LocationAdmin(admin.ModelAdmin):

    list_display = ("title", "buildingAddress", "localName_1")
    inlines = [DealInline]


admin.site.register(Location, LocationAdmin)
