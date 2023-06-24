from django.contrib import admin

from doors.models import Door, Branch, Color, CTA, Film, Panel, Accessory

# Register your models here.


@admin.register(Door)
class AdminDoor(admin.ModelAdmin):
    list_display = ("title", "branch", "price")



admin.site.register(Color)
admin.site.register(Panel)
admin.site.register(Film)
admin.site.register(Branch)
admin.site.register(CTA)
admin.site.register(Accessory)

