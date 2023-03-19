from django.contrib import admin

from .models import Image, HeroImage, Event

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class HeroImageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Image, ImageAdmin)
admin.site.register(HeroImage, HeroImageAdmin)
admin.site.register(Event, EventAdmin)